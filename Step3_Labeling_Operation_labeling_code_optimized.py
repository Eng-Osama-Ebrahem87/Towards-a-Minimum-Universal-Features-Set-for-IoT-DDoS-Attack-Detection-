'''This code compares the four tuples, i.e, source IP, source port, destination IP and destination port to identify the normal and malicious flow as defined by dataset providers.
Based upon the matching of four-tuple for each flow, the .csv files were labelled with the label that exists across the similar tuple in the label file. In this way, all the datasets were labelled.'''

import pandas as pd
import numpy as np


def add_label_to_target(
        target_file_location,
        label_file_location):
    labels = pd.read_excel(label_file_location, header=None, sheet_name=0)
    targets = pd.read_csv(target_file_location)

    print("Number of lines in the labels file: ", labels.shape[0])

    print("Number of lines in the target file: ", targets.shape[0])

    hashed_labels = {}

    # only ONE pass through label file
    for row in labels.itertuples():
        index = hash((
            row[3], row[4], row[5], row[6]
        ))  # src_ip, port, dist_ip, port ??
        hashed_labels[index] = row[21]  # label

    target_labels = []

    # only ONE pass through target file
    for row in targets.itertuples():
        index = hash((
            row[2], row[3], row[4], row[5]
        ))

        label = hashed_labels[index] if index in hashed_labels else np.nan
        target_labels.append(label)

    # new column to the target dataframe
    targets['Label_Cat_Sub-Cat'] = target_labels

    return targets


if __name__ == '__main__':
    import time

    start = time.time()

    targets_with_labels = add_label_to_target(
        target_file_location=r"C:\Users\UsEr\Desktop\Trying_Labeling_Operation\CTU-IoT-Malware-Capture-42-1\2019-01-10-14-34-38-192.168.1.197.pcap_Flow.csv",
        label_file_location=r"C:\Users\UsEr\Desktop\Trying_Labeling_Operation\CTU-IoT-Malware-Capture-42-1\bro\conn.log_WH.xlsx"
    )

    # save target dataframe to new location
    targets_with_labels.to_csv(
        r"C:\Users\UsEr\Desktop\Trying_Labeling_Operation\CTU-IoT-Malware-Capture-42-1\CTU-IoT-Malware-Capture-42-1_Labeled.csv",
        index=False)


    print(f'time = {time.time() - start}')
