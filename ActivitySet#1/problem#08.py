# Files

fname = "dataset/mbox-short.txt"
# Use the file name mbox-short.txt as the file name
#fname = input("Enter file name: ")
fh = open(fname)
count=0
total=0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    else:
        count=count+1
        a=line.find('0')
        num=float(line[a:])
        total+=num
average=total/count
print('Average spam confidence:',average)