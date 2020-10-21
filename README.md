# web-scraping-challenge
# Missions_to_Mars
## by Kimberly Gore

### PART ONE: 
### NASA Mars News

>> Scraped the [NASA Mars News Site](https://mars.nasa.gov/news/) and collected the latest News Title and Paragraph Text.

>> First, I scraped the section of html with the data needed

>> Then, I narrowed down the data until there was only the title and paragraph

>> The latest News Title and Paragraph retrieved was:

      * NASA InSight's 'Mole' Is Out of Sight
      
      * Now that the heat probe is just below the Martian surface, InSight's arm will scoop some additional soil on top to help it keep digging so it can take Mars' temperature.

### JPL Mars Space Images - Featured Image
>> Visited the url for JPL Featured Space Image [here](https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars)

>> Parsed HTML with Beautiful Soup

>> Retrieved the featured image link


Insert Screenshot here
![](https://github.com/KGore12/web-scraping-challenge/blob/main/Missions_to_Mars/images/JPL_Mars_Space_Images_-_Featured_Image.png)


### Mars Facts
>> Visitd the Mars Facts webpage [here](https://space-facts.com/mars/) for interesting facts about Mars

>> Used Pandas to scrape the table containing facts about the planet including Diameter, Mass, etc.

Insert Screenshot here of the data table
![](https://github.com/KGore12/web-scraping-challenge/blob/main/Missions_to_Mars/images/Mars_Facts_table.png)



### Mars Hemispheres
>> Visited the USGS Astrogeology site [here](https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars)

>> Scraped into Soup and then createed a dictionary to for titles & links to the hemisphere images

>> Retrieved and iterated through each div to pull titles and make list of hrefs to iterate through


Insert Screenshot here



### Part 2 - 
### MongoDB and Flask Application
>> Converted the Jupyter notebook into a Python script called scrape_mars.py with a function called scrape

>> Created a route called /scrape that will import your scrape_mars.py script and call your scrape function

>> Created a template HTML file called index.html that will take the mars data dictionary and display all of the data in the appropriate HTML elements











