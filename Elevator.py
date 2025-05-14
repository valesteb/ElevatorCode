# The code for an elevator based on my knowledge in OOP
class Elevator:
  def __init__(self):
    self.current_floor = 0

  def go_to_floor(self, floor):
    if self.current_floor == floor:
      print(f"Elevator is in floor {floor} ")
    else:
      print(f"Going to floor {floor}")
      self.current_floor = floor

if __name__ == "__main__":
  elevator = Elevator()
  elevator.go_to_floor(3)