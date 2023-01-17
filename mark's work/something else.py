ramsize = 16
ram = [] # Generates empty list the size of ramsize (global list)
ip = 0 # instruction pointer

# registers
a = 0

def load():  # loads program into RAM
  global ram
  f = open("program.vm", "r")
  ram = (f.readlines())[0].split(" ")
  print(ram)
  

def main(): # entry point for this thing, nothing should be going outside here
  load()
  global ip
  global a
  running = True
  for i in ram: # execution loop
   if(running == False):
     break
   i = int(i)
   if(i == 0): # NOP (no operation) instruction
      ip += 1
   elif(i == 1): # HLT (halt) instruction
      running = False
      ip += 1
      print("execution stopped at instruction " + str(ip))
   elif(i == 2): # LDA (load A) instruction (loads into accumulator from ram)
     print("LDA")
     a = ram[ip + 1]
     ip += 1
   elif(i == 3): # OUT instruction (outputs contents of accumulator)
     print(a)
     ip += 1
   elif(i == 4): # ADD instruction (adds to contents of accumulator from ram)
     print(a)
     ip += 1
   
     
     


 

main()