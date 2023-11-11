import feedparser
import csv

url = "https://nyaa.si/?page=rss"
feed = feedparser.parse(url)

#Loops through every entry then prints them
for entry in feed.entries:
    print(f"Title: {entry.title} \n\nTorrent Link: {entry.link} \n\nEntry Link: {entry.guid} \n\nPublished Date: {entry.published} \n\n----------------------------------\n\n")

#Prepares the CSV file
with open("rss_data.csv", mode="w", newline='', encoding='utf-8') as csv_file:
    fieldnames = ["Title", "Torrent Link", "Entry Link", "Published", "Summary"]
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    #Iterates through entries and write to the CSV file
    for entry in feed.entries:
        writer.writerow({"Title": entry.title, "Torrent Link": entry.link, "Entry Link": entry.guid, "Published": entry.published, "Summary": entry.summary})