import time

def focus_clock(duration):
    start_time = time.time()
    end_time = start_time + duration*60  # duration is in minutes

    while time.time() < end_time:
        print('Keep focusing!')
        time.sleep(60)  # pause for 60 seconds

    print('Time\'s up! Take a break.')
