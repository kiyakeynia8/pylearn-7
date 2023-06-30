from moviepy import editor
import time

start_time = time.time()

clips=["c_1.mp4",
       "c_2.mp4",
       "c_3.mp4",
       "c_4.mp4",
       "c_5.mp4"]

i = 0
for clip in clips:
    video = editor.VideoFileClip(clip)
    video.audio.write_audiofile(f"{i}.mp3")
    i += 1

end_time = time.time()
print(end_time - start_time)