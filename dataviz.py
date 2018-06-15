from collections import Counter

import csv
import matplotlib.pyplot as plt
import numpy as np

global MY_FILE
MY_FILE = "Portfolio/data/sample_sfpd_incident_all.csv"

def parse(raw_file, delimiter):     # Parses raw CSV file to a JSON-line object

    opened_file = open(raw_file)
    csv_data = csv.reader(opened_file, delimiter=delimiter)
    parsed_data = []
    fields = next(csv_data)
    for row in csv_data:
        parsed_data.append(dict(zip(fields, row)))
    opened_file.close()

    return parsed_data


def visualize_days():       # Visualize data by day of week

    data_file = parse(MY_FILE, ",")     # Grab parsed data from earlier

    counter = Counter(item["DayOfWeek"] for item in data_file)      # count how many incidents happen on each day of the week

    data_list = [
        counter["Monday"],
        counter["Tuesday"],
        counter["Wednesday"],
        counter["Thursday"],
        counter["Friday"],
        counter["Saturday"],
        counter["Sunday"]
        ]       # Separate days of week (x-axis) from number of incidents each day (y-axis)
    day_tuple = tuple(["Mon", "Tues", "Wed", "Thurs", "Fri", "Sat", "Sun"])

    plt.plot(data_list)     # Assign y-axis data to matplotlib plot

    plt.xticks(range(len(day_tuple)), day_tuple)        # Assign labels to plot

    plt.savefig("Days.png")     # Save plot

    plt.clf()       # Close plot

def visualize_type():       # Visualize data by category

    data_file = parse(MY_FILE, ",")

    counter = Counter(item["Category"] for item in data_file)

    labels = tuple(counter.keys())      # Labels from counter keys

    xlocations = np.arange(len(labels)) + 0.5       # Set where labels hit x-axis

    width = 0.5

    plt.bar(xlocations, counter.values(), width = width)        # Assign data to bar graph

    plt.xticks(xlocations + width / 2, labels, rotation = 90)       # Assign labels and ticks to x-axis

    plt.subplots_adjust(bottom = 0.5)       # Adjust label space

    plt.rcParams['figure.figsize'] = 12, 8      # Make graph larger

    plt.savefig("Type.png")
    plt.clf()

def main():
    visualize_days()
    visualize_type()

if __name__ == "__main__":
    main()

