#Step 1: skip the first Seven lines (header) from labeled file  befor Labeling

import itertools

labeled_file= r"C:\Users\UsEr\Desktop\Trying_Labeling_Operation\CTU-IoT-Malware-Capture-34-1\bro\conn.log.labeled"
 
file_without_header= r"C:\Users\UsEr\Desktop\Trying_Labeling_Operation\CTU-IoT-Malware-Capture-34-1\bro\conn.log_WH.labeled"

with open(labeled_file,'r') as f1, open(file_without_header, 'w') as f2:
	for line in itertools.islice(f1, 7, None):  # start=7, stop=None
		file_contents = f1.read() 
		f2.writelines(file_contents)
 
