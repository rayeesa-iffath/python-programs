import time
import os
from datetime import datetime

# Set shutdown/sleep time here
target_time = "22:30"   # 10:30 PM

print("Program started...")

while True:
    current_time = datetime.now().strftime("%H:%M")

    print("Current Time:", current_time)

    if current_time == target_time:
        print("Sleeping system now...")

        # Sleep for 3 minutes
        os.system("rundll32.exe powrprof.dll,SetSuspendState Sleep")

        break

    time.sleep(30)
