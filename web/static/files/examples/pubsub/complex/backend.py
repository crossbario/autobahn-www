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

import random

from twisted.internet import reactor
from twisted.internet.defer import inlineCallbacks

from autobahn.wamp.types import SubscribeOptions
from autobahn.twisted.util import sleep
from autobahn.twisted.wamp import ApplicationSession



class Component(ApplicationSession):
   """
   An application component that publishes events with no payload
   and with complex payloads every second.
   """

   def __init__(self, realm = "realm1"):
      ApplicationSession.__init__(self)
      self._realm = realm


   def onConnect(self):
      self.join(self._realm)


   @inlineCallbacks
   def onJoin(self, details):

      counter = 0
      while True:
         self.publish('com.myapp.heartbeat')

         obj = {'counter': counter, 'foo': [1, 2, 3]}
         self.publish('com.myapp.topic2', random.randint(0, 100), 23, c = "Hello", d = obj)

         counter += 1
         yield sleep(1)
