import sys
import tkinter as tk
from tkinter.filedialog import asksaveasfilename


def generate_csv_file(area, perimeter, num_samples):
    """
    A function to take a list of material strength results and print to a CSV file
    :param area: Area Statistics in array format
    :param perimeter: Perimeter Statistics in array format
    :param num_samples: Number of samples recorded in file
    :return: True if data was written out to the file successfully, false otherwise
    """

    # Step 1: create a variable to hold the file name
    # This is a simple GUI pop-up, should work nicely
    sample_name = asksaveasfilename()

    if sample_name == "":
        sys.exit("No Filename Was Entered. Please Enter a Filename Next Time.")

    str(sample_name)

    # Step 2: use open() to open the file in write mode. Set the return of open()
    # to a variable name that will be your file handle
    file = open(sample_name + '.csv', mode='w')

    # Step 3: write out the header for the CSV file. This string is provided for you so
    # your data can be loaded and checked. Use write().
    file_header = "Area Mean, Area StDev, Area Max, Area Min, Perimeter Mean, Perimeter StDev, Perimeter Max" \
                  ", Perimeter Min, Num Samples\n"

    # write header string out to file
    file.write(file_header)

    # Step 4: Iterate through the list of results. Each sample will contain the data for an individual test
    # Loop may be unnecessary? potential change here

    # Each object in the results list is of class SampleMaterial. This is just a dummy class to hold variables
    # in a single object. For your ease they have been broken out into individual variable names
    area_mean = area[0]
    area_deviation = area[1]
    area_max = area[2]
    area_min = area[3]
    perimeter_mean = perimeter[0]
    perimeter_deviation = perimeter[1]
    perimeter_max = perimeter[2]
    perimeter_min = perimeter[3]

    # Step 5: Stitch together a string, then write out the string via write().
    # Many variables above must be converted to a string via (). Commas also must be manually
    # stitched between each variable in the output. Do not round the data
    # Make sure an end-line character '\n' is always at the end of your string!

    # uncomment the line below
    string_to_write = str(area_mean) + "," + str(area_deviation) + "," + str(area_max) + "," + str(area_min) \
                      + "," + str(perimeter_mean) + "," + str(perimeter_deviation) + "," + str(perimeter_max) + \
                      "," + str(perimeter_min) + "," + str(num_samples) + "\n"

    # Finally, given that long string, write it to a file

    file.write(string_to_write)

    # close the file once all writing is complete
    file.close()

    # since we got here, it must have worked.
    return True
