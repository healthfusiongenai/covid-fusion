# covid-fusion - python applications src

This directory contains the python applications for the covid-fusion project.

The focus so far is on the weather data (GSOD) and the epidemiological data (COVID-19). This is a work in progress.

## cv_etl_gsod - Covid ETL GSOD

This application is used to extract, transform, and load the GSOD weather data into a database. For more information see the [README.md](cmds/etl/cv_gsod/README.md) file in the `cv_gsod` directory.

## cv_county_geo

This application is used to extract, transform, and load the county geo data into a database. For more information see the [README.md](cmds/etl/cv_county_geo/README.md) file in the `cv_county_geo` directory.

### Gathering test GSOD data

There are a number of parameters that can be used to control the behavior of the application. They include:

- --output-data-directory: The directory to store the output data.
- --gsod-data-directory: The directory to store the GSOD data.
- --gsod-data-file: The file to store the GSOD data.

```bash
cv_etl_gsod --output-data-directory ./data/test/gsod
```

Currently, the 2020 GSOD file listing is downloaded ahead of time, and we can only process year 2020. The file listing is stored in the `gsod-url-file-list.txt` file, and parsed by the `GsodProcesser` class. For each line in the file, the `GsodProcesser` class will download the file, and call on the `GsodDataFileProcessor` class to process the file, as is seen by the output below.

Output to the console looks like this (NOTE: for year 2020: there are 12299 files to download and parse):

```console
2024-12-09 20:30:49,446 INFO gsod_data_file_processor process_GSOD_file finished processig file
2024-12-09 20:30:49,446 INFO gsod_processor process Reading 5 of 12299: Line-5: https://www.ncei.noaa.gov/data/global-summary-of-the-day/access/2020/01003099999.csv
2024-12-09 20:30:49,446 INFO gsod_data_file_processor process_GSOD_file processing gsod file from url https://www.ncei.noaa.gov/data/global-summary-of-the-day/access/2020/01003099999.csv
2024-12-09 20:30:49,446 INFO gsod_data_file_processor _store_gsod_file_locally processing file https://www.ncei.noaa.gov/data/global-summary-of-the-day/access/2020/01003099999.csv, saving gsod file to ./data/test/gsod/2020
2024-12-09 20:30:49,718 INFO gsod_data_file_processor _process_file processing gsod data from file
2024-12-09 20:30:49,719 INFO gsod_data_file_processor _process_file processing 277 gsod data items
2024-12-09 20:30:49,719 INFO gsod_data_file_processor _process_file processing line "STATION","DATE","LATITUDE","LONGITUDE","ELEVATION","NAME","TEMP","TEMP_ATTRIBUTES","DEWP","DEWP_ATTRIBUTES","SLP","SLP_ATTRIBUTES","STP","STP_ATTRIBUTES","VISIB","VISIB_ATTRIBUTES","WDSP","WDSP_ATTRIBUTES","MXSPD","GUST","MAX","MAX_ATTRIBUTES","MIN","MIN_ATTRIBUTES","PRCP","PRCP_ATTRIBUTES","SNDP","FRSHTT"
2024-12-09 20:30:49,719 INFO gsod_data_file_processor _process_file processing line "01003099999","2020-01-01","77.0","15.5","12.0","HORNSUND, NO","   9.6","24","   5.1","24"," 991.6","24","990.2","24"," 14.8"," 8"," 13.8","24"," 25.3","999.9","  11.7"," ","   5.7"," "," 0.00","G","  4.3","000000"
2024-12-09 20:30:49,719 INFO gsod_data_file_processor _process_file processing line "01003099999","2020-01-02","77.0","15.5","12.0","HORNSUND, NO","   8.9","24","   0.0","24"," 988.5","24","987.1","24"," 19.4"," 8"," 19.7","24"," 31.1","999.9","  12.0","*","   4.3","*"," 0.00","G","  4.3","000000"
2024-12-09 20:30:49,719 INFO gsod_data_file_processor _process_file processing line "01003099999","2020-01-03","77.0","15.5","12.0","HORNSUND, NO","   6.7","24","  -3.6","24"," 983.2","24","981.8","24","  9.0"," 8"," 18.0","24"," 35.0","999.9","   9.7"," ","   3.2"," "," 0.00","G","  3.9","001000"
2024-12-09 20:30:49,719 INFO gsod_data_file_processor _process_file processing line "01003099999","2020-01-04","77.0","15.5","12.0","HORNSUND, NO","   5.8","24","  -3.6","24"," 990.2","24","988.8","24"," 25.6"," 8","  4.8","24","  9.7","999.9","  11.1"," ","  -0.0"," "," 0.00","G","  3.5","000000"
...
...
...
```
