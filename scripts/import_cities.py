#!/usr/bin/env python

import csv

import os

import sys

sys.path.append('..')

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')

from main.models import State, City



import django

django.setup()

# State.objects.all().delete()  



dir_path = os.path.dirname(os.path.abspath(__file__))

# print os.path.dirname(os.path.abspath(__file__)) + '/states.csv'

# print '%s/states.csv' % dir_path



cities_csv = os.path.join(dir_path, 'zip_codes_states.csv')

csv_file = open(cities_csv, 'r')

print csv_file

reader = csv.DictReader(csv_file)

for row in reader:

	
	state , created = State.objects.get_or_create(abbreviation=row['state'])

	new_city , create = City.objects.get_or_create(name=row['city'])
	new_city.zip_code= row ['zip_code']
	new_city.latitude = row['latitude']
	new_city.longitude = row['longitude']
	new_city.county = row['county']
	new_city.state = state


	try:
		new_city.save()
	except Exception,e:
		print e
		print new_city.name

# # states = State.objects.all()
# for state in states:
# 	print state.name

