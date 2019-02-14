def hallo(a_name):
  return ("Hallo! " + a_name)

def hallo2(name_a,name_b):
  return ("Hallo! " + name_a + " and " + name_b + " !")


def sum_two(x,y):
  z = x + y
  return z


import math
def circle_area(radius):
  a = radius**2 * math.pi
  return a

#functions with loops and lists

def my_sum(a_list):
  total = 0
  for n in a_list:
    total = total + n
  return total

def my_prod(a_list):  #multiply all items in a list as a function -> just use print(my_prod(a_list))
  total = 1
  for n in a_list:
   total = n * total
  return total

def my_count(a_list):
  total = 0
  for _ in a_list:
    total = total + 1   #alternative total = total + n/n, dies funktioniert aber mur mit zahlenlisten
  return total

#Functions with logical operators, loops and lists

def my_count_less_5(a_list):
  count = 0
  for n in a_list:
    if n < 5:
      count = count + 1
  return count #important to have the retun on that level (not within the loop itself)

def my_count_ones(a_list): 
  count = 0
  for n in a_list:
   if n == 1: #use == for comparisons!
    count = count + 1
  return count

def is_list_empty(a_list):
  if my_count(a_list) == 0:
    return True
  else:
    return False


def my_max(a_list):
  if is_list_empty(a_list):
    return None #at this point we do not need an "else", the programm will finisch the reading the function if is_list_empty is true
  count = a_list[0] # count = 0 only works if all numbers are postitive
  for n in a_list:
    if n > count:
      count = n
  return count

#get filenames (r"C:\\Users\\Maxime Zehnder\\Desktop")  """C:\\Users\\Maxime Zehnder\\Desktop"""
import os

def get_filenames(a_dirname):
  list_of_files = os.listdir(a_dirname)
  all_files = [] #this is an empty list
  for n in list_of_files:
    full_path = os.path.join(a_dirname,n) #this line is needed for reasons of \ / confusion
    if not os.path.isdir(full_path):
      all_files.append(full_path) #this line "appends" the file path to the filename
  return all_files

#[12,34[56,67]] -> [12,34,56,67] -> we create the function "flatten"

def flatten(a_list_with_list):
  new_list = []
  for n in a_list_with_list:
    if isinstance(n,list):
      for i in n:
        new_list.append(i)
      else:
        new_list.append(n)
  return new_list

#create a function that prints the list in a list

def print_right(a_list_with_list):
  for n in a_list_with_list:
    if isinstance(n,list):
      for i in n:
        print(i,end="") #important -> end=" ", ensures that the elements i of the sublists are added on the same line
      print(" ")
    else:
      print(n)



#a_list_with_list = [10,5,[3,4],7]

#a function that prints a certain input x times 

def single_row_stars(number):
  for n in range(number):
    print("*/", end="")

def single_row_of(number, string):
  for n in range(number):
    print(string, end="")

def square_of_stars(number):
  for n in range(number):
    for i in range (number):
      print ("*", end="")
    print ("")

a_list = [2,3,4]

def list_by_2(a_list):
  new_list = []
  for n in a_list:
    new_list.append(n*2)
  return new_list


def list_rev(a_list):
  new_list = []
  for i in a_list:
    new_list.insert(0, i)
  return new_list


def setup_game(size,max_alive):
  a_grid = get_grid(size)
  fill_grid_random(a_grid,max_alive)

def get_grid (size):
  new_grid = []
  for row in range(size):
    new_sublist = []
    for colum in range(size):
      new_sublist.append("-")
    new_grid.append(new_sublist)
  return new_grid


def rand_alive():
  number = random.randint(1,2)
  if number == 1:
    return True
  else:
    return False


def fill_grid_random(a_grid,max_alive):
  size= len(a_grid)
  remaining = max_alive
  for r_i in range(size):
    for c_i in range(size):
        if rand_alive() == True and remaining !=0:
          a_grid[r_i][c_i] = "x"
          remaining = remaining - 1
        else:
           a_grid[r_i][c_i] = "-"



      










