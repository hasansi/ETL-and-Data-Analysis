#!/usr/bin/env python
# -*- coding: utf-8 -*-
import xml.etree.cElementTree as ET
import pprint
import re
"""
Returns the number of users with unique 'uid'
"""

def get_user(element):
    return 
     


def process_map(filename):
    users = set()
    for _, element in ET.iterparse(filename):
        if 'uid' in element.attrib:
            uid=element.attrib['uid']
            users.add(uid)
        pass

    return users


def test():

    users = process_map('sample.osm')

    pprint.pprint(len(users))


if __name__ == "__main__":
    test()
