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
    '''reports on SLA timeouts, Empty Responses, Bid Responses, Error Responses, Internal Errors, Total DSP Requests and Unmatched requests'''
    
    def __init__(self):
        '''initialise the object'''
        self.section = {}
        self._data = self.getData()
        self.split()
        self.printSection('SLA timeout')
        self.printSection('Empty Responses')
        self.size = self.getSize('SLA timeout')
        print ' '
        print 'the amount of elements in each section is: ' + str(self.size)
        print ' '
        
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
        '''splits the json file into its different sections'''
        for each_section in self._data:
            self.section.update({each_section['target']:each_section['datapoints']})
    
    def printSection(self, section):
        print section + ": " + str(self.section[section])
    
    def getSize(self, section):
        '''returns the size of the section'''
        size = len(self.section[section])
        return size
    
    def setTime(self, size=0):
        '''set the objects time'''
        return_time = time.strftime("%a, %d %b %Y %H:%M:%S +0000", time.localtime(['section'][size][1]))
        return return_time

        time = time.strftime("%a, %d %b %Y %H:%M:%S +0000", time.localtime(['section'][size][1]))
        return time



   
report = Report()      

