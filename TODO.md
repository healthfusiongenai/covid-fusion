# COVID-FUSION TODO.md

This is TODO.md to manage the project.

The initial goal is focused on ETL'ing the GSOD weather data into a database, and county geo data. This data will be used to create a simple model that looks a rate of changes in the weather data, and the rate of changes in the COVID-19 data.

## Todo

- [ ] create a Dockerfile, and Makefile for building and running the project
- [ ] add in exception handling
- [ ] parse csv file ino GsodData class
- [ ] create the cv_county_geo application

### In Progress

- [ ] 2024-12-08 - parsing gsod data writing to screen, need to parse into GsodData class, created a VERSION file for future image creation

### Done ✓

- [x] 2021-04-11 - start to leverage D3 for visualizating county behavior, think about a risk model
- [x] 2020-04-11 - review what data is available in terms of COVID, understand formats, and access.
- [x] 2021-03-09 - create gsod python library, using text enums for dir names, update directory structure to separate out weather/gsod, instead of having one top level dir in: notebook, and datas
- [x] 2020-08-03 - research geographic information standards, start to choose what standard to follow, find access to data
- [x] 2020-06-23 - start to develop ETL capabilities
- [x] Create my first TODO.md  
