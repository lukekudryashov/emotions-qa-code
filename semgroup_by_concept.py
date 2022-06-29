# this program produces a csv of semgroup counts from a csv of semtype counts

import pandas as pd
import csv

#read data file
with open('semtype_counts_with_repeats.csv') as csvfile:
	semtype_df = pd.read_csv(csvfile)

semgroup_dicts = []
column_names = ['count','count_emotion','count_sadness', 'count_joy','count_fear','count_anger','count_surprise', 'count_disgust', 'count_trust', 'count_anticipation', 'count_confusion', 'count_denial']

semtype_df.reset_index()
semtype_df = semtype_df.fillna(0)

#iterate by row of semtype df
for index, row in semtype_df.iterrows():
	print(index)
	print("already_added reset")
	#reset already_added variable
	already_added = False

	#check if the semgroup has already been added to the semgroup dicts list
	for semgroup in semgroup_dicts:
		#print(semgroup)
		print(row['group_code'])
		if row['group_code'] in semgroup.values():
			print("group found")
			for column in column_names:
				#for each column value, if value is the semgroup dict is not null, add it to the column value in the row
				if semgroup[column]:
					semgroup[column] += row[column]
				#if semgroup dict value is null, assign the row column value to the semgroup dict value
				else:
					semgroup[column] = row[column]
			#change already_added to True to bypass the next step of creating a new dict for the semgroup
			already_added = True
			print("changed already_added to true")
	#if the semgroup hasn't already been added, create a new dict
	if already_added == False:
		print("group not found")
		new_dict = dict()
		new_dict['group_code'] = row['group_code']
		new_dict['group_name'] = row['group_name']
		#add each column value in row to the dict
		for column in column_names:
			new_dict[column] = row[column]
		#append dict to main dict list
		semgroup_dicts.append(new_dict)

#write the semgroup_counts dict to csv
with open('semgroup_counts.csv','w') as output_file:
	dict_writer = csv.DictWriter(output_file, semgroup_dicts[0].keys())
	dict_writer.writeheader()
	dict_writer.writerows(semgroup_dicts)

