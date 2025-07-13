from bs4 import BeautifulSoup
import requests

#url = "https://letterboxd.com/mirandoisa/films/"
HEADERS = {'User-Agent': 'Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148'}

def main() :
    url1 = getUrl(getUserInput())
    url2 = getUrl(getUserInput())
    print("Getting movie lists......")
    movieList1 = getMovieList(url1)
    movieList2 = getMovieList(url2)
    things = compareLists(movieList1, movieList2)
    print(str(len(things)) + " same movies")
    for thing in things:
        print(thing)

def getMovieList(url: str)->list :
    pageCount = 1
    movieList = []
    while True:
        newUrl = (url + "page/" + str(pageCount))
        page = requests.get(newUrl, headers=HEADERS)
        soup = BeautifulSoup(page.text, "html.parser")
        titles = soup.find_all("img", {"class":"image"})
        if len(titles) <= 0:
            break
        for title in titles:
            movieList.append(title.get("alt"))
        pageCount += 1    
    return movieList     

def getUrl(username: str)->str :
    return "https://letterboxd.com/" + str(username) + "/films/"

def getUserInput()->str  :
    return input()

def compareLists(movieList1: list, movieList2: list)->list    :
    intersection = list(set(movieList1).intersection(movieList2))
    return intersection

main()