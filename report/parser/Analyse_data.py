'''
python 2.6
Created on 29 Mar 2014
@version: 1.0.0
@author: darrendaly
'''

def calculateAverages(self):
    '''Calculates the average value of occurrences'''
    for each_line in self._data:
        total = 0
        for counter in range(self.size):
            total += each_line['datapoints'][counter][0]
            avg = total / self.size
        print each_line['target'] + " average value is: " + str(avg) + " and the total value is: " + str(total)
    
def findMins(self):
    '''find the minimum value in each section'''
    for each_line in self._data:
        for counter in range(self.size):
            value = each_line['datapoints'][counter][0]
            if counter == 0:
                minimum = value
            elif minimum > value:
                minimum = value
        print each_line['target'] + " minimum value = " + str(minimum)
    
def findMaxs(self):
    '''find the maximum value in each section'''
    for each_line in self._data:
        for counter in range(self.size):
            value = each_line['datapoints'][counter][0]
            if counter == 0:
                maximum = value
            elif maximum < value:
                maximum = value
        print each_line['target'] + " maximum value = " + str(maximum)
            