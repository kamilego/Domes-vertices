import matplotlib.pyplot as plt
import numpy as np
import domes_vertices as dv


# function that zips two lists of values and their units to show in top of the bar
def top_bar_value(res, unit):
    for rect, unit_val in zip(res, unit):
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width() / 2., height + 50, '%d %s' % (height, unit_val), ha='center', va='bottom')


# names of main labels
labels = ["Kopuła Żebrowa", "Kopuła Schwedlera", "Kopuła Lamella zakrzywiona"]
# values used in bar charts
displacement = [47.277, 44.707, 46.032]
forces = [948.5, 876.4, 869.0]
num_of_elem = [dv.dome_1_length, dv.dome_2_length, dv.dome_3_length]

# setting number of elements of certain data
bar_x_position = np.arange(len(labels))
width = 0.15

# creating chart with bars
fig, ax = plt.subplots()
res1 = ax.bar(bar_x_position - width, displacement, width, label=labels[0])
res2 = ax.bar(bar_x_position, forces, width, label=labels[1])
res3 = ax.bar(bar_x_position + width, num_of_elem, width, label=labels[2])

# setting descriptions for x, y labels, offsets and legend info
ax.set_xlabel("Rodzaj kopuły", labelpad=20, fontsize=14)
ax.set_ylabel("Wartości", labelpad=30, fontsize=14).set_rotation(0)
ax.set_title("Tabela doboru kopuły", fontsize=18)
ax.set_xticks(bar_x_position)
ax.set_xticklabels(labels)
ax.legend(["Max przemieszczenie pionowe [mm]", "Max siła normalna [kN]", "Łączna długość elementów [m]"], loc=2)

# list of used units
mm_unit = ['mm' for i in range(len(displacement))]
kN_unit = ['kN' for j in range(len(forces))]
m_unit = ['m' for k in range(len(num_of_elem))]

# execute function
top_bar_value(res1, mm_unit)
top_bar_value(res2, kN_unit)
top_bar_value(res3, m_unit)

# ax.bar_label(res1, padding=3)
# ax.bar_label(res2, padding=3)
# ax.bar_label(res3, padding=3)

# provide text to be always visible
fig.tight_layout()

plt.draw()
