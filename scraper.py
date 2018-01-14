import requests;
from jsonrpclib.jsonrpc import ServerProxy
from pprint import pprint

class OpenNLP:
	def __init__(self, host='localhost', port=8080):
		uri = "http://%s:%d" % (host, port)
		self.server = ServerProxy(uri)

	def parse(self, text):
		return self.server.parse(text)

if __name__ == '__main__':
	nlp = OpenNLP()
	url = 'https://hacker-news.firebaseio.com/v0/beststories.json'
	req = requests.get(url);
	data = list(req.json());

	for i in data:
		url = 'https://hacker-news.firebaseio.com/v0/item/' + str(i)+'.json';
		req = requests.get(url);
		refined = nlp.parse(dict(req.json())['title']);
		print(refined);
	
