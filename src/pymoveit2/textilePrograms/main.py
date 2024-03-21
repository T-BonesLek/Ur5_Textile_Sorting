from pick_goal import move_to_pose
from place_cotton import move_to_place_cotton
from place_mix import move_to_place_mix
from place_wool import move_to_place_wool

try:
    move_to_pose(-0.55)
    next = input("Press enter to continue to place_cotton.py")
    move_to_place_cotton()
    move_to_place_mix()
    move_to_place_wool()
    print("Program finished")

except Exception as e:
    print(f"An error occurred: {e}")