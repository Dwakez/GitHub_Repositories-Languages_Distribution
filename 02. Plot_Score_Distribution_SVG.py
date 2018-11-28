""" Plot SVG Graph from CSV """
import pandas as pd
import pygal

def main():
    """ Main Function """
    file_list = ["[Score Distribution] - Mathematics.csv",
                 "[Score Distribution] - Reading.csv",
                 "[Score Distribution] - Science.csv"]

    for data_file in file_list:
        df = pd.read_csv(data_file, index_col="Score Distribution")
        plot_graph(df, data_file.replace(".csv", ""))

    print("Line Chart Sucessfully Created !!")

def plot_graph(df, name):
    """ Plot SVG graph """
    year_list = list(map(str, range(2000, 2016, 3)))
    line_chart = pygal.Line()
    line_chart.title = "Thailand PISA " + name.strip("[]") + " during 2000 - 2015"
    line_chart.x_labels = ["5th Pecentile", "10th Pecentile", "25th Pecentile", "50th Pecentile",
                           "75th Pecentile", "90th Pecentile", "95th Percentile"]
    for i in range(len(year_list)):
        line_chart.add(year_list[i], list(df[year_list[i]]))
    line_chart.render_to_file(name + '.svg')

main()
