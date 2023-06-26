import re
s = "your str" #enter the sentence in the "your str" which you want to fix 
s = re.sub("\(.*?\)", "", s)
print(s)
