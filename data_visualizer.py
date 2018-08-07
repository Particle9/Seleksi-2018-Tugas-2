import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


with open('data/data.json') as json_data:
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

fig,ax = plt.subplots()
gen_keys = list(genre_ratings.keys())
y_pos = np.arange(len(gen_keys))
rating = list(genre_ratings.values())
error = np.random.rand(len(gen_keys))
ax.barh(y_pos, rating, align='center',color='b',ecolor='black')
ax.set_yticks(y_pos)
ax.set_yticklabels(gen_keys)
ax.invert_yaxis()  # labels read top-to-bottom
ax.set_xlabel('Performance')
ax.set_title('Genre Ratings')
fig_size = [12,9]
plt.rcParams["figure.figsize"] = fig_size
plt.savefig("pic/1.png")

actor_keys = list(actor_ratings.keys())
rating = list(actor_ratings.values())
actor_keys = [x for _,x in sorted(zip(rating,actor_keys))]
rating.sort()
rating, actor_keys = (list(t) for t in zip(*sorted(zip(rating, actor_keys))))
key_chunks = [actor_keys[x:x+50] for x in range(0, len(actor_keys), 50)]
rating_chunks = [rating[x:x+50] for x in range(0, len(rating), 50)]
key_chunks.reverse()
rating_chunks.reverse()
for i in range(0,len(key_chunks)) :
    fig,ax = plt.subplots()
    y_pos = np.arange(len(key_chunks[i]))
    ax.barh(y_pos, rating_chunks[i], align='center',color='r')
    ax.set_yticks(y_pos)
    ax.set_yticklabels(key_chunks[i])
    ax.invert_yaxis()  # labels read top-to-bottom
    ax.set_xlabel('Performance')
    ax.set_title('Actor Ratings')
    plt.savefig("pic/2-" + str(i) + ".png")


gen_y_count = {}
for x in gen_keys :
    gen_y_count[x] = {}
    
for x in film_data :
    for g in x['genre'] :
        if x['year'] in gen_y_count[g] :
            gen_y_count[g][x['year']] += 1
        else :
            gen_y_count[g][x['year']] = 1
gen_yr = list(gen_y_count.values())
gen_yrc = list(gen_y_count.keys())
for i in range(0,len(gen_yr)):
    yearsg = list(gen_yr[i].keys())
    yearsv = list(gen_yr[i].values())
    for j in range(0,len(yearsg)):
        yearsg[j] = int(yearsg[j])
    gen_yr[i] = {}
    gen_yr[i]['year'] = yearsg
    gen_yr[i]['value'] = yearsv

for i in range(0,len(gen_yr)):
    gen_yr[i]['year'], gen_yr[i]['value'] = (list(t) for t in zip(*sorted(zip(gen_yr[i]['year'], gen_yr[i]['value']))))

maxx = 0
minn = 99999
for x in gen_yr :
    if (maxx < x['year'][len(x['year']) -1]):
        maxx = x['year'][len(x['year']) -1]
    if (minn > x['year'][0]):
        minn = x['year'][0]

g_y_v = []
for i in range(0, len(gen_yr)):
    gv_e = []
    for j in range (minn,maxx + 1):
        if j in gen_yr[i]['year'] :
            gv_e.append(gen_y_count[gen_yrc[i]][str(j)])
        else :
            gv_e.append(0)
    g_y_v.append(gv_e)


plt.close()
ax.invert_yaxis()  # labels read top-to-bottom
lsss = {'x': range(minn,maxx + 1)}
for i in range(0,len(g_y_v)):
    lsss['y' + str(i)] = g_y_v[i]
df = pd.DataFrame(lsss)

print(lsss)
for i in range(0,len(g_y_v)):
    plt.plot('x','y'+ str(i), data = df, marker = 'o', label=gen_yrc[i])
plt.legend()
plt.savefig("pic/3.png")


