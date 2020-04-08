
import csv, sqlite3
import pandas as pd
from tabulate import tabulate

con = sqlite3.connect("./lexington.db")
cur = con.cursor()

number_of_nodes='SELECT COUNT(*) FROM nodes'
number_of_ways='SELECT COUNT(*) FROM ways'
number_of_unique_users='SELECT COUNT(DISTINCT(uid)) FROM (SELECT uid FROM nodes UNION ALL SELECT uid FROM ways)'
number_of_users_contributing_once='SELECT COUNT(*) FROM (SELECT user, COUNT(*) as num FROM (SELECT user FROM nodes UNION ALL SELECT user FROM ways) GROUP BY user HAVING num=1)'
contributing_users='SELECT user, COUNT(*) as num FROM (SELECT user FROM nodes UNION ALL SELECT user FROM ways) GROUP BY user ORDER BY num DESC LIMIT 5'

def map_features(feature):
	query='SELECT value, COUNT(*) as num FROM nodes_tags WHERE key='+feature+' GROUP BY value ORDER BY num DESC LIMIT 5'	
	return query

def map_feature_details(feature,detail):
	query='SELECT nodes_tags.value, COUNT(*) as num FROM nodes_tags JOIN (SELECT DISTINCT(id) FROM nodes_tags WHERE value='+feature+') i ON nodes_tags.id=i.id WHERE nodes_tags.key='+detail+' GROUP BY nodes_tags.value ORDER BY num DESC LIMIT 5'
	return query

def number_of(query):
	result = cur.execute(query)
	return result.fetchone()[0]
    
def list_of_top(query):
	users = []
	for row in cur.execute(query):
		users.append(row)
	return users

def print_in_pandas(table,column1_name):	
		df = pd.DataFrame(table, columns = [column1_name, 'Frequency of Occurrence'])
		df.index=df.index+1
		print 		
		return df


if __name__ == '__main__':

	print "Number of nodes: " , number_of(number_of_nodes)
	print "Number of ways: " , number_of(number_of_ways)
	print "Number of unique users: " , number_of(number_of_unique_users)
	print "Number of users contributing once: " , number_of(number_of_users_contributing_once)

	print print_in_pandas(list_of_top(contributing_users),'User')

	print print_in_pandas(list_of_top(map_features('"amenity"')),'Amenity')

	print print_in_pandas(list_of_top(map_feature_details('"place_of_worship"','"religion"')),'Religion')

	print print_in_pandas(list_of_top(map_feature_details('"restaurant"','"cuisine"')),'Cuisine')

	print print_in_pandas(list_of_top(map_features('"shop"')),'shop')

	print print_in_pandas(list_of_top(map_feature_details('"supermarket"','"name"')),'Supermarket Name')

	print print_in_pandas(list_of_top(map_features('"office"')),'Office')

	print print_in_pandas(list_of_top(map_feature_details('"company"','"name"')),'Company Name')
		

	
	
