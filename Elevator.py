# The code for an elevator based on my knowledge in OOP
class Elevator:
  def __init__(self, total_floors, current_floor=0):
    self.current_floor = current_floor
    self.total_floors = total_floors
    self.doors_opened = False
    self.movement = False

  #I will now make a function to call the elevator from the floor it's at to the floor where user is requesting it (current_floor)
  def call_elevator(self, current_floor):
  #If the elevator is not at the current floor, the function will call the elevator.
    if self.current_floor != current_floor and self.movement == False:
        self.movement = True
        print("Calling elevator to current floor")
        self.current_floor = current_floor
        self.movement = False #To make sure the elevator stops before opening the doors
        open_doors()        
      else:
        print ("Elevator is already here") 
        open_doors()

  def go_to_floor(self, current_floor):
    if self.current_floor == current_floor:
      print(f"Elevator is in floor {current_floor} ")
    else:
      print(f"Going to floor {current_floor}")
      self.current_floor = current_floor

if __name__ == "__main__":
  elevator = Elevator()
  elevator.go_to_floor(3)