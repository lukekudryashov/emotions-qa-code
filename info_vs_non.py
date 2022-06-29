# merges multiple csvs into one df, separates merged df into informational and non-informational needs questions, writes each into a separate csv

import pandas as pd
import csv, math, ast, json, re
import numpy as np

def join_dfs_from_files(*arg):
	"""
	takes any number of strings (file names, include '.csv')
	reads each file as pandas df, joins all dfs into one
	returns the combined dfs
	"""
	df = pd.DataFrame()

	for file_name in arg:
		#read data file
		with open(file_name) as csvfile:
			new_df = pd.read_csv(csvfile)
		
		#check if df has already been filled with the first dataframe
		if df.empty:
			df = new_df
			#print("df is empty")
		else:
			df = pd.concat([df, new_df], axis=0)
			#print("df is not empty")

	return df


def separate(df):
	"""
	takes a pandas df (df)
	separates into two dfs - one that has informational needs questions (alone or with others), the other that has any needs except informational
	writes dfs to csvs
	"""

	noninf_df = pd.DataFrame()
	inf_df = pd.DataFrame()

	#iterate over each row in the combined df
	inf_count = 0
	noninf_count = 0
	for index, row in df.iterrows():
		#takes the value of the informational_support column in that row
		inf_support = row['informational_support']
		#checks if the value is nan (type is string if there is content, float if there is not)
		if(type(inf_support) == float):
			noninf_count += 1
			#adds the row to the noninf df if informational_support column is empty
			noninf_df = noninf_df.append(row)
		else:
			#adds the row to the inf df if informational_support column is not empty
			inf_df = inf_df.append(row)
			inf_count += 1
	print(inf_count)
	print(noninf_count)

	#writes the dfs to csvs
	noninf_df.to_csv('noninf.csv')
	inf_df.to_csv('inf.csv')


	


df = join_dfs_from_files('Ann1_round2.csv', 'Ann1_round3.csv', 'Ann1_round4.csv', 'Ann2_round2.csv', 'Ann2_round3.csv', 'Ann3_round2.csv', 'Ann3_round3.csv', 'Ann3_round4.csv', 'Ann3_round5.csv', 'Ann3_round6.csv', 'Ann4_round3.csv', 'Ann4_round4.csv', 'Ann4_round5.csv', 'Ann4_round6.csv', 'Ann5_round2.csv', 'Ann5_round3.csv', 'Ann6_round3.csv', 'Ann7_round3.csv', 'Ann8_round3.csv', 'Ann8_round4_part1.csv', 'Ann9_round3.csv')
print(len(df))
separate(df)