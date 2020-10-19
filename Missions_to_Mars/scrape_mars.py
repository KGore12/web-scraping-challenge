# Import Dependencies
from splinter import Browser
from bs4 import BeautifulSoup as bs
import time
import pandas as pd
import requests as req



def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)

def scrape_info():
    browser = init_browser()

    #
    ### NASA Mars News 
    #

    # Visit url for NASA Mars News -- Latest News
    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)
    html = browser.html

    # Parse HTML with Beautiful Soup  
    soup = bs(html, "html.parser")

    # Get article title and paragraph text
    image_description = soup.find('div', class_='image_and_description_container')
    news_title = image_description.find('div', class_='content_title')
    news_p = image_description.find('div', class_='article_teaser_body')

    #
    ### JPL Mars Space Images
    #
    
    # Visit url for JPL Featured Space Image
    base_jpl_url = 'https://www.jpl.nasa.gov'
    image_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url)
    
    # Parse HTML with Beautiful Soup
    html = browser.html
    image_soup = bs(html, 'html.parser')
    # Retrieve featured image link
    relative_image_path = image_soup.find_all('img')[3]["src"]
    featured_image_url = base_jpl_url + relative_image_path

    #
    ### Mars Facts
    #

    # Visit the Mars Facts webpage for interesting facts about Mars
    facts_url = "https://space-facts.com/mars/"
    browser.visit(facts_url)
    html = browser.html

    # Use Pandas to scrape the table containing facts about the planet including Diameter, Mass, etc.
    table = pd.read_html(facts_url)
    mars_facts = table[1]

    # Rename columns
    mars_facts.columns = ['Description','Mars','Earth']

    # Reset Index to be description
    mars_facts.set_index('Description', inplace=True)

    # Use Pandas to convert the data to a HTML table string
    mars_facts.to_html('table.html')

    #
    ### Mars Hemispheres
    #

    # Visit the USGS Astrogeology site
    nextpage_urls = []
    imgtitles = []
    base_url = 'https://astrogeology.usgs.gov'
    hemispheres_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(hemispheres_url)

    # Scrape page into Soup
    html = browser.html
    soup = bs(html, "html.parser")

    # Create dictionary to for titles & links to the hemisphere images.
    hemisphere_image_urls = []

    # Retrieve all html elements that contain hemisphere images information
    hemispheres_img = soup.find_all('div', class_='description')

    # Iterate through each div to pull titles and make list of hrefs to iterate through
    counter = 0
    for div in hemispheres_img:
        # Use Beautiful Soup's find() method to navigate and retrieve attributes
        link = div.find('a')
        href=link['href']
        img_title = div.a.find('h3')
        img_title = img_title.text

        # Append the dictionary with the image url string and the hemisphere title to a list.
        # This list will contain one dictionary for each hemisphere.
        imgtitles.append(img_title)
        next_page = base_url + href
        nextpage_urls.append({"title":img_title, "img url":next_page})
        counter = counter+1
        if (counter == 4):
            break

    # Close the browser after scraping
    browser.quit()

    # Mars 
    mars_dict = {
        "news_title": news_title,
        "news_p": news_p,
        "featured_image_url": featured_image_url,
        "mars_facts": str(mars_facts),
        "hemisphere_images": nextpage_urls
    }

    return mars_dict