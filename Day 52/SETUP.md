# SETUP.md — QueryMind Local Development

Follow this to get the project running on your own machine from scratch (e.g. on a new computer, or after cloning fresh).

## 1. Prerequisites
- **Python 3.11+** (this project was set up with 3.13.7). Check with:
  ```
  python --version
  ```
- **Git** (already installed and connected to this repo).

## 2. Get the code
If starting fresh:
```
git clone https://github.com/Lakshaybh/My-Claude-Journey_60Days
cd My-Claude-Journey_60Days/Day 52/querymind
```
If you already have the repo cloned, just navigate to `Day 52/querymind`.

## 3. Create a virtual environment
A virtual environment keeps this project's Python packages separate from everything else on your machine.
```
python -m venv venv
```

## 4. Activate the virtual environment
- **Windows (PowerShell):**
  ```
  venv\Scripts\Activate.ps1
  ```
- **Windows (Git Bash, used in this session):**
  ```
  source venv/Scripts/activate
  ```
You'll know it worked when your terminal prompt shows `(venv)` at the start.

## 5. Install dependencies
```
pip install -r requirements.txt
```
This installs FastAPI, Uvicorn, the Anthropic SDK, and python-dotenv — see `ENVIRONMENT.md` for what each one does.

## 6. Set up your environment variables
```
cp .env.example .env
```
Then open `.env` in your editor and replace `your_key_here` with your real Anthropic API key (only needed starting Day 4 — not required to run today's hello-world version).

## 7. Run the app locally
```
uvicorn app.main:app --reload --port 8000
```
- `--reload` restarts the server automatically when you save a code change (useful during development).
- Open `http://127.0.0.1:8000` in your browser — you should see the QueryMind hello-world page.
- Check `http://127.0.0.1:8000/api/health` — should return `{"status":"ok"}`.

## 8. Stop the server
Press `Ctrl+C` in the terminal where it's running.

## 9. Verifying everything works (Day 3 checklist)
- [ ] Browser shows the hello-world page at `http://127.0.0.1:8000`
- [ ] `/api/health` returns `{"status":"ok"}`
- [ ] `/api/generate` returns a stub JSON response (test via the browser's dev tools, curl, or `http://127.0.0.1:8000/docs` — FastAPI's built-in interactive API tester)
