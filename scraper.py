import requests;

url = 'https://hacker-news.firebaseio.com/v0/beststories.json'
req = requests.get(url);
data = list(req.json());

for i in data:
	url = 'https://hacker-news.firebaseio.com/v0/item/' + str(i)+'.json';
	req = requests.get(url);
	print(dict(req.json())['title']);
	
