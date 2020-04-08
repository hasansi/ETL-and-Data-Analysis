"""
This program lets you audit and update the street type name. As a result, a mapping of the types is produced for use and storage in a database. 
"""
from __future__ import print_function
import xml.etree.cElementTree as ET
from collections import defaultdict
import re
import pprint
import sys
import maps
mapping=maps.mapping_street
expected=maps.expected_street
TEST=True
OSMFILE = "lexington.osm"
street_type_re = re.compile(r'\b\S+\.?$', re.IGNORECASE)


# http://pe.usps.gov/text/pub28/28apc_002.htm for street abbreviations

def audit_street_type(street_types, street_name):
    m = street_type_re.search(street_name)
    if m:
        street_type = m.group()
        if street_type not in expected:
            street_types[street_type].add(street_name)


def is_street_name(elem):
    return (elem.attrib['k'] == "addr:street")


def audit(osmfile):
    osm_file = open(osmfile, "r")
    street_types = defaultdict(set)
    for event, elem in ET.iterparse(osm_file, events=("start",)):

        if elem.tag == "node" or elem.tag == "way":
            for tag in elem.iter("tag"):
                if is_street_name(tag):
                    audit_street_type(street_types, tag.attrib['v'])
    osm_file.close()
    return street_types


def update_name(name, mapping):
     
    street_type = street_type_re.search(name).group()
    if street_type in mapping.keys():	
    	try:
		name=re.sub(street_type_re, mapping[street_type],name)
    	except:
		pass
    return name

def test():
    st_types = audit(OSMFILE)
    for key in st_types.keys():
    	if key not in mapping and key not in expected:
		print (key, st_types[key], "\n", "ALERT!!! Please investigate the street type", "\"",key,"\"", "further! and then include it in mappring or expected street types", end='\n\n') 
    sys.stdout.flush()
    #pprint.pprint(dict(st_types))

    for st_type, ways in st_types.iteritems():
        for name in ways:
            better_name = update_name(name, mapping)
            print (name, "=>", better_name)
            if name == "Nicholasville Rd":
                assert better_name == "Nicholasville Road"
            

if __name__ == '__main__':
	if TEST:    
		test()
