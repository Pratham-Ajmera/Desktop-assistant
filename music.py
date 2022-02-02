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