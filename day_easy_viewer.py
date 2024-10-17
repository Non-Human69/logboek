import os
import json
import datetime as dt
import tkinter as tk

def main():
    days = get_data_logs_json()
    print(f"Available days:{len(days.keys())}")
    make_window(days)

def get_data_logs_json():
    logs = os.listdir("logs")
    logs = [log for log in logs if log.endswith(".json")]

    days = {}
    for log in logs:
        with open("logs/" + log, "r") as file:
            data = json.load(file)
            date = dt.datetime.strptime(log.split(".")[0], "%d-%m-%Y").date()
            days[str(date)] = data

    return days

# Show the data of a specific day, the time aligns to the left with that data in the right
def show_day_data(date, days):
    window = tk.Tk()
    window.title(date)

    data = days[date]
    for time, description in data["times"].items():
        tk.Label(window, text=f"{time} - {description}").pack()
    window.mainloop()


def make_window(days):
    window = tk.Tk()
    window.title("Day Viewer")

    # An selection screen with everydate(max 6 in width, can go on forever in length, format dd-mm-yyyy), when clicked on a date it will show the data of the day
    for date in days.keys():
        tk.Button(window, text=date, command=lambda date=date: show_day_data(date, days)).pack()
    window.mainloop()
if __name__ == "__main__":
    main()