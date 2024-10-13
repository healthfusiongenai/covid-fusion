import logging
import datetime
from dataclasses import dataclass, fields

EPOCH_32_MAX=2147483647

@dataclass
class GsodData():
    gsod_data: str
    STATION: str
    DATE: str
    LATITUDE: str
    LONGITUDE: str
    ELEVATION: float
    NAME: str
    TEMP: float
    TEMP_ATTRIBUTES: str
    DEWP: float
    DEWP_ATTRIBUTES: str
    SLP: float
    SLP_ATTRIBUTES: str
    STP: float
    STP_ATTRIBUTES: str
    VISIB: float
    VISIB_ATTRIBUTES: str
    WDSP: float
    WDSP_ATTRIBUTES: str
    MXSPD: float
    GUST: float
    MAX: float
    MAX_ATTRIBUTES: str
    MIN: float
    MIN_ATTRIBUTES: str
    PRCP: float
    PRCP_ATTRIBUTES: str
    SNDP: str
    FRSHT: str
    
    def __init__(self, gsod_data: str):
        self.gsod_data = gsod_data
        date = 0
        logging.getLogger().info("Running __init__: %s", gsod_data)

        if 'DATE' in gsod_data:
            date = int(gsod_data['DATE'])
        if date > EPOCH_32_MAX:
            date /= 1000
            self.date = datetime.utcfromtimestamp(date)
        else:
            self.date = None

        for field in fields(self):
            value = gsod_data.get(field.name, '-')
            if value == '-' or value == 'None' or value is None:
                value = None
            setattr(self, field.name, value)
            logging.getLogger().info("%s %s", field.name, value)

    def __post_init__(self, gsod_data):
        self.b = self.get_b()
        self.end = 0
        self.gsod_data = gsod_data
        self.logger = logging.getLogger()
        self.logger.info("Running __post_init__")
        
        for field in fields(self):
            value = gsod_data.get(field.name, '-')
            if value == '-' or value == 'None' or value is None:
                value = None
            setattr(self, field.name, value)
            self.logger.info("%s %s", field, value)
    
    def set_0(self, _value):
 #       self.__slots__[0] = _value
        self.end = 1
        
#    def get_0(self):
#        return self.__slots__[0]
