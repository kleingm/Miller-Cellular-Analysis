# These are all the packages needed for the code to run
# No need to mess with these
import numpy as np
import statistics as stat
from write_stats import generate_csv_file
import tkinter as tk
from tkinter.filedialog import askopenfilename


def parse_cell_file(path_to_file):
    """
    Reads through selected CSV data file and returns relevant data for statistical analysis
    :param path_to_file: Path to the file in Project
    :return: Area Data, Perimeter Data
    """
    file = open(path_to_file)

    # determine when to begin reading into these files
    begin_reading = False
    area_parse = []
    perimeter_parse = []
    num_sample = 0

    # begin iterating through file
    for line in file:
        if line == '' or line == '\n':
            continue

        splits = line.strip().split(",")

        if begin_reading:
            # Gather Area and Perimeter Data from File
            area_parse.append(float(splits[1].replace('\"', '')))
            perimeter_parse.append(float(splits[5].replace('\"', '')))
            num_sample += 1

        # try to find start of data
        # Might need to edit depending on CSV given
        if splits[1] == "Area":
            begin_reading = True
    file.close()

    return np.asarray(area_parse), np.asarray(perimeter_parse), num_sample


def area_statistics(area_input):
    """
    Calculate important statistical data about the area of a cell
    :param area_input: Array of areas from cell ImageJ Data
    :return: An array of various statistical data
    """
    area_mean = stat.mean(area_input)
    area_deviation = stat.stdev(area_input)
    area_max = max(area_input)
    area_min = min(area_input)
    area_stats_array = [area_mean, area_deviation, area_max, area_min]
    np.array(area_stats_array)

    return area_stats_array


def perimeter_statistics(perimeter_input):
    """
    Calculate important statistical data about the perimeter of a cell
    :param perimeter_input: Array of perimeters from ImageJ data
    :return: An array of various statistical data
    """
    perimeter_mean = stat.mean(perimeter_input)
    perimeter_deviation = stat.stdev(perimeter_input)
    perimeter_max = max(perimeter_input)
    perimeter_min = min(perimeter_input)
    perimeter_stats_array = [perimeter_mean, perimeter_deviation, perimeter_max, perimeter_min]
    np.array(perimeter_stats_array)

    return perimeter_stats_array


# Actual RunTime Code is here

if __name__ == "__main__":

    tk.Tk().withdraw()  # we don't want a full GUI, so keep the root window from appearing
    filename = askopenfilename()  # show an "Open" dialog box and return the path to the selected file

    # Parse Data to get Area, Perimeter, and Number of Samples
    (area, perimeter, num_samples) = parse_cell_file(filename)

    # Calculate Statistics for Relevant Data
    area_stats = area_statistics(area)
    perimeter_stats = perimeter_statistics(perimeter)

    # Write gathered data to a brand-spanking-new CSV file
    generate_csv_file(area_stats, perimeter_stats, num_samples)

    print("Done!")
