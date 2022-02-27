# Data Analysis Docker Container
## Project 
We walk through the process of correctly structuring code output, creating unit tests, creating and uploading a container along with
its uses. This can provide an example as to how information can be shared and understood by people who will have no contact with the 
code author, it strucutres our code in a way were it is accessible to anyone.
## Scripts
The analysis script was improved in its output structure, were the information is described and explained. The unit test are simple 
sanity checks that make sure the code works correctly with different data samples. Lastly is the Docker file which contains the commands
normally inputted into the command line, but it executes them within this file as a shortcut.
## Instructions
1. 

2. In order to build an image we must first have a Dockerfile containing `FROM`, `RUN`,`COPY`, and `ENV PATH` commands appropriate to the
files you want to upload. In order to build the image we must do the following,
```BASH
$ docker build -t jbolivar101/ml_data_analysis:hw04 .
```

3. Running a container requires access to the profile so one must be logged in, then input the run command below, and finally call upon
the script and data file within the container. It should look like:
```BASH
$ docker login

$ docker run --rm -it -v $PWD:/data jbolivar101/ml_data_analysis:hw04 /bin/bash

$ ml_data_analysis.py /code/Meteorite_Landings.json
```

4. To use local data in this example we must first download it(it can be any link you want). This can also be run and use files locally,
while running scripts from the container. Similar to the last step we must be logged in, then execute the following command that is all in one:
```BASH
$ wget https://raw.githubusercontent.com/wjallen/coe332-sample-data/main/ML_Data_Sample.json

$ docker run --rm -v $PWD:/data jbolivar101/ml_data_analysis:hw04 ml_data_analysis.py /data/ML_Data_Sample.json
```
This example runs the container, then inputs the command and calls upon data that we just downloaded from the local folder.

5. To run the unit test from the container we must run and call it from within the container, which is then accessed within the `code` folder:
```BASH
$ docker run --rm -it -v $PWD:/data jbolivar101/ml_data_analysis:hw04 /bin/bash

$ cd code/

$ pytest 
```

## INPUTS
The scripts I have made work as long as the data provided fits within the structure of the following data set, this is because the names of the
key data points are specific to the analysis. 
```BASH
"meteorite_landings": [
    {
      "name": "Gerald",
      "id": "10001",
      "recclass": "H4",
      "mass (g)": "5754",
      "reclat": "-75.6691",
      "reclong": "60.6936",
      "GeoLocation": "(-75.6691, 60.6936)"
    }
]
```
As long as the data provided holds this information it will be capable of calculating the average mass, hemisphere, and class. In case you do not
have your own data to input, the container already has a sample and you can aquire one with ` wget https://raw.githubusercontent.com/wjallen/coe332-sample-data/main/ML_Data_Sample.json`
