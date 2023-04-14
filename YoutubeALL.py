import requests
import subprocess

def is_channel_working(url, headers=None):
    try:
        cmd = [
            "ffmpeg",
            "-headers",
            f"User-Agent: {headers['User-Agent']}" if headers and "User-Agent" in headers else "User-Agent: python-requests/2.25.1",
            "-i",
            url,
            "-t",
            "10",
            "-f",
            "null",
            "-"
        ]

        process = subprocess.run(cmd, stderr=subprocess.PIPE, universal_newlines=True, timeout=15)
        return process.returncode == 0
    except (subprocess.TimeoutExpired, subprocess.CalledProcessError):
        return False

repo_urls = [
    "https://github.com/punkstarbr/STR-YT/raw/main/REALITY'SLIVE.m3u"
]

working_channels = []

for url in repo_urls:
    m3u_response = requests.get(url)

    if m3u_response.status_code == 200:
        m3u_lines = m3u_response.text.splitlines()

        for i, line in enumerate(m3u_lines):
            if line.startswith("#EXTM3U"):
                working_channels.append({"extm3u_line": line})
            elif line.startswith("#EXTINF"):
                extinf_line = line
                extvlcopt_line = None
                kodiprop_lines = []
                stream_url = None
                headers = {}

                for j in range(i + 1, len(m3u_lines)):
                    next_line = m3u_lines[j]
                    
                    if next_line.startswith("#EXTVLCOPT"):
                        extvlcopt_line = next_line
                        if "http-user-agent" in extvlcopt_line:
                            user_agent = extvlcopt_line.split("=")[1]
                            headers["User-Agent"] = user_agent
                    elif next_line.startswith("#KODIPROP"):
                        kodiprop_lines.append(next_line)
                    elif not next_line.startswith("#"):
                        stream_url = next_line
                        break

                if stream_url:
                    if is_channel_working(stream_url, headers):
                        working_channels.append({
                            "extinf_line": extinf_line,
                            "extvlcopt_line": extvlcopt_line,
                            "kodiprop_lines": kodiprop_lines,
                            "stream_url": stream_url
                        })

with open("lista3.M3U", "w") as f:
    for channel in working_channels:
        if "extm3u_line" in channel:
            f.write(f"{channel['extm3u_line']}\n")
        else:
            f.write(f"{channel['extinf_line']}\n")
            if channel['extvlcopt_line']:
                f.write(f"{channel['extvlcopt_line']}\n")
            for kodiprop_line in channel['kodiprop_lines']:
                f.write(f"{kodiprop_line}\n")
            f.write(f"{channel['stream_url']}\n")
