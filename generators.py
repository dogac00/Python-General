def square_numbers(nums):
  result = []
  for i in nums:
    result.append(i*i)
  return result
  
my_nums = square_numbers([1,2,3,4,5])

print(my_nums) # will print the list

# to convert it to a generator

def square_numbers_generator(nums):
  for i in nums:
    yield i*i
    
my_nums_generator = square_numbers_generator([1,2,3,4,5])

print(my_nums_generator) # will print the generator object

print(next(my_nums_generator))
print(next(my_nums_generator))
print(next(my_nums_generator))
print(next(my_nums_generator))
print(next(my_nums_generator)) # do it manually by next

# can't do it one more time because it will give the error StopIteration
# since it has 5 elements

# another way is this

for num in my_nums_generator:
  print(num)
  
# much more readable with generators

# another way is with the list comprehenstion

my_nums_list_comprehension = [x*x for x in [1,2,3,4,5]]

# you can create a generator as taking out brackets and putting paranthesis

my_nums_comprehension_generator = (x*x for x in [1,2,3,4,5])

print(my_nums_comprehension_generator) # will print the generator object

print(list(my_nums_comprehension_generator))

# you lose the advantages of performance and memory
# when you pass the generator to a list like above
