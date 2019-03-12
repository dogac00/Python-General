import os
import time

curDir = os.getcwd() # current working directory
print(curDir)

# C:\Users\Dogac ... ... ...

os.mkdir("newDir") # new working directory created

time.sleep(2) # wait 2 seconds

os.rename("newDir", "newDir2") # change the name after 2 seconds

time.sleep(2)

os.rmdir("newDir2") # removes the directory after 2 seconds
