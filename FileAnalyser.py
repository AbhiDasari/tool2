# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 16:34:37 2019

@author: 761317
"""

import os
import folderstats
folder = '.'
filepaths = [os.path.join(folder, f) for f in os.listdir(folder)]
print(filepaths)
files=[]
directories=[]

for (dirpath, dirnames, filenames) in os.walk('.'):
    for f in filenames:
        print('FILE :', os.path.join(dirpath, f))
        files.append(str(os.path.join(dirpath, f)))
    for d in dirnames:
        print('DIRECTORY :', os.path.join(dirpath, d))
        directories.append(str(os.path.join(dirpath, d)))
for file in files:
    print(file)
for directory in directories: 
    print(directory)
data = folderstats.folderstats('C:\\Users\\761317\\Desktop\\Code Comparision\\Data\\App-Dev', ignore_hidden=True)
print(data.head())



###################################################################
import matplotlib.pyplot as plt

with plt.style.context('ggplot'):
    data['extension'].value_counts().plot(
        kind='bar', color='C1', title='Extension Distribution by Count');
###################################################################
    
###################################################################
            
import squarify

# Group by extension and sum all sizes for each extension
extension_sizes = data.groupby('extension')['size'].sum()
# Sort elements by size
extension_sizes = extension_sizes.sort_values(ascending=False)
plt.figure(figsize=(5,5))
squarify.plot(sizes=extension_sizes.values, label=extension_sizes.index.values)
plt.title('Extension Treemap by Size')
plt.axis('off')
plt.savefig("C:\\Users\\761317\Desktop\\Code Comparision\\Results\\size_distribution.jpg", bbox_inches="tight")
####################################################################



####################################################################
import networkx as nx

# Sort the index
data_sorted = data.sort_values(by='id')

G = nx.Graph()
for i, row in data_sorted.iterrows():
    if row.parent:
        G.add_edge(row.id, row.parent)
    
# Print some additional information
print(nx.info(G))
####################################################################

from networkx.drawing.nx_pydot import graphviz_layout

pos_dot = graphviz_layout(G, prog='dot')

fig = plt.figure(figsize=(16, 8))
nodes = nx.draw_networkx_nodes(G, pos_dot, node_size=2, node_color='C0')
edges = nx.draw_networkx_edges(G, pos_dot, edge_color='C0', width=0.5)
plt.axis('off');
