from flask import Flask, request
import json
import logging
import redis

app = Flask(__name__)
meteorites = {}
data_list = []

@app.route('/data',methods=['POST'])
def transfer_data():
    """
    This route reads meteorite landings file and sets it into the Redis container

    Args: None, it is called with /data

    Returns: None, it transfers the data 
    """

    rd = redis.Redis(host='10.97.26.170', port=6379)
    logging.info("Transferring data")
    global meteorites

    with open('ML_Data_Sample.json' , 'r') as f:
        meteorites =  json.load(f)
    for d in meteorites['meteorite_landings']:
        rd.set(d['id'],json.dumps(d))
    return f'Data transferred\n'

@app.route('/data', methods=['GET'])
def get_names():
    """
    Iterates through the list that was turned into a json dump

    Args: None, it is called with /data

    Returns: None, it returns the list of names
    """

    rd = redis.Redis(host='10.97.26.170', port=6379)
    logging.info("Gathering names")
    global data_list

    for i in range(10001, 10301, 1):
        data_list.append(json.loads(rd.get(i)))
    return json.dumps(data_list, indent=2)+'\n'

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
