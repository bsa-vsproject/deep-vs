from keras.datasets import imdb
from keras import models
from keras.models import load_model
import csv
import pandas as pd
import numpy as np
import sys
import argparse

# construct the argument parser and parse the arguments

parser = argparse.ArgumentParser()
parser.add_argument("-i", "--input")
parser.add_argument("-m", "--model", required=True,
	help="path to pre-trained model")
parser.add_argument("-o", "--output")
args = parser.parse_args()

# read data

cavity_data = pd.read_csv(args.input)
cavity_data_arr = np.asarray(cavity_data)
cavity_data_arr = np.float32(cavity_data_arr)

col_names=['mol2vec' + str(x) for x in range(000,300)]

# load model and predict

loaded_model = load_model(args.model, compile=False)
predictions = loaded_model.predict(cavity_data_arr)
results_df = pd.DataFrame(columns=col_names)
for pred in predictions:
    results_df.loc[len(results_df)] = pred
results_df.to_csv(args.output, index = False, header=True)

