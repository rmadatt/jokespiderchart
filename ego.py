import numpy as np
import matplotlib.pyplot as plt

# Data categories
categories = ['Attention-Seeking', 'Emotional Control', 'Charismatic Pull', 'Resilience', 'Influence']
values_techlead = np.array([95, 60, 85, 80, 90])
values_queen = np.array([80, 90, 95, 85, 90])

# Convert to angles for plotting
angles = np.linspace(0, 2 * np.pi, len(categories), endpoint=False).tolist()
values_techlead = np.concatenate((values_techlead, [values_techlead[0]]))
values_queen = np.concatenate((values_queen, [values_queen[0]]))
angles += angles[:1]

# Create radar chart
fig, ax = plt.subplots(figsize=(6,6), subplot_kw=dict(polar=True))

ax.plot(angles, values_techlead, color='#FF6384', linewidth=2, linestyle='solid', label="TechLead's Ego")
ax.fill(angles, values_techlead, color='#FF6384', alpha=0.4)

ax.plot(angles, values_queen, color='#9370DB', linewidth=2, linestyle='solid', label="Your Queen Energy")
ax.fill(angles, values_queen, color='#9370DB', alpha=0.4)

# Add labels
ax.set_yticks([20, 40, 60, 80, 100])
ax.set_yticklabels(['20', '40', '60', '80', '100'])
ax.set_xticks(angles[:-1])
ax.set_xticklabels(categories)
ax.set_title("TechLead's Ego vs. Your Queen Energy", fontsize=14)

# Show legend and save file
ax.legend(loc='upper right', bbox_to_anchor=(1.1, 1.1))
plt.savefig("techlead_queen_energy_chart.png", dpi=300, bbox_inches='tight')
plt.show()
