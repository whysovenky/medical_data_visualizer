import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Load data
df = pd.read_csv('medical_examination.csv')

# 1. Add 'overweight' column using BMI formula
df['overweight'] = ((df['weight'] / ((df['height'] / 100) ** 2)) > 25).astype(int)

# 2. Normalize 'cholesterol' and 'gluc' (0 = good, 1 = bad)
df['cholesterol'] = (df['cholesterol'] > 1).astype(int)
df['gluc'] = (df['gluc'] > 1).astype(int)

# 3. Categorical Plot
def draw_cat_plot():
    # Melt relevant columns into long format
    df_cat = pd.melt(df,
                     id_vars='cardio',
                     value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])

    # Group and count values
    df_cat = df_cat.value_counts(['cardio', 'variable', 'value']).reset_index(name='total')

    # Create Seaborn catplot
    fig = sns.catplot(data=df_cat, kind='bar',
                      x='variable', y='total', hue='value', col='cardio').fig

    return fig


# 4. Heatmap
def draw_heat_map():
    # Filter the data
    df_heat = df[
        (df['ap_lo'] <= df['ap_hi']) &
        (df['height'] >= df['height'].quantile(0.025)) &
        (df['height'] <= df['height'].quantile(0.975)) &
        (df['weight'] >= df['weight'].quantile(0.025)) &
        (df['weight'] <= df['weight'].quantile(0.975))
    ]

    # Correlation matrix
    corr = df_heat.corr()

    # Generate mask for upper triangle
    mask = np.triu(np.ones_like(corr, dtype=bool))

    # Set up plot
    fig, ax = plt.subplots(figsize=(12, 10))

    # Draw heatmap
    sns.heatmap(corr, mask=mask, annot=True, fmt='.1f', center=0,
                square=True, linewidths=.5, cbar_kws={"shrink": .5}, ax=ax)

    return fig
