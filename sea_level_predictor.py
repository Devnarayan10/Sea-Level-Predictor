import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv(r"SeaLevelPredictor\epa-sea-level.csv")

    # Create scatter plot
    plt.scatter(df['Year'],df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit
    fline = linregress(df['Year'],df['CSIRO Adjusted Sea Level'])
    plt.plot(range(1880,2051,1),fline.slope*range(1880,2051,1)+fline.intercept)

    # Create second line of best fit
    sline = linregress(df.query('Year >= 2000')['Year'],df.query('Year >= 2000')['CSIRO Adjusted Sea Level'])
    plt.plot(range(2000,2051,1),sline.slope*range(2000,2051,1)+sline.intercept)

    # Add labels and title
    plt.title('Rise in Sea Level')
    plt.ylabel('Sea Level (inches)')
    plt.xlabel('Year')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()