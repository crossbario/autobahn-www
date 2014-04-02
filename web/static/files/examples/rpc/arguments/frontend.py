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

from twisted.internet import reactor
from twisted.internet.defer import inlineCallbacks

from autobahn.twisted.wamp import ApplicationSession



class Component(ApplicationSession):
   """
   An application component calling the different backend procedures.
   """

   def onConnect(self):
      self.join("realm1")


   @inlineCallbacks
   def onJoin(self, details):

      yield self.call('com.arguments.ping')
      print("Pinged!")

      res = yield self.call('com.arguments.add2', 2, 3)
      print("Add2: {}".format(res))

      starred = yield self.call('com.arguments.stars')
      print("Starred 1: {}".format(starred))

      starred = yield self.call('com.arguments.stars', nick = 'Homer')
      print("Starred 2: {}".format(starred))

      starred = yield self.call('com.arguments.stars', stars = 5)
      print("Starred 3: {}".format(starred))

      starred = yield self.call('com.arguments.stars', nick = 'Homer', stars = 5)
      print("Starred 4: {}".format(starred))

      orders = yield self.call('com.arguments.orders', 'coffee')
      print("Orders 1: {}".format(orders))

      orders = yield self.call('com.arguments.orders', 'coffee', limit = 10)
      print("Orders 2: {}".format(orders))

      arglengths = yield self.call('com.arguments.arglen')
      print("Arglen 1: {}".format(arglengths))

      arglengths = yield self.call('com.arguments.arglen', 1, 2, 3)
      print("Arglen 1: {}".format(arglengths))

      arglengths = yield self.call('com.arguments.arglen', a = 1, b = 2, c = 3)
      print("Arglen 2: {}".format(arglengths))

      arglengths = yield self.call('com.arguments.arglen', 1, 2, 3, a = 1, b = 2, c = 3)
      print("Arglen 3: {}".format(arglengths))

      self.leave()


   def onLeave(self, details):
      self.disconnect()


   def onDisconnect(self):
      reactor.stop()
