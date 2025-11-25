from jinja2 import Environment, FileSystemLoader
import os

TEMPLATES_DIR = os.path.join(os.path.dirname(__file__), 'templates')
env = Environment(loader=FileSystemLoader(TEMPLATES_DIR))

def render(template_name, **ctx):
    tpl = env.get_template(template_name)
    return tpl.render(**ctx)
