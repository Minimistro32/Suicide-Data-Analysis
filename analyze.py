import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("master.csv")

def rates_x_col(df, col, order_by = None, col_handler = None):
    # Filter away null and excess columns
    df = df[df[col].notnull()]
    df_col = df.loc[:,['suicides/100k pop',col]]

    # Process the column
    if col_handler != None:
        df_col[col] = col_handler(df_col[col])

    # Specify the column's sort
    if order_by != None:
        df_col[col] = pd.Categorical(df_col[col], order_by)

    # Average rates grouped by col
    df_col_avg = df_col.groupby(col).sum().groupby(level=0).mean()

    # Sort the column
    df_col_avg.sort_values(col)

    # Plot
    df_col_avg.plot()

# Analyze the suicide rates using various cols and handlers
rates_x_col(df, "HDI for year", col_handler = lambda col: col.round(2))
rates_x_col(df, "age", order_by = ['15-24 years', '25-34 years', '35-54 years', '55-74 years', '75+ years'])
rates_x_col(df, "gdp_per_capita ($)", col_handler = lambda col: col.div(10**5).round(1).mul(10**5))
rates_x_col(df[df['year'] < 2015], "year")

#plot the graphs
plt.show()