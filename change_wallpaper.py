from unsplash.api import Api
from unsplash.auth import Auth
from requests import get

from datetime import datetime
from pathlib import Path
import os, ctypes

saveImg = False #True to save all image
client_id = ""
client_secret = ""
redirect_uri = ""

def download(url, file_name):
    # open in binary mode
    with open(file_name, "wb") as file:
        # get request
        response = get(url)
        # write to file
        file.write(response.content)

def change_wallpaper(img_name):
    path = os.path.join(os.getcwd(), img_name) #absolute path needed
    print(path)
    ctypes.windll.user32.SystemParametersInfoW(20, 0, path, 3) #this line set the wallpaper 
    print("Wallpapper set !")

def get_img():
    auth = Auth(client_id, client_secret, redirect_uri)
    api = Api(auth)
    photo = api.photo.random(query="Wallpaper", orientation="landscape")[0]

    #finding the format of the image from the download link
    link = photo.urls.full
    n = link.find('fm=')
    m = n + link[n:].find('&')
    forma = link[n+3:m]

    if saveImg:
        try:
            name = photo.alt_description.replace(" ", "_") + '.' + forma
        except:
            name = str(datetime.now())+ forma
    else:
        #find the img format to delete it 
        name = 'background.'+forma
        files = os.listdir()
        for i in range(len(files)):
            if files[i].startswith("background."):
                #remove old image
                try:
                    os.remove(files[i])
                except:
                    raise Warning("background file not found, not removing")

    download(link, name)
    return name

change_wallpaper(get_img())