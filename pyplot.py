import random
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import plotly.express as px
from plotly import graph_objects

# # Ugly ass hell
# plt.style.use('Solarize_Light2')

# Check for all available family/fontname
"""
fonts = sorted(set(f.name for f in fm.fontManager.ttflist))

for font in fonts[:20]:
    print(font)
"""

# Numpy array are faster and have more feature than python list
years = np.array([2019, 2020, 2021, 2022, 2023, 2024, 2025, 2026])
student_count_at_U1 = np.array([45, 60, 95, 43, 250, 20, 580, 15])
student_count_at_U2 = np.array([23, 33, 49, 22, 174, 90, 467, 13])
student_count_at_U3 = np.array([289, 424, 559, 220, 5, 343, 109, 97])

# Plot customization
"""
# Create a blueprint instead of manually set each parameter
line_style = dict(marker='.',
                  markersize=20,
                  markerfacecolor='#FFC514',
                  mec='#323ca8',
                  linestyle='-',
                  lw=2)

# Plot each graph on the same figure
plt.plot(years, student_count_at_U1, color='#1f77b4', **line_style)
plt.plot(years, student_count_at_U2, color='#279DFF', **line_style)
plt.plot(years, student_count_at_U3, color='#F778FF', **line_style)
plt.legend(["U1", "U2", "U3"], loc="upper right")
plt.show()
"""

# Labels
"""
plt.plot(years, student_count_at_U1)
plt.plot(years, student_count_at_U2)
plt.plot(years, student_count_at_U3)

# Set title, x label, and y label
plt.title("Class size", fontsize=25, family="Arial", fontweight="book", color="#FF000C")
plt.xlabel("Year", fontsize=15, weight="bold", color='#24A1FF')
plt.ylabel("Students", fontsize=15, weight="bold", color='#24A1FF')

# Set ticks properties
plt.tick_params(axis="both", colors="#3BB757", labelsize=12)

plt.show()
"""

# Grid (help make plots easier to read by adding reference lines)
"""
x = np.array([1, 2, 3, 4, 5])
y = np.array([10, 60, 23, 12, 59])

plt.grid(axis='y', linewidth=2, color="lightgray", linestyle='--')

plt.plot(x, y)
plt.xticks(x)
plt.show()
"""

# Bar chart (compare categories of data by representing each category with a bar)
"""
bar_color = [random.choice(['red', 'yellow', 'green', 'blue']) for _ in range(6)]

# List of string doesn't benefit from numpy array
categories = ["Grains", "Fruit", "Vegetables", "Protein", "Dairy", "Sweets"]
values = np.array([4, 3, 2, 5, 3, 1])

plt.bar(categories, values, color="darkgray", edgecolor="black")

plt.title("Daily Consumption")
plt.xlabel("Food")
plt.ylabel("Quantity")

plt.show()
"""

# Pie chart (circular chart divided into slices to show percentages of the total. Best for visualizing distribution among categories)
"""
categories = ["Freshman", "Sophomores", "Juniors", "Seniors"]
values = np.array([300, 250, 275, 225 ])
colors = ["red", "yellow", "blue", "green"]

plt.pie(values, labels=categories, autopct="%1.1f%%", colors=colors, explode=[0, 0, 0, 0.1], shadow=True, startangle=90)

plt.title("Saint Marry")

plt.show()
"""

# Scatter graph (shows the relationship between two variables. Helps to identify a correlation (+, -, None). Example: Study hours vs Test scores)
"""
x1 = np.array([0, 1, 1, 2, 3, 4, 5, 6, 7, 7, 8])  # Hours studied
y1 = np.array([55, 60, 65, 62,  68,  70, 75, 78, 82, 85, 87]) # Grade

x2 = np.array([0, 1, 2, 2, 3, 4, 5, 6, 7, 8, 8])  # Hours studied
y2 = np.array([50, 58, 65,  70, 72, 78, 83,  88, 92,  95, 97]) # Grade

plt.scatter(x1, y1, color="darkgray", alpha=0.8, s=100, label="Class A")
plt.scatter(x2, y2, color="#660000", alpha=0.5, s=100, label="Class B")

plt.title("Test scores", fontsize=25, color="darkred", fontname="Garamond")
plt.xlabel("Hours studied", size=15, color="royalblue")
plt.ylabel("Grade", size=15, color="royalblue")

plt.legend(loc="best")
plt.show()
"""

# Histogram (a visual representation of the distribution of quantitative data. They group values into bins (intervals) and count how many falls in each range)
"""
scores = np.random.normal(loc=80, scale=10, size=100)
scores = np.clip(scores, 0,  100)

plt.hist(scores, bins=10, color="lightgreen", edgecolor="black")
plt.title("Exam Scores")
plt.xlabel("Score")
plt.ylabel("# of students")

plt.show()
"""

# Subplots (figure = the entire canvas 🖼️, ax = a single plot (subplot) 📉)
"""
x = np.array([1, 2, 3, 4, 5])

figure, axes = plt.subplots(2, 2)

axes[0, 0].plot(x, x*2, color='red', ls='None', marker='.', ms=10)
axes[0, 0].set_title("x*2")

axes[0, 1].plot(x, x**2, color="darkred")
axes[0, 1].set_title("x**2")

axes[1, 0].bar(x, np.sqrt(x), color="skyblue", edgecolor='black')
axes[1, 0].set_title("square")

axes[1, 1].scatter(x, 2**x, color="lightgreen", edgecolor='black')
axes[1, 1].set_title("exp")

plt.suptitle("Four Plots", size=20, family='Garamond')
plt.tight_layout()

plt.savefig("Example.png", dpi=300, transparent=False)
plt.show()
"""

# Pandas + Matplotlib
"""
# data frame as df, open csv file using read_csv function
df = pd.read_csv("pokemon.csv")

type_count = df["Type1"].value_counts(ascending=True)

plt.barh(type_count.index, type_count.values, color="lightgreen", edgecolor='black')

plt.title("# of Pokemon by Primary Type")
plt.xlabel("Count")
plt.ylabel("Type")

plt.tight_layout()
plt.show()

"""

# 3d plotting
"""
# Need to use external tools
import matplotlib
matplotlib.use("QtAgg")
import matplotlib.pyplot as plt

ax = plt.axes(projection="3d")

t = np.arange(0, 50, 0.1)
x, y, z = (np.arange(0, 50, 0.1),
           np.cos(t),
           np.sin(t+t))

ax.plot(x, y, z, color="purple", linewidth=1.5)
ax.set_title("3d Plot (Interactive) (Lissajous Tube)")

plt.show()

# Or if laggy, open in browser
fig = px.line_3d(x=x,y=y, z=z, title="Smooth WebGL 3D Plot (Lissajous Tube)")
fig.update_traces(line=dict(width=6))
fig.write_html("plot.html", auto_open=True) # Can also use fig.show(renderer="browser") but html name is random
"""

# 3d meshgrid
"""
x = np.arange(-5, 5, 0.1)
y = np.arange(-5, 5, 0.1)

# Build 2D Mesh Grids
X, Y = np.meshgrid(x, y)

# Calculate Z values for every (X, Y) coordinate pair
z = np.sin(X) * np.cos(Y)

# Render 3D Surface Grid
fig = graph_objects.Figure(data=[graph_objects.Surface(x=x, y=y, z=z, colorscale="Viridis")])

# Optional: Display wireframe/mesh grid lines over the surface
fig.update_traces(contours_z=dict(show=True, highlightcolor="limegreen", project_z=False))

# Open in browser
fig.write_html("3d_Mesh.html", auto_open=True)
"""

# Animation (This one is advance, Gemini generated)
"""
import matplotlib

matplotlib.use("QtAgg")  # Hardware accelerated window
import matplotlib.animation as animation
import matplotlib.pyplot as plt

# 1. Setup Data & Canvas
total_flips = 100_000
batch_size = 500  # Number of flips processed per frame
num_frames = total_flips // batch_size

heads_tails = [0, 0]

fig, ax = plt.subplots()
bars = ax.bar(["Heads", "Tails"], heads_tails, color=["blue", "yellow"])
ax.set_ylim(0, 60000)
title_text = ax.set_title("Flips: 0")


# 2. Define Update Function for Animation
def update(frame):
  # Perform batch flips using fast NumPy vectorization
  flips = np.random.randint(0, 2, size=batch_size)
  heads_tails[0] += np.count_nonzero(flips == 0)
  heads_tails[1] += np.count_nonzero(flips == 1)

  # Update bar heights
  bars[0].set_height(heads_tails[0])
  bars[1].set_height(heads_tails[1])

  # Update title counter
  current_flips = (frame + 1) * batch_size
  title_text.set_text(f"Flips: {current_flips:,}")

  # Return modified artists for blitting
  return bars[0], bars[1], title_text


# 3. Create Animation Object
# interval = delay between frames in milliseconds (20ms = 50 FPS target)
anim = animation.FuncAnimation(
    fig,
    update,
    frames=num_frames,
    interval=20,
    blit=True,  # Redraws ONLY modified elements (super fast)
    repeat=False,
)

plt.show()
"""
