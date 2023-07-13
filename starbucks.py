import pandas as pd
import matplotlib.pyplot as plt
# Read the CSV file
df = pd.read_csv('Netflix_Revenue.csv')
# Extract the data from the columns and put them into the dataframe
dates = df['Date'] # Extract the 'Data' column as the x-axis data
global_trials = df['Global Trials'] # Extract the 'Global Trials' column as the y-axis data
actual_members = df['Actual Members'] # Extract the 'Actual Members' column as the y-axis data
# Plotting
plt.plot(dates, global_trials, label='Global Trials') # Plot the 'Global Trials' data as a line
plt.plot(dates, actual_members, label='Global Trials') # Plot the 'Actual Members' data as a line
plt.xlabel('Date') # Set the x-axis label
plt.ylabel('Number of Trials / Members') # Set the y-axis label
plt.title('Global Trials vs. Actual Members') # Set the title of the plot
plt.legend() # Display the legend to distinguish the lines
plt.xticks(rotation=45) # Rotate the x-axis tick labels by 45 degrees for better readability
plt.show() # Show the plot
