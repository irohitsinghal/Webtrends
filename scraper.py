import requests;
from jsonrpclib.jsonrpc import ServerProxy
from pprint import pprint
import re;
import mysql.connector;

dbconfig = { 'host': 'notebook.cjwbzocqulu8.us-east-1.rds.amazonaws.com',
                'user': 'script',
                'password': 'script@123',
                'database': 'warehouse', }


_SQL = """insert into trends(word, count) values(%s, %s)"""

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
	conn = mysql.connector.connect(**dbconfig)
	cursor = conn.cursor()

	for i in data:
		url = 'https://hacker-news.firebaseio.com/v0/item/' + str(i)+'.json';
		req = requests.get(url);
		statement = dict(req.json())['title'];
		parsed = nlp.parse(statement);		
		refined = re.split('\(',parsed);
		r = re.compile("(NNP).*");
		filtered=filter(r.match, refined)
		for j in filtered[:1]:
			j= j.strip(' ):,?\'-\"')[4:];
			j = j.strip()
			cursor.execute(_SQL, (j, 1))
			print(j+": "+statement);

	conn.commit()
	cursor.close()
	conn.close()
