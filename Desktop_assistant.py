def express(text):
    from win32com.client import Dispatch 
    speak = Dispatch("SAPI.Spvoice") 
    speak.Speak(text) 
f=open("kartik.txt","r")
b=f.read()


import datetime

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        express("Good Morning! ")
        

    elif hour>=12 and hour<18:
        express("Good Afternoon! ")   
        

    else:
        express("Good Evening! ")
        
wishMe()
express("I Am Jarvis, Your Virtual Assistant, How can i Help U")
express("I can Help u in various topics like tell me some jokes, wikipedia search, play music, open webcam , news or open recorder")
express("so What do you want from me please enter below")       
query=input("Please Enter ")
express("Here We Go"+query)

if "wikipedia" in query:
    import wikipedia 
    def wikipedia_search():
        query=input("What do you want to search ")
        express("Searching For..."+query)
# finding result for the search 

        result = wikipedia.summary(query, sentences = 2) 
        print(result) 
        express(result)
    wikipedia_search()    
# printing the result 
elif "webcam" in query:
    import cv2
    def open_webcam():
        cv2.namedWindow("preview")
        vc = cv2.VideoCapture(0)

        if vc.isOpened(): # try to get the first frame
            rval, frame = vc.read()
        else:
            rval = False

        while rval:
            cv2.imshow("preview", frame)
            rval, frame = vc.read()
            key = cv2.waitKey(20)
            if key == 27: # exit on ESC
                break
        cv2.destroyWindow("preview")
    open_webcam()
elif "recorder" in query:
    # import required libraries 
    import sounddevice as sd 
    from scipy.io.wavfile import write 
    import wavio as wv 
    def open_recorder():

        freq = 44100
        express("Please Enter the No of Seconds")

        duration = int(input("Enter The Value "))
        express("Recording Started")

        recording = sd.rec(int(duration * freq), 
				samplerate=freq, channels=2) 
        express("Recording Stoped")
        sd.wait() 

        wv.write("recording1.wav", recording, freq, sampwidth=2)
    open_recorder() 
    express("What to open the reccorded file??")
    ans=input("yes or no ")   
    if "y" or "yes" in ans:
        from pygame import mixer 
        def play_audio_recorder():
            mixer.init() 
            mixer.music.load("recording1.wav") 
            mixer.music.set_volume(0.7) 
            mixer.music.play() 
            while True: 
                print("Press 'p' to pause, 'r' to resume") 
                print("Press 'e' to close the recording file") 
                query = input(" ") 
                if query == 'p': 
                    mixer.music.pause()	 
                elif query == 'r': 
                    mixer.music.unpause() 
                elif query == 'e': 
                    mixer.music.stop() 
                    break
        play_audio_recorder()            
elif "news" in query:

    import requests	 
    def play_news(): 
# BBC news api 
        main_url = " https://newsapi.org/v1/articles?source=bbc-news&sortBy=top&apiKey=4dbc17e007ab436fb66416009dfb59a8"
        open_bbc_page = requests.get(main_url).json() 
        article = open_bbc_page["articles"] 
        results = [] 
        for ar in article: 
            results.append(ar["title"]) 
        for i in range(len(results)): 
            print(i + 1, results[i]) 
        print(results)
        express(results)
    play_news()
elif "image" in query:
    from PIL import Image  
    def open_image():
        img = Image.open('ayush.jpg') 

        img.show() 

    open_image()
elif "music" in query:
    def song(path):
        from pygame import mixer 

        mixer.init() 
        mixer.music.load(path) 
        mixer.music.set_volume(0.7) 
        mixer.music.play() 
 
        while True: 
	
	        print("Press 'p' to pause, 'r' to resume") 
	        print("Press 'e' to exit the program") 
	        query = input(" ") 
	
	        if query == 'p': 
		        mixer.music.pause()	 
	        elif query == 'r': 
		        mixer.music.unpause() 
	        elif query == 'e': 

		        mixer.music.stop() 
		        break


    def play_music():
        file_open=open("Music List.txt","r+")
        File_read=file_open.read()
        express("Choose From")
        print(File_read)
        express(File_read)
        express("These are the Songs Which are Loaded What do u Want to play Please enter below")
        take_song=input("Enter the song Name ")
    
        if "burj" in take_song:
            path="burjKhalifa.mp3"
            express("playing burjkalifa")
            song(path)
        elif "care"  in take_song:
            path="care ni Karda.mp3"
            express("playing care ni kerda")
            song(path)
        elif "zila" in take_song:
            path="Zila Helila.mp3"
            express("playing zila helila")
            song(path)
        elif "52" in take_song:
            path="52.mpeg"
            express("playing 52")
            song(path)
        elif "garmi"  in take_song:
            path="Garmi.mp3"
            express("playing germi")
            song(path) 
        elif "o"  in take_song:
            path="O Saki Saki.mp3"
            express("playing o saki saki")
            song(path)
        elif "nach"  in take_song:
            path="Naach Meri Rani.mp3"
            express("playing naach meri rani")
            song(path)
        elif "lagdi"  in take_song:
            path="Lagdi Lahore Di.mp3" 
            express("playing lagdi lahore di")
            song(path)    
        else :    
            express("song is not downloaded")
            print("song is not downloaded")              


    play_music() 
else:
    print("Please enter the valid Query")
    express("Please Enter the valid Query")       


 


