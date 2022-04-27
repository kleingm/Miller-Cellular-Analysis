import scipy.stats
import numpy as np

def parse_stats_data(path_to_file):
    file = open(path_to_file)

    # Would need to extract data from generated csv, should only be second line?

    return

def compare_means(sample_1, sample_2):
    num_samples = 0
    sample1_mean = sample_1[1]
    sample1_stdev = sample_1[2]
    dist1 = np.random.normal(loc=sample1_mean, scale=sample1_stdev, size=num_samples)

    sample2_mean = sample_2[1]
    sample2_stdev = sample_2[2]
    dist2 = np.random.normal(loc=sample2_mean, scale=sample2_stdev, size=num_samples)

    (stat, p_value) = scipy.stats.ttest_ind(dist1, dist2, alternative='two-sided')
    print(stat, p_value)

if __name__ == '__main__':

    # Some stuff would go here to load csv
    path_to_folder = "/Data/"

    file_name = 'Results'

    # File path to open
    path_to_file = path_to_folder + file_name + ".csv"

    array = parse_stats_data(path_to_file)

    # Maybe need to open two files at once for comparison?
