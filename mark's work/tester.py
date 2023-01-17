ramsize = 16
ram = [] # Generates empty list the size of ramsize (global list)
ip = 0 # instruction pointer
ci = False #current instruction
cd = False #current data
cid = [] #current instruction data
cdd = [] #current data data


# print("execution stopped at instruction " + str(ip)) HLT debug message

def load():  # loads program into RAM
  global ram
  f = open("program.vm", "r")
  ram = (f.readlines())[0].split(" ")
  print(ram)
  

def main(): # entry point for this thing, nothing should be going outside here
  load()
  global ci
  global cd
  global cdd
  global cid
  global ip
  running = True
  for i in ram: # execution loop
   if(running == False):
     break
   if ci == True:
     cid.append(i)
   if cd == True:
     cdd.append(i)
   i = int(i)
   if(i == 0): # NOP (end operation)
      ip += 1
      cd = False
      ci = False
   elif(i == 1): # Instruction Input
      ci = True
      ip += 1
     
   elif(i == 2): # Data Input
     print("LDA")
     cd = True
     ip += 1
   elif(i == 3): # OUT instruction (outputs contents of accumulator)
     ip += 1
   elif(i == 4): # ADD instruction (adds to contents of accumulator from ram)
     ip += 1
  print(cid + "abc")
  print(cdd)
     
     


 

main()