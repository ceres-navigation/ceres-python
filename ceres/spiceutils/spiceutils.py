import spiceypy as spice
import json
import base64
from typing import Optional, Union
from datetime import datetime
import urllib

import glob
import numpy as np
import pandas as pd
import os

def furnsh_directory(path_to_directory):
    if not path_to_directory.endswith('*'):
        path_to_directory = os.path.join(path_to_directory,'*')

    print(glob.glob(path_to_directory))
    for file in glob.glob(path_to_directory):
        spice.furnsh(file)

def time_to_et(input_time):
    """
    """
    if type(input_time) in [np.float64, float, int]:
        et = input_time
        
    elif type(input_time) is np.ndarray:
        if type(input_time[0]) == datetime:
            et = np.zeros(input_time.size)
            for idx,time in enumerate(input_time):
                et[idx] = spice.utc2et(time.strftime("%Y-%m-%d %X"))
        else:
            et = input_time

    elif type(input_time) is str:
        et = spice.utc2et(input_time)

    elif type(input_time) is pd.DatetimeIndex:
        et = np.zeros(len(input_time))
        for idx,time_stamp in enumerate(input_time):
            et[idx] = spice.utc2et(time_stamp.strftime("%Y-%m-%d %X"))

    elif type(input_time) in [pd.Timestamp, datetime]:
        et = spice.utc2et(input_time.strftime("%Y-%m-%d %X"))

    return et


def get_spks(obj: str, start_time: Union[str, datetime], stop_time: Union[str,datetime], 
             output_name: Optional[str] = None, output_dir: Optional[str] = 'kernels/'):
    if type(start_time) is datetime:
        start_time = start_time.strftime("%Y-%m-%d")

    if type(stop_time) is datetime:
        stop_time = stop_time.strftime("%Y-%m-%d")

    if output_name is None:
        output_name = '{}_{}_{}.bsp'.format(obj,start_time,stop_time)
    else:
        assert output_name.endswith('.bsp'), 'If an output_name is set, it must have a .bsp file extension'

    base_url = 'https://ssd.jpl.nasa.gov/api/horizons.api?'
    query='COMMAND={}&MAKE_EPHEM=YES&EPHEM_TYPE=SPK&START_TIME={}&STOP_TIME={}'.format(obj,start_time,stop_time)
    url = base_url + query

    f = urllib.urlopen(url)
    response = f.read()
    data = json.loads(response.text)
    
    with open(output_name,'wb') as f:
        f.write(base64.b64decode(data["spk"]))

    return None