# -----------------------------------------------------------
# downloads a list of available global surface summary (GSOD) 
# of the day files from NOAA. 
#
# Gathering data from NOAA Global Surface Summary of the Day - GSOD. 
# By default, download data will be from the 
#  https://www.ncei.noaa.gov/data/global-summary-of-the-day/access/2020
# 
#
# Parameters:
#   url: url to a years worth of GSOD data
#   outputfile: output file containing list of GSD csv files
# 
# 
# -----------------------------------------------------------

#
# 
import requests
from bs4 import BeautifulSoup
import csv
import os.path
from os import path
import logging
import sys

# class gsod_directory_list:
class GsodDirectoryList:
    # Class attribute

    def __init__(self, url, year, output_pathname):
        self.log = logging.getLogger()
        self.log.info('gsodDirectoryList initialized with:')
        self.log.info('  url:             %s', url)
        self.log.info('  year:            %s', year)
        self.log.info('  output_pathname: %s', output_pathname)

        self.url = url
        self.year = year
        self.output_pathname = output_pathname
        
    def get_url(self):
        return self.url

    def get_pathname(self):
        return self.output_pathname

    def _get_url_paths(self, url, ext='', params={}):
#        self.log.debug('url: %s', self.url + "/" + self.year)

        response = requests.get(url, params=params)
        if response.ok:
            response_text = response.text
        else:
            return response.raise_for_status()
        soup = BeautifulSoup(response_text, 'html.parser')
        parent = [url + node.get('href') for node in soup.find_all('a') if node.get('href').endswith(ext)]
        return parent

    def _get_gsod_directory_list(self):
#        url = 'https://www.ncei.noaa.gov/data/global-summary-of-the-day/access/2024/'
        ext = 'csv'
        result = self._get_url_paths( self.url + "/" + self.year + "/" , ext)
        # print(result)
        with open(self.output_pathname, 'w') as fp:
            fp.writelines("%s\n" % url for url in result)
        return

    def _gsod_file_exist(self):
        if path.exists(self.output_pathname):
            return True
        else:
            return False
    
    def _get_GSOD_file_list(self):
        self.log.info('reading NOAA directory: %s', self.url + "/" + self.year)
        if self._gsod_file_exist() == False:
            self._get_gsod_directory_list()
        else:
            self.log.info('file exists.')
        
    def process_gsod_files(self):
        self._get_GSOD_file_list()
        
        