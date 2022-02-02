
a="What Should I say"
print(a)
f=open("kartik.txt","r")
b=f.read()
print(b)

# importing requests package 

# importing requests package 
from win32com.client import Dispatch 
speak = Dispatch("SAPI.Spvoice") 
speak.Speak(b)