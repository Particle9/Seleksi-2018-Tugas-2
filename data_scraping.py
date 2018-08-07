from urllib.request import urlopen
from bs4 import BeautifulSoup
import json
from time import sleep

imdburl = 'https://www.imdb.com'
url = 'https://www.imdb.com/title/tt4154756/?ref_=nv_sr_1'
urlPopular = 'https://www.imdb.com/chart/top?ref_=nv_mv_250_6'
urlSearch = 'https://www.imdb.com/search/title?count=1000&title_type=feature&sort=num_votes,desc&ref_=nv_wl_img_2'
page = urlopen(url).read()

def listMoviesPop(u):
    result = []
    page = urlopen(u).read()
    soup = BeautifulSoup(page,'html.parser')
    
    movieList = soup.find_all("h3",{"class":"lister-item-header"})
    for x in movieList :
        movie = {}
        movie['url'] = 'https://www.imdb.com' + x.find('a')['href']
        movie['title'] = x.find('a').string
        result.append(movie)
    return result
    
def listMoviesRank(u):
    result = []
    page = urlopen(u).read()
    soup= BeautifulSoup(page,'html.parser')
    
    movieList = soup.find_all("td",{"class":"titleColumn"})
    for x in movieList :
        movie = {}
        movie['url'] = x.find('a')['href']
        movie['title'] = x.find('a').string
        result.append(movie)
    return result

def scrapeIMDB_Movie(u):
    result = []
    page = urlopen(u).read()
    soup = BeautifulSoup(page,'html.parser')
    
    rating = soup.find(class_="imdbRating").find(class_="ratingValue").find("span",{"itemprop":"ratingValue"})
    title = soup.find("meta",{"property":"og:title"})['content']
    desc = soup.find("meta",{"property":"og:description"})['content']
    poster = "https://www.imdb.com" + soup.find(class_="poster").find("a")['href']
    year = soup.find("span",{"id":"titleYear"}).find("a").string
    genresX = soup.find_all("span",{"itemprop":"genre"})
    castsX = soup.find("table",{"class":"cast_list"})
    castsN = castsX.find_all("span",{"itemprop":"name"}) 
    castsC = castsX.find_all("td",{"class":"character"})
    castsX = zip(castsN,castsC)
    casts = []
    for c in castsX :
        try :
            cc = {}
            cc['actor'] = c[0].string
            cc['character'] = c[1].find("a").string
            casts.append(cc)
        except Exception :
            print('A')
    genre = []

    for x in genresX :
        try :
            genre.append(x.string)
        except Exception :
            print('B')
    
    res = {}
    res['title'] = title
    res['rating'] = rating.string
    res['description'] = desc
    res['genre'] = genre
    res['poster'] = poster
    res['casts'] = casts
    res['year'] = year
    result.append(res)
    
    return res

mov_data = listMoviesPop(urlSearch)
data_fin = []
sleep(2)
for x in mov_data :
    print(x['title'])
    succ = False
    try:
        data = scrapeIMDB_Movie(x['url'])
        data_fin.append(data)
        succ = True
    except Exception as E :
        print(E)
        succ = False
    sleep(2)

with open('data.json', 'w') as outfile:
    json.dump(data_fin, outfile)
    