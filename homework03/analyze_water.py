import json
import math
from typing import List
import logging
import socket
format_str=f'%(levelname)s: %(message)s'
logging.basicConfig(level=logging.DEBUG, format=format_str)


def calculate_turbidity(a_list_of_dicts: List[dict], cali: str, detector: str, i: int) -> float:
    """
    Given a dictionary and its two strings along with the iteration value, I call two values from
    the dictionary and then compute the turbidity in the equation below.

    Args:
        a_list_of_dicts(List[dict]): List of turbidity data
        cali(string): Calls calibration value
        detector(string): Calls detector value
        i(int): Value of iteration

    Returns:
        result(float): The current turbidity value calculated by multiplying the two args.
    """
    a0 = float(a_list_of_dicts[i][cali])
    I90 = float(a_list_of_dicts[i][detector])
    T = a0 * I90
    return(T)


def calculate_time(T: float) -> float::
    """
    Given the value of current turbidity I compute the value of time and checks the turbidity against
    the threshold, then prints out the information found.

    Args:
        T(float): Value of current turbidity

    Returns:
        result(string): The function doesn't actually return anyhting, instead it outputs a log on the
        turbidity level and prints the time calculated based on the threshold.
    """
    b = 0
    Ts = 1.0
    d = 0.02
    T0 = T
    b = math.log((1/T0),0.98)
    if (Ts > T0*((1-d)**b)):
        logging.info('Turbidity is below threshold for safe use')
        print(f'Minimum time required to return below a safe threshold = {b} hours')
    else:
        logging.warning('Turbidity is above threshold for safe use')
        print(f'Minimum time required to return below a safe threshold = 0 hours') 
    return(b)

def main():
    with open('turbidity_data.json', 'r') as f:
        ty_data = json.load(f)


    T_list = 0 
    x = 0
    for i in range(1,6):
        x = len(ty_data['turbidity_data'])- i
        T = calculate_turbidity(ty_data['turbidity_data'], 'calibration_constant', 'detector_current', x)
        T_list += T
    print(f'Average turbidity based on most recent five measurements = {T_list/5} NTU')
    Time = calculate_time(T)

        
if __name__ == '__main__':
    main()
