from pydub import AudioSegment

# 載入 MP3 音檔
sound = AudioSegment.from_file('joeman.mp3', format='mp3')

# 設定每個分割檔案的長度（單位：毫秒）
#segment_length = 1000000
segment_length = 100000

# 將音檔分割成多個檔案
for i, chunk in enumerate(sound[::segment_length]):
    # 設定分割檔案的檔名
    chunk.export(f'joeman_output_{i}.mp3', format='mp3')