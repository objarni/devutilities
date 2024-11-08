import pathlib
import re

# read index.css and store it in a variable
index_css = pathlib.Path('index.css').read_text()

# replace all instances of 'rem' with 'em'

result = ""
while True:
    m = re.search('([0-9.]*[.]*[0-9]+)rem', index_css)
    if not m:
        break
    value = float(m.group(1))
    print(m.group(1), value)
    new_value = value * 0.615
    formatted_new_value = f'{new_value:1.2f}'
    result += index_css[:m.start(0)] + formatted_new_value + "rem"
    index_css = index_css[m.end(0):]

result += index_css

# save content to file index2.css
pathlib.Path('index2.css').write_text(result)
