import threading, time
from .generator import generate_single_post


def generate_batch_sync(seed_topic, count=1, publish=False, meta_description=None, word_count=2500):
    topics = [seed_topic] + [f"{seed_topic} {i}" for i in range(1, count)]
    results = []
    for t in topics:
        results.append(
            generate_single_post(
                t,
                publish=publish,
                meta_description=meta_description,
                word_count=word_count,
            )
        )
        time.sleep(0.2)
    return results


def generate_batch_async(seed_topic, count=1, publish=False, meta_description=None, word_count=2500):
    thread = threading.Thread(
        target=generate_batch_sync,
        args=(seed_topic, count, publish, meta_description, word_count),
        daemon=True,
    )
    thread.start()
    return thread
