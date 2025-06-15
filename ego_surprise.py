import numpy as np
import matplotlib.pyplot as plt

# Data categories (because why be basic?)
categories = [
    'Attention-Seeking 👀', 
    'Emotional Control 🎭', 
    'Charismatic Pull ✨', 
    'Resilience 💪', 
    'Influence 🧠'
]
values_techlead = np.array([95, 60, 85, 80, 90])  # Ego level: "Yes."
values_queen = np.array([80, 90, 95, 85, 90])    # Queen level: "Obviously."

# Close the loop (like TechLead's LinkedIn humblebrags)
angles = np.linspace(0, 2 * np.pi, len(categories), endpoint=False)
angles = np.concatenate((angles, [angles[0]]))
values_techlead = np.concatenate((values_techlead, [values_techlead[0]]))
values_queen = np.concatenate((values_queen, [values_queen[0]]))

# Create the chart (drama included)
fig, ax = plt.subplots(figsize=(10, 10), subplot_kw={'polar': True})

# Plot TechLead's ego (warning: may cause secondhand embarrassment)
ax.plot(angles, values_techlead, 'o-', color='#FF6384', linewidth=3, 
        label="TechLead's Ego (∞% confidence)")
ax.fill(angles, values_techlead, color='#FF6384', alpha=0.3)

# Plot Queen Energy (elegant dominance)
ax.plot(angles, values_queen, 'o-', color='#9370DB', linewidth=3, 
        label="Queen Energy (Deal with it.)")
ax.fill(angles, values_queen, color='#9370DB', alpha=0.3)

# Make it FANCY
ax.set_theta_offset(np.pi / 2)  # Start at the top (queens don't start at the bottom)
ax.set_theta_direction(-1)      # Clockwise (like a crown being placed)
ax.set_rlabel_position(45)      # Radial labels at a ~chic~ angle
ax.set_ylim(0, 110)            # Room for TechLead's ego to theoretically expand

# Labels with ~flair~
plt.xticks(angles[:-1], categories, fontsize=13, ha='center')
plt.yticks([20, 40, 60, 80, 100], ["Meh", "Okay", "Solid", "Slay", "GOD MODE"], 
           fontsize=10, color='gray')
plt.title("WHO RULES THE INTERNET?\n(TechLead vs. Queen Energy)", 
          fontsize=18, pad=25, fontweight='bold')

# Legend (because every drama needs a cast list)
plt.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1), 
           framealpha=1, edgecolor='gold')

# Save for clout (or memes)
plt.savefig("ego_vs_queen.png", dpi=300, bbox_inches='tight', transparent=True)
plt.show()
