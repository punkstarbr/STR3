import youtube_dl

# Define options for youtube-dl
ydl_opts = {
    'write_all_thumbnails': False,  # Don't download thumbnails
}

# Create a YoutubeDL object with the options
ydl = youtube_dl.YoutubeDL(ydl_opts)

# List the available formats for the video
try:
    with ydl:
        info = ydl.extract_info('https://vimeo.com/817420828', download=False)
        formats = info['formats']
        for f in formats:
            print(f['format_id'], f['ext'], f['format_note'])
except youtube_dl.DownloadError as e:
    print(f"youtube-dl failed for link https://vimeo.com/817420828: {e}")
