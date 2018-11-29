""" Create new CSV from Dataset """
import pandas as pd
import csv
def main():
    """ Main Function """
    # Read Dataset
    df = pd.read_csv("EdStatsDataTH-PISA_only.csv")
    print("Dataset loaded !!")

    # Convert Data to list
    # Mathematics Scores Distribution
    math_pct_list = [df.loc[i].tolist() for i in [26, *range(23, 26), *range(27, 30)]]

    # Reading Scores Distribution
    read_pct_list = [df.loc[i].tolist() for i in [33, *range(30, 33), *range(34, 37)]]

    # Science Scores Distribution
    sci_pct_list = [df.loc[i].tolist() for i in [40, *range(37, 40), *range(41, 44)]]

    print("Sucessfully converted data")

    # Store data in dictionary
    math_dis_data = {}
    read_dis_data = {}
    sci_dis_data = {}

    math_key = [math_pct_list[i][2] for i in range(7)]
    for i in math_key:
        math_dis_data[i] = [math_pct_list[math_key.index(i)][j] for j in range(4, 20, 3)]

    read_key = [read_pct_list[i][2] for i in range(7)]
    for i in read_key:
        read_dis_data[i] = [read_pct_list[read_key.index(i)][j] for j in range(4, 20, 3)]

    sci_key = [read_pct_list[i][2] for i in range(7)]
    for i in sci_key:
        sci_dis_data[i] = [sci_pct_list[sci_key.index(i)][j] for j in range(4, 20, 3)]

    # List of Values in Dictionaries
    math_values_list = list(math_dis_data.values())
    read_values_list = list(read_dis_data.values())
    sci_values_list = list(sci_dis_data.values())
    # Value List
    math_list = [i for i in math_values_list]
    read_list = [i for i in read_values_list]
    sci_list = [i for i in sci_values_list]

    # Create CSV
    create_csv("[Score Distribution] - Mathematics", list(math_dis_data.keys()), math_list)
    create_csv("[Score Distribution] - Reading", list(read_dis_data.keys()), read_list)
    create_csv("[Score Distribution] - Science", list(sci_dis_data.keys()), sci_list)
    print("Sucessfully create CSV !!")

def create_csv(name, key, row_list):
    """ Create New CSV """
    new_file_name = name + ".csv"
    with open(new_file_name, "w", newline="") as new_file_name:
        writer = csv.writer(new_file_name)
        writer.writerow(["Score Distribution"] + list(map(str, range(2000, 2016, 3))))
        for i in range(len(row_list)):
            writer.writerow([(key[i])] + row_list[i])

main()
