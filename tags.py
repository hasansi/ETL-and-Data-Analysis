#!/usr/bin/env python
# -*- coding: utf-8 -*-
import xml.etree.cElementTree as ET
import pprint
import re
"""
The purpose of this program is to explore the
"k" value for each "<tag>" and see if there are any potential problems.
"""


lower = re.compile(r'^([a-z]|_)*$')
lower_colon = re.compile(r'^([a-z]|_)*:([a-z]|_)*$')
problemchars = re.compile(r'[=\+/&<>;\'"\?%#$@\,\. \t\r\n]')

def key_type(element, keys):
    		
    if element.tag == "tag":
        m=lower.search(element.attrib['k'])
        n=lower_colon.search(element.attrib['k'])
        p=problemchars.search(element.attrib['k'])
        if m:
            keys['lower'] += 1
        elif n:
            keys['lower_colon'] += 1
        elif p:
            keys['problemchars'] += 1
	    print p.group()
            print element.attrib['k']	
        else:
            keys['other'] += 1
            
        pass
        
    return keys



def process_map(filename):
    keys = {"lower": 0, "lower_colon": 0, "problemchars": 0, "other": 0}
    for _, element in ET.iterparse(filename):
        keys = key_type(element, keys)

    return keys



def test():
    keys = process_map('sample.osm')
    pprint.pprint(keys)

if __name__ == "__main__":
    test()
