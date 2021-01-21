import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', '..')))

from p0 import linearSearch

filename = "Input1.txt"
with open(filename) as f:
    data1 = f.read()
    data1 = data1.strip().split()
    array1 = [int(x) for x in data1]
    array1 = list(dict.fromkeys(array1))

filename = "Input2.txt"
with open(filename) as f:
    data2 = f.read()
    data2 = data2.strip().split()
    array2 = [int(x) for x in data2]
    array2 = list(dict.fromkeys(array2))

addresult = str(linearSearch(array1, 1)) + str(linearSearch(array2, 1))

# Print without newline/carriage return
ofile = open('output', 'w')
ofile.write(addresult)
ofile.close()

# Create the answer file ahead of time, and do not preparefile('') it in the driver.py.
# This guarantees that users cannot modify the file when the submission is being tested.
# Users also cannot modify you driver.py, so if you need a less precise comparison, it
# can be done in the driver.py as well (ex: answer is some approximate value).
# afile = open('answer', 'w')
# afile.write('2')
# afile.close()
