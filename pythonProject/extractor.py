import requests
from bs4 import BeautifulSoup
import pandas

# Fetching web page content
pages = list()

# Since we have 4 pages we are going to iterate on this number
for i in range(1, 5):
    url = 'https://web.archive.org/web/20121007172955/http://www.nga.gov/collection/anZ' + \
          str(i) + '.htm'
    pages.append(url)

# Storing our data in those lists
names = list()
links = list()

for item in pages:
    page = requests.get(item)

# Parsing
    soup = BeautifulSoup(page.text, 'html.parser')

# Extracting data

# Remove bottom links
    last_links = soup.find('table', {'class': 'AlphaNav'})
    last_links.decompose()

# Pull all text from the BodyText div
    artist_name_list = soup.find('div', {'class': 'BodyText'})

# Pull text from all instances of <a> tag within BodyText div
    artist_name_list_items = artist_name_list.find_all('a')

# Getting all artist's names
    for artist_name in artist_name_list_items:
        fullname = artist_name.text

# print(artist_name.prettify()) / prettify help to get a nice shape of our html tags
        link = 'https://web.archive.org' + artist_name.get('href')

        names.append(fullname)
        links.append(link)

# We store our data in a dictionary using pandas
df = pandas.DataFrame({'name': names, 'link': links})

# We rite to an excel file
df.to_csv("my_file.csv")
