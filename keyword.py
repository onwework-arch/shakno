import random

def generate_focus_keyword(topic: str) -> str:
    variations = [
        f"{topic} review",
        f"{topic} full specifications",
        f"{topic} price in India",
        f"{topic} camera test",
        f"{topic} vs competitors",
        f"{topic} pros and cons",
        f"{topic} buying guide",
        f"{topic} long-term review"
    ]
    return random.choice(variations)
