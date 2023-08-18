from bs4 import BeautifulSoup
import requests
import sqlite3
import time

with sqlite3.connect('DBBrowser/mydb.db') as db:
    cursor = db.cursor()
    query = """
    CREATE TABLE IF NOT EXISTS search(
        id INTEGER,
        name TEXT,
        price INT,
        description TEXT,
        img TEXT,
        h1 TEXT,
        h2 TEXT,
        h3 TEXT,
        h4 TEXT,
        h5 TEXT,
        PRIMARY KEY(ID)
)
    """
    cursor.executescript(query)

response = requests.get('https://bolshayastrana.com/tury')
soup = BeautifulSoup(response.content, 'lxml')
pages = soup.find_all('a', class_='pagination__item')
maxpage = (pages[-1].text).replace(' ', '')
print(maxpage)
global idcount
idcount = 0

the_index = 0

url = 'https://bolshayastrana.com/tury?plainSearch=1&page='
for i in range(int(maxpage))[1::]:

    fut = sqlite3.connect("DBBrowser/mydb.db")
    searchs = fut.cursor()
    response = requests.get(url + str(i))

    soup = BeautifulSoup(response.content, 'lxml')
    inf = soup.find_all('div', class_='as-col tour-previews__col')
    for infr in inf:
        imgs = infr.find('img', class_='tour-preview__photo')
        if imgs is not None:
            a = imgs["src"]
        else:
            None
        meta = infr.find('meta', {'itemprop': 'url'})
        url2 = meta.get('content')
        response2 = requests.get('https://bolshayastrana.com/' + url2)
        soup2 = BeautifulSoup(response2.content)
        price = soup2.find('strong', {'class': 'sidebar-resume__price-value'}).text.strip()
        price = price.replace(' ', '')
        price = price.replace('₽', '')
        price = price.replace('от', '')
        name = soup2.find('h1', {'itemprop': 'name'}).text.strip()
        description = soup2.find('div', {'class': 'article-text tour-main-info__description'}).text.strip()
        images = soup2.find_all('img', {'class': 'tile-gallery__image'})
        images_list = []
        print(images)
        for i in images:
            # images_list.append(img['src'])
            if images.index(i) == 5:
                break
            searchs.execute(f"UPDATE search SET h{images.index(i)+1}='{i['src']}' WHERE ID={idcount}")
            fut.commit()
        values = [name, price, description, a]
        searchs.execute("INSERT INTO search(name, price, description, img) VALUES(?,?,?,?)", values)
        fut.commit()
        idcount += 1


