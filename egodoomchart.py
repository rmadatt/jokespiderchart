import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
import matplotlib.patheffects as path_effects

# ====== DATA SETUP (FOR THE DAMNED) ====== #
categories = [
    'Attention-Seeking 👁️‍🗨️ (pls notice me)', 
    'Emotional Control 🎭 (or lack thereof)', 
    'Charismatic Pull ✨ (or cult leader?)', 
    'Resilience 💀 (how much can they take?)', 
    'Influence 🧟 (zombie followers?)'
]
values_techlead = np.array([666, 20, 85, 40, 90])  # TechLead's ego broke the scale.
values_queen = np.array([80, 95, 666, 90, 666])    # Queen's power is... unnatural.

# ====== CHART FROM THE NETHER REALMS ====== #
fig, ax = plt.subplots(figsize=(12, 12), subplot_kw={'polar': True}, facecolor='black')
fig.patch.set_alpha(0.0)  # For that "void aesthetic"

# ====== PLOT THE DAMNED ====== #
# TechLead's Ego (a tale of woe and cringe)
ax.plot(angles, values_techlead, 'o-', color='#FF0000', linewidth=4, 
        label="TECHLEAD'S EGO (ERROR: OVERFLOW)", 
        path_effects=[path_effects.withGlow(alpha=0.8, blur=10)])
ax.fill(angles, values_techlead, color='#FF0000', alpha=0.2)

# Queen Energy (eldritch horror in purple)
ax.plot(angles, values_queen, 'o-', color='#9400D3', linewidth=4, 
        label="QUEEN ENERGY (POWER LEVEL: ???)", 
        path_effects=[path_effects.withGlow(alpha=0.6, blur=15)])
ax.fill(angles, values_queen, color='#9400D3', alpha=0.2)

# ====== CHART CUSTOMIZATION (NOW WITH MORE EVIL) ====== #
ax.set_theta_offset(np.pi / 2)  
ax.set_theta_direction(-1)      
ax.set_ylim(0, 666)            # Yes, the limit is 666. Deal with it.
ax.set_facecolor('black')      # Void background
ax.spines['polar'].set_color('white')  # Spooky outline

# ====== LABELS FROM BEYOND ====== #
plt.xticks(angles[:-1], categories, fontsize=14, color='white', 
           path_effects=[path_effects.withStroke(linewidth=3, foreground='black')])
plt.yticks([0, 100, 200, 300, 400, 500, 600], 
           ["MORTAL", "MEH", "OK", "YIKES", "OH NO", "RUN", "666"], 
           fontsize=12, color='#FF5555')

# ====== TITLE & LEGEND (FOR THE BRAVE) ====== #
plt.title("THE ULTIMATE SHOWDOWN:\nTECHLEAD'S EGO VS. QUEEN'S ELDRITCH POWER", 
          fontsize=18, pad=30, color='white', fontweight='black',
          path_effects=[path_effects.withStroke(linewidth=4, foreground='red')])

legend = ax.legend(loc='upper right', bbox_to_anchor=(1.35, 1.15), 
                  facecolor='black', edgecolor='red', 
                  fontsize=12, labelcolor='white')
legend.get_frame().set_alpha(0.7)

# ====== FINAL TOUCHES (CHAOS, GLOW, DESPAIR) ====== #
# Add a pentagram for ~aesthetic~ reasons
pentagram_angles = np.linspace(0, 2 * np.pi, 5, endpoint=False)
pentagram_angles = np.concatenate((pentagram_angles, [pentagram_angles[0]]))
ax.plot(pentagram_angles, [700]*6, color='white', linewidth=2, alpha=0.5)

# Add a creepy circle (because why not)
ax.add_patch(Circle((0, 0), 700, fill=False, edgecolor='#FF0000', 
                    linestyle='--', alpha=0.3))

# ====== SAVE FOR POSTERITY (OR YOUR DEMONIC PORTFOLIO) ====== #
plt.savefig("techead_vs_queen_apocalypse.png", dpi=300, bbox_inches='tight', 
            transparent=True, facecolor='black')
plt.show()
