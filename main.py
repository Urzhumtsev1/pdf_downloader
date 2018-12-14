from lxml import html
import requests, wget, os

page = requests.get('http://cired.net/publications/cired2017/authors.html')
webpage = html.fromstring(page.content)

links = webpage.xpath('//a/@href')

for i in links:
    if '.pdf' in i:
        file_path = 'http://cired.net/publications/cired2017' + i[1:]
        r = requests.get(file_path)
        if r.ok:
            filename = wget.download(file_path)
            os.rename(filename, u''+os.getcwd()+'/'+filename)



