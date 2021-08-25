import sounddevice as sd
from scipy.io.wavfile import write
import datetime

# frequency record avg [44100 - 48000]
frame = 44100
# second
time = 5
print("start")
record = sd.rec(int(frame*time), samplerate=frame, channels=1)
sd.wait()
print(record)
# filename = str(datetime.datetime.now().strftime("%d %b %Y_%H%M%S")) + ".wav"
# write(filename, frame, record)
# print("done")