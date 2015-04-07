# zuobiao
Use django to analysis data from zuobiao.me.

## Requirements
* Python 3
* Django 1.8
* PostgreSQL or other database

## Install
    virtualenv -p python3 zuobiaoenv
    pip install -r requirements.txt
Change `zuobiao/settings.py` for your database.

## Import csv data to database
Makesure `zuobiao/2014data.csv` exists([download](http://zuobiao.me/resources/2014data.csv)), then run:

    python tools.py

## Run
    cd zuobiao
    python manage.py runserver

open [admin](http://127.0.0.1:8000/admin).

## Changelog
* 2015-04-01 Init


## Licence
MIT
