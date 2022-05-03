# Meteorite landing generator and time calculator

## Project Description
The folder contains three files that work together in unison in order to first generate the landing sites, then the actual list,
and lastly calculate the time spent on each crater and traveling. This can be applied in the real world with non randomized values,
but instead real data from any planet as long as we have its radius.

## Scripts
The scripts use random number generation and json to organize the longitudes and latitudes into lists, which are then transferred into
the json file and retrived in the calculation script. Here I input my values into the function provided by the professor and check the
composition of the meteorite. This iterates and prints the information until it reaches the end of the list and provides a total.

## Instructions
To run this code first the generation script must be executed to create the json file, this then allows the calculation script to be executed and provide the results.
```BASH
python3 generate_sites.py

python3 calculate_trip.py
```
The output should create a json file and count the number of journeys, time spent traveling, and time spent sampling, lastly outputting the total amount of time the rover was working.
```BASH
vel =  11.054270617118885  hr, time to sample =  2  hr
leg =  2 , time to travel =  9.085207311819472  hr, time to sample =  2  hr
leg =  3 , time to travel =  5.121241970636911  hr, time to sample =  1  hr
leg =  4 , time to travel =  6.895951898758706  hr, time to sample =  2  hr
leg =  5 , time to travel =  9.90414941011794  hr, time to sample =  3  hr
number of legs = 5, total time elapsed =  52.06082120845191  hr
```
