#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This program parses the osm file and returns a dictionary with the 
tag name as the key and number of times this tag can be encountered in 
the map as value.
"""
import xml.etree.cElementTree as ET
import pprint
from collections import defaultdict
tagsdic=defaultdict(int)
def count_tags(filename):
    for event, elem in ET.iterparse(filename):
        tagsdic[elem.tag] +=1
    return tagsdic    


def test():

    tags = count_tags('sample.osm')
    print(tags['node'],tags['way'])
    
if __name__ == "__main__":
    test()
