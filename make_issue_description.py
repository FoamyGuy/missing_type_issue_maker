from jinja2 import Template
from find_missing_type_annotations import find_missing_annotations

def make_issue_description(missing_types):
    f = open("templates/issue_template", "r")
    issue_template = Template(f.read())
    f.close()

    _rendered_template_text = issue_template.render(
        missing_type_annotations=missing_types)

    f = open("missing_types_issue.txt", "w")
    f.write(_rendered_template_text)
    f.close()


if __name__ == "__main__":
    make_issue_description(missing_types=find_missing_annotations("../Adafruit_CircuitPython_ImageLoad/adafruit_imageload"))
