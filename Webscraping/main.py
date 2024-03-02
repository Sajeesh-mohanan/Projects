import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(url=URL)
response_txt = response.text

soup = BeautifulSoup(response_txt, "html.parser")
h_tags = soup.find_all("h3", class_="title")

movie_titles = [tag.get_text() for tag in reversed(h_tags)]

h1_tag = soup.find("h1").get_text()

with open(f"{h1_tag}", mode="w", errors="ignore") as file:
    for movie in movie_titles:
        file.write(movie+"\n")



