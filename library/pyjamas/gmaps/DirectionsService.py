# Copyright (C) 2009 Daniel Carvalho <idnael@gmail.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from __pyjamas__ import JS

DirectionsStatus = JS("$wnd.google.maps.DirectionsStatus")
DirectionsTravelMode = JS("$wnd.google.maps.DirectionsTravelMode")
DirectionsUnitSystem = JS("$wnd.google.maps.DirectionsUnitSystem")

from pyjamas.gmaps.Utils import gmapsJsObjectToPy
from Utils import dictToJs

from Geocoder import geocoderResultToPy

#
#        listFields=JS('["trips","warnings","routes","steps", /*geocoder fields:*/  "types","address_components"]')
#
#        dictFields=JS('["results","trips[]","routes[]","steps[]","start_geocode","end_geocode", /*geocoder fields:*/  "address_components[]","geometry"]')
#        
#        results=gmapsJsObjectToPy(jsResults,"results",listFields,dictFields)
       


directionsResultsFields = dictToJs({
        "trips":'l' , "warnings":'l' , "routes":'l' , "steps":'l' , 
        "results":'d' , "trips[]":'d' , "routes[]":'d' , "steps[]":'d' , 

        "start_geocode":geocoderResultToPy , "end_geocode":geocoderResultToPy , 
        })

def directionsResultsToPy(jsResults):
    results = gmapsJsObjectToPy(jsResults, "results", directionsResultsFields)

    # DirectionsRenderer will need this!
    results.__jsResults = jsResults

    return results
    


class DirectionsService:
    def __init__(self):
        self.ds = JS("""new $wnd.google.maps.DirectionsService();""")

    def route(self, request, callback):
        self.ds.route(request, lambda jsResults, status: callback(directionsResultsToPy(jsResults), status))
        

def DirectionsRequest(**params):
    return dictToJs(params)

def DirectionsWaypoint():
    JS("return {};")

def DirectionsTrip():
    JS("return {};")

def DirectionsRoute():
    JS("return {};")

def DirectionsStep():
    JS("return {};")

def DirectionsDistance():
    JS("return {};")

def DirectionsDuration():
    JS("return {};")


