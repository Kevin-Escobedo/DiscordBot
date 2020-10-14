import wikipedia

def search(topic: str) -> str:
    '''Searches Wikipedia for the specified topic'''
    articles = wikipedia.search(topic, results = 2)

    if len(articles) != 0:
        try:
            summary = wikipedia.summary(articles[1], sentences = 2)
            return summary
        except:
            message = "Sorry, there was an error getting info about "
            return "{} \"{}\"".format(message, articles[1])

    else:
        return "Sorry, it seems like I can't find anything on your topic."

if __name__ == "__main__":
    topic = input("Enter Topic: ")
    results = search(topic)

    print(results)
