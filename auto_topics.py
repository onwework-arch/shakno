import random

TRENDING_SEEDS = [
    "best phones 2025", "budget gaming laptop", "true wireless earbuds", "4k monitors",
    "smartwatch fitness review", "noise cancelling headphones", "best robot vacuums",
    "affordable DSLR alternatives", "portable power banks", "home wifi mesh routers"
]

TITLE_TEMPLATES = [
    "{topic} — Full Review and Buying Guide",
    "Is {topic} Worth Buying in 2025? Full Review",
    "{topic}: Pros, Cons & Real-World Performance",
    "{topic} Deep Dive: Specs, Camera, Battery & More",
    "Top Reasons to Choose {topic} (and What to Watch Out For)"
]

RELATED_SUFFIXES = [
    "Camera", "Battery", "Performance", "Gaming", "Accessories",
    "Durability", "Comparison", "Specs", "User Experience", "Charging"
]

def generate_from_seed(seed, count=15):
    """Generate `count` unique subtopics starting from seed string."""
    seed = seed.strip()
    if not seed:
        # return trending seeds expanded
        seed = random.choice(TRENDING_SEEDS)
    topics = []
    i = 0
    base = seed
    while len(topics) < count:
        # choose a suffix to diversify
        suffix = random.choice(RELATED_SUFFIXES + ["Review", "Full Review", "Guide", "Overview"])
        # minor variation: add variant numbers or modifiers
        variant = random.choice(["", " (2025)", " Pro Test", " - In Depth", f" {random.choice(['Plus', 'Max','Lite'])}"])
        candidate = f"{base} {suffix}{variant}".strip()
        candidate = candidate.replace("  ", " ")
        if candidate not in topics:
            topics.append(candidate)
        i += 1
        if i > count * 6:
            # safety fallback
            break
    # If still short, append variations with numbers
    idx = 1
    while len(topics) < count:
        topics.append(f"{base} Extra {idx}")
        idx += 1
    return topics

def randomize_title(topic):
    tpl = random.choice(TITLE_TEMPLATES)
    return tpl.format(topic=topic)
