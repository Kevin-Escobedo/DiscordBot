import requests
import json
import random
import secret
def joke(theme = ""):

	if theme != "":
		data = requests.get("https://official-joke-api.appspot.com/jokes/"+theme+"/random")
		try:
			data_text_dict = json.loads(data.text)[0]
		except:
			return ["No jokes found for the theme " + theme + "!"]

	else:
		data  =requests.get("https://official-joke-api.appspot.com/random_joke")
		data_text_dict = json.loads(data.text)
	
	return [data_text_dict["setup"],data_text_dict["punchline"]]

def weather(location = ""):
	print(location)
	try:
		data = json.loads(requests.get("http://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+secret.open_weather_api_key).text)
		country = data["sys"]["country"]
		temp = str(round(int(data["main"]["temp"]) - 273.15))		
		weather_decription = data["weather"][0]["description"]
		real_name = data['name']
		return real_name + " (" + country + ") is experiencing " + weather_decription + " and the temperature is " + temp + " C." 
	except:
		return "there was a problem getting weather data for " + location + "!"

def image(theme = ""):
	headers = {
    'x-rapidapi-host': "bing-image-search1.p.rapidapi.com",
    'x-rapidapi-key': "7ba2b448famsh1a9b782f4bd7ec3p12da67jsn9fcff09ab2cf"
    }
	url = "https://rapidapi.p.rapidapi.com/images/trending"
	data = requests.request("GET", url, headers=headers)

	return data