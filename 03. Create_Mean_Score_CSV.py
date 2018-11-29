""" Create new CSV from Dataset """
import pandas as pd
import csv
def main():
    """ Main Function """
    # Read Dataset
    df = pd.read_csv("EdStatsDataTH-PISA_only.csv")
    print("Dataset loaded !!")

    # Convert Data to list
    # Mathematics Mean Score
    math_mean_list = [df.loc[i].tolist() for i in range(90, 93)]

    # Reading Mean Score
    read_mean_list = [df.loc[i].tolist() for i in range(93, 96)]

    # Science Mean Score
    sci_mean_list = [df.loc[i].tolist() for i in range(96, 99)]

    print("Sucessfully converted data")

    # Store data in dictionary
    math_mean_data = {}
    read_mean_data = {}
    sci_mean_data = {}

    math_key = [math_mean_list[i][2] for i in range(3)]
    for i in math_key:
        math_mean_data[i + ". Both" if math_key.index(i) == 0 else i] = [math_mean_list[math_key.index(i)][j] for j in range(4, 20, 3)]

    read_key = [read_mean_list[i][2] for i in range(3)]
    for i in read_key:
        read_mean_data[i + ". Both" if read_key.index(i) == 0 else i] = [read_mean_list[read_key.index(i)][j] for j in range(4, 20, 3)]

    sci_key = [sci_mean_list[i][2] for i in range(3)]
    for i in sci_key:
        sci_mean_data[i + ". Both" if sci_key.index(i) == 0 else i] = [sci_mean_list[sci_key.index(i)][j] for j in range(4, 20, 3)]

    # List of Values in Dictionaries
    math_values_list = list(math_mean_data.values())
    read_values_list = list(read_mean_data.values())
    sci_values_list = list(sci_mean_data.values())
    # Value List
    math_list = [i for i in math_values_list]
    read_list = [i for i in read_values_list]
    sci_list = [i for i in sci_values_list]

    # Create CSV
    create_csv("[Mean Score] - Mathematics", list(math_mean_data.keys()), math_mean_data, math_list)
    create_csv("[Mean Score] - Reading", list(read_mean_data.keys()), read_mean_data, read_list)
    create_csv("[Mean Score] - Science", list(sci_mean_data.keys()), sci_mean_data, sci_list)
    print("Sucessfully create CSV !!")

def create_csv(subject, key, dis_data, row_list):
    """ Create New CSV """
    new_file_name = subject + ".csv"
    with open(new_file_name, "w", newline="") as new_file_name:
        writer = csv.writer(new_file_name)
        writer.writerow(["Mean Score"] + list(map(str, range(2000, 2016, 3))))
        for i in range(len(row_list)):
            writer.writerow([(key[i])] + row_list[i])

main()
