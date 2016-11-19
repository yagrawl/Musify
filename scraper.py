import urllib2
from bs4 import BeautifulSoup
from clarifai.rest import ClarifaiApp
from clarifai.rest import Image as CImage
import requests
from os import system 
opener = urllib2.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0')]


label = 'action'
url = "https://pixabay.com/en/photos/?q=" + label

r  = requests.get(url)

data = r.text

soup = BeautifulSoup(data)
bparse = ''
images = []
i = 0
for link in soup.find_all('img'):
    bparse = link.get('data-lazy-srcset')
    if bparse is None:
        continue
    index = bparse.find(',') + 2
    
    system('wget --no-check-certificate -O pics/' + label + str(i) + ' '+ bparse[index:-3] )
    i+= 1
