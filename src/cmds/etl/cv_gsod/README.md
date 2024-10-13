cv_gsod - used to download gsod weather data from NOAA site
==============================

The overall goal of this utility app is to download GSOD data to be used to data science
applications. 

building and running
------------
I created the following dir structure to facilitate development
```
/Users/owenmccusker/Documents/dev/data-science/machine-learning/healthcare/covid-fusion-env
```
cd into the directory and then run

```
cd /Users/owenmccusker/Documents/dev/data-science/machine-learning/healthcare/covid-fusion-env
```

run the ingestor on a directory. The ingestor uses the current directory ./ to parse in data from
```
cv_etl_gsod --gsod-output-pathname=./test.csv
```



- cd into project  (make a env)
- python setup.py develop
- /Users/owenmccusker/.pyenv/versions/3.10.2/bin/cv_etl_gsod
- ~> cv_etl_gsod --output-pathname=./test.csv

```
➜  covid-fusion-env cv_etl_gsod --output-pathname=./test.csv
2022-05-29 14:12:15,167 INFO __main__ main Starting Weather GSOD ETL - GSOD Data
2022-05-29 14:12:15,167 INFO gsod_directory_list __init__ gsodDirectoryList initialized with:
2022-05-29 14:12:15,167 INFO gsod_directory_list __init__   url:             https://www.ncei.noaa.gov/data/global-summary-of-the-day/access
2022-05-29 14:12:15,167 INFO gsod_directory_list __init__   year:            2020
2022-05-29 14:12:15,167 INFO gsod_directory_list __init__   output_pathname: ./test.csv
2022-05-29 14:12:15,167 INFO gsod_directory_list get_GSOD_file_list reading NOAA directory: https://www.ncei.noaa.gov/data/global-summary-of-the-day/access/2020
2022-05-29 14:12:15,167 INFO gsod_directory_list get_GSOD_file_list file exists.
2022-05-29 14:12:15,168 INFO __main__ main Finishing Weather GSOD ETL - GSOD Data
```



References
------------

- I used this page to get started (Written using R): https://www.kaggle.com/code/johnjdavisiv/intro-to-the-us-counties-covid19-data/report


TODO
------------

- 2022-05-29 - start to add in arguments to filter e.g. specific days, and to also persist data into various data repos: CSV, mongo, postgresql.
