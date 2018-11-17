import csv

data_one = []
data_two = []

with open("master_file.csv", "r") as file_to_read:
	csv_to_read = csv.reader(file_to_read)
	for row in csv_to_read:
		data_one.append([row[0], row[1], row[2], row[3], "No"])


with open("uof_incidents.csv", "r") as file_to_read:
	csv_to_read = csv.reader(file_to_read)
	for row in csv_to_read:
		data_two.append(row[0])

#print str(data_one)
#print str(data_two)

for row in data_one:
	for incident in data_two:
		if row[0] == incident:
			row[4] = "Yes"


with open("final_data.csv","w") as file_to_write:
	csv_to_write = csv.writer(file_to_write)
	csv_to_write.writerow(['Incident ID','Day of Week','Time of Day','Nature of Incident','Incident of Violence'])
	for row in data_one:
		csv_to_write.writerow(row)

print "Finished"