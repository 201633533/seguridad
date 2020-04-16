from bs4 import BeautifulSoup
import requests
import psycopg2


#get request
html_doc = requests.get('http://toscrape.com/', headers = {'Accept-Encoding':'identity'})

#pasar contenido html a la una variable BeautifulSoup
soup = BeautifulSoup(html_doc.content, 'html.parser')
print(soup)

for link in soup.find_all('a'):
	print(link)
	print(link.get('href'))
datos=str(soup.find_all('a'))
	
conexion1 = psycopg2.connect(database="scraping", user="postgres", password="123456")
cursor1=conexion1.cursor()
sql="INSERT INTO links(url) VALUES ('"+datos+"');"
cursor1.execute(sql)
conexion1.commit()
conexion1.close()


