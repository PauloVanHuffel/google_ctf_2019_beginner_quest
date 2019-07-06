from bs4 import BeautifulSoup

import requests

result_dict = {"too fast": "slow_down",
               "getting away": False,
               "closer": True}


def make_step(url):

    #url = "https://drivetothetarget.web.ctfcompetition.com/"

    r = requests.get(url)

    data = r.text
    soup = BeautifulSoup(data, "lxml")

    lon = soup.find_all('input', {"name": "lon"})[0]["value"]
    lat = soup.find_all('input', {"name": "lat"})[0]["value"]
    token = soup.find_all('input', {"name": "token"})[0]["value"]
    result = [x.text for x in soup.find_all('p') if not "Hurry up" in x.text and x.text]
    if not result:
        result = ""
    else:
        result = result[0]
    return result, token, lat, lon

base_url = 'https://drivetothetarget.web.ctfcompetition.com/'
start_url = 'https://drivetothetarget.web.ctfcompetition.com/?lat=51.602489999985046&lon=-0.1929&token=gAAAAABdF6BuXoOTZ0sC2MKFMAi_QumSqlCK90S-ExGtRg7cGEMN6o8P4BzabHbiJ3cCEFO5PB_OK4AJsMYvXqDlYh5Lfy0ly8oKIZ9R5zuJaDWSbhoJzypfO1ZX1Yd_WYEBFFvlBNiV'

result, token, lat, lon = make_step(start_url)

lat_step = 0.00002
lon_step = 0.00003

going_the_right_way = None
first = True
while going_the_right_way or first:
    first = False
    going_the_right_way = None
    for key in result_dict.keys():
        if key in result:
            going_the_right_way = result_dict[key]
            break
        if result == "":
            going_the_right_way = True
            break

    if going_the_right_way is None:
        print("new result type: " + str(result))
        break

    new_lat = str(float(lat) - lat_step)
    new_lon = str(float(lon))

    if going_the_right_way == 'slow_down':
        going_the_right_way = True
        lat_step -= 0.00001

    new_url = base_url + "?lat=" + new_lat + "&lon=" + new_lon + "&token=" + token
    print(new_url)

    result, token, lat, lon = make_step(new_url)
    print(result)
