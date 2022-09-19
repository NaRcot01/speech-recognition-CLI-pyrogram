from vosk import Model,KaldiRecognizer
import pyaudio
import wave
import sys
import json
from pydub import AudioSegment
def speachR(audio_file_name:str) -> str : 
    
    """ convert ogg to wave format """
    
    sound = AudioSegment.from_ogg(r"downloads/{}".format(audio_file_name))
    sound.export("converted/converted.wav", format="wav")
    sound = AudioSegment.from_wav("converted/converted.wav")
    sound = sound.set_channels(1)
    sound = sound.set_sample_width(2)
    sound.export("converted/converted.wav", format="wav")
    
    """ open audio file and check it """
    
    wf=wave.open('converted/converted.wav','rb')
    if wf.getnchannels() != 1 or wf.getsampwidth() != 2 or wf.getcomptype() != "NONE":
        print("Audio file must be WAV format mono PCM.")
        print(wf.getnchannels())
        print(wf.getsampwidth())
        print(wf.getcomptype())
        sys.exit(1)
        
    """ speech recognition model """
    
    model=Model(r"Path/To/The/Model")
    recognizer=KaldiRecognizer(model,16000)

    """ for using mic instead of audio file """
    # mic=pyaudio.PyAudio()
    # stream=mic.open(format=pyaudio.paInt16,channels=1,rate=16000,input=True,frames_per_buffer=8192)
    # stream.start_stream()

    rec = KaldiRecognizer(model, wf.getframerate())
    rec.SetWords(True)
    rec.SetPartialWords(True)

    while True:
        data = wf.readframes(4000)
        if len(data) == 0:
            break
        if rec.AcceptWaveform(data):
            pass
        
    text=rec.FinalResult()
    text = json.loads(text)
    return text['text']
    
if "__main__" == __name__:
    # if you wan to test the speech recognition, Put your ogg format audio file named "test.ogg" in "downloads" Folder.
    hello_world=speachR("test.ogg")
    print(hello_world)