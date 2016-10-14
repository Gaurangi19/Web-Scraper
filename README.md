# Web-Scraper

I am extracting information about restaurants in LA from www.yellowpages.com.  
I have created a manual wrapper.It extracts information based on the HTML tags and class selector values, so the items don’t have to be in a fixed, known order.  

  
Base URL:  
http://www.yellowpages.com/search?search_terms=restaurant&geo_location_terms=Los%20Angeles%2C%20CA  

Extracted fields:  
URL: It is the URL of the webpage from which fields are extracted.  
Business-name: The name of the restaurant.  
Address.street: Street address of the restaurant.  
Address.city: City where the restaurant is located.  
Address.state: State where the restaurant is located.  
Address.code: Pin code where the restaurant is located.  
Phone: Phone number of the restaurant.  
Regular-hours.day: The regular working days of the restaurant e.g. Mon – Fri  
Regular-hours.hours: The regular working hours of the restaurants e.g. 11:00 am to 3:00 pm  
Rating: The rating for the restaurant out of 5.0  
Website: The official website of the restaurant.  

The get_links.py program takes a seed URL and crawls a given number of pages to extract links for restaurants on Yellowpages and writes them to a file named “restaurant_links.txt”.   
  
The second program, get_data.py reads “restaurant_links.txt” and scrapes information from each link in the file. 
