# Name: FLARE
# my_name_is ='Flare'
import wikipedia
import datetime
import cv2
import time
import speech_recognition
import pyttsx3
import webbrowser
import subprocess
import os
import random
import smtplib
import pywhatkit
from goto import goto
import pyautogui
import keyboard as k
import pyjokes
wished=False

f=open("C:\\Users\\Dell\\PycharmProjects\\firstprog\\name_of_flare.txt",'r+')
my_name_is=f.read()
f.seek(0,0)
contacts = {'anjali':'+919717756404','pranshu':'+919773757123'}
dic = {"pranshu": "sapphiregoel@gmail.com", "emerald": "emeraldgoel@gmail.com"}

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty("rate", 180)
engine.setProperty('voice', voices[1].id)


def speak(text):
    engine.say(text)
    engine.runAndWait()


def wish():
    hour = int(datetime.datetime.now().hour)
    if hour < 12:
        speak("Good morning!")
    elif hour < 18:
        speak("Good afternoon!")
    else:
        speak("Good evening!")
    speak(f"I am your friend {my_name_is}. How may I help you?")


def listen():
    inp = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening...")
        inp.energy_threshold = 900
        inp.pause_threshold = 0.6
        audio = inp.listen(source)
    try:
        print("Recognizing...")
        data = inp.recognize_google(audio, language='en-in')
        print(f"You said: {data}")
    except Exception:
        speak("Pardon,Can you say that again?")
        # return "None"
        return listen()
    if data.lower() == 'stop':
        goto(90)
    return data.lower()


def sendemail(recieved_by, contents):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    f_o=open("C:\\Users\\Dell\\PycharmProjects\\firstprog\\myemail.txt","r")
    em=f_o.readline()
    p=f_o.readline()
    server.login(em,p)
    sub="None"
    while sub=='None':
        speak("May I know the subject?")
        sub = listen()
    contents = "SUBJECT:"+sub+"\n\n"+contents
    server.sendmail('emeraldgoel@gmail.com', recieved_by, contents)
    server.close()






if __name__=="__main__":
    key=True
    if wished==False:
        wish()
        wished=True
    while key:
        query=listen().lower()
        if "wikipedia" in query :
            speak("Please wait. Searching Wikipedia.")
            query = query.replace("according to wikipedia", "")
            query = query.replace("can you kindly tell me about", "")
            query = query.replace("can you tell me about", "")
            query = query.replace("can you please tell me about", "")
            query = query.replace("tell me about", "")
            results=wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            speak(results)
        elif "quit" in query:
            key=False
        elif "open youtube" in query:
            webbrowser.open("youtube.com")
        elif "open google" in query:
            webbrowser.open("google.com")
        elif "play music" in query or "play songs" in query or "play song" in query:
            music_dir="D:\\my_music"
            songs=os.listdir(music_dir)
            speak("Available songs are:")
            for i in songs:
                s=i
                l=s.rsplit(".",1)
                print(l[0])
                speak(l[0])
            speak("Would you like to specify the song?")
            answer=listen().lower()
            if answer !="yes":
                a = random.randint(0, len(songs) - 1)
                os.startfile(os.path.join(music_dir, songs[a]))
            else:
                speak("Song name please.")
                flag=1
                while flag :
                    s=listen().lower()
                    for i in songs:
                        if s in i.lower():
                            os.startfile(os.path.join(music_dir,i))
                            flag=0
                            break
                    if flag==1:
                        speak("please repeat the name")
        elif "time" in query:
            s_time=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Time is {s_time}")
            print("TIME: ",s_time)
        elif "open v s code" in query or "open vscode" in query or "open vs code" in query:
            vs_c_path="C:\\Users\\Dell\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(vs_c_path)
        elif 'email to' in query:
            try:
                receiver=""
                l=query.split()
                flag=0
                for i in l:
                    if flag==1:
                        receiver=i
                        break
                    if i=="to":
                        flag=1
                speak("What should i say?")
                content=listen()
                if receiver not in dic:
                    speak("Not in contacts")
                    continue
                to=dic[receiver]
                sendemail(to,content)
                speak("Done")
            except Exception:
                speak("Sorry, something went wrong.")
        elif 'whatsapp' in query:
            try:
                name=""
                s=""
                while name not in contacts:
                    speak('May i know the person name?')
                    name = listen()
                    s = contacts[name]
                speak('May i know the message?')
                msg = listen()
                h = datetime.datetime.now().hour
                m = datetime.datetime.now().minute
                m += 3
                if m > 60:
                    h += 1
                    m = m % 60
                pywhatkit.sendwhatmsg(s,msg,h,m)
                pyautogui.click(1313, 708)
                k.press_and_release('enter')
            except Exception:
                speak('Sorry something went wrong!')
        elif 'search' in query and 'youtube' in query:
            try:
                query = query.replace('on youtube', '')
                query = query.replace('in youtube', '')
                query=query.replace('youtube', '')
                query=query.replace("search", "")
                pywhatkit.playonyt(query)
            except Exception:
                speak('Sorry something went wrong!')
        elif 'search' in query and 'google' in query:
            try:
                query = query.replace('on google', '')
                query = query.replace('in google', '')
                query=query.replace('google', '')
                query=query.replace("search", "")
                pywhatkit.search(query)
            except Exception:
                speak('Sorry something went wrong!')
        elif 'change' in query and 'name' in query:
            speak('What would you like to call me?')
            my_name_is=listen()
            f.write(my_name_is)
            f.write("                                                               ")
            speak(f'So from now i am {my_name_is}')
        elif 'joke' in query or 'jokes' in query:
            speak(pyjokes.get_joke())
        elif 'question' in query:
            import wolframalpha
            speak('What would you like to search?')
            q=listen()
            speak('Got it')
            f_o=open("C:\\Users\\Dell\\PycharmProjects\\firstprog\\wol_flare.txt","r")
            app_id =f_o.readline()
            client = wolframalpha.Client(app_id)
            res = client.query(q)
            answer = next(res.results).text
            speak(answer)
            print(answer)
        elif 'news' in query:
            import requests
            import json
            r = requests.get("https://newsapi.org/v2/top-headlines?sources=bbc-news&apiKey=53b56b1334e9495998758fddda7a2e16")
            parsed = json.loads(r.content)
            speak('So the news is')
            count = 1
            for i in parsed['articles']:
                speak(count)
                print(count, ":", i["title"])
                speak(i["title"])
                count += 1
        elif 'lock window' in query:
            speak('locking')
            import ctypes
            ctypes.windll.user32.LockWorkStation()
        elif 'shutdown system' in query:
            speak('Just a second')
            subprocess.call('shutdown /p /f')
        elif 'sleep' in query:
            speak('for how long should i sleep?')
            try:
                a=int(listen())
            except Exception:
                speak("kindly just say the number of seconds")
                try:
                    a=int(listen())
                except Exception:
                    speak('sorry')
                    continue
            speak(f'I won\'t disturb you for {a} seconds')
            time.sleep(a)
        elif 'restart' in query:
            subprocess.call(["shutdown","/r"])
        elif 'hibernate' in query:
            speak('hibernating')
            subprocess.call('shutdown /h')
        elif "take a picture"in query or"take a photo"in query or"camera"in query:
            a='None'
            while a=="None":
                speak("what name would you like?")
                a=listen()
            cam_port = 0
            cam = cv2.VideoCapture(cam_port)
            result, image = cam.read()
            if result:
                cv2.imshow(a, image)
                a += '.jpg'
                a='F:\\python_fun\\'+a
                cv2.imwrite(a, image)
            cam.release()
            cv2.destroyAllWindows()
        elif "video" in query:
            cap=cv2.VideoCapture(0)
            if cap.isOpened()==False:
                print("Sorry, unable to open camera")
                continue
            name="None"
            while name=="None":
                speak('What would you like to same it as?')
                name=listen()
            speak('Remember to press s to stop')
            f_w=int(cap.get(3))
            f_h=int(cap.get(4))
            video_cod=cv2.VideoWriter_fourcc(*'XVID')
            name+='.avi'
            name='F:\\python_fun\\'+name
            vedio_out=cv2.VideoWriter(name,video_cod,10,(f_w,f_h))
            result,frame=cap.read()
            while result:
                vedio_out.write(frame)
                cv2.imshow(name,frame)
                if cv2.waitKey(1)& 0xFF==ord('s'):
                    break
                result, frame = cap.read()
            cap.release()
            vedio_out.release()
            cv2.destroyAllWindows()
            speak('Done')
        elif 'make note' in query:
            speak('What should i note?')
            note=listen()
            try:
                file=open("F:\\python_fun\\flare_notes.txt",'w')
                choice="None"
                while choice=="None":
                    speak('Do you want date to be included?')
                    choice=listen()
                if 'yes' in choice or 'ok' in choice or 'sure' in choice:
                    s_t=datetime.datetime.now().strftime("%H:%M:%S")
                    file.write(s_t)
                    file.write(': ')
                file.write(note)
                speak("Done")
            except Exception:
                speak("Couldn't open the file")
        elif 'speak note' in query or 'show note' in query or 'speak notes' in query or 'show notes' in query:
            try:
                file=open("F:\\python_fun\\flare_notes.txt",'r')
                data=file.read()
                print(data)
                speak(data)
            except Exception:
                speak("No note available")
        elif "alarm" in query:
            i=False
            while True:
                speak('At what hour should it ring?')
                try:
                    h=int(listen())
                except Exception:
                    speak("Invalid input")
                    i=True
                    break
                if h>-1 and h<25:
                    break
            while True & i==False:
                speak('And how many minutes?')
                try:
                    m = int(listen())
                except Exception:
                    speak("Invalid input")
                    i=True
                    break
                if m > -1 and m < 60:
                    break
            if i==True:
                continue
            while datetime.datetime.now().hour!=h or datetime.datetime.now().minute!=m:
                time.sleep(60)
            os.startfile('D:\\my_music\\BTS EUPHORIA.mp3')
        elif "todays date" in query or "today's date" in query:
            speak(datetime.date)
        elif "todays day" in query or "today's day" in query:
            speak(datetime.datetime.day)
    speak("Bye bye miss")





