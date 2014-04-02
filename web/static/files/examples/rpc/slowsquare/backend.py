###############################################################################
##
##  Copyright (C) 2014 Tavendo GmbH
##
##  Licensed under the Apache License, Version 2.0 (the "License");
##  you may not use this file except in compliance with the License.
##  You may obtain a copy of the License at
##
##      http://www.apache.org/licenses/LICENSE-2.0
##
##  Unless required by applicable law or agreed to in writing, software
##  distributed under the License is distributed on an "AS IS" BASIS,
##  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
##  See the License for the specific language governing permissions and
##  limitations under the License.
##
###############################################################################

from twisted.internet.defer import Deferred, \
                                   inlineCallbacks, \
                                   returnValue

from autobahn.twisted.wamp import ApplicationSession
from autobahn.twisted.util import sleep



class Component(ApplicationSession):
   """
   A math service application component.
   """

   def __init__(self, realm = "realm1"):
      ApplicationSession.__init__(self)
      self._realm = realm


   def onConnect(self):
      self.join(self._realm)


   def onJoin(self, details):

      def square(x):
         return x * x

      self.register(square, 'com.math.square')


      @inlineCallbacks
      def slowsquare(x):
         yield sleep(1)
         returnValue(x * x)

      self.register(slowsquare, 'com.math.slowsquare')
