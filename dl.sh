DIR=https://gpm1.gesdisc.eosdis.nasa.gov/data/GPM_L3/GPM_3IMERGDF.06/2000/06/
wget --load-cookies .urs_cookies --save-cookies .urs_cookies --keep-session-cookies -r -c -nH -nd -np -A nc4 --content-disposition $DIR
