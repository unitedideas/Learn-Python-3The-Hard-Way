
import requests

def print_data(f):
    f.read(f)

r = requests.get('https://or.water.usgs.gov/non-usgs/bes/hayden_island.rain')

contents = r.text

print(contents)