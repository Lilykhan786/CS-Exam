# 15. Count the number of records and column names present in the CSV file.

import csv
def pro15():
  fields = []
  rows = []
  with open('students.csv', newline='') as f:
    data = csv.reader(f)
    # Following command skips the first row of CSV file
    fields = next(data)
    print('Field names are:')
    for field in fields:
      print(field, "\t")
    print()
    print("Data of CSV File:")
    for i in data:
      print('\t'.join(i))
  print("\nTotal no. of rows: %d"%(data.line_num))
pro15()