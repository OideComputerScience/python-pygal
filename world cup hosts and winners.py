import pygal
from pygal.style import Style
from pygal.maps.world import World

#Custom colours specified
custom_style = Style(
    colors=('#FFD700', '#1E90FF', '#228B22')  # Yellow, Blue, Green
)

# Data for country hosts and winners
hosts = {
    'uy': 1, 'it': 2, 'fr': 2, 'br': 2, 'ch': 1, 'se': 1, 'cl': 1,
    'mx': 2, 'de': 2, 'ar': 1, 'es': 1, 'us': 1, 'jp': 1, 'kr': 1,
    'za': 1, 'ru': 1, 'qa': 1, 'ca': 1
}

winners = {
    'br': 5, 'de': 4, 'it': 4, 'ar': 3, 'fr': 2, 'uy': 2, 'gb': 1, 'es': 1
}

# Categorize
hosts_only = {}
winners_only = {}
both = {}

all_countries = set(hosts) | set(winners)

for country in all_countries:
    hosted = hosts.get(country, 0)
    won = winners.get(country, 0)
    if hosted > 0 and won == 0:
        hosts_only[country] = hosted
    elif hosted == 0 and won > 0:
        winners_only[country] = won
    elif hosted > 0 and won > 0:
        both[country] = hosted + won

# Create map with custom style
wm = World(style=custom_style)
wm.title = "FIFA Men's World Cup Hosts and Winners"

wm.add('Hosted Only', hosts_only)
wm.add('Winners Only', winners_only)
wm.add('Hosted & Won', both)

# Save to file
wm.render_to_file('fifa_world_cup_hosts_and_winners.svg')
