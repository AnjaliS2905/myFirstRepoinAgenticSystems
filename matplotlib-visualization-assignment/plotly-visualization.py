import pandas as pd
import plotly.express as px

df = pd.DataFrame({
    "epoch": range(1, 11),
    "loss": [0.9, 0.8, 0.75, 0.7, 0.65, 0.6, 0.58, 0.55, 0.52, 0.5] 
})

fig=px.line(df,x="epoch",y="loss",title="Training Loss Over Time",labels={"epoch": "Epoch", "loss": "Loss"})
fig.add_annotation(
    x=5, 
    y=0.65,
    text= "Training Plateau",
    showarrow=True,
    arrowhead=6 
)
fig.show()