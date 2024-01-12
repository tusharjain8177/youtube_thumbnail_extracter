import pytube
import urllib.request

def get_thumbnail(url):
    video = pytube.YouTube(url)
    thumbnail_url = video.thumbnail_url
    return thumbnail_url

def download_thumbnail(url):
    video = pytube.YouTube(url)
    thumbnail_url = video.thumbnail_url
    urllib.request.urlretrieve(thumbnail_url, "download.jpg")


