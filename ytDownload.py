import yt_dlp

# 設定選項
ydl_opts = {
    'format': 'bestaudio/best',
    'outtmpl': 'joeman',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}

# 填入影片的URL
url = 'https://www.youtube.com/watch?v=PRp3kJtMQwU'

# 建立 yt_dlp 下載器物件
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])