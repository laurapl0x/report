'''
python 2.6

Created on 28 Mar 2014
@version: 1.0.0
@author: darrendirl
'''

import json
import urllib2
import time

class Report:
    '''takes in json data and breaks it into separate sections so they can be compared and analysed, allows printing of sections in full, getting the length of the report and setting the start and end times of the report
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
            json_data = json.load(urllib2.urlopen("http://messaging001.us-ec.adtech.com/render/?_salt=1395936062.612&target=alias%28stacked%28sumSeries%28stats.gauges.*.us-ec.adtech.com.webiface.dsps.adcom.sla_timeout_responses%29%29%2C%22SLA%20timeout%22%29&target=alias%28stacked%28sumSeries%28stats.gauges.*.us-ec.adtech.com.webiface.dsps.adcom.empty_responses%29%29%2C%22Empty%20Responses%22%29&target=alias%28stacked%28sumSeries%28stats.gauges.*.us-ec.adtech.com.webiface.dsps.adcom.bids%29%29%2C%22Bid%20Response%22%29&target=alias%28stacked%28sumSeries%28stats.gauges.*.us-ec.adtech.com.webiface.dsps.adcom.error_responses%29%29%2C%22Error%20Responses%22%29&target=alias%28stacked%28sumSeries%28stats.gauges.*.us-ec.adtech.com.webiface.dsps.adcom.internal_errors%29%29%2C%22Internal%20Errors%22%29&target=alias%28dashed%28lineWidth%28sumSeries%28stats.gauges.*.us-ec.adtech.com.webiface.dsps.adcom.dsp_requests%29%2C2%29%29%2C%22Total%20DSP%20Requests%22%29&target=alias%28dashed%28lineWidth%28sumSeries%28stats.gauges.*.us-ec.adtech.com.webiface.dsps.adcom.uss_retrieve_misses%29%2C2%29%29%2C%22Unmatched%20requests%22%29&width=586&height=308&format=json"))
            return json_data
        except urllib2.URLError:
            print "URL Error Occurred"
        except urllib2.HTTPError:
            print "HTTP Error Occurred"
    
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
    

