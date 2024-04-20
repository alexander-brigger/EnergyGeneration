import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import numpy as np

df = pd.read_csv("generation_data.csv")

def frame1():
    num_types = df.value_counts('ENERGY SOURCE')
    num_types = num_types.drop('Total')
    return num_types

def plot1(frame):
    frame.plot.bar(color = "Yellow")
    plt.xlabel('Energy Types')
    plt.title(('Total Uses of Each Energy Source from 2001-2022'), fontsize = 24)
    plt.ylabel('Number of Occurences')
    plt.yticks(np.arange(0, 100000, step=20000))
    plt.tight_layout()


def frame2():
    year = [2021]
    df21 = df.loc[df['YEAR'].isin(year)]
    return df21.groupby(['STATE']).agg({'GENERATION (Megawatthours)': sum}).drop('US-TOTAL').sort_values(by='GENERATION (Megawatthours)', ascending=False).head(5)


def plot2(frame2):
    frame2.plot.bar(color = "blue")
    plt.xlabel('States')
    plt.title(('Top 5 Energy Producing States in 2021'), fontsize = 24)
    plt.ylabel('Megawatt Hours Produced (MwH)')
    plt.legend().remove()

    
def frame3():
    graph3 = df.loc[:,["YEAR", "ENERGY SOURCE", "GENERATION (Megawatthours)"]]
    ff = ["Coal", "Natural Gas", "Petroleum"]
    rslt_df = graph3.loc[df['ENERGY SOURCE'].isin(ff)]
    result = rslt_df.groupby(['YEAR']).agg({'GENERATION (Megawatthours)': sum}).drop(2022)
    return result


def plot3():
    years = np.array(range(2001,2022))
    frame_run = frame3()
    production = np.array(frame_run["GENERATION (Megawatthours)"])
    plt.scatter(years, production, label = 'Total Generation Per Year', color="green")
    plt.ylabel("Fossil Fuel Usage in Megawatt Hours (MwH)")
    plt.xlabel("Year")
    plt.title(("Total Power Production Of Fossil Fuels Each Year"), fontsize = 24)
    plt.xticks(np.arange(2001, 20021, step=2))
    a, b = np.polyfit(years, production, 1)
    plt.plot(years, a*years+b, color= "red")        


def main():
    graph_frame = frame1()
    plot1(graph_frame)
    plt.show()

    graph_frame2 = frame2()
    plot2(graph_frame2)
    plt.show()

    plot3()
    plt.show()
if __name__ == "__main__":
    main()


