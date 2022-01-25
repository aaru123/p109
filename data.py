import random
from cv2 import mean
import plotly.figure_factory as ff
import plotly.express as px
import statistics
import csv
import pandas as pd
import plotly.graph_objects as go

df = pd.read_csv('StudentsPerformance.csv')
data = df['reading score'].tolist()

Mean = statistics.mean(data)
Median = statistics.median(data)
Mode = statistics.mode(data)
sd = statistics.stdev(data)

print(Mean)
print(Median)
print(Mode)
print(sd)

first_sd_start, first_sd_end = Mean-sd, Mean+sd
second_sd_start, second_sd_end = Mean-(2*sd), Mean+(2*sd)
third_sd_start, third_sd_end = Mean-(3*sd), Mean+(3*sd)


list_of_data_within_1_sd = [result for result in data if result > first_sd_start and result < first_sd_end]
print("{}% of data lies within 1 standard deviation", format(len(list_of_data_within_1_sd)*100.0/len(data) ))
s1 = len(list_of_data_within_1_sd)*100.0/len(data) 
list_of_data_within_2_sd = [result for result in data if result > second_sd_start and result < second_sd_end]
print("{}% of data lies within 2 standard deviation", format(len(list_of_data_within_2_sd)*100.0/len(data) ))
s2 = len(list_of_data_within_2_sd)*100.0/len(data)
list_of_data_within_3_sd = [result for result in data if result > third_sd_start and result < third_sd_end]
print("{}% of data lies within 3 standard deviation", format(len(list_of_data_within_3_sd)*100.0/len(data)  ))
s3 =len(list_of_data_within_3_sd)*100.0/len(data)

fig = ff.create_distplot([data],["Reading score"], show_hist= False)
fig.add_trace(go.Scatter(x =[Mean,Mean], y = [0,0.14],mode='lines', name = 'MEAN',))
fig.add_trace(go.Scatter(x =[s1,s1], y = [0,0.14],mode='lines', name = 'standard deviation 1',))
fig.add_trace(go.Scatter(x =[s2,s2,], y = [0,0.14],mode='lines', name = 'standard deviation 2',))
fig.add_trace(go.Scatter(x =[s3,s3,], y = [0,0.14],mode='lines', name = 'standard deviation 3',))
fig.show()