from analyze_water import calculate_turbidity
from analyze_water import calculate_time
import json
import pytest

data = {}
data['info'] = []
data['info'].append( {'cali': 1, 'detector': 2} )
data['info'].append( {'cali': 2, 'detector': 3} )
data['info'].append( {'cali': 2, 'detector': '3'} )
a=0
b=1
c=2

def test_calculate_turbidity():
    assert calculate_turbidity(data['info'], 'cali', 'detector', a) == 2
    assert calculate_turbidity(data['info'], 'cali', 'detector', b) == 6
    assert isinstance(calculate_turbidity(data['info'], 'cali', 'detector', a), float) == True

def test_calculate_turbidity_exceptions():
    with pytest.raises(IndexError):
        calculate_turbidity( [ {'cali' : 2, 'detector' : 3} ], 'cali',' detect', b)
    with pytest.raises(NameError):
        calculate_turbidiy( [ {'cali' : 1, 'detector' : 2} ], 'cali', 'detector', a)

def test_calculate_time():
    assert calculate_time(3) == 54.37945872310939
    assert calculate_time(4) == 68.61923698304129
    assert isinstance(calculate_time(4), float) == True

def test_calculate_time_exceptions():
    with pytest.raises(TypeError):
        calculate_time([ { 'cali' : 1}, 1 ])
    with pytest.raises(NameError):
        calculate_tim([ {'cali' : 1, 'detector' : 2} ], 1)
