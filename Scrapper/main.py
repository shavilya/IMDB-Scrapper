# Importing all the required libraries for web scrapping and file handling in python. 

import requests
from bs4 import BeautifulSoup
import pandas as pd 
import os 
from datetime import datetime 

# Initializing all the required lists such as title , rating , year , certification , genre,vote and time. 
title_list = []
rating_list = []
year_list = []
certification_list = []
genre_list = []
vote_list = []
time_list = []

# IMDB Scrapper function to scrape 100 pages of imdb using the required genre. 

def imdb_scraper(genre):
    for page in range(1, 101):  # Scrape 100 pages
        url = f"https://www.imdb.com/search/title/?genres={genre}&start={page * 50}&explore=title_type,genres&ref_=adv_prv"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        movie_containers = soup.find_all('div', class_='lister-item mode-advanced')

        for container in movie_containers:
            # Extract movie details
            title = container.h3.a.text.strip()
            title_list.append(title)

            rating_element = container.find('div', class_='ratings-imdb-rating')
            rating = rating_element.strong.text if rating_element else ''       
            rating_list.append(rating)

            year = container.h3.find('span', class_='lister-item-year').text.strip('()')
            year_list.append(year)

            certification = container.find('span', class_='certificate').text if container.find('span', class_='certificate') else ''
            certification_list.append(certification) 

            genres = container.find('span', class_='genre').text.strip()
            genre_list.append(genres)

            vote_element = container.find('span', attrs={'name': 'nv'})
            vote = vote_element['data-value'] if vote_element else ''
            vote_list.append(vote)

            time_element = container.find('span', class_='runtime')
            time = time_element.text.strip() if time_element else ''
            time_list.append(time)

genre = input("Enter the genre name you want to scrape: ").lower()  # Initialize the genre which you want to scrape. 

imdb_scraper(genre)  # Calling the scrapper function. 


# Creating a dictionary to store all the lists which are generated using scrapper. 

imdb_dict = {
        'Title' : title_list , 
        'Rating' : rating_list , 
        'Year' : year_list ,
        'Certification' : certification_list , 
        'Genre' : genre_list , 
        'Vote' : vote_list , 
        'Time' : time_list
        }

imdb_df = pd.DataFrame.from_dict(imdb_dict)  # Creating a dataframe to save .csv file of imdb dictionary.

# Naming the csv file and the future versions. {Naming convention} 

csv_file = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}_imdb.csv"  
imdb_df.to_csv('/IMDB/Dataset/{}'.format(csv_file))  # Saving the dataframe into .csv 

imdb_df.head()

