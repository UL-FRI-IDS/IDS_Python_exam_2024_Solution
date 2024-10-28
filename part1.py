from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import json

URL = "https://www.imdb.com/chart/top/"

driver = webdriver.Chrome()
driver.get(URL)
sleep(2)

# switch to detailed view which shows the movie stars too for each movie
driver.find_element(By.CSS_SELECTOR, "#list-view-option-detailed").click()
sleep(2)

# at this point, the raw html has everything needed - so we could save it and use BS4 too.
movielist = driver.find_elements(By.CSS_SELECTOR, "li.ipc-metadata-list-summary-item")
data = []
for movie in movielist:
    title = movie.find_element(By.CSS_SELECTOR, "h3").text
    # remove the leaderboard number from the title
    first_space_in_title = title.index(" ")
    title = title[first_space_in_title+1:]

    year = movie.find_elements(By.CSS_SELECTOR, "span.dli-title-metadata-item")[0].text
    rating = movie.find_element(By.CSS_SELECTOR, "span.ipc-rating-star--rating").text

    directors = movie.find_elements(By.CSS_SELECTOR, "a.dli-director-item")
    directors = [director.text for director in directors]
    movie_stars = movie.find_elements(By.CSS_SELECTOR, "a.dli-cast-item")
    movie_stars = [moive_star.text for moive_star in movie_stars]

    data.append({
        "title": title,
        "year": int(year),
        "rating": float(rating),
        "directors": directors,
        "movie_stars": movie_stars
    })

driver.close()

# dump the data into a json file
with open("imdb_top_250_movies.json", "w") as f:
    json.dump(data, f, indent=4)
