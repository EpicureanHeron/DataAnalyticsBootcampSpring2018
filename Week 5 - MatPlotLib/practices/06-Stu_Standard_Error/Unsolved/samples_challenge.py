# Dependencies
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd


# Read and shuffle data
housing_data = pd.read_csv("../Resources/housing_data.csv")
housing_data = housing_data.sample(frac=1).reset_index(drop=True)
