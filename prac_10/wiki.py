import wikipedia

choice = input(">>> ")
while choice != "":
    try:
        user_searched = wikipedia.page(choice, auto_suggest=False)
        print(user_searched.title)
        print(user_searched.summary)
        print(user_searched.url)
    except wikipedia.exceptions.DisambiguationError as e:
        print(e.options)
    choice = input(">>> ")

print("thank you for searching the Wiki.")
