import re
from pyquery import PyQuery as pq

with open('base.html', 'r') as f:
    base = f.read()

for pk in range(1, 51):
    filename = 'anser{}.html'.format(pk)
    with open(filename, 'r') as f:
        html = f.read()
        html = html.replace(
            """<title>anser_temp</title>""",
            """<title>Zuobiao on IPython</title>"""
            )
    with open(filename, 'w') as f:
        f.write(html)

