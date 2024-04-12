import numpy as np

data = np.genfromtxt(r"C:\Users\Gandhi Uday\OneDrive\Desktop\PPFD exam ore\PythonSet2\ReadCSV\CSVfile.csv", delimiter=',')

for i, row in enumerate(data):
    row_without_nan = row[~np.isnan(row)]  # Remove nan values from the row
    average = np.mean(row_without_nan)
    print("Average of row {}: {}".format(i + 1, average))
