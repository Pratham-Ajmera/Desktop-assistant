# Python package supporting common text-to-speech engines 
# importing the module 
import wikipedia 
#search what you want
query=input("What do you want to search ")
print("Searching For...",query)
# finding result for the search 
# sentences = 2 refers to numbers of line 
result = wikipedia.summary(query, sentences = 2) 

# printing the result 
print(result) 
