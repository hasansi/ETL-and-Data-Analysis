#Build database of the CSV files with the corresponding table names.

import csv, sqlite3
from collections import OrderedDict

mdb = sqlite3.connect("lexington.db")
mdb.text_factory = str
cur = mdb.cursor()


def MakeTable(column_dict, filename):

	table='CREATE TABLE '+filename+'('+(', '.join("{} {}".format(k, v) for k, v in column_dict.items()))+');'
	cur.execute(table)

	with open(filename+'.csv','rb') as file_in:
    		dict_reader = csv.DictReader(file_in) 
    		db_column='('+(', '.join("i['{}']".format(k) for k,v in column_dict.items()))+')'
    		db_column='['+db_column.replace('\"','')+" for i in dict_reader]"
    		#print(db_column)
    		db_columns = eval(db_column)
	insert_into_table="INSERT INTO "+filename+'('+(', '.join("{}".format(k) for k, v in column_dict.items()))+')'+"VALUES ("+str("?,")*(len(column_dict)-1)+"?);"
	cur.executemany(insert_into_table, db_columns)
	mdb.commit()

#Make nodes table
nodes_columns=OrderedDict([('id', 'serial primary key'), ('lat', 'double precision'), ('lon', 'double precision'), ('user', 'varchar'), ('uid', 'varchar'), ('version', 'double precision'), ('changeset', 'varchar'), ('timestamp', 'DATETIME')])
MakeTable(nodes_columns,'nodes')

#Make nodes_tags table
nodes_tags_columns=OrderedDict([('id', 'serial references nodes(id)'), ('key', 'varchar'), ('value', 'varchar'), ('type', 'varchar')])
MakeTable(nodes_tags_columns,'nodes_tags')

#Make ways table
ways_columns=OrderedDict([('id', 'serial primary key'), ('user', 'varchar'), ('uid', 'varchar'), ('version', 'double precision'), ('changeset', 'varchar'), ('timestamp', 'DATETIME')])
MakeTable(ways_columns,'ways')

#Make ways_tags table
ways_tags_columns=OrderedDict([('id', 'serial references ways(id)'), ('key', 'varchar'), ('value', 'varchar'), ('type', 'varchar')])
MakeTable(ways_tags_columns,'ways_tags')

#Make ways_nodes table
ways_nodes_columns=OrderedDict([('id', 'serial NOT NULL'), ('node_id', 'serial NOT NULL'), ('position', 'double precision')])
MakeTable(ways_nodes_columns,'ways_nodes')







