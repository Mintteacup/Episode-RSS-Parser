import feedparser
import csv
import os

#Deletes the csv file so no duplicates
def delete_csv_file(file_path):
    try:
        os.remove(file_path)
    except OSError:
        pass

#Function to get feed data
def fetch_rss_data(url, quality, title):
    feed = feedparser.parse(url)
    print(f"Feed Title: {feed.feed.title}")

    #Loops through every entry then prints them
    for entry in feed.entries:
        if quality in entry.title and any(match in entry.title for match in title):
            print(f"Title: {entry.title} \n\nTorrent Link: {entry.link} \n\nEntry Link: {entry.guid} \n\nPublished Date: {entry.published} \n\n----------------------------------\n\n")

    return feed.entries

def write_to_csv(entries, file_path, quality, title):
    #Prepares the CSV file
    with open(file_path, mode="a", newline='', encoding='utf-8') as csv_file:
        fieldnames = ["Title", "Torrent Link", "Entry Link", "Published", "Summary"]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        #Iterates through entries and write to the CSV file
        for entry in entries:
            if quality in entry.title and any(match in entry.title for match in title):
                writer.writerow({"Title": entry.title, "Torrent Link": entry.link, "Entry Link": entry.guid, "Published": entry.published, "Summary": entry.summary})

def main():
    rss_feed_urls = [
        "https://nyaa.si/?page=rss&u=Ember_Encodes",
        "https://nyaa.si/?page=rss&u=subsplease"
    ]

    quality = "1080p"
    title = ["Jujutsu Kaisen", "Sousou no Frieren", "Undead Unluck", "Dr. Stone", "Kusuriya no Hitorigoto"]
    
    csv_file_path = "rss_data.csv"
    
    delete_csv_file(csv_file_path)

    for url in rss_feed_urls:
        entries = fetch_rss_data(url, quality, title)
        write_to_csv(entries, csv_file_path, quality, title)

main()