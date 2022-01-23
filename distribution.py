import pandas as pd 
import statistics

df = pd.read_csv("data.csv")
height=df ["Height(Inches)"].tolist()
import plotly.figure_factory as fg
fig = fg.create_distplot([df["Height(Inches)"].to_list()],["height"],show_hist=False)

mean = statistics.mean(height)
median = statistics.median(height)
mode = statistics.mode(height)
print(mean,median,mode)

stdev = statistics.stdev(height)
print(stdev)
stdev_1_start = mean - stdev
stdev_1_end = mean + stdev
stdev_2_start = mean - (2*stdev)
stdev_2_end = mean + (2*stdev)
stdev_3_start = mean - (3*stdev)
stdev_3_end = mean + (3*stdev)
#fig.show()
data_within_1sd = [result for result in height if result>stdev_1_start and result<stdev_1_end]
data_within_2sd = [result for result in height if result>stdev_2_start and result<stdev_2_end]
data_within_3sd = [result for result in height if result>stdev_3_start and result<stdev_3_end]

percent_data_within_1sd = (len(data_within_1sd)/len(height))*100
percent_data_within_2sd = (len(data_within_2sd)/len(height))*100
percent_data_within_3sd = (len(data_within_3sd)/len(height))*100
print(percent_data_within_1sd)
print(percent_data_within_2sd)
print(percent_data_within_3sd)