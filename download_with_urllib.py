from urllib.request import urlopen

url = "https://www1.ncdc.noaa.gov/pub/data/ghcn/daily/readme.txt"
save_as = "climatology.txt"

# Download from URL
with urlopen(url) as file:
    content = file.read().decode()

# Save to file
with open(save_as, 'w') as download:
    download.write(content)