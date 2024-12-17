#This step convert Labled file from TSV format to CSV format 


# Importing modules

import csv
from xlsxwriter.workbook import Workbook

# Input file path
labeled_file= r"C:\Users\UsEr\Desktop\Trying_Labeling_Operation\CTU-IoT-Malware-Capture-34-1\bro\conn.log_WH.labeled"
 
# Output file path
Xlsx_file= r"C:\Users\UsEr\Desktop\Trying_Labeling_Operation\CTU-IoT-Malware-Capture-34-1\bro\conn.log_WH.xlsx"
  
# Creating an XlsxWriter workbook object and adding 
# a worksheet.

workbook = Workbook(Xlsx_file)
worksheet = workbook.add_worksheet()

# Reading the tsv file.
read_tsv = csv.reader(open(labeled_file, 'r', encoding='utf-8'), delimiter='\t')
# We'll use a loop with enumerate to pass the data 
# together with its row position number, which we'll
# use as the cell number in the write_row() function.

for row, data in enumerate(read_tsv):
	worksheet.write_row(row, 0, data)

# Closing the xlsx file.
workbook.close()
