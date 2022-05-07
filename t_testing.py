import scipy.stats
import numpy as np
import matplotlib.pyplot as plt

def parse_stats_data(path_to_file):
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
    num_samples = []

    # begin iterating through file
    for line in file:
        if line == '' or line == '\n':
            continue

        splits = line.strip().split(",")

        if begin_reading == True:
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

def compare_area_means(sample_1, sample_2, num):
    num_samples = num
    sample1_mean = sample_1[0]
    sample1_stdev = sample_1[1]
    dist1 = np.random.normal(loc=sample1_mean, scale=sample1_stdev, size=num_samples)

    sample2_mean = sample_2[0]
    sample2_stdev = sample_2[1]
    dist2 = np.random.normal(loc=sample2_mean, scale=sample2_stdev, size=num_samples)

    (stat, p_value) = scipy.stats.ttest_ind(dist1, dist2, alternative='two-sided')
    print("The p values for the areas is " + p_value)

    return p_value

def compare_perimeter_means(sample_1, sample_2, num):
    num_samples = num
    sample1_mean = sample_1[0]
    sample1_stdev = sample_1[1]
    dist1 = np.random.normal(loc=sample1_mean, scale=sample1_stdev, size=num_samples)

    sample2_mean = sample_2[0]
    sample2_stdev = sample_2[1]
    dist2 = np.random.normal(loc=sample2_mean, scale=sample2_stdev, size=num_samples)

    (stat, p_value) = scipy.stats.ttest_ind(dist1, dist2, alternative='two-sided')
    print("The p-value for the perimeters is" + p_value)

    return p_value

if __name__ == '__main__':
    # Change to reflect which folder ImageJ CSV is stored
    # Change to reflect which folder ImageJ CSV is stored
    data_folder = "Processed Data"

    # modify this line to select different samples in the material folder
    sample_name_one = "Miller_Processed"
    sample_name_two = "vash_Processed"

    ### Do not modify below this line ###

    path_to_directory = "./Data/"
    path_to_samples = path_to_directory + data_folder + "/"

    # Filepath for parsing function
    path_to_file_one = path_to_samples + sample_name_one + ".csv"
    path_to_file_two = path_to_samples + sample_name_two + ".csv"

    # Parse Data to pull Area and Mean data out into Arrays
    (area_one, perimeter_one, num_samples_one) = parse_stats_data(path_to_file_one)
    (area_two, perimeter_two, num_samples_two) = parse_stats_data(path_to_file_two)

    # Run through Two-Sided T-Test to Compare means, looking for p < 0.05 for significance
    area_p = compare_area_means(area_one, area_two, min(int(num_samples_one[0]), int(num_samples_two[0])))
    perimeter_p = compare_perimeter_means(perimeter_one, perimeter_two,
                                          min(int(num_samples_one[0]), int(num_samples_two[0])))
    area_fake = 0.005

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
    ax.set_title('Two-Sided t-test of the Perimeters ' + sample_name_one + ' and ' + sample_name_two)
    ax.yaxis.grid(True)
    if perimeter_p < 0.05:
        ax.annotate('*', xy=(0.5, 0.90), xytext=(0.5, .92), xycoords='axes fraction',
                fontsize=10 * 1.5, ha='center', va='bottom',
                arrowprops=dict(arrowstyle='-[, widthB=4.0, lengthB=1', lw=2.0))

    plt.tight_layout()
    plt.show()

    print("Done!")
