import csv
import numpy

def main():
  info = loadCsvData('learningOutcomes.csv')
  pval(info, 542, 510, 8.201367484, 50000)

def pval(array, samp1len, samp2len, val, x):
  size = len(array[0])
  diffbigger = 0
  for i in range(x):
    samptot = numpy.random.choice(array[0], size, replace=False)
    samp1 = samptot[0:samp1len]
    samp2 = samptot[samp1len:size]
    avg1 = sum(samp1)/samp1len
    avg2 = sum(samp2)/samp2len
    #counts how many times the average is more extreme
    if (abs(avg2-avg1)>=val):
      diffbigger += 1
  #computes p-value
  print diffbigger/(x*1.0)

#loads data from textfile into matrix
def loadCsvData(fileName):
  matrix = []
  doubleRow = []
  with open(fileName) as f:
    reader = csv.reader(f)
    for row in reader:
      for value in row:
        doubleRow.append(float(value))
    matrix.append(doubleRow)
  return matrix

def printData(matrix):
	for row in matrix:
		print row

# This if statement passes if this
# was the file that was executed
if __name__ == '__main__':
	main()
