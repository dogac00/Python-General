import mem_profile
import random
import time

names = ['Rick', 'John', 'Adam', 'Steve', 'Thomas']
majors = ['Math','Engineering','CompScience','Arts','Business']

print("Memory (Before): {} MB".format(mem_profile.memory_usage_resource()))

def people_list(num_people):
  result = []
  for i in range(num_people):
    person = {
      'id':i,
      'name':random.choice(names),
      'major':random.choice(majors)
    }
  result.append(person)
  return result
  
def people_generator(num_people):
  for i in range(num_people):
    person = {
      'id':i,
      'name':random.choice(names),
      'major':random.choice(majors)
    }
    yield person
    
t1 = time.clock()
people = people_list(1000000)
t2 = time.clock()

# t1 = time.clock()
# people = people_generator(1000000)
# t2 = time.clock()

print("Memory (AFter): {} MB".format(mem_profile.memory_usage_resource()))
print("Took {} Seconds".format(t2-t1))    

# you can try with people generator list by uncommenting
# the lines above
# you will see that it is much better in performance and memory

# ----- EXAMPLE OUTPUT -----

# with people_list()
# Memory (Before): 15.92578125 MB
# Memory (After):  318.92578125 MB
# Took 1.232136 Seconds

# with people_generator()
# Memory (Before): 15.98046875 MB
# Memory (After):  15.9921875 MB
# Took 2e-06 Seconds
