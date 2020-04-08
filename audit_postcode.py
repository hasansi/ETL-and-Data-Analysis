"""
This program lets you audit and update the postcode type name. As a result, a mapping of the postcode types is produced for use and storage in a database. 
"""
from __future__ import print_function
import xml.etree.cElementTree as ET
from collections import defaultdict
import re
import pprint
import sys
import maps
mapping=maps.mapping_postcode
expected=maps.expected_postcode
TEST=True
OVERLOOKEXPECTED=False
OSMFILE = "lexington.osm"
postcode_type_re = re.compile(r'\b\S+\.?$', re.IGNORECASE)

def audit_postcode_type(postcode_types, tentative_postcode_type):
    postcode_type = postcode_type_re.search(tentative_postcode_type).group()
    if postcode_type not in expected or OVERLOOKEXPECTED:
            postcode_types[postcode_type].add(tentative_postcode_type)


def is_postcode(elem):
    return (elem.attrib['k'] == "addr:postcode")


def audit(osmfile):
    osm_file = open(osmfile, "r")
    postcode_types = defaultdict(set)
    for event, elem in ET.iterparse(osm_file, events=("start",)):

        if elem.tag == "node" or elem.tag == "way":
            for tag in elem.iter("tag"):
                if is_postcode(tag):
                    audit_postcode_type(postcode_types, tag.attrib['v'])
    osm_file.close()
    return postcode_types


def update_name(name, mapping):
     
    postcode_type = postcode_type_re.search(name).group()
    if postcode_type in mapping.keys():	
    	try:
		name=mapping[postcode_type]
    	except:
		pass
    return name

def test():
    postcode_types = audit(OSMFILE)
    for key in postcode_types.keys():
    	if key not in mapping and key not in expected:
		print (key, postcode_types[key], "\n", "ALERT!!! Please investigate the postcode type", "\"",key,"\"", "further! and then include it in mappring or expected postcode types", end='\n\n') 
    sys.stdout.flush()
    #pprint.pprint(dict(postcode_types))

    for postcode_type, ways in postcode_types.iteritems():
        for name in ways:
            better_name = update_name(name, mapping)
            print (name, "=>", better_name)
            

if __name__ == '__main__':
	if TEST:    
		test()
