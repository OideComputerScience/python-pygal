import pygal

# Historical populations (approximate, in millions)
population_data = {
    "Ireland": [5.1, 6.9, 4.5, 2.9, 3.8],
    "UK": [16.0, 27.5, 38.0, 50.0, 59.1],
    "France": [29.0, 36.0, 41.0, 42.5, 59.3],
    "Germany": [24.0, 35.0, 56.0, 69.0, 82.0]
}

# Generate sparkline text for each country
spark_texts = {}
for country, data in population_data.items():
    chart = pygal.Line()
    chart.add(country, data)
    spark_texts[country] = chart.render_sparktext()

# Build HTML content
html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Population Sparklines: 1800-2000</title>
    <style>
        table { border-collapse: collapse; width: 60%; }
        th, td { border: 1px solid #ccc; padding: 8px; text-align: center; }
        th { background-color: #eee; }
    </style>
</head>
<body>
    <h1>Population of Ireland, UK, France, Germany: 1800-2000</h1>
    <table>
        <thead>
            <tr>
                <th>Country</th>
                <th>Population Sparkline</th>
            </tr>
        </thead>
        <tbody>
"""

# Add table rows for each country
for country, spark in spark_texts.items():
    html_content += f"            <tr><td>{country}</td><td>{spark}</td></tr>\n"

# Close HTML tags
html_content += """
        </tbody>
    </table>
</body>
</html>
"""

# Save HTML to file
with open("europe_population_sparklines.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("HTML page generated: europe_population_sparklines.html")
