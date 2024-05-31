import sys
import pandas as pd
import numpy as np
import find_modified_position

def main():

    if len(sys.argv) != 2:
        print("Usage: python count.py FILENAME")
    
    path = sys.argv[1]
    find_modified_position.find_most_modified_loci(path)

main()