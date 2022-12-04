import pandas as pd

# list_df = pd.read_csv('data.tsv', sep='\t')
fs="/t"
table = str.maketrans('/t', fs)
fName = 'title_akas.tsv'
f = open(fName,'r', encoding="utf8")

try:
  line = f.readline()
  x = 0
  while x <= 10:
    print(line.translate(table), end = "")
    line = f.readline()
    x += 1

except IOError:
  print("Could not read file: " + fName)

finally:
  f.close()