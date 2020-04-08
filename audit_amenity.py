"""
This program lets you audit and update the amenity type name. As a result, a mapping of the amenity types is produced for use and storage in a database. 
"""
from __future__ import print_function
import xml.etree.cElementTree as ET
from collections import defaultdict
import re
import pprint
import sys
import maps
mapping=maps.mapping_amenity
expected=maps.expected_amenity
TEST=True
OVERLOOKEXPECTED=False
OSMFILE = "lexington.osm"
amenity_type_re = re.compile(r'\b\S+\.?$', re.IGNORECASE)

def audit_amenity_type(amenity_types, tentative_amenity_type):
    amenity_type = amenity_type_re.search(tentative_amenity_type).group()
    if amenity_type not in expected or OVERLOOKEXPECTED:
            amenity_types[amenity_type].add(tentative_amenity_type)


def is_amenity(elem):
    return (elem.attrib['k'] == "amenity")


def audit(osmfile):
    osm_file = open(osmfile, "r")
    amenity_types = defaultdict(set)
    for event, elem in ET.iterparse(osm_file, events=("start",)):

        if elem.tag == "node" or elem.tag == "way":
            for tag in elem.iter("tag"):
                if is_amenity(tag):
                    audit_amenity_type(amenity_types, tag.attrib['v'])
    osm_file.close()
    return amenity_types


def update_name(name, mapping):
     
    amenity_type = amenity_type_re.search(name).group()
    if amenity_type in mapping.keys():	
    	try:
		name=mapping[amenity_type]
    	except:
		pass
    return name

def test():
    amenity_types = audit(OSMFILE)
    for key in amenity_types.keys():
    	if key not in mapping and key not in expected:
		print (key, amenity_types[key], "\n", "ALERT!!! Please investigate the amenity type", "\"",key,"\"", "further! and then include it in mappring or expected amenity types", end='\n\n') 
    sys.stdout.flush()
    #pprint.pprint(dict(amenity_types))

    for amenity_type, ways in amenity_types.iteritems():
        for name in ways:
            better_name = update_name(name, mapping)
            print (name, "=>", better_name)
            

if __name__ == '__main__':
	if TEST:    
		test()
