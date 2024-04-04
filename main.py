import os
import sys

from pytube import YouTube  # type: ignore

path = os.path.dirname(os.path.abspath(__file__))


class Downloader:
    def __init__(self, url: str, path: str, name: str, audio: bool):
        self.url = url
        self.path = path
        self.name = name
        self.type = "audio" if audio else "video"
        self.stream = None

    @staticmethod
    def get_size(stream: YouTube.streams) -> str:
        ext = "kb"
        size = stream.filesize_kb
        if size > 1024:
            ext = "mb"
            size = stream.filesize_mb
        if size > 1024:
            ext = "gb"
            size = stream.filesize_gb
        return str(size) + ext

    def select_stream(self) -> None:
        streams = YouTube(self.url, on_complete_callback=print).streams.filter(
            type=self.type
        )
        for stream in enumerate(streams):
            human_readable_size = self.get_size(stream[1])
            if self.type == "video":
                print(
                    f"{stream[0]}: {stream[1].resolution} - {stream[1].fps}fps - {human_readable_size}"
                )
            else:
                print(f"{stream[0]}: {stream[1].abr} - {human_readable_size}bytes")

        index = int(input("Enter num: "))
        itag = streams[index].itag
        self.stream = streams.get_by_itag(itag)

    def download(self) -> None:
        self.select_stream()
        print(self.stream)
        self.stream.download(self.path, self.name)


def main():
    if 4 < len(sys.argv) < 2:
        print("Usage: python main.py <url> <name> <audio_only>")
        sys.exit(1)

    url = sys.argv[1]
    d_path = path
    name = sys.argv[2]
    audio_only = sys.argv[3] if len(sys.argv) == 4 else False

    name.replace(" ", "_")
    name.replace(".", "_")
    if audio_only:
        name += ".mp3"
    else:
        name += ".mp4"

    downloader = Downloader(url, d_path, name, audio_only)
    downloader.download()


# TODO: add help and different usage for functions call

if __name__ == "__main__":
    main()
