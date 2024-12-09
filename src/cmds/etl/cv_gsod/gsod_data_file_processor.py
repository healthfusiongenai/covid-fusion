import logging
import requests
from bs4 import BeautifulSoup
import csv
import os.path
from os import path
import sys
import json

class GsodDataFileProcessor:
    # Class attribute
    type = "gsod csv data file reader"

    def __init__(self, gsod_output_pathname, url, year, save_gsod_files, persist_data, output_data_directory):
        self.logger = logging.getLogger()
        self.gsod_output_pathname = gsod_output_pathname
        self.local_gsod_pathname = "" # initialized in _get_gsod_file
        self.year = year
        self.url = url
        self.save_gsod_files = save_gsod_files
        self.persist_data = persist_data
        self.output_data_directory = output_data_directory
        self.logger.info("Initialized with year %s gsod file pathname %s to store in %s", 
                         self.year, self.gsod_output_pathname, self.output_data_directory+"/"+self.year)
    
    def get_output_directory(self):
        return self.output_data_directory+"/"+self.year
    
    def _get_gsod_file(self, gsod_file_url, gsod_dir):
        head, gsod_filename = os.path.split(gsod_file_url)
        
        # save the local pathname to be used to read and persist later
        self.local_gsod_pathname = gsod_dir+'/'+gsod_filename
        
        self.logger.debug('_get_gsod_file: Extracting gsod data file: (' + gsod_file_url + ')')
        r = requests.get(gsod_file_url)
        
        if r.status_code != 404:
            with open(self.local_gsod_pathname, 'wb') as fp:
                fp.write(r.content)
            return True
        else:
            self.logger.warning('Response 404: Extracting gsod data file: (' + gsod_file_url + ')')
            return False
    
    def _store_gsod_file_locally(self, fileUrlPathname):
        self.logger.info("processing file %s, saving gsod file to %s", 
                         fileUrlPathname,
                         self.output_data_directory+"/"+self.year)
        self._get_gsod_file(fileUrlPathname, self.output_data_directory+"/"+self.year)
        
    def _process_file(self):
        self.logger.info("processing gsod data from file")
        
        with open(self.local_gsod_pathname, 'r') as fp:
            lines = len(fp.readlines())
            self.logger.info("processing %d gsod data items", lines)
            # need to rewind the file pointer to the beginning
            fp.seek(0)
            for line in fp:
                self.logger.info("processing line %s", line.strip())
                # gsoddata = GsodData(line.strip())
                # gsoddata.set_0(1)
                # self.logger.info("processed gsod data %s", gsoddata)
                
        # TODO: implement persisting data to mongo, or cassandra, one line, or a batch
        if self.persist_data == True:
            self._persist_gsod_data()
        
    def _persist_gsod_data(self):
        self.logger.info("persisting gsod data to mongo")
    
    def process_GSOD_file(self, fileUrlPathname):
        self.fileUrlPathname = fileUrlPathname
        self.logger.info("processing gsod file from url %s", fileUrlPathname)
        if self.save_gsod_files == True:
            self._store_gsod_file_locally(fileUrlPathname)
        
        self._process_file()
        
        self.logger.info("finished processig file")
        
        

