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
from tqdm.auto import tqdm

#%%
command_line=sys.argv[1]
key=str(command_line)

#%%
def do_api(url_address):
	data=urllib.request.urlopen(url_address)
	response=data.read()
	encoding=data.info().get_content_charset('utf-8')
	raw_data=json.loads(response.decode(encoding))
	return raw_data

#%%

def min_parts():
	"""
	Returns an integer value
	"""
	# you must replace this with your own value
	return 1150

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
	page_size = 10000

	url='https://rebrickable.com/api/v3/lego/sets/?'\
    'page_size={}&ordering=-num_parts&key={}&min_parts={}'\
    .format(page_size,key,min_parts())

	raw_data = do_api(url)
	
	print(raw_data['count'])
	raw_data = raw_data['results'][:300]
	return raw_data

all_sets = lego_sets()

#%%

all_parts = []
for lego_set in tqdm(all_sets[:10]):
	url='https://rebrickable.com/api/v3/lego/sets/{}/parts/?key={}'\
			.format(lego_set['set_num'], key)
	raw_data = do_api(url)
	raw_data = raw_data['results'][:20]
	for part in raw_data:
		all_parts.append(
			{
				'id': part['part']['part_num'] + '_' + part['color']['rgb'],
				'color': part['color']['rgb'],
				'quantity': part['quantity'],
				'name': part['part']['name'],
				'number': part['part']['part_num'],
				'set_num': lego_set['set_num']
			}
		)


#%%

def hex2rgb(hex):
	return tuple(str(int(hex[i:i+2], 16)) for i in (0, 2, 4))

#Constructing a graph using the pygexf
def gexf_graph():
	"""
	return the completed Gexf graph object
	"""
	sys.path.append('../gexf')
	from gexf import Gexf, GexfImport

	# test helloworld.gexf
	gexf = Gexf("Ashkan Yousefi", "A hello world! file")
	graph = gexf.addGraph("undirected", "static", "a hello world graph")

	for lego_set in all_sets:
		node = graph.addNode(id=lego_set['set_num'], label=lego_set['name'],
							 r='0', g='0', b='0')
		node.Type = 'set'
	
	for lego_part in all_parts:
		rgb_color = hex2rgb(lego_part['color'])
		node = graph.addNode(id=lego_part['id'], label=lego_part['name'],
							 r=rgb_color[0], g=rgb_color[1], b=rgb_color[2])
		node.Type = 'part'

	for i, lego_part in enumerate(all_parts):
		node = graph.addEdge(id=str(i), source=lego_part['set_num'], target=lego_part['id'], weight=lego_part['quantity'])
		node.Type = 'part'

	with open("lego_graph.gexf","wb") as lego_file:
		gexf.write(lego_file)

	# you must replace these lines and supply your own graph
	# my_gexf = Gexf("author", "title")
	# gexf.addGraph("undirected", "static", "I'm an empty graph")
	# return gexf.graphs[0]
gexf_graph()

#%%
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