# importing modules
import json
import os
import pathlib
from datetime import date

import helper
import requests

# setup
root = pathlib.Path(__file__).parent.parent.resolve()
LAT = os.getenv("lat")
LON = os.getenv("lon")
APIKEY = os.getenv("open_weather_key")
url = (
    "https://api.openweathermap.org/data/2.5/onecall?lat=%s&lon=%s&appid=%s&exclude=current,minutely,hourly,alerts&units=metric"
     % (LAT, LON, APIKEY)
)

response = requests.get(url)
response_dict = json.loads(response.text)
d = date.today()
output_date = d.strftime("%A %d. %B %Y")

today_weather = str(response_dict["daily"][0]["temp"]["day"])
high_temp = str(response_dict["daily"][0]["temp"]["max"])
low_temp = str(response_dict["daily"][0]["temp"]["min"])
today_desc = str(response_dict["daily"][0]["weather"][0]["description"])

string_today = f"#### Today's date is {output_date}\n\n"
string_today += f"- The average temperature today is {today_weather}˚C;\n"
string_today += f"- With highs of {high_temp}˚C and lows of {low_temp}˚C.\n"
string_today += f"- You can expect {today_desc} for the day.\n"

# processing
if __name__ == "__main__":
    p = root / "_pages/morning.md"
    c = p.open().read()
    f = helper.replace_chunk(c, "weather_marker", string_today)
    p.open("w").write(f)

print("Weather completed")
