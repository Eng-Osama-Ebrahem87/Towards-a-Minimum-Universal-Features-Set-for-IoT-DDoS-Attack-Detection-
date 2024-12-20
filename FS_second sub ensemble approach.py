
#This code excute the Second sub-approach / Feature Selection Stage .. . 

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


# mutual information  Method

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

print(" ........................  .......................... ...................... .................... ...........")


print(" from Filter Methods >>   Variance Threshold Method  .. . ")
print(" ........................  .......................... ...................... .................... ...........")

from sklearn.feature_selection import VarianceThreshold
# Variance threshold  # 6 features .. . threshold=500000
# Variance threshold  # 16 features .. . threshold=100000
# Variance threshold  # 22 features .. . threshold=10000
# Variance threshold  #  25  features .. . threshold=1000
# Variance threshold  #   29  features .. . threshold=500


threshold_VT=100000 # 16 features 
#threshold_VT=83000
selector = VarianceThreshold(threshold_VT)

sel = selector.fit(X)
sel_index = sel.get_support()
X_vt = X.iloc[:, sel_index]
print("the result of Variance Threshold Method when threshold = ",threshold_VT, "is .. .  ", X_vt.columns)


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

print(" from Warpper Methods .. . SelectKBest with chi2 then Mutual_info_classif  Method  .. . ")

from sklearn.feature_selection import SelectKBest
#Compute the Chi-square statistic
from sklearn.feature_selection import chi2

threshold = 10  # the number of most relevant features
skb = SelectKBest(score_func=chi2, k=threshold)
sel_skb = skb.fit(X, y)
sel_skb_index = sel_skb.get_support()

df_skb = X.iloc[:, sel_skb_index]
print('p_values', sel_skb.pvalues_)

print("the result of  SelectKBest with chi2  = ", df_skb.columns)



























