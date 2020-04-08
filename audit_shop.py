"""
This program lets you audit and update the shop type name. As a result, a mapping of the shop types is produced for use and storage in a database. 
"""
from __future__ import print_function
import xml.etree.cElementTree as ET
from collections import defaultdict
import re
import pprint
import sys
import maps
mapping=maps.mapping_shop
expected=maps.expected_shop
TEST=True
OVERLOOKEXPECTED=True
OSMFILE = "lexington.osm"
shop_type_re = re.compile(r'\b\S+\.?$', re.IGNORECASE)

def audit_shop_type(shop_types, tentative_shop_type):
    shop_type = shop_type_re.search(tentative_shop_type).group()
    if shop_type not in expected or OVERLOOKEXPECTED:
            shop_types[shop_type].add(tentative_shop_type)


def is_shop(elem):
    return (elem.attrib['k'] == "shop")


def audit(osmfile):
    osm_file = open(osmfile, "r")
    shop_types = defaultdict(set)
    for event, elem in ET.iterparse(osm_file, events=("start",)):

        if elem.tag == "node" or elem.tag == "way":
            for tag in elem.iter("tag"):
                if is_shop(tag):
                    audit_shop_type(shop_types, tag.attrib['v'])
    osm_file.close()
    return shop_types


def update_name(name, mapping):
     
    shop_type = shop_type_re.search(name).group()
    if shop_type in mapping.keys():	
    	try:
		name=mapping[shop_type]
    	except:
		pass
    return name

def test():
    shop_types = audit(OSMFILE)
    for key in shop_types.keys():
    	if key not in mapping and key not in expected:
		print (key, shop_types[key], "\n", "ALERT!!! Please investigate the shop type", "\"",key,"\"", "further! and then include it in mappring or expected shop types", end='\n\n') 
    sys.stdout.flush()
    #pprint.pprint(dict(shop_types))

    for shop_type, ways in shop_types.iteritems():
        for name in ways:
            better_name = update_name(name, mapping)
            print (name, "=>", better_name)
            

if __name__ == '__main__':
	if TEST:    
		test()
