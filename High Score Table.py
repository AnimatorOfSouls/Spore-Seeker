def insert_sort(table):
    tempstore = 0
    listpoint = 0

    #Looping through the scores
    for i in range (len(table)):
        #Initiating temporary variables
        listpoint = i
        tempstore = table[listpoint]


        #Sorting the list
        while listpoint > 0 and table[listpoint] < table[listpoint-1]:
            print("i =",i)
            print(tempstore)
            table[listpoint] = table[listpoint-1]
            listpoint = listpoint-1
            table[listpoint] = tempstore

    return table



#Calling Functions
score_table = [1,9,2,4,3]
sorted_table = insert_sort(score_table)



#Printing the sorted table
print("Name:\t\tScore:")
for i in range(len(sorted_table)):
    print(sorted_table[i])
