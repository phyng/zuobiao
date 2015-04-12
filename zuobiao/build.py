import os
import json
import re

for pk in range(50, 51):

    print(pk)

    temp_ipynb = 'anser_temp.ipynb'
    temp_html = 'anser_temp.html'
    target_html = 'build/anser{}.html'.format(pk)

    with open('anser.ipynb', 'r') as f:
        text = f.read()
        text = re.sub('PK = 1', 'PK = {}'.format(pk), text)
        with open(temp_ipynb, 'w') as g:
            g.write(text)

    os.system("""ipython nbconvert \
            --to=html --ExecutePreprocessor.enabled=True {}""".format(temp_ipynb)
        )
    os.system('cp -f {} {}'.format(temp_html, target_html))
