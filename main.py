ramsize = 256 # This variable defines the size of the RAM, i see
ram = [0] * ramsize # Generates empty list the size of ramsize (global list)
ip = 0 # instruction pointer
def load():  # loads program into RAM
  f = open("program.vm", "r")
  print(f.read())
  

def main(): # entry point for this thing, nothing should be going outside here
  running == True
  while(running == True):
   for i in range(ramsize): # execution loop
     if(ram[i] == 0):
        ip += 1
main()