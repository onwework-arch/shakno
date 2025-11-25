# ShakNow Pro — Ultra Full AI CMS

Quick start (local):
1. python -m venv .venv
2. source .venv/bin/activate  # or .venv\Scripts\activate on Windows
3. pip install -r requirements.txt
4. Copy `.env.example` -> `.env` and set OPENAI_API_KEY
5. Edit `config/wp_config.yaml` with WP credentials
6. streamlit run app.py

Notes:
- Use WordPress application passwords.
- Test publish on staging WP site first.
- Do NOT commit .env or secrets.
