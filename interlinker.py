def build_internal_links(topic, candidates, max_links=6):
    links = []
    tset = set(topic.lower().split())
    for c in candidates:
        score = len(tset & set(c.lower().split()))
        links.append({'title': c, 'slug': c.replace(' ', '-').lower(), 'score': score})
    links.sort(key=lambda x: x['score'], reverse=True)
    return links[:max_links]
