from flask import Flask, render_template, request
import requests
import matplotlib.pyplot as plt
import numpy as np


#initialize flask
app = Flask(__name__)
#route your webpage
@app.route("/")
def visitors():

	# Load current count
	counter_read_file = open("count.txt", "r")
	visitors_count = int(counter_read_file.read())
	counter_read_file.close()

	# Increment the count
	visitors_count = visitors_count + 1

	# Overwrite the count
	counter_write_file = open("count.txt", "w")
	counter_write_file.write(str(visitors_count))
	counter_write_file.close()
# Render HTML with count variable
	return render_template("index.html", count=visitors_count)

#route your webpage
@app.route('/', methods=['post'])
def covid_stats():
	# Load current count
	counter_read_file = open("count.txt", "r")
	visitors_count = int(counter_read_file.read())
	counter_read_file.close()

	#complete the code
	text = request.form['text']
	# corona_data = 'https://covidstats-sdbd.onrender.com/?country='+text
	# print(corona_data)
	
	url = "https://covid-19-coronavirus-statistics.p.rapidapi.com/v1/total"

	querystring = {
		'country': text 
	}
	print(querystring)
	headers = {
        "X-RapidAPI-Key": "06e4bfb70emsh34e74328519271cp14e7dbjsn6c9c6918c36b",
        "X-RapidAPI-Host": "covid-19-coronavirus-statistics.p.rapidapi.com"
    }

	response = requests.request("GET", url, headers=headers, params=querystring)  

# {"error":false,
# "statusCode":200,
# "message":"OK",
# "data":{
# "recovered":null,
# "deaths":530779,
# "confirmed":44690738,
# "lastChecked":"2023-03-27T15:07:07+00:00","lastReported":"2023-03-10T04:21:03+00:00",
# "location":"India"}}

	print(response.text)
	data = response.text[3]
	print(data)
	
	return render_template("index.html", image="https://www.google.com/imgres?imgurl=https%3A%2F%2Fmedia.istockphoto.com%2Fid%2F1322277517%2Fphoto%2Fwild-grass-in-the-mountains-at-sunset.jpg%3Fs%3D612x612%26w%3D0%26k%3D20%26c%3D6mItwwFFGqKNKEAzv0mv6TaxhLN3zSE43bWmFN--J5w%3D&tbnid=4POnWjbftJPE5M&vet=12ahUKEwju_J3Utfz9AhUeHLcAHQ6BDicQMygDegUIARDHAQ..i&imgrefurl=https%3A%2F%2Fwww.istockphoto.com%2Fphotos%2Fnature&docid=tnVTsEa64LdCyM&w=612&h=408&q=image&ved=2ahUKEwju_J3Utfz9AhUeHLcAHQ6BDicQMygDegUIARDHAQ", count=visitors_count)
#add code for executing flask

if __name__ == "__main__":
	app.run()