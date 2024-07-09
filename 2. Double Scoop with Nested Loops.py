# Objective: The aim of this assignment is to practice using nested loops in Python.
# Task 1: Your Mood Tracker Simulate a mood tracker that 
# records your mood at three different times of the day (morning, afternoon, evening) 
# for each day of the week. 
# Use nested loops to implement this: the outer loop should iterate over the days, 
# and the inner loop should iterate over the times of the day. For each time, 
# randomly select a mood from a predefined list and print it. 
# Use the random module again to randomly select the mood.
# Example Outcome: An example would be "On Tuesday afternoon you were sad" 
# "On Tuesday night you were happy" "On Wednesday morning you were tired"

import random

days = ["Monday", "Tuesday", "Wendesday", "Thursday", "Friday", "Saturday", "Sunday"]
time_of_days = ["morning", "afternoon", "evening"]
moods = ["happy", "tired", "sad", "frustated", "anxious", "joyful", "excited"]

for day in days:
    for time_of_day in time_of_days:
            random_mood = random.choice(moods)
            print(f"On {day} {time_of_day} you were {random_mood}") 