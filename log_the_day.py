import json
import os
import datetime as dt
from collections import namedtuple

def main():
    while True:
        try:
            date = dt.datetime.now().strftime("%d-%m-%Y")
        except ValueError:
            print("Invalid date format. Please try again.")
            continue

        if date:
            answer = input(f"Do you want to save the date {date}? (yes/y to confirm)(n): ")
            if answer.lower() in ["yes", "y"]:
                times = get_times()
                save_data(date, times)
                break
            elif answer.lower() == "n":
                times = get_times(True)
                save_data(date, times)
                break
            else:
                answer = input(f"Do you want to save a other date? (yes/y to confirm): ")
                if answer.lower() in ["yes", "y"]:
                    date = dt.datetime.strptime(input("Enter the date (DD-MM-YYYY): "), "%d-%m-%Y").date().strftime("%d-%m-%Y")
                    times = get_times()
                    save_data(date, times)
                    break
                break

def get_times(bool = False):
    times_texts = {}
    while True:
        if bool == False:
            time = input("Enter the time (HH:MM)(n): ")
        else:
            time = 'n'

        # Check if the time is in the correct format
        try:
            if time == "n" or time == "now":
                time = dt.datetime.now().strftime("%H:%M")

            dt.datetime.strptime(time, "%H:%M")
            times_texts.update({time: input("Enter a description: ")})
        except ValueError:
            print("Invalid time format. Please try again.")
            continue

        if input("Do you want to add another time? (y/n): ").lower() == "n":
            break
    return times_texts


def get_old_data_data(filename):
    if os.path.exists(filename):
        with open(filename, "r") as file:
            return json.load(file)
    return {}


def save_data(date, times):
    filename = str(date) + ".json"
    old_data = get_old_data_data("logs/" + filename)

    if "times" in old_data:
        old_data["times"].update(times)
    else:
        old_data["times"] = times

    # Sort the times dictionary by keys (time)
    old_data["times"] = dict(sorted(old_data["times"].items()))

    with open(("logs/" + filename), "w") as file:
        json.dump(old_data, file, indent=4)
if __name__ == "__main__":
    main()