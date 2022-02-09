import json
import math

with open('meteorites.json', 'r') as f:
    data = json.load(f)

mars_radius = 3389.5    # km

def calc_gcd(latitude_1: float, longitude_1: float, latitude_2: float, longitude_2: float) -> float:
    lat1, lon1, lat2, lon2 = map( math.radians, [latitude_1, longitude_1, latitude_2, longitude_2] )
    d_sigma = math.acos( math.sin(lat1) * math.sin(lat2) + math.cos(lat1) * math.cos(lat2) * math.cos(abs(lon1-lon2)))
    return ( mars_radius * d_sigma )

def compute_lat_lon(list_of_dicts, lat, lon, composition):
    robot_lat = 16.0 #Robots location
    robot_lon = 82.0
    totime=0
    time_list = [] #Empty lists

    for i in range(len(list_of_dicts)): #Iterates over list of sites
        trdist= calc_gcd(robot_lat, robot_lon, float(list_of_dicts[i][lat]), float(list_of_dicts[i][lon]))
        robot_lat= float(list_of_dicts[i][lat])
        robot_lon= float(list_of_dicts[i][lon])
        trtime= trdist/10        

        if(str(list_of_dicts[i][composition]) == "stony"): #Checks for compostion
            stime = 1
        elif(str(list_of_dicts[i][composition]) == "iron"):
            stime = 2
        else:
            stime = 3

        totime=stime+trtime+totime
        print("leg = ", i+1, ", time to travel = ", trtime, " hr, time to sample = ", stime, " hr")
    print("number of legs = 5, total time elapsed = ", totime, " hr")
    return(0)

 
print(compute_lat_lon(data['sites'], 'latitude', 'longitude', 'composition'))            
