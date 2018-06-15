
import geojson 

from dataviz import parse, MY_FILE

def create_map(data_file):

    geo_map = {"type": "FeatureCollection"}     # Type of GeoJSON

    item_list = []      # List to collect each point to graph

    for index, line in enumerate(data_file):     # Iterate data using enumerate to get line and index
        if line['X'] == "0" or line['Y'] == "0":        # Skip 0,0 coordinate outliers that throw off map
            continue
        data = {}       # New dict for each iteration

#       # Assign line items to appropriate GeoJSON fields.
        data['type'] = 'Feature'
        data['id'] = index
        data['properties'] = {'title': line['Category'],
                              'description': line['Descript'],
                              'date': line['Date']}
        data['geometry'] = {'type': 'Point',
                            'coordinates': (line['X'], line['Y'])}

        item_list.append(data)      # Append to list

    for point in item_list:
        geo_map.setdefault('features', []).append(point)        # Add point to dict from item_list

    with open('file_sf.geojson', 'w') as f:
        f.write(geojson.dumps(geo_map))     # Write to file

def main():
    data = parse(MY_FILE, ",")

    return create_map(data)

if __name__ == "__main__":
    main()
