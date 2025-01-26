
# The libraries we need


import os
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

 
Target_file_loc = r"E:\Datasets by kaggle 2\CICIDS2017\MachineLearningCSV\MachineLearningCVE\Friday-WorkingHours-Afternoon-DDos.pcap_ISCX.csv"
  

df = pd.read_csv(Target_file_loc)

df.info()

print(" >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>. .. .. .. .")


df.columns = df.columns.str.replace(' ', '')  

#Data_target_df = df[[ 'PacketLengthMean', 'AveragePacketSize', 'BwdPacketLengthMin', 'FwdPackets/s' , 'MinPacketLength', 'Down/UpRatio', 'Label']]

Data_target_df = df[[ 'PacketLengthMean', 'AveragePacketSize', 'BwdPacketLengthMin', 'FwdPackets/s' , 'MinPacketLength', 'Down/UpRatio']]  



#Data Cleaning and Feature Engineering

#There are some columns that are not really useful and hence we will proceed to drop them.
#Also, there are some missing values so let’s drop all those rows with empty values:

print(Data_target_df.info())


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




# Find the pearson correlations matrix

print("\n Pearson correlations matrix: \n ")
corr = Data_target_df.corr(method = 'pearson')
#method : In method we can choose any one from {'pearson', 'kendall', 'spearman'}
#pearson is the standard correlation coefficient matrix i.e default

# Set display option to show all columns
pd.set_option('display.max_columns', None)

# Show the columns
print(corr ) 

#Plot the correlation matrix with the seaborn heatmap:

plt.figure(figsize=(8,10), dpi =100)
sns.heatmap(corr,annot=True,fmt=".2f", linewidth=.7)

plt.title("Pearson correlations matrix ")
  
# displaying the plotted heatmap 
plt.show()





















  


