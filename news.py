
import requests	 

def NewsFromBBC(): 
	
	# BBC news api 
	main_url = " https://newsapi.org/v1/articles?source=bbc-news&sortBy=top&apiKey=4dbc17e007ab436fb66416009dfb59a8"

	open_bbc_page = requests.get(main_url).json() 
	article = open_bbc_page["articles"] 
 
	results = [] 
	
	for ar in article: 
		results.append(ar["title"]) 
		
	for i in range(len(results)): 
		

		print(i + 1, results[i]) 
 
	
	print(news)
	NewsFromBBC() 
