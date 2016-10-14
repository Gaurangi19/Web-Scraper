#web-scrapper to scrape yellowpages restaurants
import json
import requests
from bs4 import BeautifulSoup

#this module writes raw webpage content to a text file
def write_raw(lid, r):
    file_name = "C:/USC stuff/Information Integration/Homework/HW3/data/" + str(lid) + ".txt"
    output_file = open(file_name, "w", encoding="latin1")
    output_file.write(str(r.content))
    output_file.close()

#this module scrapes the url provided
def web_scrape(url):
    r = requests.get(url)
    #lid = url[(url.find("lid=") + 4):]
    #write_raw(lid, r)
    soup = BeautifulSoup(r.content, "html.parser")
    fields = {}
    fields["URL"] = url
    #get restaurant_name
    g_data = soup.find_all("div", {"class": "sales-info"})
    for item in g_data:
        try:
            fields["business-name"] = item.contents[0].text
        except:
            pass

    #get address and phone
    g_data = soup.find_all("div", {"class": "contact"})
    for item in g_data:
        try:
            fields["address.street"] = item.contents[0].find_all("p", {"class": "street-address"})[0].text
        except:
            pass
        try:
            fields["address.city"] = item.contents[0].find_all("span", {"itemprop": "addressLocality"})[0].text
        except:
            pass
        try:
            fields["address.state"] = item.contents[0].find_all("span", {"itemprop": "addressRegion"})[0].text
        except:
            pass
        try:
            fields["address.code"] = item.contents[0].find_all("span", {"itemprop": "postalCode"})[0].text
        except:
            pass
        try:
            fields["phone"] = item.contents[1].text
        except:
            pass

    #get regular hours
    g_data = soup.find_all("time", {"itemprop": "openingHours"})
    for item in g_data:
        try:
            fields["regular-hours.day"] = item.contents[0].text
        except:
            pass
        try:
            fields["regular-hours.hours"] = item.contents[1].text
        except:
            pass

    #get restaurant website
    g_data = soup.find_all("a", {"class": "custom-link"})
    for item in g_data:
        try:
            fields["website"] = item.get("href")
        except:
            pass

    #get restaurant ratings
    g_data = soup.find_all("div", {"class": "ratings"})
    for item in g_data:
        try:
            fields["rating"] = item.contents[0].find_all("meta", {"itemprop": "ratingValue"})[0].get('content')
        except:
            pass
        
    return fields

#read input file for restaurant links
input_file = open("C:/USC stuff/Information Integration/Homework/HW3/restaurant_links.txt", "r", encoding="latin1")
lines = input_file.readlines()

#write output to json file
with open('C:/USC stuff/Information Integration/Homework/HW3/extractions1.json', 'w') as outfile:
    for line in lines:
        url_link = line.strip()
        #print(url_link)
        extracted_data = web_scrape(url_link)
        json.dump(extracted_data, outfile, sort_keys=True)
        outfile.write("\n")

#close input file
input_file.close()
