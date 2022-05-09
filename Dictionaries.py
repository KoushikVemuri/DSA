'''nyc_weather.csv contains new york city weather for first few days in the month of January. Write a program that can answer following,
What was the average temperature in first week of Jan
What was the maximum temperature in first 10 days of Jan
What was the temperature on Jan 9?
What was the temperature on Jan 4?'''

count = 0
arr = {}
with open('ny_temp.csv', 'r') as data:
    for row in data:
        if count != 0:
            List = row.split(',')
            arr[List[0]] = int(List[1])
        count+=1
avg = 0
for data in arr.keys():
    if data == '8-Jan':
        break
    avg+=arr[data]
print(avg/7)

max_val = 0
for data in arr.values():
    if max_val < data:
        max_val = data
print(max_val)
    
print(arr['9-Jan'])
print(arr['4-Jan'])


#read this file in python and print every word and its count

words = {}
with open('poem.txt', 'r') as poem:
    for line in poem:
        L = line.split(' ')
        for word in L:
            word = word.replace('\n','') 
            word = word.replace(',','') 
            word = word.replace('!','')
            if word in words.keys():
                words[str(word)]+=1
            else:
                words[str(word)]=1
    print(words['diverged'])
    print(words['in'])
