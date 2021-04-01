import plotly.express as px
import csv

with open("D:/C-106/Ice Cream Sale vs Temperature data.csv") as csv_file:
    df=csv.DictReader(csv_file)
    fig=px.scatter(df,x="Temperature",y="Ice-cream Sales( â‚¹ )")
    fig.show()