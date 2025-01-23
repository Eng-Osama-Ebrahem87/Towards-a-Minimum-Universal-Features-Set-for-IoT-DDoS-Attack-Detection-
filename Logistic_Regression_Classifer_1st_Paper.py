#Importing Python Libraries and Loading our Data Set into a Data Frame

import time
import os

import types

import pandas as pd
import numpy as np

 
from sklearn.model_selection import train_test_split
 
from sklearn.linear_model import LogisticRegression
 
from sklearn.metrics import classification_report 


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

X = Data_target_df[[ 'PacketLengthMean', 'AveragePacketSize', 'BwdPacketLengthMin', 'FwdPackets/s' , 'MinPacketLength', 'Down/UpRatio']]  


#X = Data_target_df[[ 'PacketLengthMean', 'AveragePacketSize', 'BwdPacketLengthMin', 'FwdPackets/s' ]]


#X = Data_target_df[[ 'PacketLengthMean', 'AveragePacketSize']]  # 2 Features  from the First Approach


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

start_train = time.time()

# Fit the model
LRc.fit(X_train, y_train)
print(f'training_time = {time.time() - start_train}')


start_pred = time.time()

# making predictions on the testing set
y_pred = LRc.predict(X_test)
print(f'predict_time = {time.time() - start_pred}')

# Measure model performance
 
report = classification_report(y_test, y_pred)
print("\nClassification Report: \n")
print(report)


#calculate the memory usage according to each feature subset: 

def is_instance_attr(obj, name):
  if not hasattr(obj, name):
    return False
  if name.startswith("__") and name.endswith("__"):
    return False
  v = getattr(obj, name)
  if isinstance(v, (types.BuiltinFunctionType, types.BuiltinMethodType, types.FunctionType, types.MethodType)):
    return False
  # See https://stackoverflow.com/a/17735709/
  attr_type = getattr(type(obj), name, None)
  if isinstance(attr_type, property):
    return False
  return True

def get_instance_attrs(obj):
  names = dir(obj)
  names = [name for name in names if is_instance_attr(obj, name)]
  return names


def sklearn_sizeof(obj):
  sum = 0
  names = get_instance_attrs(obj)
  for name in names:
    v = getattr(obj, name)
    v_type = type(v)
    v_sizeof = v.__sizeof__()
    sum += v_sizeof
  return sum

print("Instance state: {} B".format(sklearn_sizeof(LRc)))
 
 



























 







