# REDIS, FLASKS, and PEOPLE
## Overview
Connecting to a personal Redis port and making sure it keeps backing itself is part of this flask container and it allows us to extract specific information. It can be used to analyze different databases in real time and take it as far as to automate it as it updates to the website. This is the purpose of putting all of this into a network that connects the three services.
## Scripts
The two scripts used within this app program will either POST or GET the information from the database which will load the data into the Redis container or read the data respectively. Besides that the dockerfile sets it all up, and we must intitate the Redis container in the command line.
## Instructions
### Launch Redis
In order to run a Redis containter we must input the following command into the command line, `docker run -d -p <your-redis-port>:6379 -v </path/on/host>:/data --name=<your_name>-redis redis:6 --save 1 1`
and in our case the command should be as follows,
`docker run -d -p 6404:6379 -v $(pwd)/data:/data --name=jorgeb-redis redis:6 --save 1 1`
### Flask
We must first run the dockerfile in order to provide the set up. Starting up the flask is the same as always where we must start it in a background shell and run the following commands,
```BASH
export FLASK_APP=app.py
export FLASK_ENV=development
flask run -p 5004
```
### POST and GET
In order to finish gathering the data we must curl from the flask with the following two commands which will first load the data and then do the POST and GET commands.
```BASH
curl localhost:5004/data -X POST
curl localhost:5004/data
```
### Data
Lastly we is deciphering the data which is showing the location of the meteorite landings classified by name, id, etc.
```BASH
  {
    "name": "Jennifer",
    "id": "10299",
    "recclass": "L5",
    "mass (g)": "539",
    "reclat": "-84.0579",
    "reclong": "69.9994",
    "GeoLocation": "(-84.0579, 69.9994)"
  },
  {
    "name": "Christina",
    "id": "10300",
    "recclass": "H5",
    "mass (g)": "4291",
    "reclat": "-38.1533",
    "reclong": "-46.7127",
    "GeoLocation": "(-38.1533, -46.7127)"
  }
```
