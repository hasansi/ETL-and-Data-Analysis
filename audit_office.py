"""
This program lets you audit and update the office type name. As a result, a mapping of the office types is produced for use and storage in a database. 
"""
from __future__ import print_function
import xml.etree.cElementTree as ET
from collections import defaultdict
import re
import pprint
import sys
import maps
mapping=maps.mapping_office
expected=maps.expected_office
TEST=True
OVERLOOKEXPECTED=True
OSMFILE = "lexington.osm"
office_type_re = re.compile(r'\b\S+\.?$', re.IGNORECASE)

def audit_office_type(office_types, tentative_office_type):
    office_type = office_type_re.search(tentative_office_type).group()
    if office_type not in expected or OVERLOOKEXPECTED:
            office_types[office_type].add(tentative_office_type)


def is_office(elem):
    return (elem.attrib['k'] == "office")


def audit(osmfile):
    osm_file = open(osmfile, "r")
    office_types = defaultdict(set)
    for event, elem in ET.iterparse(osm_file, events=("start",)):

        if elem.tag == "node" or elem.tag == "way":
            for tag in elem.iter("tag"):
                if is_office(tag):
                    audit_office_type(office_types, tag.attrib['v'])
    osm_file.close()
    return office_types


def update_name(name, mapping):
     
    office_type = office_type_re.search(name).group()
    if office_type in mapping.keys():	
    	try:
		name=mapping[office_type]
    	except:
		pass
    return name

def test():
    office_types = audit(OSMFILE)
    for key in office_types.keys():
    	if key not in mapping and key not in expected:
		print (key, office_types[key], "\n", "ALERT!!! Please investigate the office type", "\"",key,"\"", "further! and then include it in mappring or expected office types", end='\n\n') 
    sys.stdout.flush()
    #pprint.pprint(dict(office_types))

    for office_type, ways in office_types.iteritems():
        for name in ways:
            better_name = update_name(name, mapping)
            print (name, "=>", better_name)
            

if __name__ == '__main__':
	if TEST:    
		test()
