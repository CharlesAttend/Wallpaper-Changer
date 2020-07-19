# Wallpaper-Changer
Small python script to download a image from Unsplash and set it as windows wallpaper

### Set up the script
1) Create an apps here : https://unsplash.com/oauth/applications
2) Get your keys and your Redirect URI and write them in the python file
3) Set `saveImg` parameter to `True` to save all downloaded image. The images will be named with there description or the date that they have been downloaded.
   If `saveImg` is set to `False`, every image will be named `background` and replace the last downloaded one. 
  
### Automaticly execute the script 
On linux you can use crontab !
On windows use the task scheduler !
Create a task and fill it like this :
![tuto1](/tuto1.png)
Trigger it when you want, don't forget to check `Run task as soon as possible after a scheduled start is missed` in the setting tab. 
You can also check `start only if the following network connection is available` in the Condition tab. 
You don't need admin privileges.
