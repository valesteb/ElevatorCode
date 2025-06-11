# The code for an elevator based on my knowledge in OOP
class Elevator:
    def __init__(self, total_floors, current_floor=1):
        self.current_floor =  current_floor
        
        self.total_floors = total_floors
        self.doors_open = False
        self.moving = False

    def call_elevator(self, current_floor):
      print(f"Elevator is Currently on the floor: {self.get_current_floor()}")
      if self.current_floor != current_floor:
        print("Calling elevator to current floor")
        self.current_floor = current_floor      
        print ("Elevator is here")
        self.open_doors()
      else:
        print ("Elevator is already here")
      
    def move_to_floor(self, target_floor):
        if target_floor < 1 or target_floor >= self.total_floors:
            print("Invalid floor selection.")
            return
        
        if self.doors_open:
            self.close_doors()  # Make sure doors are closed before moving

        print(f"Moving from floor {self.current_floor} to floor {target_floor}...")
        self.moving = True
        # Simulate movement
        self.current_floor = target_floor
        self.moving = False
        print(f"Arrived at floor {self.current_floor}.")
        self.open_doors()  # Automatically open doors at arrival
        print(f"Current floor: {self.get_current_floor()}")  # Inform user of current floor

    def open_doors(self):
        if self.moving:
            print("Cannot open doors while moving.")
            return
        
        if not self.doors_open:
            self.doors_open = True
            print("Doors are now open.")
        else:
            print("Doors are already open.")

    def close_doors(self):
        if self.moving:
            print("Doors are already closed while moving.")
            return

        if self.doors_open:
            self.doors_open = False
            print("Doors are now closed.")
        else:
            print("Doors are already closed.")

    def get_current_floor(self):
        return self.current_floor

# Example usage
if __name__ == "__main__":
      elevator = Elevator(total_floors=10)
    # Call the elevator to the current floor
      elevator.call_elevator(int(input("Requesting elevator from floor: ")))
    # Move to a target floor
      target_floor = int(input("Enter the floor you want to move to: "))  # Get target floor from user
      elevator.move_to_floor(target_floor)  # Move to the specified floor
      elevator.call_elevator(int(input("Requesting elevator from floor: ")))