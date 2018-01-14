import requests;
from jsonrpclib.jsonrpc import ServerProxy
from pprint import pprint
import re;

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

	
#	print(filtered);

	for i in data:
		url = 'https://hacker-news.firebaseio.com/v0/item/' + str(i)+'.json';
		req = requests.get(url);
		statement = dict(req.json())['title'];
		parsed = nlp.parse(statement);		
		refined = re.split('\(',parsed);
		r = re.compile("(NNP).*");
		filtered=filter(r.match, refined)
		for j in filtered:
			j= j.strip(' ):,?\'-"')[3:];
			print(j);
	
