import json
import getpass
import requests



BASE_DOMAIN = 'secure.mealpal.com'
BASE_URL = 'https://' + BASE_DOMAIN
LOGIN_URL = BASE_URL + '/1/login'
CITIES_URL = BASE_URL + '/1/functions/getCitiesWithNeighborhoods'
MENU_URL = BASE_URL + '/api/v1/cities/%s/product_offerings/lunch/menu'
RESERVATION_URL = BASE_URL + '/api/v2/reservations'
KITCHEN_URL = BASE_URL + '/1/functions/checkKitchen3'

LOGGED_IN_COOKIE = 'isLoggedIn'

HEADERS = {
    'Host': BASE_DOMAIN,
    'Origin': BASE_URL,
    'Referer': BASE_URL + '/login',
    'Content-Type': 'application/json',
}

COOKIES = None

def login():
	data = {'username': 'plantspreferstanding@gmail.com', 'password': 'qpal1029'}
	r = requests.post(LOGIN_URL, data = json.dumps(data), headers = HEADERS)
	r.cookies.set(LOGGED_IN_COOKIE, 'true', domain = BASE_URL)
	COOKIES = r.cookies
	print(COOKIES)
	return r.status_code

def reserve():
	meal_id = '57465f9e-22a3-498c-9586-9ef339bd4586'
	reserve_data = {'quantity': 1, 'schedule_id': meal_id, 'pickup_time': '12:30pm-12:45pm', 'source': 'Web'}
	r = requests.post(RESERVATION_URL, data=json.dumps(reserve_data), headers= HEADERS, cookies= COOKIES)
	print(r.status_code,r.json())
	return r.status_code

def get_current_meal():
    r = requests.post(KITCHEN_URL, headers= HEADERS, cookies= COOKIES)
    print(r.json())


login()
# reserve()
get_current_meal()