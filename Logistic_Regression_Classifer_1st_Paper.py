#Importing Python Libraries and Loading our Data Set into a Data Frame

import time
import os

import pandas as pd
import numpy as np

 
from sklearn.model_selection import train_test_split
 
from sklearn.linear_model import LogisticRegression
 
from sklearn.metrics import classification_report 


start = time.time()



######################################################### CICIDS2017 from kaggle -- - All files Available

Target_file_loc = r"E:\Datasets by kaggle 2\CICIDS2017\MachineLearningCSV\MachineLearningCVE\Friday-WorkingHours-Afternoon-DDos.pcap_ISCX_Pre.csv"


#Target_file_loc = r"E:\Datasets by kaggle 2\CICIDS2017\MachineLearningCSV\MachineLearningCVE\Friday-WorkingHours-Afternoon-PortScan.pcap_ISCX.csv"

#Target_file_loc = r"E:\Datasets by kaggle 2\CICIDS2017\MachineLearningCSV\MachineLearningCVE\Friday-WorkingHours-Morning.pcap_ISCX.csv"

#Target_file_loc = r"E:\Datasets by kaggle 2\CICIDS2017\MachineLearningCSV\MachineLearningCVE\Monday-WorkingHours.pcap_ISCX.csv" 


#Target_file_loc = r"E:\Datasets by kaggle 2\CICIDS2017\MachineLearningCSV\MachineLearningCVE\Thursday-WorkingHours-Afternoon-Infilteration.pcap_ISCX.csv"


#Target_file_loc = r"E:\Datasets by kaggle 2\CICIDS2017\MachineLearningCSV\MachineLearningCVE\Thursday-WorkingHours-Morning-WebAttacks.pcap_ISCX.csv"

#Target_file_loc = r"E:\Datasets by kaggle 2\CICIDS2017\MachineLearningCSV\MachineLearningCVE\Tuesday-WorkingHours.pcap_ISCX.csv"

#Target_file_loc = r"E:\Datasets by kaggle 2\CICIDS2017\MachineLearningCSV\MachineLearningCVE\Wednesday-workingHours.pcap_ISCX.csv"


#####################################################
 

Data_target_df = pd.read_csv(Target_file_loc)

Data_target_df.info()
print(" >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>. .. .. .. .")

#get file size  # Conversion to kilobytes, megabytes  .. .

file_size_bytes = os.path.getsize(Target_file_loc)
file_size_kb = file_size_bytes / 1024
file_size_mb = file_size_kb / 1024


print("File Size is :", file_size_mb, "MB")

 
Data_target_df.columns = Data_target_df.columns.str.strip()


print("analyze class distribution ", Data_target_df.groupby("Label").size())


print(" **************************************")


# X .. features , y .. target 


############ X,y ...   CICIDS2017 from kaggle

#X = Data_target_df[[ 'PacketLengthMean', 'AveragePacketSize', 'BwdPacketLengthMin', 'FwdPackets/s' , 'MinPacketLength', 'Down/UpRatio']]  


#X = Data_target_df[[ 'PacketLengthMean', 'AveragePacketSize', 'BwdPacketLengthMin', 'FwdPackets/s' ]]


X = Data_target_df[[ 'PacketLengthMean', 'AveragePacketSize']]  # 2 Features  from the First Approach


#X = Data_target_df[[ 'PacketLengthMean', 'BwdPacketLengthMin', 'FwdPackets/s' ]]  # # # 3 Features  from the Second Approach


#X = Data_target_df[[ 'MinPacketLength', 'Down/UpRatio']]


#X = Data_target_df[[ 'PacketLengthMean' , 'MinPacketLength', 'Down/UpRatio']]     


#X = Data_target_df[[ 'AveragePacketSize', 'BwdPacketLengthMin', 'FwdPackets/s' , 'MinPacketLength', 'Down/UpRatio']]  ##### 5 Features without PacketLengthMean


#X = Data_target_df[[ 'AveragePacketSize', 'BwdPacketLengthMin', 'FwdPackets/s' ]]  # # 3Features  which M important


y = Data_target_df['Label']    


###############################################################

print(" **************************************")


# Create training/ test data split

#Splitting our Data Set Into Training Set and Test Set .. .
#We will split the dataset into training and test sets.
#We will use 70% of the data for training and 30% for testing

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)



# Create an instance of  Logistic Regression .. . 
LRc = LogisticRegression()


# Fit the model
LRc.fit(X_train, y_train)


# making predictions on the testing set
y_pred = LRc.predict(X_test)

# Measure model performance
 
report = classification_report(y_test, y_pred)
print("\nClassification Report: \n")
print(report)

 

print(f'\n LR_time = {time.time() - start } \n')





