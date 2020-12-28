from movie_list import movie_list

print("Top 10 most popular movies of all time:")
print("---------------------------------------")

# the version i ended up doing but with movie_list.py adjusted idk if thats allowed

list = []
top_ten = []
for movie in movie_list:
    list.append(movie)
    list.sort(reverse=True)
# print(list)
for i in range(0,10):
    top_ten.append(list[i])
i=0
for x in top_ten:
    tuple = top_ten[i]
    # print(tuple)
    i+=1
    votes, year, film = tuple
    print(str(i) + " " + str(film) + " " + "(" + str(year) + ")")


