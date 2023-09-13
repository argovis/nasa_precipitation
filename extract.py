import xarray, numpy, scipy
from pymongo import MongoClient

client = MongoClient('mongodb://database/argo')
db = client.argo

xar = xarray.open_dataset('data/3B-DAY.MS.MRG.3IMERG.20000601-S000000-E235959.V06.nc4')

raw = numpy.nan_to_num(xar['HQprecipitation'][0].to_numpy())
raw[raw<1] = 0 # less than this threshold effectively counts as no precipitation
lon = xar['lon'].to_numpy()
lat = xar['lat'].to_numpy()
storms = scipy.ndimage.label(raw, structure=[[1,1,1],[1,1,1],[1,1,1]])

#print(numpy.unique(storms[0]))
#print(numpy.shape(raw))
#print(xar['time'].to_numpy()[0].isoformat())

docs = [{'_id': f'{i}_{xar["time"].to_numpy()[0].isoformat()[0:10]}', 'data':[[]], 'raster':[]} for i in range(storms[1]+1)]

for lonidx in range(3600):
    for latidx in range(1800):
        groupnumber = storms[0][lonidx][latidx]
        if groupnumber == 0:
            continue
        docs[groupnumber]['data'][0].append(raw[lonidx][latidx].item())
        docs[groupnumber]['raster'].append({'type':'Point', 'coordinates':[lon[lonidx].item(),lat[latidx].item()]})

db.precip.insert_many(docs[1:])