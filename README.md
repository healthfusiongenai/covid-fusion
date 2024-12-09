# covid-fusion

## Overview

This research is focusedon SARS-COV-2 transmition leveraging data fusion and machine learning models.

One of the goals of the projects is to establish a data science development lifecycle, that leverages jupyter/python, then moves to create applications from the initial POC, either in java, golang, and/or python. Later POCs and development can easily be focused in a separate project.

The layout of the directory structure is conducive to transitional research moving toward development.

### Overall Concepts

- Fuse weather data (GSOD), geo locat to geographic extends e.g. counties - focus on humidity, temperature, and wind
- Gather sentiment on mask use
- COVID data transmission is ground truth
- Gather information of "travelness" of county (airport hub)
- Gather information of population density of county
- Create temporary COVID risk-behavior data for D3 visualizations
- Explainable risk, in terms of geolocation of fused health data
- visualization of risk behaviors

### TODO

- 2024-12-08 - parsing gsod data writing to screen, need to parse into GsodData class, created a VERSION file for future image creation
  - create a Dockerfile, and Makefile for building and running the project
  - parse csv file ino GsodData class
- 2021-04-11 - start to leverage D3 for visualizating county behavior, think about a risk model
- 2020-04-11 - review what data is available in terms of COVID, understand formats, and access.
- 2021-03-09 - create gsod python library, using text enums for dir names, update directory structure to separate out weather/gsod, instead of having one top level dir in: notebook, and datas
- 2020-08-03 - research geographic information standards, start to choose what standard to follow, find access to data
- 2020-06-23 - start to develop ETL capabilities

## Building and running

- cd into project
- python setup.py develop
  - Installing cv_etl_county_geo script to /Users/owenmccusker/.pyenv/versions/3.10.12/bin
  - Installing cv_etl_gsod script to /Users/owenmccusker/.pyenv/versions/3.10.12/bin

For testing, run (need to create test data directory first):

- cv_etl_gsod --output-data-directory ./data/test/gsod

## References

- I used this page to get started (Written using R): [Intro to the US Counties COVID19 Data](https://www.kaggle.com/code/johnjdavisiv/intro-to-the-us-counties-covid19-data/report)

## Project Organization

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io

The Project structured was based on the [cookiecutter data science project template](https://drivendata.github.io/cookiecutter-data-science/)
