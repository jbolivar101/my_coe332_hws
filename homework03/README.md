# Turbidity Data Analyzer

## Description
This project allows the user to read and use the data from a given file. Through this we are able to 
calculate the turbidity of the water, its time to decay, and if its safe to drink. This can be used 
in real situations such as the water crisis Austin was in a week ago, this code can check for the
safety of the population. This can be applied to other forms of data, as long as the code is generalized
and broadened to fit specific approaches.

## Script
The actual script contains two functions that calculate the values and one main function that works
to put together the information and print it out. We also use unit tests to check that the code can
work with different situations and how it will act if it fails. We have 5 unit tests for each function.


## Instructions
You can download the list by opening the link `https://raw.githubusercontent.com/wjallen/turbidity/main/turbidity_data.json` then copying it and pasting it after the command wget inside the folder. After this you can execute the code using python3 and finding the most current 
turbidity data available, as the site updates. The output will provide the average turbidity of the
5 most recent samples, wheter the water is safe, and the time it takes to decay. The unit test can
be run with pytest and it will either pass or fail depending on the actual tests provided and if 
the data matches the functions.


