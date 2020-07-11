import csv
import pandas as pd
import numpy as np
import sys
import argparse
from sklearn.metrics.pairwise import cosine_similarity

# construct the argument parser and parse the arguments

parser = argparse.ArgumentParser()
parser.add_argument('-i', '--input_file', type=argparse.FileType('r', encoding='UTF-8'))
parser.add_argument('-l', '--library_file', type=argparse.FileType('r'))
args = parser.parse_args()


def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

# read data

predicted_df = pd.read_csv(args.input_file)
library_df = pd.read_csv(args.library_file)

library_data = np.asarray(library_df)

pred_data_arr = predicted_df.iloc[:,0:].values
lb_data_arr = library_df.iloc[:,3:].values

vectorList_lib = lb_data_arr
vectorList_pred = pred_data_arr


# screen the library and find most similar ligand

print("number of ligand to be predicted:", len(vectorList_pred))
distanceList = []
for i in range(len(vectorList_pred)):
    reshaped_i = vectorList_pred[i].reshape(1,-1)
    for j in range(len(vectorList_lib)):
        cos_lib = cosine_similarity(reshaped_i, vectorList_lib[j].reshape(1,-1))
        distanceList.append( [cos_lib[0][0], (i,j)] )
idx_list = []
max_dist = 0

max_dist = -1
split_dist = list(chunks(distanceList, len(distanceList)//len(vectorList_pred)))

for chunk in split_dist:
    for idx, dist in enumerate(chunk):
        if dist[0] > max_dist:
            max_dist = dist[0]
            max_index = idx
    print(chunk[max_index])  
    x= (((chunk[max_index])[1])[1])          
    max_dist = -1
    max_index = -1
    print((library_data[x])[1])

