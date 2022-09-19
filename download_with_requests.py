import requests

url = 'https://www1.ncdc.noaa.gov/pub/data/ghcn/daily/readme.txt'
r = requests.get(url, allow_redirects=True)
open('climatology_req', 'wb').write(r.content)
