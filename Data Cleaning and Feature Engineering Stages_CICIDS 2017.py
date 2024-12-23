#This code excute Data Cleaning and Feature Engineering Stages 

# The libraries we need


import os
import pandas as pd
import numpy as np

 
Target_file_loc = r"E:\Datasets by kaggle 2\CICIDS2017\MachineLearningCSV\MachineLearningCVE\Friday-WorkingHours-Afternoon-DDos.pcap_ISCX.csv"
  

Data_target_df = pd.read_csv(Target_file_loc)

Data_target_df.info()

print(" >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>. .. .. .. .")

#get file size  # Conversion to kilobytes, megabytes  .. .

file_size_bytes = os.path.getsize(Target_file_loc)
file_size_kb = file_size_bytes / 1024
file_size_mb = file_size_kb / 1024


print("Sample Size is :", file_size_mb, "MB")

# remove special character  .. . to solve error in other data set ..
Data_target_df.columns = Data_target_df.columns.str.replace(' ', '')  


print("analyze class distribution ", Data_target_df.groupby("Label").size())


#Data Cleaning and Feature Engineering

#There are some columns that are not really useful and hence we will proceed to drop them.
#Also, there are some missing values so let’s drop all those rows with empty values:

print(Data_target_df.info())

# drop the column("Dst Port") and other metadata features  .. .

print("drop the column Dst Port and other metadata features  .. .")

Data_target_df.drop(labels=["DestinationPort"],axis=1,inplace=True)


print(" **************************************")


print("DataFrame  after modified  >>> ")

Data_target_df.head()

# The noisy data rectifying step:
#Removing duplicate records can help reduce noise and redundancy in our dataset.
# Remove duplicate rows:  
Data_target_df = Data_target_df.drop_duplicates()


# The null value data rectifying step:
#Removing rows or columns with a significant amount of missing data. 
#Remove rows with missing values:  
Data_target_df = Data_target_df.dropna()


# The infinity data values rectifying step:
Data_target_df.replace([np.inf, -np.inf], np.nan)
Data_target_df.dropna(inplace=True)


# label encoding
from sklearn.preprocessing import LabelEncoder
for col in Data_target_df.columns:
    le = LabelEncoder()
    Data_target_df[col] = le.fit_transform(Data_target_df[col])
Data_target_df.info()


# save target dataframe to new location
Data_target_df.to_csv(
         r"E:\Datasets by kaggle 2\CICIDS2017\MachineLearningCSV\MachineLearningCVE\Friday-WorkingHours-Afternoon-DDos.pcap_ISCX_Pre.csv",
        index=False)

 



