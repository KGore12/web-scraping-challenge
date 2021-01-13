# Import dependencies
from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars


# Create an instance of Flask
app = Flask(__name__)

# Use PyMongo to establish Mongo connection
mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_app")
mars_data = mongo.db.mars_data

# Route to render index.html template using data from Mongo
@app.route("/")
def home():

    # Find one record of data from the mongo database
    mars_dict = mongo.db.mars_dict.find_one()

    # Return template and data
    return render_template("index.html", mars=mars_dict)

# Route that will trigger the scrape function
@app.route("/scrape")
def scrape():

    mars_dict = mongo.db.mars_dict

    # Run the scrape function
    scraped_data = scrape_mars.scrape()

    # Update the Mongo database using update and upsert=True
    mars_data.update({}, scraped_data, upsert=True)

    # Redirect back to home page
    return redirect("/data")  



if __name__ == "__main__":
    app.run(debug=True)
