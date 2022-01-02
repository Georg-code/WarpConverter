import json

f = open('data.json')
sql = open('homes.sql', 'a')
data = json.load(f)
 
# Iterating through the json
# list
for i in data['homes']:
    uuid : str = i
    for j in data['homes'][i]:
        try:
            sql.write(f"INSERT INTO homes (uuid, name, x, y, z, yaw, pitch, world) VALUES ('{uuid}', '{j}', {round(data['homes'][i][j]['x'])}, {round(data['homes'][i][j]['y'])}, {round(data['homes'][i][j]['z'])}, {data['homes'][i][j]['yaw']}, {data['homes'][i][j]['pitch']}, '{data['homes'][i][j]['world']}'); \n")
            print(data['homes'][i][j]['x'])
        except:
            print(data['homes'][i][j])
        
 
# Closing file
f.close()
sql.close()

