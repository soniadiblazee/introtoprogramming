def launch_sequence():
    print("initalizing countdown....")
    print("3.. 2.. 1.. lift-off!")

def mars_mission(distance, speed, fuel, crew_ready):
    mars_mission(225000000,25000, 600000, True)
    time = distance / speed
    if speed < 20000:
        print("WARNING: speed too low for timely arrival.")
    elif speed > 50000:
        print("WARNING: risk of overshooting mars; speed is too fast.")
    else:
        print("optimal speed for mars mission.")

    if fuel < 500000:
        print("not enough fuel for journey!")
    else:
        print("enough fuel for mission")

    if crew_ready:
        print("crew is ready for the mission.")
    else:
        print("crew is not ready. mission delayed.")
