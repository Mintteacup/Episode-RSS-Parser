import feedparser

url = "https://nyaa.si/?page=rss"
feed = feedparser.parse(url)

print(feed)