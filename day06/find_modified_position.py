import sys
import pandas as pd
import numpy as np

def find_most_modified_loci(my_path):
    
    df = pd.read_csv(my_path, index_col=0)

    df["sum_modifications"] = df.sum(axis=1)
    index_of_max_modifications = df["sum_modifications"].idxmax()
    print(
        "The loci that found to be modified in most of the conditions is: ",
        index_of_max_modifications,
    )
    return index_of_max_modifications




    







# num_modifications = df.loc[index_of_max_modifications, "sum_modifications"]
# print(num_modifications)
