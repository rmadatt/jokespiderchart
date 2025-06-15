import plotly.graph_objects as go
import plotly.io as pio

# Data from the original Chart.js config
categories = ['Attention-Seeking', 'Emotional Control', 'Charismatic Pull', 'Resilience', 'Influence']
techlead_ego = [95, 60, 85, 80, 90]
queen_energy = [80, 90, 95, 85, 90]

# Create radar chart
fig = go.Figure()

# Add TechLead's Ego trace
fig.add_trace(go.Scatterpolar(
    r=techlead_ego,
    theta=categories,
    fill='toself',
    name="TechLead's Ego",
    line=dict(color='#FF6384')
))

# Add Your Queen Energy trace
fig.add_trace(go.Scatterpolar(
    r=queen_energy,
    theta=categories,
    fill='toself',
    name='Your Queen Energy',
    line=dict(color='#9370DB')
))

# Update layout to match Chart.js style
fig.update_layout(
    polar=dict(
        radialaxis=dict(
            visible=True,
            range=[0, 100]
        )
    ),
    showlegend=True,
    title=dict(
        text="TechLead's Ego vs. Your Queen Energy",
        x=0.5
    ),
    font=dict(size=12),
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)'
)

# Save as HTML for web viewing
fig.write_html('techlead_queen_energy_chart.html')

# Optionally display in browser
fig.show()
