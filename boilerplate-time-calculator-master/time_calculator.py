def add_time(start, duration, dow="none"):
	
	days = 0
	new_dow = ""
	days_later = ""
	dow_dict = { 
		"monday": 0, 
		"tuesday": 1, 
		"wednesday": 2, 
		"thursday": 3, 
		"friday": 4, 
		"saturday": 5, 
		"sunday": 6 
		}

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
		start_hour = start_hour + 12

	total_hours = start_hour + duration_hours
	total_minutes = start_minute + duration_minutes

	#Calculates days based on a 24hr day and hours on 60 minute hour
	while total_minutes > 60:
		total_hours += 1
		total_minutes -= 60
	while total_hours >= 24:
		days += 1
		total_hours -= 24

	#Creating 
	if days > 1:
		days_later = f" ({days} days later)"
	elif days == 1:
		days_later = " (next day)"
	
	#If there was no Day of the Week (dow) passed as a param
	if dow != "none" :
		lower_dow = dow.lower()
		number_dow = dow_dict[lower_dow]
		dow_total = number_dow + days

		#If days elapsed are over a week, roll over
		while dow_total > 6:
			dow_total = dow_total - 7

		#Converting int to string based on day of the week
		dow_list = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
		new_dow = ", " + dow_list[dow_total]

	#Formats the 24Hr time to 12hr with AM and PM
	if 11 < total_hours < 24 :
		total_hours -= 12
		AorP = " PM"
	else:
		AorP = " AM"

	#Solution needs to be in 12hr format not 24hr	
	if total_hours == 0:
		total_hours = 12

	#Formatting the minutes
	if len(str(total_minutes)) == 1:
		total_minutes = "0" + str(total_minutes)

	#Concatenating all the strings for intended return
	new_time = str(total_hours) + ":" + str(total_minutes) + AorP + new_dow + days_later

	return new_time


# ======== TESTING ONLY BELOW HERE ======== #

#print(add_time("11:59 PM", "24:05"))
