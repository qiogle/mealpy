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

class MealPal(object):

	def __init__(self):
		self.headers = HEADERS
		self.cookies = None
		self.cities = None
		self.schedules = None

	def login(self):
		data = {'username': 'plantspreferstanding@gmail.com', 'password': 'qpal1029'}
		r = requests.post(
			LOGIN_URL, data = json.dumps(data), headers = self.headers)
		self.cookies = r.cookies
		self.cookies.set(LOGGED_IN_COOKIE, 'true', domain = BASE_URL)
		return r.status_code

	def get_schedules(self):
		city_id = '00000000-1000-4000-9845-9344bdb9408c'
		r = requests.get(
			MENU_URL % city_id, headers = self.headers, cookies = self.cookies)
		print(r.json().keys())
		return r.json()

	# def get_schedule_by_restaurant_name(
 #            self, restaurant_name, city_name=None, city_id=None):
 #        if not self.schedules:
 #            self.get_schedules(city_name, city_id)
 #        return filter(lambda x: x'restaurant']['name'] == restaurant_name,
 #                      self.schedules)[0]
        
	# def	reserve_meal(
 #            self, timing, restaurant_name=None, meal_name=None, city_name=None,
 #            city_id=None, cancel_current_meal=False):
 #        assert restaurant_name or meal_name
 #        if cancel_current_meal:
 #            self.cancel_current_meal()

 #        if meal_name:
 #            schedule_id = self.get_schedule_by_meal_name(
 #                meal_name, city_name, city_id)['id']
 #        else:
 #            schedule_id = self.get_schedule_by_restaurant_name(
 #                restaurant_name, city_name, city_id)['id']

 #        reserve_data = {
 #            'quantity': 1,
 #            'schedule_id': schedule_id,
 #            'pickup_time': timing,
 #            'source': 'Web'
 #        }

 #        r = requests.post(
 #            RESERVATION_URL, data=json.dumps(reserve_data),
 #            headers=self.headers, cookies=self.cookies)
 #        return r.status_code

mp = MealPal()

mp.login()
restaurants = mp.get_schedules()

data = {'item1': 'text1', 'item2': 'text2'}
with open('data.txt', 'w') as outfile:
	json.dump(restaurants, outfile)