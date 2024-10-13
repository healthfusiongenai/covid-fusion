import logging
import datetime
from pickle import NONE
from threading import Lock

from calendar import timegm
from concurrent.futures import ThreadPoolExecutor
from csv import DictReader as csv_dict_reader
from datetime import datetime, timedelta
from gzip import open as gz_open
from os.path import basename
from parquet import DictReader as parquet_dict_reader
from threading import Lock

import boto3
import io

from botocore.exceptions import PaginationError
from dateutil.rrule import rrule, DAILY



DEFAULT_FIELDS = (
    'version',
    'account_id',
    'interface_id',
    'srcaddr',
    'dstaddr',
    'srcport',
    'dstport',
    'protocol',
    'packets',
    'bytes',
    'start',
    'end',
    'action',
    'log_status',
)
DUPLICATE_NEXT_TOKEN_MESSAGE = 'The same next token was received twice'

# The lastEventTimestamp may be delayed by up to an hour:
# https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_LogStream.html  # noqa
LAST_EVENT_DELAY_MSEC = 3600000

ACCEPT = 'ACCEPT'
REJECT = 'REJECT'
SKIPDATA = 'SKIPDATA'
NODATA = 'NODATA'

THREAD_LOCK = Lock()


class GsodData:

#    __slots__ = 'test1','test2'

#    __slots__ = 'STATION','DATE','LATITUDE','LONGITUDE','ELEVATION','NAME','TEMP','TEMP_ATTRIBUTES','DEWP','DEWP_ATTRIBUTES','SLP','SLP_ATTRIBUTES','STP','STP_ATTRIBUTES','VISIB','VISIB_ATTRIBUTES','WDSP','WDSP_ATTRIBUTES','MXSPD','GUST','MAX','MAX_ATTRIBUTES','MIN','MIN_ATTRIBUTES','PRCP','PRCP_ATTRIBUTES','SNDP','FRSHTT',
    
    """
    __slots__ = [
        'STATION',
        'DATE',
        'LATITUDE',
        'LONGITUDE',
        'ELEVATION',
        'NAME',
        'TEMP',
        'TEMP_ATTRIBUTES',
        'DEWP',
        'DEWP_ATTRIBUTES',
        'SLP',
        'SLP_ATTRIBUTES',
        'STP',
        'STP_ATTRIBUTES',
        'VISIB',
        'VISIB_ATTRIBUTES',
        'WDSP',
        'WDSP_ATTRIBUTES',
        'MXSPD',
        'GUST',
        'MAX',
        'MAX_ATTRIBUTES',
        'MIN',
        'MIN_ATTRIBUTES',
        'PRCP',
        'PRCP_ATTRIBUTES',
        'SNDP',
        'FRSHTT',        
    ]
        """
        
        
    def __init__(self, gsod_data, EPOCH_32_MAX=2147483647):
#        self.log = logging.getLogger()
        self.end = None
    
  
    """
    def __init__(self, gsod_data, EPOCH_32_MAX=2147483647):
        self.log = logging.getLogger()
        
        if 'DATE' in gsod_data:
            date = int(gsod_data['DATE'])
        if date > EPOCH_32_MAX:
            date /= 1000
            self.date = datetime.utcfromtimestamp(date)
        else:
            self.date = None
        
        for key, func in (            
            ('STATION', str),
            ('DATE', str),
            ('LATITUDE', str),
            ('LONGITUDE', str),
            ('ELEVATION', float),
            ('NAME', str),
            ('TEMP', float),
            ('TEMP_ATTRIBUTES', str),
            ('DEWP', float),
            ('DEWP_ATTRIBUTES', str),
            ('SLP', float),
            ('SLP_ATTRIBUTES', str),
            ('STP', float),
            ('STP_ATTRIBUTES', str),
            ('VISIB', float),
            ('VISIB_ATTRIBUTES', str),
            ('WDSP', float),
            ('WDSP_ATTRIBUTES', str),
            ('MXSPD', float),
            ('GUST', float),
            ('MAX', float),
            ('MAX_ATTRIBUTES', str),
            ('MIN', float),
            ('MIN_ATTRIBUTES', str),
            ('PRCP', float),
            ('PRCP_ATTRIBUTES', str),
            ('SNDP', str),
            ('FRSHTT', str),
        ):
            value = gsod_data.get(key, '-')
            if value == '-' or value == 'None' or value is None:
                value = None
            else:
                value = func(value)

            setattr(self, key, value)   
    """
        
   
    def __eq__(self, other):
        try:
            return all(
                getattr(self, x) == getattr(other, x) for x in self.__slots__
            )
        except AttributeError:
            return False

    def __hash__(self):
        return hash(tuple(getattr(self, x) for x in self.__slots__))

    def __str__(self):
        ret = []
        for key in self.__slots__:
            value = getattr(self, key)
            if value is not None:
                ret.append('{}: {}'.format(key, value))
        return ', '.join(ret)

    def to_dict(self):
        ret = {}
        for key in self.__slots__:
            value = getattr(self, key)
            if value is not None:
                ret[key] = value

        return ret

    def to_message(self):
        D_transform = {
            'start': lambda dt: str(timegm(dt.utctimetuple())),
            'end': lambda dt: str(timegm(dt.utctimetuple())),
        }

        ret = []
        for attr in self.__slots__:
            transform = D_transform.get(attr, lambda x: str(x) if x else '-')
            ret.append(transform(getattr(self, attr)))

        return ' '.join(ret) 
    
