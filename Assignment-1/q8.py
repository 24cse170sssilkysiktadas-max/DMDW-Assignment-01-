# q8) WAP to copy the content from file.txt to file3.txt

f1 = open("file1.txt","w")
f1.write("hello World!!!!")
f1.close()
f1 = open("file1.txt","r")
data = f1.read()
f2 = open("file3.txt","w")
f2.write(data)
f1.close()
f2.close()
print("Content Copied Successfully")
