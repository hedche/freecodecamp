def add_time(start, duration, dow="none"):
	
	week_dict = { 
		"monday": 0, 
		"tuesday": 1, 
		"wednesday": 2, 
		"thursday": 3, 
		"friday": 4, 
		"saturday": 5, 
		"sunday": 6 
		}

	#If there was no Day of the Week (dow) passed as a param
	if dow not in week_dict :
                lower_dow = dow.lower()
                number_dow = week_dict[lower_dow]
	
	#Going from "1:20 PM" to ("1:20", "PM")	
	split_start = start.split()

	#Going from "1:20" to ("1", "20")
	split_hm = split_start[0].split(":")	
	
	start_hour = int(split_hm[0])
	start_minute = int(split_hm[1])
	
	duration_hours = int((duration.split(":")[0]))
	
	#If it's PM add on 12hrs to the hour of split_hm[0]
	if split_start[1] == "PM":
		
		total_hours = start_hour + 12

	total_hours = start_hour + duration_hours
		

	return total_hours


print(add_time("1:20 PM", "24:20", "tueSday"))
