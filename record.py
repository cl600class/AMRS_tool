# -*- coding: utf-8 -*-
import threading
import pyaudio
import wave
import speech_recognition as sr
import time
#import tkinter as tk
from datetime import date
index=0
flag=0
speaker_t = ""
global f
def recording(time1,speaker):
    #open the wav file
    wav = sr.AudioFile("Oldboy.wav")
    r = sr.Recognizer()

    #setting the parameter of recording
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 44100
    RECORD_SECONDS = time1

    #setting the outputfile 


    #submit transformation job to google
    def job(): 
        #print("start")
        with wav as source:
            audio = r.record(source)
            try:
                pre = r.recognize_google(audio, language='zh-TW')
                #pre = r.recognize_google(audio, language='en-US', show_all=True)
                f.write(speaker+": "+str(pre)+'\n')
            except:
                pass
            #print(speaker+": "+pre)
            #tt.insert('end',speaker+": "+str(pre)+'\n')
        #print("done")

    #turn on the micphone and recording     
    with sr.Microphone() as source:
        #read the white noise 
        #doing recording until quit
        #call model recording 
        p = pyaudio.PyAudio()
        stream = p.open(format=FORMAT,
                        channels=CHANNELS,
                        rate=RATE,
                        input=True,
                        frames_per_buffer=CHUNK)
        #start recording 
        print("開始錄音,請說話......")
        tStart = time.time()
        frames = []
        tpre = 0
        for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
            data = stream.read(CHUNK)
            frames.append(data)
            t = int (RECORD_SECONDS-time.time()+tStart)
            if t != tpre:
                tpre = t
                print("\r"+"remain: "+str(t)+"/"+str(RECORD_SECONDS)+"(s)",end="")
                #entry1.delete(0,tk.END)
                #entry1.insert(0,t)
        print("\n錄音結束!\n")
        #tt.insert('end',"結束錄音\n")

        stream.stop_stream()
        stream.close()
        p.terminate()
        #wave processing 
        WAVE_OUTPUT_FILENAME = "Oldboy.wav"
        wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(p.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(frames))
        wf.close()
        # muti-task sub job to google
        try:
            t = threading.Thread(target = job)
            t.start()
        except:
            pass
        # ask for next speaker 
        #speaker = input("Speaker: ")
    flag =0

if __name__ == "__main__":
    meeting = "DSP Final"
    print("==================================\n\n"+meeting+"\n")
    today = date.today().strftime("%B %d, %Y")
    print(today+"\n\n==================================\n")
    name1 = input("主席：")
    name2 = input("與會1：")
    name3 = input("與會2：")
    settingtime=int(input("每人發言時間(秒)："))
    f =open("f.txt","w")
    r = sr.Recognizer()
    print("Please wait. Calibrating microphone...")
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=5)

    f.write("=============會議記錄============="+'\n')
    f.write("會議名稱: "+meeting+'\n')
    f.write("會議日期: "+today+'\n')
    f.write("主席: "+name1+'\n')
    f.write("列席: "+name2+'\n')
    f.write("列席: "+name3+'\n')
    f.write("=================================="+'\n')
    message = "發言者 ("+name1+":1 "+name2+":2 "+name3+":3 離開:q)："
    while(True):
        speaker_t = input(message)
        if(speaker_t=="1"):
            name = name1
        elif(speaker_t=="2"):
            name = name2
        elif(speaker_t=="3"):
            name = name3
        else:
            break
        recording(settingtime, name)
    f.close()