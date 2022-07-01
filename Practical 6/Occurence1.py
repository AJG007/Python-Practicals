#Count occurrence of each word in the given list
sentence = input("Enter the sentence: ")
list = sentence.split()
ans = {}
for i in list:
    if i in ans:
        ans[i] += 1
    else:
        ans[i] = 1
for k,v in ans.items():
    print(k,"-",v)