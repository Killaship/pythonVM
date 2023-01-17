# 0 NOP
# 1 HLT
# 2 LDA
# 3 ADD
# 4 SUB
# 5 OUT
# 6 JMP
# 7 JEZ (Jump if Equal to zero)
# 8 JNZ (Jump if Not equal to Zero)
# More will probably be added.
from time import sleep # For debug options, custom VM speed. Not required.

# programs

# Example program A
# Tests all instructions, A should not be 69 at the end
# program = [6, 4, 0, 1, 2, 12, 4, 3, 5, 8, 6, 7, 3, 2, 69, 1]
# JMP, 4
# NOP
# HLT
# LDA, 12
# SUB, 3
# OUT
# JNZ, 6
# JE, 3
# LDA, 69
# HLT

# initial state options
ip = 0
a = 1234
running = True
program = [6, 4, 0, 1, 2, 12, 4, 3, 5, 8, 6, 7, 3, 2, 69, 1]

# debug options
debug = True  # Turning this off disables the custom speed and variable printouts. Goes as fast as possible.
vmspeed = 0.1 # This is the length of time (seconds) it takes for 1 cycle.

def fetch(location): # Returns the value of memory pointed to by [location]
  return program[location]

def jumpto(location):
  global ip
  ip = location - 1
  # Developer's note:
  # For whatever reason, because of the way stuff doesn't "update" until
  # the next execution cycle, you need to decrement the IP to jump to by one.
  # The VM does it for you so it's less complicated.
  # TL;DR, don't touch it, it's magic!

def eval(instruction): # Evaluates instructions in a crappy elif chain.
  # This is Python 3.8. Why did they wait till 3.10 for switch/case?
  global ip, running, debug, a, vmspeed
  if(instruction == 0): # NOP
    if(debug == True):
      print("NOP" + " ip = " + str(ip), "a = " + str(a))
    pass
  elif(instruction == 1): # HLT
    print("HLT" + " ip = " + str(ip), "a = " + str(a))
    running = False
  elif(instruction == 2): # LDA
    if(debug == True):
      print("LDA, " + str(fetch(ip + 1)) + " ip = " + str(ip), "a = " + str(a))
    a = fetch(ip + 1)
    ip += 1
  elif(instruction == 3): # ADD
    if(debug == True):
      print("ADD, " + str(fetch(ip + 1)) + " ip = " + str(ip), "a = " + str(a))
    a = a + fetch(ip + 1)
    ip += 1
  elif(instruction == 4): # SUB
    if(debug == True):
      print("SUB, " + str(fetch(ip + 1)) + " ip = " + str(ip), "a = " + str(a))
    a = a - fetch(ip + 1)
    ip += 1
  elif(instruction == 5): # OUT
    if(debug == True):
      print("OUT, " + str(a) + " ip = " + str(ip), "a = " + str(a))
    if(debug != True):
      print(str(a))
  elif(instruction == 6): # JMP
    if(debug == True):
      print("JMP, " + str(fetch(ip + 1)) + " ip = " + str(ip), "a = " + str(a))
    jumpto(fetch(ip + 1))
  elif(instruction == 7): # JEZ
    if(debug == True):
      print("JEZ, " + str(fetch(ip + 1)) + " ip = " + str(ip), "a = " + str(a))
    if(a == 0):
      jumpto(fetch(ip + 1))
      if(debug == True):
        print("(jumped)")
    else:
      ip += 1
      if(debug == True):
        print("(did not jump)")
  elif(instruction == 8): # JNZ
    if(debug == True):
      print("JNZ, " + str(fetch(ip + 1)) + " ip = " + str(ip), "a = " + str(a))
    if(a != 0):
      jumpto(fetch(ip + 1))
      if(debug == True):
        print("(jumped)")
    else:
      ip += 1
      if(debug == True):
        print("(did not jump)")
  else: # If no other instruction matches, give an error.
    raise ValueError("\n\nIllegal instruction at program address " + str(ip) + ". Accumulator value was " + str(a) + ". Instruction value was " + str(fetch(ip)) + ".") # Throw error!
    running = False # Not needed, here for redundancy.
    print("invalid instruction at " + str(ip)) # Also redundant.
def main():
  global ip, running
  running == True
  while(running == True):
    eval(fetch(ip))
    ip += 1
    if(debug == True): # delay the proper amount of time in debug mode.
      sleep(vmspeed)
main()