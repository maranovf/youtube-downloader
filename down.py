#!/usr/bin/env python3
import sys
import yt_dlp

def get_url():
    while True:
        url = input("Zadejte URL videa: ").strip()
        if url:
            return url
        print("Musíte zadat URL.")

def download_audio(url: str):
    ydl_opts = {
        'format': 'bestaudio/best',
        #name of output got from YTB title
        'outtmpl': '%(title)s.%(ext)s',
        'postprocessors': [
            {
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            },
            {
                'key': 'FFmpegMetadata',
            },
        ],

        #script obfuscation as a normal client - prevents bot detection
        'extractor_args': {
            'youtube': {
                'player_client': ['mweb', 'android', 'ios'],
            }
        },
        
        'quiet': False,
    }

    try:
        print("\nZahajování stahování")
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print("\nGreat success!")
    except Exception as e:
        print(f"\nErr: {e}", file=sys.stderr)

if __name__ == "__main__":
    try:
        url = get_url()
        download_audio(url)
    except KeyboardInterrupt:
        sys.exit(0)
