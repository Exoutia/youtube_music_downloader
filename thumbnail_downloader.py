import urllib.request

import pytube

from main import main


def download_thumbnail(filename):
    search_video_res = pytube.Search(filename)
    video = search_video_res.results[0]
    thumbnail_url = video.thumbnail_url
    urllib.request.urlretrieve(thumbnail_url, filename.replace(" ", "_") + ".jpg")


def download_thumbnail_two(filename):
    search = pytube.Search(filename)
    video = search.results[0]
    thumbnail_url = video.thumbnail_url
    print(thumbnail_url)
    with urllib.request.urlopen(thumbnail_url) as res:
        data = res.read()
        with open(filename.replace(" ", "_") + "url_open.jpg", "wb") as f:
            f.write(data)


def download_thumbnail_using_url(url, filename):
    video = pytube.YouTube(url)
    thumbnail_url = video.thumbnail_url
    print(thumbnail_url)
    urllib.request.urlretrieve(
        thumbnail_url, filename.replace(" ", "_") + "using_link.jpg"
    )

# TODO: Find the right method to download the thumbnail from youtube.

if __name__ == "__main__":
    download_thumbnail_using_url("https://youtube.com/watch?v=WszNqHKwQbk", "bohoo")
