import urllib.request
from html.parser import HTMLParser
import json
import sys


followers = None


class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        # print("Encountered a start tag")
        pass

    def handle_endtag(self, tag):
        # print("Encountered an end tag")
        pass

    def handle_data(self, data):
        if "edge_followed_by" in data:
            # print("IMPORTANT DATA:", data[21:])
            json_data = json.loads(str(data[21:-1]))
            global followers
            followers = json_data["entry_data"]["ProfilePage"][0]["graphql"]["user"]["edge_followed_by"]["count"]

def getFollowers(username):
    parser = MyHTMLParser()
    try:
        html = urllib.request.urlopen(f"https://www.instagram.com/{username}/").read()
        parser.feed(str(html))
    except:
        print(f"\nUsername: \"{username}\" does not exist.")
        sys.exit()
    return followers

if len(sys.argv) == 2:
    print(getFollowers(sys.argv[1]))
else:
    print(f"\n1 argument is needed. {len(sys.argv)-1} was given. You need to put the Instagram username as an argument, and only that.")
    sys.exit()
