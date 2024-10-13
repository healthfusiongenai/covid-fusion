#  Copyright 2020
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
import sys

from argparse import ArgumentParser
from datetime import datetime
from itertools import chain
from uuid import uuid4

import boto3

def main(argv=None):
    argv = argv or sys.argv[1:]
    parser = ArgumentParser(description='Read VPC Flow Log Records')
    # Required paramters
    parser.add_argument(
        'location',
        type=str,
        help='CloudWatch Logs group name or S3 bucket/prefix',
    )
    parser.add_argument(
        'action',
        type=str,
        nargs='*',
        default=['print'],
        help='action to take on log records',
    )
    # Location paramters
    parser.add_argument(
        '--location-type',
        type=str,
        help='location type (CloudWatch Logs or S3), default is cwl',
        choices=['cwl', 's3'],
        default='cwl',
    )
    parser.add_argument(
        '--region', type=str, default='', help='AWS region for the location'
    )
    # Time filter paramters
    parser.add_argument(
        '--start-time',
        '-s',
        type=str,
        help='return records at or after this time',
    )
    parser.add_argument(
        '--end-time', '-e', type=str, help='return records before this time'
    )
    parser.add_argument(
        '--time-format',
        type=str,
        default='%Y-%m-%d %H:%M:%S',
        help='format of time to parse',
    )
    # Other filtering parameters
    parser.add_argument(
        '--fields',
        type=str,
        help='Log line format (CWL only)',
    )
    parser.add_argument(
        '--filter-pattern',
        type=str,
        help='return records that match this pattern (CWL only)',
    )
    parser.add_argument(
        '--include-accounts',
        type=str,
        help='comma-separated list of accounts to consider (S3 only)',
    )
    parser.add_argument(
        '--include-regions',
        type=str,
        help='comma-separated list of regions to consider (S3 only)',
    )
    # AWS paramters
    parser.add_argument(
        '--profile',
        type=str,
        default='',
        help='boto3 configuration profile to use',
    )
    parser.add_argument(
        '--role-arn', type=str, help='assume role specified by this ARN'
    )
    parser.add_argument(
        '--external-id',
        type=str,
        help='use this external ID for cross-account acesss',
    )
    parser.add_argument(
        '--thread-count', type=int, help='number of threads used when reading'
    )
    args = parser.parse_args(argv)

    # Confirm the specified boto session arguments are valid
    if args.external_id and not args.role_arn:
        print('must give a --role-arn if an --external-id is given')
        return

#    reader = get_reader(args)
#    action_method(reader, *args.action[1:])


if __name__ == '__main__':
    main()
