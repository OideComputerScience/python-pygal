import pygal

population_data = {
    "Ireland": [5.1, 6.9, 4.5, 2.9, 3.8],
    "UK": [16.0, 27.5, 38.0, 50.0, 59.1],
    "France": [29.0, 36.0, 41.0, 42.5, 59.3],
    "Germany": [24.0, 35.0, 56.0, 69.0, 82.0]
}

years = ["1800", "1850", "1900", "1950", "2000"]

#Create bar chart
bar_chart = pygal.Bar(show_legend=True, x_title="Year", y_title="Population (millions)")
for country, data in population_data.items():
    bar_chart.add(country, data)
    
#Generate table of population data
html_table = bar_chart.render_table(style=True)


#Generate sparklines
spark_texts = {}
for country, data in population_data.items():
    chart = pygal.Line()
    chart.add(country, data)
    spark_texts[country] = chart.render_sparktext()


#Generate HTML page
html_content = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Population Bar Chart, Table & Sparklines</title>
    <style>
        body {{ font-family: Arial, sans-serif; }}
        table {{ border-collapse: collapse; width: 70%; margin-bottom: 30px; }}
        th, td {{ border: 1px solid #ccc; padding: 6px; text-align: center; }}
        th {{ background-color: #eee; }}
    </style>
</head>
<body>
    <h1>Population of Ireland, UK, France, Germany (1800-2000)</h1>

    <h2>1. Bar Chart</h2>
    {bar_chart.render(is_unicode=True)}

    <h2>2. Data Table for Population of each Country</h2>
    {html_table}

    <h2>3. Sparklines</h2>
    <table>
        <thead>
            <tr><th>Country</th><th>Sparkline</th></tr>
        </thead>
        <tbody>
"""

for country, spark in spark_texts.items():
    html_content += f"            <tr><td>{country}</td><td>{spark}</td></tr>\n"

html_content += """
        </tbody>
    </table>
</body>
</html>
"""


#Save as HTML file
with open("population_combined.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("HTML page generated: population_combined.html")
