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
    mars_news_url = 'https://mars.nasa.gov/news/'
    browser.visit(url)
    time.sleep(1)

    # Create the HTML object
    html = browser.html

    # Parse HTML with Beautiful Soup  
    soup = bs(html, "html.parser")


    # Get the first <li> item under <ul> list of headlines: this contains the latest news title and paragraph text
    first_li = soup.find('li', class_='slide')

    # Save the news title under the <div> tag with a class of 'content_title'
    news_title = first_li.find('div', class_='content_title').text

    # Save the paragraph text under the <div> tag with a class of 'article_teaser_body'
    news_para = first_li.find('div', class_='article_teaser_body').text

    print("Mars News: Scraping Complete!")

    # Get article title and paragraph text
    # image_description = soup.find('div', class_='image_and_description_container')
    # news_title = image_description.find('div', class_='content_title')
    # news_p = image_description.find('div', class_='article_teaser_body')

    #
    ### JPL Mars Space Images
    #
    #################################################################
    ##  Commenting this section out due to JPL's site no longer having a featured image
    ##  since this was assigned a few months ago. 
    ##  I was unable to figure out how to pull an image successfully at present. 
    ##  The commented part below is the code I was able to get working back in October. 
    #################################################################

    # Visit url for JPL Featured Space Image
    # base_jpl_url = 'https://www.jpl.nasa.gov'
    # image_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    #browser.visit(url)
    
    # Create the HTML object
    
    #html = browser.html

    # Parse HTML with Beautiful Soup
    # image_soup = bs(html, 'html.parser')
    
   
    # Retrieve featured image link
    # relative_image_path = image_soup.find_all('img')[3]["src"]
    # featured_image_url = base_jpl_url + relative_image_path

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
    #nextpage_urls = []
    #imgtitles = []
    base_url = 'https://astrogeology.usgs.gov'
    hemispheres_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    

    print("Scraping Mars Hemisphere Images...")

    # Visit the Mars Hemisphere website
    browser.visit(hemispheres_url)

        # Create the HTML object
    html = browser.html

    # Parse HTML with Beautiful Soup  
    soup = bs(html, "html.parser")

    # Retrieve all the parent div tags for each hemisphere 
    hemisphere_divs = soup.find_all('div', class_="item")


    # Create empty dictionary to for titles & links to the hemisphere images.
    hemisphere_image_urls = []

    # Retrieve all html elements that contain hemisphere images information
    hemispheres_img = soup.find_all('div', class_='description')

    # Loop through each div item to get hemisphere data
    for hemisphere in range(len(hemisphere_divs)):

        # --- use splinter's browser to click on each hemisphere's link in order to retrieve image data ---
        hem_link = browser.find_by_css("a.product-item h3")
        hem_link[hemisphere].click()
        time.sleep(1)
    
        # --- create a beautiful soup object with the image detail page's html ---
        img_detail_html = browser.html
        imagesoup = BeautifulSoup(img_detail_html, 'html.parser')
    
        # --- create the base url for the fullsize image link ---
        base_url = 'https://astrogeology.usgs.gov'
    
        # --- retrieve the full-res image url and save into a variable ---
        hem_url = imagesoup.find('img', class_="wide-image")['src']
    
        # --- complete the featured image url by adding the base url ---
        img_url = base_url + hem_url

        # --- retrieve the image title using the title class and save into variable ---
        img_title = browser.find_by_css('.title').text
    
        # --- add the key value pairs to python dictionary and append to the list ---
        hemisphere_image_data.append({"title": img_title, "img_url": img_url})
    
        # --- go back to the main page ---
        browser.back()

    # --- Quit the browser after scraping ---
    browser.quit()

    print("Mars Hemisphere Images: Scraping Complete!")
    
    
    
    #counter = 0
    #for div in hemispheres_img:
        # Use Beautiful Soup's find() method to navigate and retrieve attributes
        #link = div.find('a')
        #href=link['href']
        #img_title = div.a.find('h3')
        #img_title = img_title.text

        # Append the dictionary with the image url string and the hemisphere title to a list.
        # This list will contain one dictionary for each hemisphere.
        #imgtitles.append(img_title)
        #next_page = base_url + href
        #nextpage_urls.append({"title":img_title, "img url":next_page})
        #counter = counter+1
        #if (counter == 4):
            #break

    # Close the browser after scraping
    #browser.quit()

    # Mars 
    #mars_dict = {
        #"news_title": news_title,
        #"news_p": news_p,
        #"mars_facts": str(mars_facts),
        #"hemisphere_images": nextpage_urls
    #}

#  Store all values in dictionary
    scraped_data = {
        "news_title": news_title,
        "news_para": news_para,
        "mars_fact_table": html_table, 
        "hemisphere_images": hemisphere_image_data
    }


    #return mars_dict
    return scraped_data