from flask import Flask, render_template, jsonify, request
from operator import itemgetter
import json
import numpy as np
import matplotlib.pyplot as plt

# Variabel global
app = Flask(__name__)

# Fungsi untuk mencari rating aktor dari film
def CalculateRate(film_data) :
    actor_ratings = {}
    actor_rating_count = {}
    for x in film_data :
        for y in x['casts'] :
            if y['actor'] in actor_ratings :
                actor_ratings[y['actor']] += x['rating']
                actor_rating_count[y['actor']] += 1
            else :
                actor_ratings[y['actor']] = x['rating']
                actor_rating_count[y['actor']] = 1
    for k,v in actor_ratings.items() :
        actor_ratings[k] = v/actor_rating_count[k]
    return actor_ratings

# Membaca data dari file data.json
with open('File/data.json') as json_data:
    film_data = json.load(json_data)

for x in film_data :
    x['rating'] = float(x['rating'])

genre_ratings = {}
genre_rating_count = {}
for x in film_data :
    for y in x['genre'] :
        if y in genre_ratings :
            genre_ratings[y] += x['rating']
            genre_rating_count[y] += 1
        else :
            genre_ratings[y] = x['rating']
            genre_rating_count[y] = 1
for k,v in genre_ratings.items() :
    genre_ratings[k] = v/genre_rating_count[k]

genreRatingList =[]
for genre in genre_ratings :
    genreRatingList.append((genre, genre_ratings[genre]))

actor_ratings = CalculateRate(film_data)
# Membuat list yang menyimpan nama aktor dan rating aktor tersebut
actorRatingList = []
for actor in actor_ratings:
    actorRatingList.append((actor, actor_ratings[actor]))

# Mengurutkan aktor sesuai dengan rating
# Pengurutan dilakukan dari rating besar ke kecil
actorList = sorted(actorRatingList, key=itemgetter(1), reverse=True)


# Mencari aktor top 10
topTen = []
x = 0
while (x<=10):
        topTen.append((actorList[x][0],actorList[x][1]))
        x = x + 1

topTenName = []
topTenRate = []
for actor in topTen :
    topTenName.append(actor[0])
    topTenRate.append(actor[1])

@app.route('/ratingfilm', methods=['GET'])
def rating() :
    #Mengirimkan file data.json untuk menampilkan rating film
    ratingFilm = []
    for rate in film_data :
        ratingFilm.append((str(rate['title'].replace("'"," ")), float(rate['rating'])))
    # Membuka ratingfilm.html untuk halaman
    return render_template("ratingfilm.html", rating=ratingFilm)

@app.route('/ratingTop10', methods=['GET'])
def actorTop() :
    # Mengirimkan file data.json untuk menampilkan nama aktor dengan rating 10 tertinggi
    ratingTop10 =[]
    ratingTop10 = topTen
    return render_template("ratingTop10.html", top10=ratingTop10)

@app.route('/ratinggenre', methods=['GET'])
def ratingGenre() :
    # Mengirimkan file data.json untuk menampilkan rating dari genre film
    rateGenre = []
    rateGenre = genreRatingList
    return render_template("ratingGenre.html", rate=rateGenre)

@app.route('/ratingaktor', methods=['GET'])
def actor() :
    # Mengirimkan file data.json untuk menampilkan nama aktor beserta ratingnya
    ratingAktor = []
    ratingAktor = actorRatingList
    return render_template("ratingaktor.html", actorRate=ratingAktor)

@app.route('/')
def menu() :
    return render_template("data.html")

@app.route('/visualgenre')
def visGenre() :
    return render_template("visualgenre.html")

@app.route('/visualaktor')
def visAktor() :
    return render_template("visualaktor.html")

if __name__ == '__main__':
   app.run(debug=True)
