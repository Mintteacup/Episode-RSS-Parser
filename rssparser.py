import feedparser

url = "https://nyaa.si/?page=rss"
feed = feedparser.parse(url)

for entry in feed.entries:
    print(f"Title: {entry.title} \n\nTorrent Link: {entry.link} \n\nPublished Date: {entry.published} \n\n----------------------------------\n\n")