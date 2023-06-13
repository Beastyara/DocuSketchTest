import pandas as pd
from pandas.api.types import is_numeric_dtype
import matplotlib.pyplot as plt
def draw_plots(f):
    df = pd.DataFrame.from_dict(f) #convert python dictionary to Dataframe
    numcols = [] 
    for colname in list(df.columns): #check is column numerical
        if is_numeric_dtype(df[colname]) == True:
            numcols.append(colname) #add to list if column is numerical
    plotpaths = []
    for i in range(len(numcols)):
        for j in range(i+1, len(numcols)):
            plt.scatter(df[numcols[i]], df[numcols[j]])
            plotname = numcols[i] + ' VS ' + numcols[j]
            plt.xlabel(numcols[i])
            plt.ylabel(numcols[j])
            plt.title(plotname)
            plotpath = 'plots/' + numcols[i] + 'VS' + numcols[j] + '.png'
            plt.savefig(plotpath) #create and save the plot
            plt.clf()
            plotpaths.append(plotpath) #add the path to the plot in the list
    return plotpaths #return list with all paths to the plots 
    
