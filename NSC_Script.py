import pandas as pd

#This line loads the csv into a pandas data frame, you'll have to change it to the location of your NSC file
data = pd.read_csv("C:/Users/rjlopez/Desktop/EVC Tracker.csv")


#formatting the dates columns to proper date format, some interpreters will change these columns to a number if we don't format the columns
data['Enrollment Begin'] = pd.to_datetime(data['Enrollment Begin'], format='%Y%m%d')
data['Enrollment End'] = pd.to_datetime(data['Enrollment End'], format='%Y%m%d')
data['Graduation Date'] = pd.to_datetime(data['Graduation Date'], format='%Y%m%d')

#Grouping all the records by student ID and college
#Change all instances of 'Requester Return Field' to 'Your Unique Identifier' if student IDs are in the 'Your Unique Identifies' column
group = data.groupby(['Requester Return Field', 'College Code/Branch'], as_index=False)

#Finding the earliest and latest enrollment date at each college
groupmin = group['Enrollment Begin'].min()
groupmax= group['Enrollment End'].max()

#Renaming the columns
groupmin = groupmin.rename( columns={"Enrollment Begin": "Earliest Enrollment"})
groupmax = groupmax.rename( columns={"Enrollment End": "Latest Enrollment"})

#Joining the earliest and latest enrollment date at each institution
test = pd.merge(data, groupmin, how = 'left', on = ['Requester Return Field', 'College Code/Branch'])

test = pd.merge(test, groupmax, how = 'left', on = ['Requester Return Field', 'College Code/Branch'])

#Selecting all the graduation records and dropping duplicate columns
grads = data.loc[data['Graduated?'] =='Y']

grads = grads[['Requester Return Field', 'College Code/Branch', 'Graduated?', 'Graduation Date', 'Degree Title', 'Degree Major 1', 'Degree CIP 1']]

test = test.drop(['Enrollment Begin', 'Enrollment End', 'Graduated?', 'Graduation Date', 'Degree Title', 'Degree Major 1', 'Degree CIP 1'], axis = 1)

#Joining the graduation records to the main dataset
test = pd.merge(test, grads, how = 'left', on = ['Requester Return Field', 'College Code/Branch'])

#Dropping duplicate records
final_df = test.drop_duplicates(['Requester Return Field', 'College Code/Branch'], keep='first')


#This line exports your dataframe to a csv. Change this part to name the file and the location you want the file to be placed in.
final_df.to_csv("C:/Users/rjlopez/Desktop/Evergreen Valley Tracker File.csv")
