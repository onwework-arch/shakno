import os, yaml, json
from slugify import slugify

def ensure_dir(path):
    os.makedirs(path, exist_ok=True)

def slug(text):
    return slugify(text)

def save_output(path, content):
    ensure_dir(os.path.dirname(path))
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    return path

def read_yaml(path):
    if not os.path.exists(path):
        return None
    with open(path, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)
