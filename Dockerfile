FROM python:3.11

RUN apt-get update -y
RUN apt-get install -y nano
RUN pip install nose netCDF4 pymongo xarray numpy geopy scipy
RUN apt-get install -y fio

WORKDIR /app
COPY extract.py extract.py
RUN chown -R 1000660000 /app
