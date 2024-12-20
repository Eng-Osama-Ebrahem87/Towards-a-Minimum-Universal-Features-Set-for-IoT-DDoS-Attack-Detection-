
#This code excute the Second Scenario / the first sub-approach / Feature Selection Stage .. . 

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

# mutual information  Method then ANOVA then Variance Threshold Method
print(" mutual information  Method then ANOVA then Variance Threshold Method   **********************")

print(" from Filter Methods >>   Mutual_info_classif  Method  .. . ")
print(" ........................  .......................... ...................... .................... ...........")


from sklearn.feature_selection import mutual_info_classif
threshold_mic = 10  # the number of most relevant features

high_score_features = []

feature_scores = mutual_info_classif(X, y, random_state=0)
for score, f_name in sorted(zip(feature_scores, X.columns), reverse=True)[:threshold_mic]:
        print(f_name, score)
        high_score_features.append(f_name)
df_Result_mic = X[high_score_features]

print("the result of mutual information  Method when threshold = ", threshold_mic, "is .. .  ", df_Result_mic.columns)
#Bwd Seg Size Avg, Pkt Len Mean, SYN Flag Cnt, Bwd Header Len, Bwd Pkt Len Mean, Subflow Bwd Pkts, Tot Fwd Pkts, Subflow Fwd Pkts, Pkt Len Var, Tot Bwd Pkts

print(" ************************************** ")

print(" from Filter Methods >>   F_classif Method   OR   ANOVA f-test  .. . ")
print(" ........................  .......................... ...................... .................... ...........")

from sklearn.feature_selection import f_classif
threshold_fc = 8  # the number of most relevant features
#threshold_fc = 5  # the number of most relevant features

high_score_features = []
feature_scores = f_classif(df_Result_mic, y)[0]
for score, f_name in sorted(zip(feature_scores, df_Result_mic.columns), reverse=True)[:threshold_fc]:
      print(f_name, score)
      high_score_features.append(f_name)
df_Result_fc = X[high_score_features]
print("the result of ANOVA   Method when threshold = ", threshold_fc, "is .. .  ",df_Result_fc.columns)
#Tot Fwd Pkts, Subflow Fwd Pkts, Tot Bwd Pkts, Subflow Bwd Pkts, Bwd Seg Size Avg, Pkt Len Var, Bwd Pkt Len Mean, Pkt Len Mean
#Tot Fwd Pkts, Subflow Fwd Pkts, Tot Bwd Pkts, Subflow Bwd Pkts, Bwd Seg Size Avg


print(" **************************************")

print(" from Filter Methods >>   Variance Threshold Method  .. . ")
print(" ........................  .......................... ...................... .................... ...........")

from sklearn.feature_selection import VarianceThreshold
# Variance threshold  # 6 features .. . threshold=500000
# Variance threshold  # 16 features .. . threshold=100000
# Variance threshold  # 22 features .. . threshold=10000
# Variance threshold  #  25  features .. . threshold=1000
# Variance threshold  #   29  features .. . threshold=500


#threshold_VT=500
threshold_VT=50

selector = VarianceThreshold(threshold_VT)

sel = selector.fit(df_Result_fc)
sel_index = sel.get_support()
X_vt = df_Result_fc.iloc[:, sel_index]
print("the result of Variance Threshold Method when threshold = ",threshold_VT, "is .. .  ", X_vt.columns)

#the result of Variance Threshold Method when threshold =  500 is .. .   Index(['Pkt Len Var', 'Pkt Len Mean'], dtype='object')
#the result of Variance Threshold Method when threshold =  500 is .. .   Index(['Pkt Size Avg', 'Pkt Len Mean', 'Bwd Seg Size Avg'], dtype='object') .. IoT_23_Split_Malware_Cap1_1_00000_20180509183031.pcap_Flow.csv
# Bwd Seg Size Avg', 'Bwd Pkt Len Mean', 'Pkt Size Avg', 'Pkt Len Mean ... . IoT_23_Split_Malware_Cap1_1_00001_20180510230633.pcap_Flow.csv

#ValueError: No feature in X meets the variance threshold 500000.00000
#ValueError: No feature in X meets the variance threshold 100000.00000
#ValueError: No feature in X meets the variance threshold 10000.00000
#ValueError: No feature in X meets the variance threshold 1000.00000













