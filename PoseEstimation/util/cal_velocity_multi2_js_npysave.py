import pandas as pd
import numpy as np
from scipy.signal import savgol_filter

# Set the input and output directory paths
input_directory = "./"
output_directory = "./npy/"

# Open the text file containing the input file names
with open("id", "r") as file:
    # Loop over the file names in the text file
    for input_file_name in file:
        # Remove any trailing whitespace characters from the input file name
        input_file_name = input_file_name.strip()
        
        # Construct the input and output file paths
        input_file_path = input_file_name + "_t.csv"
        
        # Load CSV file into data frame
        df = pd.read_csv(input_file_path)
        df.fillna(method='ffill', inplace=True)
        df = df.astype(float)

        # Function to calculate the distance for given columns
        def calculate_distance(df, col1, col2, col3, col4):
            point1 = np.array([df.iloc[:, col1],df.iloc[:, col2]])
            point2 = np.array([df.iloc[:, col3].shift(),df.iloc[:, col4].shift()])
            return np.linalg.norm(point2-point1, axis=0)

        df['v'] = calculate_distance(df, 8, 9, 8, 9) / 0.01666667
        df['vh'] = calculate_distance(df, 2, 3, 2, 3) / 0.01666667
        df['vl'] = calculate_distance(df, 11, 12, 11, 12) / 0.01666667
        df['vr'] = calculate_distance(df, 17, 18, 17, 18) / 0.01666667
        df['vhl'] = calculate_distance(df, 35, 36, 35, 36) / 0.01666667
        df['vhr'] = calculate_distance(df, 42, 43, 42, 43) / 0.01666667

        # Apply Savitzky-Golay filter to the velocity columns
        window_size = 60  
        polynomial_order = 2  
        for col in ['v', 'vh', 'vl', 'vr','vhl','vhr']:
            df[col] = df[col].fillna(method='ffill').fillna(method='bfill')
            df[col+'_filtered'] = savgol_filter(df[col], window_size, polynomial_order)

        # Save data frame to CSV file
        df.to_csv(input_file_name + '_vel.csv', index=False)

        # Save 'v_filtered' columns as a .npy file
        filtered_data = np.array([df['v_filtered'], df['vh_filtered'], df['vl_filtered'], df['vr_filtered'], df['vhl_filtered'], df['vhr_filtered']])
        np.save('npy/' + input_file_name + '_vame_vel.npy', filtered_data)
