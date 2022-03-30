
from requests_html import HTMLSession
session = HTMLSession()
url = 'https://data.anbima.com.br/web-bff/v1/debentures?page=0&size=20&field=&order=&'

r = session.get(url)
r.html.render(sleep=1, keep_page=True, scrolldown=2)
obj = r.html.find('#video-title')

for item in obj:
    video = {
        'title': item.text,
        'link': item.absolute_links
    }
    print(video)
