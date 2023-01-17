# 0 NOP
# 1 HLT
# 2 LDA
# 3 ADD
# 4 SUB
# 5 OUT
# 6 JMP
# 7 JEZ (Jump if Equal to zero)
# 8 JNZ (Jump if Not equal to Zero)
from time import sleep

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
debug = True
vmspeed = 0.1

def fetch(location):
  return program[location]

def jumpto(location):
  global ip
  ip = location - 1
  # Developer's note:
  # For whatever reason, because of the way stuff doesn't "update" until
  # the next execution cycle, you need to decrement the IP to jump to by one.
  # The VM does it for you so it's less complicated.
  # TL;DR, don't touch it, it's magic!

def eval(instruction):
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
  else:
    running = False
    print("invalid instruction at " + str(ip))
def main():
  global ip, running
  running == True
  while(running == True):
    eval(fetch(ip))
    ip += 1
    if(debug == True):
      sleep(vmspeed)
main()