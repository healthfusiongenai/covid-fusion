# covid-fusion

## Overview

This research is focused on SARS-COV-2 transmition leveraging data fusion and machine learning models.

One of the goals of the projects is to establish a data science development lifecycle, that leverages jupyter/python, then moves to create applications from the initial POC to a set of python applications.
Later on, either in java, golang, and/or python. Later POCs and development can easily be focused in a separate project.

There are two major development pipelines facilitated by this project:

- The initial research was done using python-based notebooks which is documented in [notebooks/README-notebooks.md](notebooks/README-notebooks.md).
- The python applications are in the [src](src) directory, and are documented in [src/README-src.md](src/README-src.md).

The layout of the directory structure is conducive to transitional research moving toward development.
The Project structured was based on the [cookiecutter data science project template](https://drivendata.github.io/cookiecutter-data-science/)

This project adheres to the [PEP 518](https://peps.python.org/pep-0518/) standard for building python packages.

## Overall Concepts

The overall concept of this project is to fuse weather data (GSOD), geo locat to geographic extends e.g. counties - focus on humidity, temperature, and wind, along with epidemiological data to create a risk model. Other data sources can be added to the model, such as airport hub, population density, and sentiment on mask use.

The following are the goals of the project:

- Fuse weather data (GSOD), geo locat to geographic extends e.g. counties - focus on humidity, temperature, and wind
- Gather sentiment on mask use
- COVID data transmission is ground truth
- Gather information of "travelness" of county (airport hub)
- Gather information of population density of county
- Create temporary COVID risk-behavior data for D3 visualizations
- Explainable risk, in terms of geolocation of fused health data
- visualization of risk behaviors

### ETL'ing GSOD data

A listing of a years worth of GSOD data is contained in the file ./data/interim/weather/gsod/gsod-url-file-list.txt. This files is currently downloaded ahead of time, for 2020. In the future, we will need to download this first, per year, and then process the files.


GSOD data is downloaded from the [NOAA GSOD](https://www.ncei.noaa.gov/data/global-summary-of-the-day/access/2020/01011099999.csv) website.

## TODO

The following TODO.md file is a list of the next steps for the project.

- [TODO.md](TODO.md)

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
