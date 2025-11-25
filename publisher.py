import os, requests
from .utils import read_yaml

CFG_PATH = os.path.normpath(os.path.join(os.path.dirname(__file__), '..', 'config', 'wp_config.yaml'))

def publish_to_wordpress(title, html_content, excerpt='', publish=False):
    cfg = read_yaml(CFG_PATH)
    if not cfg:
        raise RuntimeError('Missing config/wp_config.yaml')
    url = cfg.get('url').rstrip('/') + '/posts'
    auth = (cfg.get('username'), cfg.get('application_password'))
    data = {
        'title': title,
        'content': html_content,
        'status': 'publish' if publish else 'draft',
        'excerpt': excerpt,
        'tags': cfg.get('default_tags', []),
        'categories': cfg.get('default_categories', [])
    }
    resp = requests.post(url, auth=auth, json=data, timeout=30)
    if resp.status_code not in (200, 201):
        raise RuntimeError(f'WP publish failed: {resp.status_code} {resp.text}')
    return resp.json().get('id')
