import pandas as pd
import matplotlib.pyplot as plt
# Read the CSV file
df = pd.read_csv('movies.csv')
# Count the occurrences of each genre
genre_counts = df['genre'].value_counts()
# Plotting
plt.pie(genre_counts.values, labels=genre_counts.index, autopct='%1.1f%%') # Create a pie chart with genre counts 
plt.title('Most Liked Genre') # Set the title of the plot
plt.axis('equal') # Equal aspect ratio ensures that the pie is drawn as a circle
plt.show() # Display the plot
