# Step 1: Install matplotlib and numpy
# Open your terminal and run:
# pip install matplotlib numpy

# Step 2: Import necessary libraries
import matplotlib.pyplot as plt
import numpy as np

# Step 3: Define key events in AI history with a flag for breakthroughs (1) and setbacks (-1)
events = [
    ("1950", "Turing Test", 1),
    ("1956", "Dartmouth Conference", 1),
    ("1966", "ELIZA", 1),
    ("1970", "Shakey the Robot", 1),
    ("1974", "First AI Winter", -1),
    ("1980", "Expert Systems", 1),
    ("1987", "Second AI Winter", -1),
    ("1997", "Deep Blue vs. Kasparov", 1),
    ("2011", "IBM Watson wins Jeopardy", 1),
    ("2012", "AlexNet wins ImageNet", 1),
    ("2016", "AlphaGo vs. Lee Sedol", 1),
    ("2020", "GPT-3 released", 1)
]

# Step 4: Extract dates, event descriptions, and flags
dates, descriptions, flags = zip(*events)

# Convert dates to numerical values for plotting
years = np.array([int(date) for date in dates])
popularity = np.array(flags)

# Create a smooth line using interpolation
smooth_years = np.linspace(years.min(), years.max(), 300)
smooth_popularity = np.interp(smooth_years, years, popularity)

# Step 5: Plot the timeline
plt.figure(figsize=(12, 6))
plt.plot(years, popularity, "ro")  # Plot points
plt.plot(smooth_years, smooth_popularity, "b-", label="Popularity Trend")  # Plot smooth line
plt.ylim(-2, 2)

# Annotate each event
for i, (date, description, flag) in enumerate(events):
    plt.text(int(date), flag + 0.1 if flag == 1 else flag - 0.3, description, rotation=45, ha='right')

# Add title and labels
plt.title("Key Events in the History of Artificial Intelligence")
plt.xlabel("Year")
plt.ylabel("Event Type")
plt.yticks([-1, 1], ["Setback", "Breakthrough"])
plt.legend()

# Show the plot
plt.show()