str1 = input("Enter the Sentence")
total = 1
for i in range(len(str1)):
    if(str1[i]==''):
        total=total+1
        
print("Total number of words in the sentence is = ", total)