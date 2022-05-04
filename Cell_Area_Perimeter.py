# These are all the packages needed for the code to run
# No need to mess with these
import numpy as np
import statistics as stats
from write_stats import generate_csv_file


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

    # begin iterating through file
    for line in file:
        if line == '' or line == '\n':
            continue

        splits = line.strip().split(",")

        if begin_reading == True:
            # Gather Area and Perimeter Data from File
            area_parse.append(float(splits[0].replace('\"', '')))
            perimeter_parse.append(float(splits[1].replace('\"', '')))

        # try to find start of data
        # Might need to edit depending on CSV given
        if splits[0] == "Area":
            begin_reading = True
    file.close()

    return np.asarray(area_parse), np.asarray(perimeter_parse)


def area_statistics(area):
    """
    Calculate important statistical data about the area of a cell
    :param area: Array of areas from cell ImageJ Data
    :return: An array of various statistical data
    """
    area_mean = stats.mean(area)
    area_stdev = stats.stdev(area)
    area_max = max(area)
    area_min = min(area)
    area_stats_array = [area_mean, area_stdev, area_max, area_min]
    np.array(area_stats_array)

    return area_stats_array


def perimeter_statistics(perimeter):
    """
    Calculate important statistical data about the perimeter of a cell
    :param perimeter: Array of perimeters from ImageJ data
    :return: An array of various statistical data
    """
    perimeter_mean = stats.mean(perimeter)
    perimeter_stdev = stats.stdev(perimeter)
    perimeter_max = max(perimeter)
    perimeter_min = min(perimeter)
    perimeter_stats_array = [perimeter_mean, perimeter_stdev, perimeter_max, perimeter_min]
    np.array(perimeter_stats_array)

    return perimeter_stats_array


# Actual RunTime Code would Go Under here

if __name__ == "__main__":

    # Change to reflect which folder ImageJ CSV is stored
    material_folder = "Raw CSV"

    # modify this line to select different samples in the material folder
    sample_name = "example_data_2"

    # Modify this line to change what name the data is saved as
    output_name = "data_2"

    ### Do not modify below this line ###

    path_to_directory = "./Data/"
    path_to_samples = path_to_directory + material_folder + "/"

    # Filepath for parsing function
    path_to_file = path_to_samples + sample_name + ".csv"

    # Parse Data to get Area and Perimeter "Array?"
    (area, perimeter) = parse_cell_file(path_to_file)
    print(area)
    # Calculate Statistics for Relevant Data
    area_stats = area_statistics(area)
    perimeter_stats = perimeter_statistics(perimeter)

    # Write gathered data to a brand-spanking-new CSV file
    generate_csv_file(output_name + ".csv", area_stats, perimeter_stats)

    print("Done!")
