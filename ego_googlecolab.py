import numpy as np
import matplotlib.pyplot as plt

# Data setup
categories = ['Attention-Seeking', 'Emotional Control', 'Charismatic Pull', 'Resilience', 'Influence']
values_techlead = np.array([95, 60, 85, 80, 90])
values_queen = np.array([80, 90, 95, 85, 90])

# Angle calculations
angles = np.linspace(0, 2 * np.pi, len(categories), endpoint=False)
angles = np.concatenate((angles, [angles[0]]))  # Close the loop
values_techlead = np.concatenate((values_techlead, [values_techlead[0]]))
values_queen = np.concatenate((values_queen, [values_queen[0]]))

# Create figure
plt.figure(figsize=(8, 8))
ax = plt.subplot(111, polar=True)

# Plot data
ax.plot(angles, values_techlead, 'o-', color='#FF6384', linewidth=2, label="TechLead's Ego")
ax.fill(angles, values_techlead, color='#FF6384', alpha=0.25)

ax.plot(angles, values_queen, 'o-', color='#9370DB', linewidth=2, label="Queen Energy")
ax.fill(angles, values_queen, color='#9370DB', alpha=0.25)

# Formatting
ax.set_theta_offset(np.pi/2)  # Start at top
ax.set_theta_direction(-1)  # Clockwise
ax.set_rlabel_position(30)  # Radial label position
ax.set_ylim(0, 100)

# Labels and ticks
plt.xticks(angles[:-1], categories, fontsize=12)
plt.yticks([20, 40, 60, 80, 100], ["20", "40", "60", "80", "100"], fontsize=10)
plt.title("Personality Radar Chart", size=16, pad=20)

# Legend and display
plt.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1))
plt.tight_layout()
plt.show()
