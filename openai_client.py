import os
try:
    import openai
except Exception:
    openai = None

def generate_with_openai(prompt, max_tokens=2000, temperature=0.7):
    key = os.getenv('OPENAI_API_KEY')
    if not key or openai is None:
        return None
    openai.api_key = key
    try:
        resp = openai.ChatCompletion.create(
            model='gpt-4o-mini',
            messages=[{"role":"user","content":prompt}],
            max_tokens=max_tokens,
            temperature=temperature
        )
        return resp.choices[0].message.content
    except Exception:
        return None
