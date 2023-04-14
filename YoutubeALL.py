import yt_dlp

# Define options for yt-dlp
ydl_opts = {
    'format': 'best',  # Selects the best quality available
    'outtmpl': '%(title)s.%(ext)s',  # Output filename template
    'write_all_thumbnails': False,  # Don't download thumbnails
    'skip_download': False,  # Download the video
}

# Create a YoutubeDL object with the options
ydl = yt_dlp.YoutubeDL(ydl_opts)

# List the available formats for the video
try:
    with ydl:
        ydl.extract_info('https://vimeo.com/817420828', download=False)
except yt_dlp.utils.DownloadError as e:
    print(f"yt-dlp failed for link https://vimeo.com/817420828: {e}")
