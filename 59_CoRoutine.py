#coroutine wo hotay hain jb ak function ka initialize ma time lgna hoo tb use hotay hain
def searcher():
    import time
    # Some 4 seconds time consuming task
    book = "This is a book written by Saaad Ahmad A well known Programmmer"
    time.sleep(4)

    while True:
        text = (yield)
        if text in book:
            print("Your text is in the book")
        else:
            print("Text is not in the book")

search = searcher()
print("search started")
next(search)
print("Next method run")
search.send("Saaad")
search.close()#coroutine close ho gya hay 


