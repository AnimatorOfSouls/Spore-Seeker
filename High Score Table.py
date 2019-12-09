import csv

#Importing score from file
def import_score():
    score = []
    score_table = score*9
    #Defining the 2D array
    
    #Importing the score into the 2D array
    with open("highscores.csv") as score_file:
        reader = csv.reader(score_file)
        
        for row in reader:
            score_table.append(row)
            
        return score_table



#Sorting the scores
def insert_sort(table):
    tempstore = 0
    listpoint = 0
    
    #Looping through the scores
    for i in range (len(table)):
        #Initiating temporary variables
        listpoint = i
        tempstore = table[listpoint]
        
        
        #Sorting the list
        while listpoint > 0 and table[listpoint][1] < table[listpoint-1][1]:
            table[listpoint] = table[listpoint-1]
            listpoint = listpoint-1
            table[listpoint] = tempstore
        
    return table



#Calling Functions
score_table = import_score()
sorted_table = insert_sort(score_table)



#Printing the sorted table
print("Name:\t\tScore:")
for i in range(len(sorted_table)):
    print(sorted_table[i][0] + "\t\t" + sorted_table[i][1])