import json
trans_fname = "./nyc_transmission.json"
with open(trans_fname, 'r') as infile:
    trans_data = json.load(infile)



vis_data = {}
vis_data['nodes'] = []
vis_data['links'] = []


for key, value in trans_data.iteritems():
    if value['object'] == 't_node':
        try:
            del value['id']
            del value['gldIndex']
        except KeyError:
            pass
        vis_data['nodes'].append(value)
    if value['object'] == 't_line':
        try:
            del value['id']
            del value['gldIndex']
        except KeyError:
            pass
        vis_data['links'].append(value)
    if value['object'] == 'centroid':
        # append centroid
        try:
            del value['id']
            del value['gldIndex']
        except KeyError:
            pass
        vis_data['nodes'].append(value)
        # make a new centroid line
        newCentroidLine = {
            'object': 'centroid_line',
            'from': value['parent'],
            'to': value['name']
        }
        vis_data['links'].append(newCentroidLine)

casename = "newyork"
networktype = "transmission"
transmissionName = "transmission"
fname = "./../data/cases/" + casename + "/jsondata/" + networktype + "/input/" + transmissionName + ".json"
with open(fname, 'w') as outfile:
    json.dump(vis_data, outfile, indent=4)