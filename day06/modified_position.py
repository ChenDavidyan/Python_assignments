import sys
import pandas as pd
import numpy as np
import find_modified_position

# def find_most_modified_loci(my_path):
    
#     df = pd.read_csv(my_path, index_col=0)

#     df["sum_modifications"] = df.sum(axis=1)
#     index_of_max_modifications = df["sum_modifications"].idxmax()
#     print(
#         "The loci that found to be modified in most of the conditions is: ",
#         index_of_max_modifications,
#     )

def main():

    try:
        path = sys.argv[1]
    except IndexError:
        print("Please add the path to your csv next time you run the code")
        sys.exit(1)

    find_modified_position.find_most_modified_loci(path)

main()