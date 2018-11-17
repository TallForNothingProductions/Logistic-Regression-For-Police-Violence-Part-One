import csv

data = []
#List of files to read
array_of_files = ['uof20161.csv','uof20162.csv','uof20163.csv','uof20164.csv','uof20171.csv','uof20172.csv','uof20173.csv','uof20174.csv']

#For each file in the array
for file_name in array_of_files:
	#Open the file
	with open(file_name, 'r') as file_to_read:
		csv_to_read = csv.reader(file_to_read)
		#For each row in the array
		for row in csv_to_read:
			if row[0][0:3] == "B16" or row[0][0:3] == "B17":
				data.append(row[0])
	print "Finished a file"

with open('uof_incidents.csv','w') as file_to_write:
	csv_to_write = csv.writer(file_to_write)
	csv_to_write.writerow(['Use of Force Incident ID'])
	for row in data:
		csv_to_write.writerow([row])