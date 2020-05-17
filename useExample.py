import selenium
from selenium import webdriver
from picoscrape import UnsplashDownloader

browser = webdriver.Chrome('chromedriver.exe')

unsplash = UnsplashDownloader(browser,'C:\Users')
unsplash.download('car', 5, 360)
