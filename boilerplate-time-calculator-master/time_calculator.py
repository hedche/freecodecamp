def add_time(start, duration, dow="none"):
	
	days = 0
	new_dow = " "
	dow_dict = { 
		"monday": 0, 
		"tuesday": 1, 
		"wednesday": 2, 
		"thursday": 3, 
		"friday": 4, 
		"saturday": 5, 
		"sunday": 6 
		}
	value = 3
	if value in dow_dict:
		print(dow_dict[value])
	#If there was no Day of the Week (dow) passed as a param
	if dow != "none" :
		lower_dow = dow.lower()

	number_dow = dow_dict[lower_dow]
	
	#Going from "1:20 PM" to ("1:20", "PM")	
	split_start = start.split()

	#Going from "1:20" to ("1", "20")
	split_hm = split_start[0].split(":")	
	
	start_hour = int(split_hm[0])
	start_minute = int(split_hm[1])
	
	duration_hours = int((duration.split(":")[0]))
	duration_minutes = int((duration.split(":")[1]))

	#If it's PM add on 12hrs to the hour of split_hm[0]
	if split_start[1] == "PM":
		total_hours = start_hour + 12

	total_hours = start_hour + duration_hours
	total_minutes = start_minute + duration_minutes

	#Calculates days based on a 24hr day
	while total_hours > 24:
		days += 1
		total_hours -= 24
				
	dow_total = number_dow + days

	if days > 1:
		days_later = f"({days} days later)"
		
		#If days elapsed are over a week, carry over for wee
		while dow_total > 6:
			dow_total = dow_total - 7
		print(type(dow_total))
		
		new_dow = dow_dict[dow_total]

	#Formats the 24Hr time to 12Hr with AM and PM
	if total_hours < 24 and total_hours > 12:
		total_hours -= 12
		AorP = " PM"
	else:
		AorP = " AM"

	#Calculates if days elapsed are over a week
	while dow_total > 6:
		dow_total = dow_total - 7

	new_time = str(total_hours) + ":" + str(total_minutes) + AorP + new_dow + days_later

	return new_time


print(add_time("1:20 PM", "230:20", "tueSday"))
