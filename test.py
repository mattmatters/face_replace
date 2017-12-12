import requests
from face_replace import replace_faces

FILE_PATH = './image.jpg'
URL = 'https://static01.nyt.com/images/2017/12/12/us/12Alabama1/12Alabama1-facebookJumbo.jpg'

img = requests.get(URL).content

newIm = replace_faces(img, "./dmx-head.png")
newIm.save('./test_good/new.png')
