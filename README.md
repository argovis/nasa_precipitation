data: see for example https://gpm1.gesdisc.eosdis.nasa.gov/data/GPM_L3/GPM_3IMERGDF.06/2000/06/, use `dl.sh` and place in `./data`

run: `docker container run -it -v $(pwd)/data:/app/data --network travis argovis/nasaprecip:dev python extract.py`
