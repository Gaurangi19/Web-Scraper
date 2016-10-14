#program to get list of restaurants for web-scraping
import requests
from bs4 import BeautifulSoup

#this module scrapes the url provided
def web_scrape(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")
    g_data = soup.find_all("div", {"class": "info"})
    for item in g_data:
        try:
            lid_link = item.contents[0].find_all("a", {"class": "business-name"})[0].get("href")
            link = "http://www.yellowpages.com" + lid_link
            rest_list.append(link)
        except:
            pass

rest_list = []
#seed_url = "http://www.yellowpages.com/search?search_terms=coffee&geo_location_terms=Los%20Angeles%2C%20CA"
seed_url = "http://www.yellowpages.com/search?search_terms=restaurant&geo_location_terms=Los%20Angeles%2C%20CA"
web_scrape(seed_url)
for i in range(2, 20):
    url_page = seed_url + "&page=" + str(i)
    web_scrape(url_page)

#print("Number of restaurant links:", len(rest_list))

#create output file to print the inference
output_file = open("C:/USC stuff/Information Integration/Homework/HW3/restaurant_links.txt", "w", encoding="latin1")

count = 0
for j in range(0, len(rest_list)):
    if "?lid=" in rest_list[j]:
        output_file.write(str(rest_list[j]) + "\n")
        count += 1
print("Number of restaurant links:", count)

#close output file
output_file.close()
