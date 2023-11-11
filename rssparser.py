import feedparser
import csv
import os

#Deletes the csv file so no duplicates
os.remove("rss_data.csv")

rss_feed_urls = [
    "https://nyaa.si/?page=rss&u=Ember_Encodes",
    "https://nyaa.si/?page=rss&u=subsplease"
]

#Function to get feed data
def fetch_rss_data(url):
    global feed
    feed = feedparser.parse(url)
    print(f"Feed Title: feed.feed.title")
    #Loops through every entry then prints them
    for entry in feed.entries:
        print(f"Title: {entry.title} \n\nTorrent Link: {entry.link} \n\nEntry Link: {entry.guid} \n\nPublished Date: {entry.published} \n\n----------------------------------\n\n")

def to_csv():
    #Prepares the CSV file
    with open("rss_data.csv", mode="a", newline='', encoding='utf-8') as csv_file:
        fieldnames = ["Title", "Torrent Link", "Entry Link", "Published", "Summary"]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        #Iterates through entries and write to the CSV file
        for entry in feed.entries:
            writer.writerow({"Title": entry.title, "Torrent Link": entry.link, "Entry Link": entry.guid, "Published": entry.published, "Summary": entry.summary})

for url in rss_feed_urls:
    fetch_rss_data(url)
    to_csv()