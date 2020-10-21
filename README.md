# web-scraping-challenge
# Missions_to_Mars


## by  Kimberly Gore

### Part One: Scraping NASA Mars News

>> Scraped the [NASA Mars News Site](https://mars.nasa.gov/news/) and collected the latest News Title and Paragraph Text.
>> First, I scraped the section of html with the data needed
>> Then, I narrowed down the data until there was only the title and paragraph
>> The latest News Title and Paragraph retrieved was:
      * NASA InSight's 'Mole' Is Out of Sight
      * Now that the heat probe is just below the Martian surface, InSight's arm will scoop some additional soil on top to help it keep digging so it can take Mars' temperature.

>> Calculated total crime data for each Agency in Cuyahoga County

![](https://github.com/drjulie2105/Group_Project_1/blob/master/Crime_Cuyahoga/Output_Images/Crimes_per_County_df.PNG)

>> Compared population totals to crime totals for each Agency

>> Created visual graphics for crime totals and population using Pandas and Matplotlib

>> Focused on Top 7 Agencies by Population Totals and Top 7 Agencies by Crime Totals

**Conclusions:**

  1. Cleveland has the highest crime totals for Cuyahoga County.  Will utilize Cleveland for further analysis due to highest crime totals.
  
  ![](https://github.com/drjulie2105/Group_Project_1/blob/master/Crime_Cuyahoga/Output_Images/pop_totcrime_cleveland_2017_bar.png)

  2. The most common type of crime committed for all agencies is property crime. 
  
  ![](https://github.com/drjulie2105/Group_Project_1/blob/master/Crime_Cuyahoga/Output_Images/cle_vs_suburbs_2017_bar.png)



### Part Two: Analysis of Age Data and Race Data for all Crime Categories for Cleveland in 2017

>> Utilized ![FBI API key](https://crime-data-explorer.fr.cloud.gov/api) to obtain age and race data for Cleveland in 2017]

>> Created Data Frame for age and race data for all crime categories

>> Utilized Data Frames to create separate bar graphs for each crime category utilizing Pandas and Matplotlib

>> Created a pie chart of age data for further visualization

![](https://github.com/drjulie2105/Group_Project_1/blob/master/Crime_Cuyahoga/Output_Images/totcrimes_age_2017_pie.png)

**Conclusions:**

  1. The highest totals in the race category for all crime categories is the Black or African American category.
  
  ![](https://github.com/drjulie2105/Group_Project_1/blob/master/Crime_Cuyahoga/Output_Images/race_groups_df.PNG)

  2. The highest totals in the age category for all crime categories is in the 20-29 Age Group, with the exception of arson (the highest totals for arson was in the 
  10-19 age group.)

  ![](https://github.com/drjulie2105/Group_Project_1/blob/master/Crime_Cuyahoga/Output_Images/Age_Groups_df.PNG)



### Part Three: Utilized Crime Totals and Population to create heat maps.

**Utilizing Total Crime Data Only:**

![](https://github.com/drjulie2105/Group_Project_1/blob/master/Crime_Cuyahoga/Output_Images/totcrime_cuyahoga_2017_heatmap.png)

**Utilizing Crime Totals by Population:**

![](https://github.com/drjulie2105/Group_Project_1/blob/master/Crime_Cuyahoga/Output_Images/crime_by_pop_cuyahoga_2017_heatmap.png)
