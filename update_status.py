#!/usr/bin/python

# Script to update status.json (as used by SpaceAPI) to indicate if space is open or closed
# if someones on the wifi, assume space = open else space = closed.

# yes I know it's flawed - someone should interface with doorbot. or a switch. Or something.

# Andrew Elwell <Andrew.Elwell@gmail.com> March 2013

import json
import time

# set paths as needed
template = 'default.json'
out = 'status.json'



with open(template,'r') as infile:
	data = json.load(infile)


# do wondrous things with 'open' here....
webcam_users = 1

if webcam_users > 0:
    data['open'] = True
    data['state']['open'] = True

# update timestamp
data['state']['lastchange'] = time.time()

with open(out,'w') as outfile:
    outfile.write(json.dumps(data))
