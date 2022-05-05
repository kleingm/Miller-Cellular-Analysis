def generate_csv_file(filename, area, perimeter):
    """
    A function to take a list of material strength results and print to a CSV file
    :param filename: File that should be written to
    :param area: Area Statistics in array format
    :param perimeter: Perimeter Statistics in array format
    :return: True if data was written out to the file successfully, false otherwise
    """

    # Step 1: create a variable to hold the file name

    # Change to reflect which folder ImageJ CSV is stored
    data_folder = "Processed Data"

    # modify this line to select different samples in the material folder
    sample_name = filename
    str(sample_name)

    # Modify this line to change what name the data is saved as
    path_to_directory = "./Data/"
    path_to_samples = path_to_directory + data_folder + "/"

    # Filepath for parsing function
    output_file_name = path_to_samples + sample_name

    # Step 2: use open() to open the file in write mode. Set the return of open()
    # to a variable name that will be your file handle

    # uncomment the line below
    file = open(output_file_name, mode='w')

    # Step 3: write out the header for the CSV file. This string is provided for you so
    # your data can be loaded and checked. Use write().
    file_header = "Area Mean, Area StDev, Area Max, Area Min, Perimeter Mean, Perimeter StDev, Perimeter Max" \
                  ", Perimeter Min\n"

    # write header string out to file
    file.write(file_header)

    # Step 4: Iterate through the list of results. Each sample will contain the data for an individual test
    # Loop may be unnecessary? potential change here

    # Each object in the results list is of class SampleMaterial. This is just a dummy class to hold variables
    # in a single object. For your ease they have been broken out into individual variable names
    area_mean = area[0]
    area_stdev = area[1]
    area_max = area[2]
    area_min = area[3]
    perimeter_mean = perimeter[0]
    perimeter_stdev = perimeter[1]
    perimeter_max = perimeter[2]
    perimeter_min = perimeter[3]

    # Step 5: Stitch together a string, then write out the string via write().
    # Many variables above must be converted to a string via (). Commas also must be manually
    # stitched between each variable in the output. Do not round the data
    # Make sure an endline character '\n' is always at the end of your string!

    # uncomment the line below
    string_to_write = str(area_mean) + "," + str(area_stdev) + "," + str(area_max) + "," + str(area_min) \
                      + "," + str(perimeter_mean) + "," + str(perimeter_stdev) + "," + str(perimeter_max) +\
                      "," + str(perimeter_min) + "\n"

    # Finally, given that long string, write it to a file

    file.write(string_to_write)

    # close the file once all writing is complete
    file.close()

    # since we got here, it must have worked.
    return True