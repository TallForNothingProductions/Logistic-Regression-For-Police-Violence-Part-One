import csv

data = []
#List of files to read
array_of_files = ['cfs20161.csv','cfs20162.csv']
array_of_files_two = ['cfs20163.csv','cfs20164.csv','cfs20171.csv','cfs20172.csv','cfs20173.csv','cfs20174.csv']

#This function gets time data and returns whether this event occurred in the morning time, day time, or night time.
def time_of_day(text):
	am_or_pm = text.split(" ")[1]
	hour = int(text.split(":")[0])

	if am_or_pm == "AM":
		if hour == 12:
			return "NIGHT"
		elif hour <= 5:
			return "NIGHT"
		else:
			return "MORNING"
	elif am_or_pm == "PM":
		if hour == 12:
			return "DAY"
		if hour <= 7:
			return "DAY"
		else:
			return "NIGHT"
	return "ERROR"

#This function gets military time data and returns whether this event occurred in the morning time, day time, or night time.
def time_of_day_military(text):
	hour = int(text.split(":")[0])

	if hour < 6:
		return "NIGHT"
	elif hour >= 6 and hour < 12:
		return "MORNING"
	elif hour >= 12 and hour < 20:
		return "DAY"
	else:
		return "NIGHT"

#For each file in the array
for file_name in array_of_files:
	#Open the file
	with open(file_name, 'r') as file_to_read:
		csv_to_read = csv.reader(file_to_read)
		#For each row in the array
		for row in csv_to_read:
			#Skip the first line
			try:
				case_number = row[0]
				day_of_the_week = row[4]
				time_of_day_of_event = time_of_day(row[2])
				nature_of_call = row[5]

				#Add data to global array 
				data.append([case_number, day_of_the_week, time_of_day_of_event, nature_of_call])
			except:
				pass
	print "Finished a file"

#For each file in the array
for file_name in array_of_files_two:
	#Open the file
	with open(file_name, 'r') as file_to_read:
		csv_to_read = csv.reader(file_to_read)
		#For each row in the array
		for row in csv_to_read:
			#Skip the first line
			try:
				case_number = row[0]
				day_of_the_week = row[4]
				time_of_day_of_event = time_of_day_military(row[2])
				nature_of_call = row[5]

				#Add data to global array 
				data.append([case_number, day_of_the_week, time_of_day_of_event, nature_of_call])
			except:
				pass
	print "Finished a file"

with open('master_file.csv','w') as file_to_write:
	csv_to_write = csv.writer(file_to_write)
	csv_to_write.writerow(['Case Number','Day of the Week','Time of the Day','Nature of the Call'])
	for row in data:
		csv_to_write.writerow(row)

print "Finished Analysis"

