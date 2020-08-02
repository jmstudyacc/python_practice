premium = float(125.00)
ground_flat = float(20.00)

def ground_shipping(weight):
  if weight <= 2:
    shipping = (1.50*weight)+ground_flat
    return float(shipping)
  elif weight > 2 and weight <= 6:
    shipping = (3.00*weight)+ground_flat
    return float(shipping)
  elif weight > 6 and weight <= 10:
    shipping = (4.00*weight)+ground_flat
    return float(shipping)
  else:
    shipping = (4.75*weight)+ground_flat
    return float(shipping)

#ground_shipping()

def drone_shipping(weight):
  if weight <= 2:
      drone = (4.50*weight)
      return float(drone)
  elif weight > 2 and weight <= 6:
      drone = 9.00*weight
      return float(drone)
  elif weight > 6 and weight <= 10:
      drone = 12.00*weight
      return float(drone)
  else:
      drone = 14.25*weight
      return float(drone)

#drone_shipping()

def ground_or_drone():
    weight = float(input("What is the weight of your package? "))
    ground = ground_shipping(weight)
    drone = drone_shipping(weight)
    if ground < drone and ground < premium:
        return print("Ground shipping is the cheapest method and this would cost "+str(ground))
    elif drone < ground and drone < premium:
        return print("Drone shipping is the cheapest method and this would cost "+ str(drone))
    else:
        return print("Premium shipping is cheapest: "+str(premium)) #+ "\nGround shipping would cost: " +str(ground)+" "+ "\nDrone shipping would cost: "+str(drone))

ground_or_drone()
