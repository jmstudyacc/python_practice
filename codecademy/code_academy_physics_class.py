"""
def f_to_c(temp_input):
  f_temp =  temp_input
  c_temp = (f_temp - 32)* 5/9
  print(c_temp)
  return c_temp     #ends your function

temp_input = int(input("What is the temperature in Fahrenheit? "))

f_to_c(temp_input)

def c_to_f(temo_input):
  c_temp = temp_input
  f_temp = c_temp*(9/5) + 32
  print(f_temp)
  return f_temp     #ends your function

temp_input = int(input("What is the temperature in Celsius? "))

c_to_f(temp_input)
"""

"""
train_mass = int(input("What is the train's mass in kg? "))
train_acceleration = int(input("What is the train's acceleration? "))
"""

"""              
get_force(train_mass, train_acceleration)
"""

"""
def get_energy(mass):
  c = 3*10**8
  bomb_energy = mass * c**2
  print("A " + str(mass) + "kg bomb supplies " + str(bomb_energy) + " Joules.")
  return bomb_energy

mass = int(input("What is the mass of the bomb? "))
get_energy(mass)
"""

def get_force():
  train_mass = int(input("What is the train's mass in kg? "))   # Inputs make more flexible
  train_acceleration = int(input("What is the train's acceleration? "))
  n_force = train_mass*train_acceleration
  print("The GE train supplies " + str(n_force) + " Newtons of force.")
  return n_force

def get_work():
  n_force = get_force()         # Calls the get_force() function to eliminate repetition, assigns to n_force as that function provides the force
  n_distance = int(input("What is the distance of travel? "))
  n_work = n_force * n_distance   # Calls the global variable - n_force
  print("The GE train does " + str(n_work) + " Joules of work over " + str(n_distance) + " metres.")

get_work()

