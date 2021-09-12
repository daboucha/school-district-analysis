# Add dependencies
import pandas as pd
import os

# Files to load
# Store the base directory of this file
base_dir = os.path.abspath('')
# Indirect path to resource files
schools_file = os.path.join(base_dir, "resources", "schools_complete.csv")
students_file = os.path.join(base_dir, "resources", "students_complete.csv")

# Read the csv files
schools_data_df = pd.read_csv(schools_file)
schools_data_df

