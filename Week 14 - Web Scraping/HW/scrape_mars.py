# import dependicies
from bs4 import BeautifulSoup as bs
import requests
from splinter import Browser
import time
import pandas as pd
import numpy as np

# TODO: see if I can only call browser once
def scrape():
    # get url
    url = 'https://mars.nasa.gov/news/'

    # get html
    response = requests.get(url)

    # create bs obj
    soup = bs(response.text, 'lxml')

    content_titles = soup.find_all('div', class_ = 'content_title')

    # initalize lists
    titles = []
    paragraphs = []

    for title in content_titles:
        titles.append(title.a.text.strip())

    content_paragraphs = soup.find_all('div', class_ = 'rollover_description_inner')

    for paragraph in content_paragraphs:
        paragraphs.append(paragraph.text.strip())

    # grab latest content
    latest_title = titles[0]
    latest_paragraph = paragraphs[0]

    # use splinter to grab image urls
    executable_path = {'executable_path': 'chromedriver'}
    browser = Browser('chrome', **executable_path, headless=False)
    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url)
    browser.click_link_by_partial_text('FULL IMAGE')

    # wait 3 seconds to search for url
    time.sleep(3)
    html = browser.html
    soup = bs(html, 'html.parser')
    featured_image_url = soup.find_all('img', class_ = 'fancybox-image')

    featured_image_url = 'https://www.jpl.nasa.gov' + featured_image_url[0]['src']

    executable_path = {'executable_path': 'chromedriver'}
    browser = Browser('chrome', **executable_path, headless=False)
    url = 'https://twitter.com/marswxreport?lang=en'
    browser.visit(url)

    html = browser.html
    soup = bs(html, 'html.parser')
    tweets = soup.find_all('div', class_ = 'js-tweet-text-container')

    # get the latest tweet
    for tweet in tweets:
        mars_weather = tweet.p.text
        break

    url = 'https://space-facts.com/mars/'
    mars_facts = pd.read_html(url)


    mars_facts = mars_facts[0]

    mars_facts.columns = ['Category', 'Value']

    mars_facts.set_index('Category', inplace=True)

    mars_facts = mars_facts.to_dict()

    mars_facts = mars_facts['Value']

    # obtain high resolution image urls for each of Mar's hemispheres
    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    response = requests.get(url)
    soup = bs(response.text, 'html.parser')
    # grab each link on page and put in list
    links = soup.find_all('a', class_ = 'itemLink product-item')

    urls = []
    for link in links:
        urls.append(link['href'])

    # set base url
    base_url = 'https://astrogeology.usgs.gov'

    # initalize lists
    image_urls = []
    image_titles = []

    # loop through list and visit each page
    for url in urls:
        response = requests.get(base_url + url)
        soup = bs(response.text, 'html.parser')
        # grab image url
        image_url = soup.find_all('div', class_ = 'downloads')
        image_urls.append(image_url[0].li.a['href'])
        # grab image title
        image_title = soup.find_all('h2', class_ = 'title')
        image_titles.append(image_title[0].text)

    clean_titles = []

    for title in image_titles:
        split = title.split('Enhanced')
        clean_titles.append(split[0].strip())

    hemisphere_image_urls = []

    for i in np.arange(len(image_titles)):
        hemisphere_image_urls.append({"Title" : clean_titles[i],
                                     "img_url" : image_urls[i]})

    # TODO: return dictionary of values
    scrape_dict = {
        "latest_title" : latest_title,
        "latest_paragraph" : latest_paragraph,
        "featured_image_url" : featured_image_url,
        "mars_weather" : mars_weather,
        "mars_facts" : mars_facts,
        "hemisphere_image_urls" : hemisphere_image_urls
    }

    return scrape_dict
