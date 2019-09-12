#%%
import http.client
import json
import time
import timeit
import sys
import collections
from pygexf.gexf import *

from pprint import pprint
import urllib.request # I have added as it is a standard library_AY.

#%%
# ash_key=str(sys.argv)


#%%
key = '50ea93987447c4d7483b02d78f98f2ce'
# key = sys.argv[1]


#%%
def min_parts():
	"""
	Returns an integer value
	"""
	# you must replace this with your own value
	return 270

#%%

# ? There is a message that urllib does not have a request module. However, it works just fine in the 
# Jupyter notebook running on Anaconda
def lego_sets():
	"""
	return a list of lego sets.
	this may be a list of any type of values
	but each value should represent one set
	e.g.,
	biggest_lego_sets = lego_sets()
	print(len(biggest_lego_sets))
	> 280
	e.g., len(my_sets)
	"""
	# you must replace this line and return your own list
	max_parts = 300
	page_size = 10
	limit = 300

	url='https://rebrickable.com/api/v3/lego/sets/?'\
    'page_size={}&ordering=-num_parts&key={}&limit={}'\
    .format(page_size,key,limit)

	# url='https://rebrickable.com/api/v3/lego/sets/?'\
	# 	'page_size={}&min_parts={}&max_parts={}&key={}&oredering=num_parts'\
	# 	.format(page_size, min_parts(), max_parts, key)
	data=urllib.request.urlopen(url)
	
	response=data.read()
	encoding=data.info().get_content_charset('utf-8')
	raw_data=json.loads(response.decode(encoding))
	
	raw_data['results'] = raw_data['results'][:300]
	# total_set_num=[]
	# for i in range(300):
	# 	total_set_num.append(raw_data['results'][i]['set_num'])
	return raw_data['results']

results = lego_sets()

#%%
set_number_parts={}

for set_num in results[0:3]:

	# ?? Not sure why do I need to close the broken line with ' 
	url='https://rebrickable.com/api/v3/lego/sets/parts/?'\
		'key={}/'.format(key)

	data=urllib.request.urlopen(url)
	# temp_read_data=data.read()
	# encoding=data.info().get_content_charset('utf-8')
	# raw_data_part=json.loads(temp_read_data.decode(encoding))


	# print(raw_data_part)
	# part_color=raw_data_part['results']
	# part_quantity
	# part_name
	# part_number
	
	# set_number_parts.update()

#%%
#This is a test cell 
f=open('Results_Dictionary.txt','r')
data=f.read()


#%%
#Constructing a graph using the pygexf
def gexf_graph():
	"""
	return the completed Gexf graph object
	"""
	sys.path.append('../gexf')
	from gexf import Gexf, GexfImport

	# test helloworld.gexf
	gexf = Gexf("Paul Girard","A hello world! file")
	graph=gexf.addGraph("directed","static","a hello world graph")

	graph.addNode("0","hello")
	graph.addNode("1","World")
	graph.addEdge("0","0","1")

	output_file=open("helloworld.gexf","w")
	gexf.write(output_file)

	# you must replace these lines and supply your own graph
	# my_gexf = Gexf("author", "title")
	# gexf.addGraph("undirected", "static", "I'm an empty graph")
	# return gexf.graphs[0]

# complete auto-grader functions for Q1.2.d

def avg_node_degree():
	"""
	hardcode and return the average node degree
	(run the function called “Average Degree”) within Gephi
	"""

	# you must replace this value with the avg node degree
	return -1

def graph_diameter():
	"""
	hardcode and return the diameter of the graph
	(run the function called “Network Diameter”) within Gephi
	"""
	# you must replace this value with the graph diameter
	return -1

def avg_path_length():
	"""
	hardcode and return the average path length
	(run the function called “Avg. Path Length”) within Gephi
	:return:
	"""
	# you must replace this value with the avg path length
	return -1
#%%
def get_lego_parts(leg_set):
	set_numbers = [lego_set['set_num'] for lego_set in results['results']]
	page_size = 1000
	for lego_sets in set_numbers:
		ulr = 'https://rebrickable.com/api/v3/lego/sets/{}/parts/?key={}&page_size={}'.format(lego_sets, key, page_size)
		data=urllib.request.urlopen(url)
		response=data.read()
		encoding=data.info().get_content_charset('utf-8')
		raw_data=json.loads(response.decode(encoding))

# for each in range(len(Set_Num)):
#     Temp=API_URL_Template.split('/')
#     Temp[7]=Set_Num[each]
#     API_URL='/'.join(Temp)
#     API_Response=requests.get(API_URL,{'key':value_key})
#     API_Data.update([(Set_Num[each],API_Response.json())])