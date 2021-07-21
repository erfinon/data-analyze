import json
from numpy import true_divide
import pandas as pd
from pandas.core.frame import DataFrame
import os


data = pd.DataFrame([],columns=["time_ms","time","message"])

print("Logger")
def lformat(i):
        r = ""
        r += str(i//100)
        r += str(int((i -(i%10))/10))
        r += str(i%10)
        return r




