import matplotlib.pyplot as plt
import numpy as np

def top_bar_value(res):
    for rect in res:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width() / 2., height, '%d' % int(height), ha='center', va='bottom')

labels = ["Kopuła Żebrowa", "Kopuła Schwedlera", "Kopuła Lamella zakrzywiona"]
displacement = [47.277, 44.707, 46.032]
forces = [948.5, 876.4, 869.0]
num_of_elem = []

bar_x_position = np.arange(len(labels))
width = 0.1

fig, ax = plt.subplots()
res1 = ax.bar(bar_x_position - width, displacement, width, label =labels[0])
res2 = ax.bar(bar_x_position, forces, width, label =labels[1])
res3 = ax.bar(bar_x_position + width, displacement[2], width, label =labels[2])

ax.set_ylabel("Przemieszczenie")
ax.set_title("Tabela")
ax.set_xticks(bar_x_position)
ax.set_xticklabels(labels)
ax.legend()

top_bar_value(res1)
top_bar_value(res2)
top_bar_value(res3)

ax.bar_label(res1, padding=3)
ax.bar_label(res2, padding=3)
ax.bar_label(res3, padding=3)

fig.tight_layout()

plt.show()
