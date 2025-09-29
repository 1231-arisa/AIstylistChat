# AIstylistChat

AIstylist is a tiny Flask prototype that lets you ask a question like “What should I wear for a rainy Monday at work?” and gets outfit suggestions from Together API.

## Features
- Simple homepage with a text area to ask a fashion question
- Uses Together API with the DeepSeek model
- System prompt set to a structured personal stylist scenario
- Friendly, concise suggestions rendered on a result page

## Requirements
- Python 3.9+
- A Together API key (`TOGETHER_API_KEY`) or a local `together.key` file

## Quickstart (Windows PowerShell)
1) Clone or download this repo.

2) (Optional) Create and activate a virtual environment:
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

3) Install dependencies:
```powershell
pip install flask together
```

4) Set your Together API key (open a new PowerShell after setting):
```powershell
setx TOGETHER_API_KEY "your_together_api_key_here"
```

5) (Optional) Set a Flask secret key for session flashes:
```powershell
setx FLASK_SECRET_KEY "a_random_secret"
```

6) Run the app:
```powershell
python app.py
```

7) Open in your browser:
```
http://127.0.0.1:5000/
```

## How it works
- `app.py` defines two routes:
  - `/` renders `templates/index.html` with a simple form
  - `/result` handles form submission, calls Together API, and renders `templates/result.html`
- Uses Together SDK: `from together import Together` → `client.chat.completions.create(...)`
- Model: `deepseek-ai/DeepSeek-R1-Distill-Llama-70B-free`
- System prompt embeds a structured stylist scenario (sunny, 15°C) and expected sections
- Basic error handling with flash messages

## Project structure
```
AIstylistChat/
├─ app.py
└─ templates/
   ├─ index.html
   └─ result.html
```

## Troubleshooting
- "Together API key not found": Set `TOGETHER_API_KEY` or create a `together.key` file in the project root containing only your key.
- Import error for `together`: Run `pip install together` and ensure your virtual environment is activated.
- The server starts but suggestions do not appear: Check your terminal for errors; network/firewall issues can block outbound requests.

## Notes
- You can store the key in `together.key` (already listed in `.gitignore`) for local use.
- This is a prototype; do not expose your API key in client-side code.
