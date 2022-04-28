# ISS FLOW
## Overview
Simplifying a coding project to a flowchart allows for the user to read and understand what the scripts are actually doing and what paths are taken. It is extremely helpful when sharing a project with others especially with users who are not sure how navigate through the file.
## Files
The only files included are the README and the image of the flowchart, I will also be including the link to the ISS_Positioning repository which this flowchart is based on. It goes more in depth and explains the code there. Choose either:
```BASH
git pull git@github.com:jbolivar101/ISS_Positioning.git

git pull https://github.com/jbolivar101/ISS_Positioning.git
```
## Image
![image](https://user-images.githubusercontent.com/77854904/165704983-a2794049-4a14-41f2-a8e3-76c764b9e1a7.png)
#### 1)
The flowchart follows the path of the flask as it tries to gather the information from the given data set.
#### 2)
First path is to simply `/read` which loads all the data into the system so it can be analyzed
#### 3)
Second it splits of into paths, with the option to as for `/help` which would output all the options for routes
#### 4)
Third is the option to call for a name of one of the locations/epochs which lead to each other and output a list
#### 5) 
Lastly is a specific input that can be chosen from one of the lists and it will output the information of that specific point

