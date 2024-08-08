# Exponential Backoff
# This prog increase the wait time by 2 for each re attempt and maximum attempt is 5

import time

attempt = 0
wait_time = 1
max_attempt = 5

while attempt < max_attempt :
    print("Attempt ", attempt + 1, "- wait_time ", wait_time)
    time.sleep(wait_time) # time.sleep halt the program execution for specific time
    wait_time *= 2
    attempt += 1