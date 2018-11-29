""" Plot SVG Graph from CSV """
import pandas as pd
import pygal

def main():
    """ Main Function """
    file_list = ["[Mean Score] - Mathematics.csv",
                 "[Mean Score] - Reading.csv",
                 "[Mean Score] - Science.csv"]

    for data_file in file_list:
        df = pd.read_csv(data_file, index_col="Mean Score")
        plot_graph(df, data_file.replace(".csv", ""))

    print("Line Chart Sucessfully Created !!")

def plot_graph(df, name):
    """ Plot SVG graph """
    year_list = list(map(str, range(2000, 2016, 3)))
    line_chart = pygal.Line()
    line_chart.title = "Thailand PISA " + name.lstrip("[").replace("]", "") + " during 2000 - 2015"
    line_chart.x_labels = ["Both", "Female", "Male"]
    for i in range(len(year_list)):
        line_chart.add(year_list[i], list(df[year_list[i]]))
    line_chart.render_to_file(name + '.svg')

main()
