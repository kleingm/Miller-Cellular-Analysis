import scipy.stats
import numpy as np

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

        # try to find start of data
        if splits[0] == "Area Mean":
            begin_reading = True
    file.close()

    return np.asarray(area_parse), np.asarray(perimeter_parse)

def compare_area_means(sample_1, sample_2):
    num_samples = 20  # Edit this Value Based on how many Cell Samples were used to find Mean
    sample1_mean = sample_1[0]
    sample1_stdev = sample_1[1]
    dist1 = np.random.normal(loc=sample1_mean, scale=sample1_stdev, size=num_samples)

    sample2_mean = sample_2[0]
    sample2_stdev = sample_2[1]
    dist2 = np.random.normal(loc=sample2_mean, scale=sample2_stdev, size=num_samples)

    (stat, p_value) = scipy.stats.ttest_ind(dist1, dist2, alternative='two-sided')
    print(stat, p_value)

def compare_perimeter_means(sample_1, sample_2):
    num_samples = 20  # Edit this Value Based on how many Cell Samples were used to find Mean
    sample1_mean = sample_1[0]
    sample1_stdev = sample_1[1]
    dist1 = np.random.normal(loc=sample1_mean, scale=sample1_stdev, size=num_samples)

    sample2_mean = sample_2[0]
    sample2_stdev = sample_2[1]
    dist2 = np.random.normal(loc=sample2_mean, scale=sample2_stdev, size=num_samples)

    (stat, p_value) = scipy.stats.ttest_ind(dist1, dist2, alternative='two-sided')
    print(stat, p_value)

if __name__ == '__main__':
    # Change to reflect which folder ImageJ CSV is stored
    material_folder = "Raw CSV"

    # modify this line to select different samples in the material folder
    sample_name_one = "data_1"

    sample_name_two = "data_2"


    ### Do not modify below this line ###

    path_to_directory = "../Miller-Cellular-Analysis/"
    path_to_samples = path_to_directory

    # Filepath for parsing function
    path_to_file_one = path_to_samples + sample_name_one + ".csv"
    path_to_file_two = path_to_samples + sample_name_two + ".csv"

    # Parse Data to pull Area and Mean data out into Arrays
    (area_one, perimeter_one) = parse_stats_data(path_to_file_one)
    (area_two, perimeter_two) = parse_stats_data(path_to_file_two)

    # Run through Two-Sided T-Test to Compare means, looking for p < 0.5 for significance
    compare_area_means(area_one, area_two)
    compare_perimeter_means(perimeter_one, perimeter_two)

    print("Done!")
