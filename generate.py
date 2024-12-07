import requests
import json
import random

#collects books already given by generator as to not repeat while the app is running
bookHistory = []

'''
Takes in user genres and randomly picks one from the weighted genre choices
Examples of acceptable input
example = [("Fantasy, lightnovel, Horror, Thriller, Crime",), ("Fantasy, Horror, lightnovel, Mystery, Thriller",)]
example1 = [('Fantasy',), ('Fantasy',), ('Horror',)]
'''
def generateGenre(entryGenres):
    genres = {}

    #takes apart the users genres and calculates the weight for each genre
    for row in entryGenres:
        newList = row[0].split(", ")
        for entry in newList:
            if entry in genres:
                genres[entry] += 1
            else:
                genres[entry] = 1

    options = list(genres.keys())
    weights = list(genres.values())

    #chooses one option out of all the users genres with 
    #specefic weights for each genre and returns a string of the genre
    option = random.choices(options, weights=weights,k=1)[0]
    return option

def generateBook(genre):
    url = "https://openlibrary.org/search.json"
    params = {
        "subject": genre,
        "sort": "readinglog",
        "fields": "title, author_name",
        "limit": 50
    }
    response = requests.get(url, params=params)
    #stores the top 50 most saved books of a certain genre
    response = response.json()
    book = {}

    while True:
        try:
            #Randomly chooses a book from the 50 availble and returns a dictionary with the
            #title and author and retries if it chooses a book that isn't available
            #such as when there are less than 50 books available in a genre
            randNumber = random.randint(0,49)
            book = response["docs"][randNumber]
            #checks if chosen book has already been seen before and if true it gets another book
            if book['title'] in bookHistory:
                continue
            #adds book title to list of already seen books
            bookHistory.append(book['title'])
            break
        except:
            continue
    return book
