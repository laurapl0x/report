'''
python 2.6

Created on 28 Mar 2014
@version: 1.0.0
@author: darrendirl
'''

import json
import time

class Report:
    '''takes in json data and creates a report instance of it then breaks the report into its seperate sections so they can be compared and analysed
    reports on SLA timeout, Empty Responses, Bid Response, Error Responses, Internal Errors, Total DSP Requests and Unmatched requests'''
    
    def __init__(self):
        '''initialise the report object'''
        self.sections = {}
        self._data = self.getData()
        self.split()
        self.size = self.getSize('SLA timeout')
        self.start_time = self.setTime(0, self.sections['SLA timeout'])
        self.end_time = self.setTime(self.size - 1, self.sections['SLA timeout'])
        
    def getData(self):
        '''open the URL and returns a dictionary representation of the object'''
        try:
            json_data = open('C:\Users\darrendirl\Downloads\json script') ############################change this to your downloads directory###################
            data = json.load(json_data)
            return data
        except:
            print "Error Occurred"

    
    def split(self):
        '''splits the json file into its different sections, creating a dictionary representation of each section'''
        for each_section in self._data:
            self.sections.update({each_section['target']:each_section['datapoints']})
            
    def printSection(self, sections):
        '''print out the sections name and all the data points it contains'''
        print sections + ": " + str(self.sections[sections])
    
    def getSize(self, sections):
        '''returns the amount of data points in the specified section'''
        size = len(self.sections[sections])
        return size
    
    def setTime(self, size=0, sections=None):
        '''set the reporting time'''
        return_time = time.strftime("%a, %d %b %Y %H:%M:%S +0000", time.localtime(sections[size][1]))
        return return_time
    

