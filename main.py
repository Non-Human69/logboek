import json
import os
import datetime as dt
from collections import namedtuple

def main():
    while True:
        try:
            date = dt.datetime.strptime(input("Enter the date (DD-MM-YYYY): "), "%d-%m-%Y").date()
        except ValueError:
            print("Invalid date format. Please try again.")
            continue

        if date:
            answer = input(f"Do you want to save the date {date}? (yes/y to confirm): ")
            if answer.lower() in ["yes", "y"]:
                times = get_times()
                save_data(date, times)
            else:
                continue

        if input("Do you want to add another date? (y/n): ").lower() == "n":
            break

def get_times():
    times_texts = {}
    while True:
        time = input("Enter the time (HH:MM): ")

        # Check if the time is in the correct format
        try:
            dt.datetime.strptime(time, "%H:%M")
            times_texts.update({time: input("Enter a description: ")})
        except ValueError:
            print("Invalid time format. Please try again.")
            continue

        if input("Do you want to add another time? (y/n): ").lower() == "n":
            break
    return times_texts

def save_data(date, times):
    filename = date.strftime("%d-%m-%Y") + ".json"
    data = {str(date): {"times": times}}
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)

if __name__ == "__main__":
    main()