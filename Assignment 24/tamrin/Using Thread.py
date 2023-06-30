from moviepy import editor
from threading import Thread
import time

start_time = time.time()

def conversion(clip,i):
    video = editor.VideoFileClip(clip)
    video.audio.write_audiofile(f"{i}.mp3")

clips=["c_1.mp4",
       "c_2.mp4",
       "c_3.mp4",
       "c_4.mp4",
       "c_5.mp4"]

i = 0
threads = []
for clip in clips:
    new_thread = Thread(target=conversion,args=[clip,i])
    threads.append(new_thread)
    i += 1

for t in threads:
    t.start()

for t in threads:
    t.join()

end_time = time.time()
print(end_time - start_time)

