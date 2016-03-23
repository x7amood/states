#!/usr/bin/env python

import csv
import os
import sys


sys.path.append('..')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')

from main.models import State, StateCapital

import django
django.setup()
# State.objects.all().delete()  

dir_path = os.path.dirname(os.path.abspath(__file__))
# print os.path.dirname(os.path.abspath(__file__)) + '/states.csv'
# print '%s/states.csv' % dir_path

states_csv = os.path.join(dir_path, 'states.csv')
csv_file = open(states_csv, 'r')
print csv_file

reader = csv.DictReader(csv_file)
for row in reader:

	new_state, created = State.objects.get_or_create(name=row['state'])
	new_state.abbreviation = row['abbrev']
	new_state.save()

	new_capital, created = StateCapital.objects.get_or_create(name=row['capital'])
	new_capital.state = new_state
	new_capital.latitude = row['latitude']
	new_capital.longitude = row['longitude']
	new_capital.capital_population = row['population']
	new_capital.save()

# # states = State.objects.all()
# for state in states:
# 	print state.name









