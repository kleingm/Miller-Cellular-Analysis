# These are all the packages needed for the code to run
# No need to mess with these
from scipy import stats
import numpy as np
import matplotlib.pyplot as plt
import os
import sys
import tkinter as tk
from tkinter.filedialog import askopenfilename


def parse_stats_data(path_to_file):
    """
    Reads through selected CSV data file and returns relevant data for statistical analysis
    :param path_to_file: Path to the file in Project
    :return: Area Data, Perimeter Data
    """
    file = open(path_to_file)

    area_parse = []
    perimeter_parse = []
    # determine when to begin reading into these files
    begin_reading = False
    num_samples = []

    # begin iterating through file
    for line in file:
        if line == '' or line == '\n':
            continue

        splits = line.strip().split(",")

        if begin_reading:
            # parse the actual data
            area_parse.append(float(splits[0].replace('\"', '')))
            area_parse.append(float(splits[1].replace('\"', '')))
            area_parse.append(float(splits[2].replace('\"', '')))
            area_parse.append(float(splits[3].replace('\"', '')))
            perimeter_parse.append(float(splits[4].replace('\"', '')))
            perimeter_parse.append(float(splits[5].replace('\"', '')))
            perimeter_parse.append(float(splits[6].replace('\"', '')))
            perimeter_parse.append(float(splits[7].replace('\"', '')))
            num_samples.append(float(splits[8].replace('\"', '')))

        # try to find start of data
        if splits[0] == "Area Mean":
            begin_reading = True
    file.close()

    return np.asarray(area_parse), np.asarray(perimeter_parse), np.array(num_samples)


def compare_area_means(sample_1, sample_2, num_1, num_2):

    # Pulling relevant data from arrays of first sample
    num1_samples = num_1
    sample1_mean = sample_1[0]
    sample1_deviation = sample_1[1]

    # Pulling relevant data from arrays of second sample
    num2_samples = num_2
    sample2_mean = sample_2[0]
    sample2_deviation = sample_2[1]

    # This is the t-test run on the stats given from the .csv files
    (stat, p_value) = stats.ttest_ind_from_stats(sample1_mean, np.sqrt(sample1_deviation), num1_samples,
                                                 sample2_mean, np.sqrt(sample2_deviation), num2_samples,
                                                 equal_var=False)
    print("The p values for the areas is " + str(p_value))

    return p_value


def compare_perimeter_means(sample_1, sample_2, num_1, num_2):

    # Pulling relevant data from arrays of first sample
    num1_samples = num_1
    sample1_mean = sample_1[0]
    sample1_deviation = sample_1[1]

    # Pulling relevant data from arrays of second sample
    num2_samples = num_2
    sample2_mean = sample_2[0]
    sample2_deviation = sample_2[1]

    # This is the t-test run on the stats given from the .csv files
    (stat, p_value) = stats.ttest_ind_from_stats(sample1_mean, np.sqrt(sample1_deviation), num1_samples,
                                                 sample2_mean, np.sqrt(sample2_deviation), num2_samples,
                                                 equal_var=False)
    print("The p-value for the perimeters is " + str(p_value))

    return p_value

# This is the actual runtime code


if __name__ == '__main__':

    tk.Tk().withdraw()  # we don't want a full GUI, so keep the root window from appearing
    filename_one = askopenfilename()  # show an "Open" dialog box and return the path to the selected file

    # Exit Condition if no file Chosen
    if filename_one == '':
        sys.exit('First Input File was not Chosen. Please Choose a File to Import.')

    tk.Tk().withdraw()  # we don't want a full GUI, so keep the root window from appearing
    filename_two = askopenfilename()  # show an "Open" dialog box and return the path to the selected file

    # Exit Condition if no file Chosen
    if filename_two == '':
        sys.exit('Second Input File was not Chosen. Please Choose a File to Import.')

    sample_name_a = os.path.basename(filename_one)
    sample_name_b = os.path.basename(filename_two)
    sample_name_one = sample_name_a.replace(".csv", "")
    sample_name_two = sample_name_b.replace(".csv", "")

    # Check if file exists, close if not
    exist_one = os.path.exists(filename_one)
    if not exist_one:
        sys.exit(filename_one + " does not exist.")

    exist_two = os.path.exists(filename_two)
    if not exist_two:
        sys.exit(filename_two + " does not exist.")

    # Parse Data to pull Area and Mean data out into Arrays
    (area_one, perimeter_one, num_samples_one) = parse_stats_data(filename_one)
    (area_two, perimeter_two, num_samples_two) = parse_stats_data(filename_two)

    # Run through Two-Sided T-Test to Compare means, looking for p < 0.05 for significance
    area_p = compare_area_means(area_one, area_two, int(num_samples_one[0]), int(num_samples_two[0]))
    perimeter_p = compare_perimeter_means(perimeter_one, perimeter_two,
                                          int(num_samples_one[0]), int(num_samples_two[0]))

    # Plot for the two areas
    fig, ax = plt.subplots()
    ax.bar([sample_name_one, sample_name_two], [area_one[0], area_two[0]], yerr=[area_one[1], area_two[1]],
           align='center', alpha=0.5, ecolor='black', capsize=10)
    ax.set_ylabel('Mean Cell Area (units)')
    ax.set_xticks([sample_name_one, sample_name_two])
    ax.set_xticklabels([sample_name_one, sample_name_two])
    ax.set_title('Two-Sided t-test of the Areas of ' + sample_name_one + ' and ' + sample_name_two)
    ax.yaxis.grid(True)
    if area_p < 0.05:
        ax.annotate('*', xy=(0.5, 0.90), xytext=(0.5, .92), xycoords='axes fraction',
                    fontsize=10 * 1.5, ha='center', va='bottom',
                    arrowprops=dict(arrowstyle='-[, widthB=4.0, lengthB=1', lw=2.0))

    plt.tight_layout()
    plt.show()

    # Plot for the two perimeters
    fig_2, ax = plt.subplots()
    ax.bar([sample_name_one, sample_name_two], [perimeter_one[0], perimeter_two[0]],
           yerr=[perimeter_one[1], perimeter_two[1]], align='center', alpha=0.5, ecolor='black', capsize=10)
    ax.set_ylabel('Mean Cell Perimeter (units)')
    ax.set_xticks([sample_name_one, sample_name_two])
    ax.set_xticklabels([sample_name_one, sample_name_two])
    ax.set_title('Two-Sided t-test of the Perimeters of ' + sample_name_one + ' and ' + sample_name_two)
    ax.yaxis.grid(True)
    if perimeter_p < 0.05:
        ax.annotate('*', xy=(0.5, 0.90), xytext=(0.5, .92), xycoords='axes fraction',
                    fontsize=10 * 1.5, ha='center', va='bottom',
                    arrowprops=dict(arrowstyle='-[, widthB=4.0, lengthB=1', lw=2.0))

    plt.tight_layout()
    plt.show()

    print("Done!")
