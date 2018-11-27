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
    math_10th_pct = df.loc[23].tolist()
    math_25th_pct = df.loc[24].tolist()
    math_50th_pct = df.loc[25].tolist()
    math_05th_pct = df.loc[26].tolist()
    math_75th_pct = df.loc[27].tolist()
    math_90th_pct = df.loc[28].tolist()
    math_95th_pct = df.loc[29].tolist()

    # Reading Scores Distribution
    read_10th_pct = df.loc[30].tolist()
    read_25th_pct = df.loc[31].tolist()
    read_50th_pct = df.loc[32].tolist()
    read_05th_pct = df.loc[33].tolist()
    read_75th_pct = df.loc[34].tolist()
    read_90th_pct = df.loc[35].tolist()
    read_95th_pct = df.loc[36].tolist()

    # Science Scores Distribution
    sci_10th_pct = df.loc[37].tolist()
    sci_25th_pct = df.loc[38].tolist()
    sci_50th_pct = df.loc[39].tolist()
    sci_05th_pct = df.loc[40].tolist()
    sci_75th_pct = df.loc[41].tolist()
    sci_90th_pct = df.loc[42].tolist()
    sci_95th_pct = df.loc[43].tolist()

    print("Sucessfully converted data")

    # Store data in dictionary
    math_dis_data = {
        math_05th_pct[2]: [math_05th_pct[i] for i in range(4, 20, 3)],
        math_10th_pct[2]: [math_10th_pct[i] for i in range(4, 20, 3)],
        math_25th_pct[2]: [math_25th_pct[i] for i in range(4, 20, 3)],
        math_50th_pct[2]: [math_50th_pct[i] for i in range(4, 20, 3)],
        math_75th_pct[2]: [math_75th_pct[i] for i in range(4, 20, 3)],
        math_90th_pct[2]: [math_90th_pct[i] for i in range(4, 20, 3)],
        math_95th_pct[2]: [math_95th_pct[i] for i in range(4, 20, 3)]
    }

    read_dis_data = {
        read_05th_pct[2]: [read_05th_pct[i] for i in range(4, 20, 3)],
        read_10th_pct[2]: [read_10th_pct[i] for i in range(4, 20, 3)],
        read_25th_pct[2]: [read_25th_pct[i] for i in range(4, 20, 3)],
        read_50th_pct[2]: [read_50th_pct[i] for i in range(4, 20, 3)],
        read_75th_pct[2]: [read_75th_pct[i] for i in range(4, 20, 3)],
        read_90th_pct[2]: [read_90th_pct[i] for i in range(4, 20, 3)],
        read_95th_pct[2]: [read_95th_pct[i] for i in range(4, 20, 3)]
    }

    sci_dis_data = {
        sci_05th_pct[2]: [sci_05th_pct[i] for i in range(4, 20, 3)],
        sci_10th_pct[2]: [sci_10th_pct[i] for i in range(4, 20, 3)],
        sci_25th_pct[2]: [sci_25th_pct[i] for i in range(4, 20, 3)],
        sci_50th_pct[2]: [sci_50th_pct[i] for i in range(4, 20, 3)],
        sci_75th_pct[2]: [sci_75th_pct[i] for i in range(4, 20, 3)],
        sci_90th_pct[2]: [sci_90th_pct[i] for i in range(4, 20, 3)],
        sci_95th_pct[2]: [sci_95th_pct[i] for i in range(4, 20, 3)]
    }

    math_values_list = list(math_dis_data.values())
    read_values_list = list(read_dis_data.values())
    sci_values_list = list(sci_dis_data.values())
    math_list = [[math_values_list[i][j] for i in range(len(math_values_list))] for j in range(6)]
    read_list = [[read_values_list[i][j] for i in range(len(read_values_list))] for j in range(6)]
    sci_list = [[sci_values_list[i][j] for i in range(len(sci_values_list))] for j in range(6)]
    create_csv("Mathematics_Score_Distribution", math_dis_data, math_list)
    create_csv("Reading_Score_Distribution", read_dis_data, read_list)
    create_csv("Science_Score_Distritbution", sci_dis_data, sci_list)

def create_csv(subject, dis_data, row_list):
    """ Create New CSV """
    new_file_name = subject + ".csv"
    with open(new_file_name, "w", newline="") as new_file_name:
        writer = csv.writer(new_file_name)
        writer.writerow(dis_data.keys())
        for i in range(len(row_list)):
            writer.writerow(row_list[i])
    print("Sucessfully create CSV !!")

main()
