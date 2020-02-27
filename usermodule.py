import random #import random library
import time #import time library

############Classes and Functions################
class American: #Queue for American Airlines
  def __init__(self):
    self.american = []
  def enqueue(self, item):
    self.american.append(item)
  def dequeue(self):
    return self.american.pop()
  def len(self):
    return self.american.length()
  def length(self):
    return len(self.american)
amer = American()
amer.enqueue('American 127 DCA 10')
amer.enqueue('American 322 BUF 11')
amer.enqueue('American 233 FLL 12')
amer.enqueue('American 742 LAX 13')
amer.enqueue('American 112 CAE 14')
amer.enqueue('American 437 LGA 15')
#print(amer.dequeue())
#print(amer.american)


class Delta: #Queue for Delta Airlines
  def __init__(self):
    self.delta = []
  def enqueue(self, item):
    self.delta.append(item)
  def dequeue(self):
    return self.delta.pop()
  def length(self):
    return len(self.delta)
delt = Delta()
delt.enqueue('Delta 221 SFO 20')
delt.enqueue('Delta 348 DET 21')
delt.enqueue('Delta 765 CVG 22')
delt.enqueue('Delta 612 SAN 23')
delt.enqueue('Delta 148 FLL 24')
#print(delt.dequeue())
#print(delt.delta)

class Southwest: #Queue for Southwest Airlines
  def __init__(self):
    self.southwest = []
  def enqueue(self, item):
    self.southwest.append(item)
  def dequeue(self):
    return self.southwest.pop()
  def length(self):
    return len(self.southwest)
south = Southwest()
south.enqueue('Southwest 345 LGA 40')
south.enqueue('Southwest 657 PHL 41')
south.enqueue('Southwest 211 BOS 42')
south.enqueue('Southwest 324 SFO 43')
south.enqueue('Southwest 367 SAN 44')
south.enqueue('Southwest 311 LAX 45')
south.enqueue('Southwest 375 FLL 46')
#print(south.dequeue())
#print(south.southwest)

class Runway: 
  def __init__(self):
    self.runway = []
  def enqueue(self, item):
    self.runway.append(item)
  def dequeue(self):
    return self.runway.pop()
  def length(self):
    return len(self.runway)
run = Runway()

rand_num = random.randint(0,1)
secs = time.time()

def add_to_runway():
  x = rand_num
  if x == 0 and x <=.33:
    amer.dequeue()
    run.enqueue(amer.dequeue())
  elif x >= .33 and x <= .67:
    delt.dequeue()
    run.enqueue(delt.dequeue())
  elif x >= .67 and x <= 1:
    south.dequeue()
    run.enqueue(south.dequeue())

  if len(amer.american) == 0: 
    if x >= 0 and x <= .5:
      run.enqueue(delt.delt[0])
    elif x >= .5 and x <= 1:
      run.enqueue(south.southwest[0])
    elif len(delt.delta) == 0: 
      if x >= 0 and x <= .5:
        run.enqueue(amer.american[0])
      elif x >= .5 and x <= 1:
        run.enqueue(south.southwest[0])
    elif len(south.southwest) == 0: 
      if x >= 0 and x <= .5:
        run.enqueue(amer.american[0])
      elif x >= .5 and x <= 1:
        run.enqueue(delt.delt[0])

  print('The flight(s) in the Runway Queue is/are:', run.runway, '.')

def takeoff():
  y = rand_num
  if y >= 0 and y <= .5:
    run.dequeue()
    print('Flight ', run.dequeue() , ' has taken off.')
    run.dequeue()
  elif y >= .5 and y <= 1:
    time.sleep(4)
    print('There is a flight landing, please wait.')
  if run.length == 0:
    print('All flights have taken off.')
  print(amer.queue())
  print('')
  print(delt.queue())
  print('')
  print(south.queue())
  print('')
  print(run.runway)


def cancellation():
  z = random.randint(0,.9)
  if z >= 0 and z <= .1:
    amer.dequeue()
    print('Flight ', amer.dequeue(), ' has been cancelled')
    if amer.length() == 0:
      print('No flight was cancelled.')
  elif z >= .5 and z <= .6:
    delt.dequeue()
    print('Flight ', delt.dequeue(), ' has been cancelled.')
    if delt.length() == 0:
      print('No flight was cancelled.')
  elif z >= .8 and z <=.9:
    south.dequeue()
    print('Flight ', south.dequeue(), ' has been cancelled.')
    if south.length() == 0:
      print('No flight was cancelled.')

add_to_runway()
takeoff()
cancellation()


