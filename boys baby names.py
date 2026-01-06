import pygal

boys_chart = pygal.Bar(
    title="Most Popular Boys Names in Ireland - 2024",
    x_title="Name",
        
)

boys_names = ["Jack", "Noah", "Rían", "Cillian", "James"]
boys_counts = [490, 486, 432, 352, 336]

boys_chart.x_labels = boys_names
boys_chart.add("Boys", boys_counts)
boys_chart.render_to_file("ireland_boys_names_2024.svg")