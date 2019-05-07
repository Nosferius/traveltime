#!/usr/bin/python

# ToDo:
# - Files
# - Slecht weer
# - 

print ('Please type 0 when there are no bridges or traffic lights. \n\n' + 
      'Please use a . [dot] when writing decimals, not a comma! \n\n ')

#input
distance = float(input("Distance: "))
speed = float(input("speed: ")) / 60
bridges = 0 + int(input("How many bridges are there?: ")) * 5
traffic_lights = 0 + int(input("How many traffic lights are there?: "))

#calculations
time = float(distance / speed)
jam = bridges + traffic_lights
realistic_traveltime = float(time + (jam / 2))
estimate = float(time + jam)
max_traveltime = float(time + float(jam * 2))

#output
def readable_time (jam, realistic_traveltime, estimate, max_traveltime):
	if max_traveltime >= 60:
		print ('Your absolute minimum traveltime is ' + str(int(time / 60)) + ' hours and ' + str(round((time / 60 - int(time / 60)) * 60, 1)) + ' minutes.')
		print ('Your realistic minimum traveltime is ' + str(int(realistic_traveltime / 60)) + ' hours and ' + str(round((realistic_traveltime / 60 - int(realistic_traveltime / 60)) * 60, 1)) + ' minutes.')
		print ('Your estimated traveltime is ' + str(int(estimate / 60)) + ' hours and ' + str(round((estimate / 60 - int(estimate / 60)) * 60, 1)) + ' minutes.')
		print ('Your maximum traveltime is ' + str(int(max_traveltime / 60)) + ' hours and ' + str(round((max_traveltime / 60 - int(max_traveltime / 60)) * 60, 1)) + ' minutes.') 
	else:
		print ('The absolute minimum traveltime is ' + str(round(time, 1)) + ' minutes.')
		print ('The realistic minimum traveltime is ' + str(round(realistic_traveltime, 1)) + ' minutes.')
		print ('The estimated traveltime is ' + str(round(estimate, 1)) + ' minutes.')
		print ('The maximum traveltime is ' + str(round(max_traveltime, 1)) + ' minutes.')
		
readable_time(jam, realistic_traveltime, estimate, max_traveltime)

# test environment https://trinket.io/python
