import pygal

bar_chart = pygal.Bar(
    title="Most Popular Tractor Brands in Ireland 2023"
)


bar_chart.x_labels = [
    "John Deere", "Massey Ferguson", "New Holland", "Others",
    "Case-IH", "Valtra", "Claas", "Kubota", "Fendt", "Deutz"
]

bar_chart.add("Units Sold", [595, 374, 334, 273, 194, 115, 94, 89, 81, 43])

bar_chart.render_to_file("ireland_tractor_brands.svg")
