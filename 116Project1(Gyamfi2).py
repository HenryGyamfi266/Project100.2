"""Author: Henry Gyamfi

  Date-Written: 2/3/2021

  Date-Modified: 2/9/2021

  Description: In this project, I created a program that sorts a random of integers using Bubble Sort, Python Sort and Selection Sort.
  It would arrange the numbers in order and give an account of the time taken to arrange the data list in order.
  

  Variables Used:

     selfButton1 - Tells the first button which was created in the GUI
     
     selfButton2 - Shows the second button in the GUI 

     SelfButton3 - Shows the third button in a GUI
     
     self.addLabel- Provides a label with text or integers on the GUI

     self.addButton - Provides button to be pressed on in the GUI

     self.myListA - Randomizes the data in A

     self.myListB - Randomizes the data in B

     self.myListC - Randomizes the data in C

     start - Starts recording the time as soon as the button is clicked

     elapsedTime = time for the data to be arranged in order

     maxInList - Refers to all data in the list"""







import random

import time

import sys

from breezypythongui import EasyFrame

class Sorts(EasyFrame):

    def __init__(self):

        EasyFrame.__init__(self, title = "Comparison of Common Sorts")

        self.addLabel(text = "Bubble Sort", row = 0, column = 0)
        self.addLabel(text = "Selection Sort", row = 0, column = 3)
        self.addLabel(text = "Python's Sort", row = 0, column = 8)

        self.addLabel(text = "100", row = 1, column= 0)        ###Creates the label
        self.outputFieldC1 = self.addFloatField( value= "0", row = 1, column = 1, width = 5, precision= 4 )   ### Display time in seconds 
        self.addLabel(text = "1000", row = 2, column = 0)
        self.outputFieldC2 = self.addFloatField (value = "0", row = 2, column = 1, width = 5, precision = 4)
        self.addLabel(text = "2000", row = 3, column = 0)
        self.outputFieldC3 = self.addFloatField (value = "0", row = 3, column = 1, width = 5, precision = 4)

        self.addLabel(text = "100", row = 1, column = 3)
        self.outputFieldB1 = self.addFloatField (value = "0", row = 1, column = 3, width = 5, precision = 4)
        self.addLabel(text = "1000", row = 2, column = 3)
        self.outputFieldB2 = self.addFloatField (value = "0", row = 2, column = 3, width = 5, precision = 4)
        self.addLabel(text = "2000", row = 3, column = 3)
        self.outputFieldB3 = self.addFloatField (value = "0", row = 3, column = 3, width = 5, precision = 4)

        self.addLabel(text = "100", row = 1, column= 8)
        self.outputFieldA1 = self.addFloatField( value= "0", row = 1, column = 8, width = 5, precision= 4 )
        self.addLabel(text = "1000", row = 2, column = 8)
        self.outputFieldA2 = self.addFloatField (value = "0", row = 2, column = 8, width = 5, precision = 4)
        self.addLabel(text = "2000", row = 3, column = 8)
        self.outputFieldA3 = self.addFloatField (value = "0", row = 3, column = 8, width = 5, precision = 4)

        self.Button1 = self.addButton(text = "Sort Using Bubble Sort", row = 5, column = 0, command = self.BubbleSort)

        self.Button2 = self.addButton(text = "Sort Using Selection Sort", row = 5, column = 3, command = self.SelectionSort)

        self.Button3 = self.addButton(text = "Sort Using Python's Sort", row = 5, column = 8, command = self.PythonSort)

        

        self.myListA = random.sample(range(100),100)      ###randomizes all data in A
        
        self.myListB = random.sample(range(1000), 1000)    ###randomizes all data in B
        
        self.myListC = random.sample(range(2000), 2000)    ###randomizes all data in C
        
        self.groupListAll = [self.myListA, self.myListB, self.myListC] 

    def swap(self, aList, i, j):
        
        hold = aList[i]
                
        aList[i] = aList[j]
        
        aList[j] = hold

        

    def SelectionSort(self):

        start = time.time()                   ###STARTS RECORDING TIME FOR SORTING
        for i in range(len(self.myListA)-1):
            
            min=i
            
            for j in range((i+1), len(self.myListA)):
                
                if self.myListA[j] < self.myListA[min]:
                    
                    min=j

                    self.swap(self.myListA, i, min)     ###swap occurs 
                    
        elapsedTime = time.time() - start                ###time for sorting is recorded
        
        self.outputFieldB1.setNumber(elapsedTime)      ###provides the seconds for sorting
        
        start = 0
        elapsedTime = 0

        start = time.time()
        for i in range(len(self.myListB)-1):
            
            min=i
            
            for j in range((i+1), len(self.myListB)):
                
                if self.myListB[j] < self.myListB[min]:
                    
                    min=j

                    self.swap(self.myListB, i, min)
                    
        elapsedTime = time.time() - start
        
        self.outputFieldB2.setNumber(elapsedTime)
        
        start = 0
        elapsedTime = 0

        start = time.time()
        for i in range(len(self.myListC)-1):
            
            min=i
            
            for j in range((i+1), len(self.myListC)):
                
                if self.myListC[j] < self.myListC[min]:
                    
                    min=j

                    self.swap(self.myListC, i, min)
                    
        elapsedTime = time.time() - start
        
        self.outputFieldB3.setNumber(elapsedTime)
        
        start = 0
        elapsedTime = 0




    

       
                       

     

    def BubbleSort(self):
        

        start = time.time()              ###Starts recording Time
        maxInList=len(self.myListA)      

        Sorted=False                   

        while not Sorted:                   ###It starts to go through the loop while not sorted

            Sorted=True

            for i in range(maxInList-1):

                if self.myListA[i] > self.myListA[i+1]:                ###compare the values, swaps if it satisfies the situation

                    self.swap(self.myListA, i, i+1)

                    Sorted = False

                    maxInList-=1
        
        elapsedTime = time.time() - start                   ###Provides the time for sorting
        self.outputFieldC1.setNumber(elapsedTime)
        start = 0
        elapsedTime = 0
        
    

        start = time.time()
        maxInList=len(self.myListB)

        Sorted=False

        while not Sorted:

            Sorted=True

            for i in range(maxInList-1):

                if self.myListB[i] > self.myListB[i+1]:

                    self.swap(self.myListB, i, i+1)

                    Sorted = False

                    maxInList-=1
        
        elapsedTime = time.time() - start
        self.outputFieldC2.setNumber(elapsedTime)
        start = 0
        elapsedTime = 0

        start = time.time()
        maxInList=len(self.myListC)

        Sorted=False

        while not Sorted:

            Sorted=True

            for i in range(maxInList-1):

                if self.myListC[i] > self.myListC[i+1]:

                    self.swap(self.myListC, i, i+1)

                    Sorted = False

                    maxInList-=1
        
        elapsedTime = time.time() - start
        self.outputFieldC3.setNumber(elapsedTime)
        start = 0
        elapsedTime = 0
        
        

        
    
    def PythonSort(self):
        start = time.time()
        self.myListA.sort()                            ###Used python's simple sort to arrange individual numbers
        elapsedTime = time.time() - start
        self.outputFieldA1.setNumber(elapsedTime)
        start = 0
        elapsedTime = 0

        start = time.time()
        self.myListB.sort()
        elapsedTime = time.time() - start
        self.outputFieldA2.setNumber(elapsedTime)
        start = 0
        elapsedTime = 0

        start = time.time()
        self.myListC.sort()
        elapsedTime = time.time() - start
        self.outputFieldA3.setNumber(elapsedTime)
        start = 0
        elapsedTime = 0


                  


                         


def main():

    Sorts().mainloop()

if __name__  ==  "__main__" :
    main()
    
