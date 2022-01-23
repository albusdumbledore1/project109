import pandas as pd 
import statistics

df = pd.read_csv("StudentsPerformance.csv")
math=df ["math score"].tolist()
import plotly.figure_factory as fg
fig = fg.create_distplot([df["math score"].to_list()],["math score"],show_hist=False)

mean = statistics.mean(math)
median = statistics.median(math)
mode = statistics.mode(math)
print(mean,median,mode)

stdev = statistics.stdev(math)
print(stdev)
stdev_1_start = mean - stdev
stdev_1_end = mean + stdev
stdev_2_start = mean - (2*stdev)
stdev_2_end = mean + (2*stdev)
stdev_3_start = mean - (3*stdev)
stdev_3_end = mean + (3*stdev)
#fig.show()
data_within_1sd = [result for result in math if result>stdev_1_start and result<stdev_1_end]
data_within_2sd = [result for result in math if result>stdev_2_start and result<stdev_2_end]
data_within_3sd = [result for result in math if result>stdev_3_start and result<stdev_3_end]

percent_data_within_1sd = (len(data_within_1sd)/len(math))*100
percent_data_within_2sd = (len(data_within_2sd)/len(math))*100
percent_data_within_3sd = (len(data_within_3sd)/len(math))*100
print(percent_data_within_1sd)
print(percent_data_within_2sd)
print(percent_data_within_3sd)