#! python3
import json, requests, sys

# Check usage & get location
if len(sys.argv) < 2:
	print('Usage: quickWeather.py "City, State"')
	print('Example: quickWeather.py Spokane, WA')
	sys.exit()
location = ' '.join(sys.argv[1:])

# Download JSON data from OpenWeatherMap.org's API
url = 'http://api.openweathermap.org/data/2.5/forcast/daily?q=%s&cnt=3' % (location)   # %s = place holder for location, which is referenced after the string.
response = requests.get(url)
response.raise_for_status # Check for errror

# Load JSON data to python object & print
weatherData = json.loads(response.text)

print (weatherData)

w = weatherData['list']
print('Current weather in %s:' % (location))
print(w[0]['weather'][0]['main'], '-', w[0]['weather'][0]['description'])
print()
print('Tomorrow:')
print(w[1]['weather'][0]['main'], '-', w[1]['weather'][0]['description'])
print()
print('Day after tomorrow:')
print(w[2]['weather'][0]['main'], '-', w[2]['weather'][0]['description'])

# TODO Create webserver to pull data to
# TODO Create android\iphone app to collect data
# TODO Average weather data from mutiple sources
# TODO Create a config file to save preferences; location, # of days to display, alert settings, scheduling settings, email\phone number, weather data sources
# TODO Scheduling
# TODO Alerts & Reminders