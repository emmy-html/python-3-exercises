weight = 41.5
# Ground Shipping
if weight <= 2:
  cost_ground = weight * 1 + 20
elif weight > 2 and weight <= 6:
  cost_ground = weight * 3 + 20
elif weight > 6 and weight <= 10:
  cost_ground = weight * 4 + 20
else:
  cost_ground = weight * 4.75 + 20
# Ground Shipping Premium
cost_ground_premium = 125
# Drone Shipping
if weight <= 2:
  cost_drone = weight * 4.50
elif weight > 2 and weight <= 6:
  cost_drone = weight * 9
elif weight > 6 and weight <= 10:
  cost_drone = weight * 12
else:
  cost_drone = weight * 14.25
# Testing all of the shipping rates
print(cost_ground)
print(cost_ground_premium)
print(cost_drone)