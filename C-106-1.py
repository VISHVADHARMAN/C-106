import plotly.express as px
import csv

with open("D:/C-106/cups of coffee vs hours of sleep.csv") as csv_file:
    df=csv.DictReader(csv_file)
    fig=px.scatter(df,x="week",y="Coffee in ml")
    fig.show()