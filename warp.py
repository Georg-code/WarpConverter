import json

f = open('data.json')
sql = open('warps.sql', 'a')
data = json.load(f)
 
# Iterating through the json
# list
for i in data['warps']:
    sql.write(f"INSERT INTO warps (name, x, y, z, yaw, pitch, world) VALUES ('{i}', '{data['warps'][i]['x']}', '{data['warps'][i]['y']}', '{data['warps'][i]['z']}', '{data['warps'][i]['yaw']}', '{data['warps'][i]['pitch']}', '{data['warps'][i]['world']}'); \n")

 
# Closing file
f.close()
sql.close()