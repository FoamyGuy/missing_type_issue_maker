from jinja2 import Template
from find_missing_type_annotations import find_missing_annotations

f = open("templates/issue_template", "r")
issue_template = Template(f.read())
f.close()

rendered_template_text = issue_template.render(missing_type_annotations=find_missing_annotations("../Adafruit_CircuitPython_ImageLoad/adafruit_imageload"))

f = open("output.txt", "w")
f.write(rendered_template_text)
f.close()