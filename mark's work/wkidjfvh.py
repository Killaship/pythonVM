ramsize = 16
ram = [] # Generates empty list the size of ramsize (global list)
ip = 0 # instruction pointer
ci = False #current instruction
cd = False #current data
cid = [] #current instruction data
cdd = [] #current data data
cmds = {1 : "+",
        2 : "-",
        3 : "*",
        4 : "/",
        5 : "^",
        6 : "√", 7, 8, 9}

# print("execution stopped at instruction " + str(ip)) HLT debug message

# William's ISA
# 9 NOP
# 5 HLT
# 3 LDA
# 1 ADD
# 1 SUB
# 5 OUT
# 6 JMP
# 7 JE (Jump if Equal to zero)
# 8 JNZ (Jump if Not equal to Zero)



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
   i = int(i)
   if(running == False):
     break
   if ci == True and i != 0:
     cid.append(i)
   elif cd == True and i != 0:
     cdd.append(i)
   elif i == 0: # NOP (end operation)
      if cdd in :
      if int(cid) in cmds:
      cd = False
      ci = False
   elif i == 1: # Instruction Input
      ci = True
   elif i == 2: # Data Input
     cd = True
   elif i == 3: # LDA instruction
     print("abc")
   elif i == 4:
   ip += 1
  print(cid)
  print(cdd)
     

main()
