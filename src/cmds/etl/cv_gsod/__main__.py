# -----------------------------------------------------------
# demonstrates how to write ms excel files using python-openpyxl
# cv_gsod version 0.0.1
#
# Parameters:
#
# -u (--url): url, per year, to download GSOD files from e.g. 
#         https://www.ncei.noaa.gov/data/global-summary-of-the-day/access/2020
# -y (--year): year, as subdir to gather data from e.g. 2020
# -o (--output): output file to download list to 
# -h (--help): display this help
#
#  Copyright 2020, Owen McCusker
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# -----------------------------------------------------------
#
import sys
import logging

from argparse import ArgumentParser
from datetime import datetime
from itertools import chain
from uuid import uuid4

import boto3

from .gsod_directory_list import (
    GsodDirectoryList,
)

from .gsod_data_file_processor import (
    GsodDataFileProcessor,
)

from .gsod_processor import (
    GsodProcesser,
)

def main(argv=None):
    argv = argv or sys.argv[1:]
    parser = ArgumentParser(description='Read VPC Flow Log Records')
    # Required paramters
#    parser.add_argument(
#        'location',
#        type=str,
#        help='CloudWatch Logs group name or S3 bucket/prefix',
#    )
#    parser.add_argument(
#        'action',
#        type=str,
#        nargs='*',
#        default=['print'],
#        help='action to take on log records',
#    )
    # Location paramters
    parser.add_argument(
        '--url',
        type=str,
        default='https://www.ncei.noaa.gov/data/global-summary-of-the-day/access',
        help='url of NOAA gsod directory, without the year default: https://www.ncei.noaa.gov/data/global-summary-of-the-day/access/',
    )
    parser.add_argument(
        '--year', 
        type=str, 
        default='2020', 
        help='year to download, default: 2020'
    )
    parser.add_argument(
        '--thread-count', type=int, help='number of threads used when reading'
    )
    parser.add_argument(
        '--save-gsod-files', type=bool, help='store intermediate gsod files locally in output dir, and using year'
    )
    parser.add_argument(
        '--persist-data', type=bool, help='persist gsod data using mongo'
    )
    parser.add_argument(
        '--gsod-output-pathname', 
        type=str, 
        default='../data/interim/gsod-url-file-list.txt', 
        help='pathname to download the file list: defaults: ../data/interim/gsod-url-file-list.txt'
    )
    parser.add_argument(
        '--output-data-directory', 
        type=str, 
        default='../data', 
        help='base directory holding gsod data'
    )
    args = parser.parse_args(argv)
    
    #                  
    # TODO: move this to the __main__.py
    #
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.INFO)

    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s %(levelname)s %(module)s %(funcName)s %(message)s',
    #                    handlers=[logging.FileHandler("my_log.log", mode='w'),
    #                              stream_handler])
                        handlers=[stream_handler])
    log = logging.getLogger()

    log.info('Starting Weather GSOD ETL - GSOD Data')
    gsodDataListFile = GsodDirectoryList(args.url,
                                     args.year,
                                     args.gsod_output_pathname)

    gsodDataListFile.process_gsod_files()
    
    fileProcessor = GsodDataFileProcessor(args.gsod_output_pathname,
                                args.url,
                                args.year,
                                args.save_gsod_files,
                                args.persist_data,
                                args.output_data_directory)
    
    processor = GsodProcesser(gsodDataListFile, fileProcessor)
    
    processor.process()

    log.info('Finishing Weather GSOD ETL - GSOD Data')

if __name__ == '__main__':
    main()
