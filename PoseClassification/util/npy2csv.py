import pandas as pd
import numpy as np

# Set the input and output directory paths
input_directory = "/VAME/hmm-22/22_km_label_"
output_directory = "./22km/"

# Open the text file containing the input file names
with open("id_analysis", "r") as file:
    # Loop over the file names in the text file
    for input_file_name in file:
        # Remove any trailing whitespace characters from the input file name
        input_file_name = input_file_name.strip()
        
        # Construct the input and output file paths
        input_file_path = input_file_name + input_directory + input_file_name + ".npy"
        output_file_path = output_directory + input_file_name.replace(".npy", ".csv")
        
        # Load the npy file
        arr = np.load(input_file_path, mmap_mode=None, allow_pickle=False, fix_imports=True)

        # convert array into dataframe
        DF = pd.DataFrame(arr)

        # Save the array as a CSV file
        # np.savetxt(output_file_path, arr, delimiter=',')

        # save the dataframe as a csv file
        DF.to_csv(output_file_path + ".csv")
