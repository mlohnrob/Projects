import requests
import sys
import webbrowser


def searchWiki(searchName):
    url = "https://en.wikipedia.org/w/api.php"
    qParams = {
        "action": "query",
        "list": "search",
        "srsearch": searchName,
        "format": "json"}

    raw = requests.get(url, params=qParams)
    data = raw.json()
    return data


def getWikiSources(pageid):
    url = "https://en.wikipedia.org/w/api.php"
    qParams = {
        "action": "parse",
        "pageid": pageid,
        "prop": "externallinks",
        "format": "json"}

    raw = requests.get(url, params=qParams)
    data = raw.json()
    sources = data["parse"]["externallinks"]
    return sources


searchList = searchWiki(sys.argv[1])
searchListLength = 0
for i in range(len(searchList["query"]["search"])):
    badSearchList = searchList["query"]["search"][i]["title"]
    print(f"({i+1}) {badSearchList}")
    searchListLength += 1

searchListLengthList = [i + 1 for i in range(searchListLength)]


def userMenu():
    userInput = input("\nChoose the page you are looking for. If it is not there type: \"exit\".\n")
    try:
        userInput = int(userInput)
    except:
        if userInput == "exit" or userInput == "Exit":
            sys.exit()
        else:
            print("\nInput is not valid. It must be an integer or string saying: \"exit\". Try again...")
            userMenu()

    for i in range(10):
        if userInput == i + 1:
            sources = getWikiSources(
                searchList["query"]["search"][i]["pageid"])
            print(sources)

    userInput = input("\nDo you want to open the links in you browser? (y/n)\n")
    if userInput == "y":
        for i in sources:
            webbrowser.open_new_tab(i)
    elif userInput == "n":
        sys.exit()
    else:
        print("You messed up!")
        userMenu()


if __name__ == "__main__":
    userMenu()
