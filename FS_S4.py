
#This code excute the Fourth Scenario / the first sub-approach / Feature Selection Stage .. . 

# The libraries we need
import os

import pandas as pd
import numpy as np

 
Target_file_loc = r"C:\Users\UsEr\Desktop\Trying_Labeling_Operation\CTU-IoT-Malware-Capture-42-1\CTU-IoT-Malware-Capture-42-1_Labeled_Pre.csv"



Data_target_df = pd.read_csv(Target_file_loc)

Data_target_df.info()
print(" >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>. .. .. .. .")

print("analyze class distribution ", Data_target_df.groupby( "Label_Cat_Sub-Cat").size())



# X .. features , y .. target 
X = Data_target_df.drop(columns=['Label_Cat_Sub-Cat'], axis=1)
y = Data_target_df['Label_Cat_Sub-Cat']

print(" **************************************")

# ANOVA Method then mutual information  then Variance Threshold Method 

print(" ANOVA Method then  mutual information  Method  then Variance Threshold Method   **********************")

print(" ************************************** ")

print(" from Filter Methods >>   F_classif Method   OR   ANOVA f-test  .. . ")
print(" ........................  .......................... ...................... .................... ...........")

from sklearn.feature_selection import f_classif
threshold_fc = 10  # the number of most relevant features

high_score_features = []
feature_scores = f_classif(X, y)[0]
for score, f_name in sorted(zip(feature_scores, X.columns), reverse=True)[:threshold_fc]:
      print(f_name, score)
      high_score_features.append(f_name)
df_Result_fc = X[high_score_features]
print("the result of ANOVA   Method when threshold = ", threshold_fc, "is .. .  ",df_Result_fc.columns)

print(" **************************************")

print(" from Filter Methods >>   Mutual_info_classif  Method  .. . ")
print(" ........................  .......................... ...................... .................... ...........")


from sklearn.feature_selection import mutual_info_classif

threshold_mic = 5  # the number of most relevant features
#threshold_mic = 8  # the number of most relevant features

high_score_features = []

feature_scores = mutual_info_classif(df_Result_fc, y, random_state=0)
for score, f_name in sorted(zip(feature_scores, df_Result_fc.columns), reverse=True)[:threshold_mic]:
        print(f_name, score)
        high_score_features.append(f_name)
df_Result_mic = df_Result_fc[high_score_features]

print("the result of mutual information  Method when threshold = ", threshold_mic, "is .. .  ", df_Result_mic.columns)
#the result of mutual information  Method when threshold =  5 is .. .   Index(['Tot Bwd Pkts', 'Bwd Pkt Len Mean', 'Fwd Pkt Len Max', 'Tot Fwd Pkts','Pkt Len Var'],  dtype='object')

print(" **************************************")

print(" from Filter Methods >>   Variance Threshold Method  .. . ")
print(" ........................  .......................... ...................... .................... ...........")

from sklearn.feature_selection import VarianceThreshold

threshold_VT=50
#threshold_VT=500

selector = VarianceThreshold(threshold_VT)

sel = selector.fit(df_Result_mic)
sel_index = sel.get_support()
X_vt = df_Result_mic.iloc[:, sel_index]
print("the result of Variance Threshold Method when threshold = ",threshold_VT, "is .. .  ", X_vt.columns)
#the result of Variance Threshold Method when threshold =  500 is .. .   Index(['Pkt Len Var'], dtype='object')  .............. threshold_mic = 5
#the result of Variance Threshold Method when threshold =  500 is .. .   Index(['Pkt Len Var', 'Pkt Len Std'], dtype='object') ........ threshold_mic = 8








