# Buzzline – Custom Producer & Consumer (Joanna Farris)

This project includes **custom streaming components** that generate and monitor log messages in real time.

- **Producer:** `producers/basic_producer_joannafarris.py`  
  Generates themed messages (e.g., “I just debugged a model! It was fantastic.”) at a configurable interval.

- **Consumer:** `consumers/basic_consumer_joannafarris.py`  
  Tails the log file and performs **real-time alerts** (e.g., alerts on “debugged a model” or “inspiring”).  
  Prints a lightweight heartbeat to avoid terminal flicker and does **not** write alerts back into the same log (prevents feedback loops).

---

## Setup

### Create and Activate Virtual Environment

python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt   # or: pip install loguru python-dotenv

## Environment File

Create a `.env` in the repo root:

### message production interval in seconds
MESSAGE_INTERVAL_SECONDS=3

Logs are written to `logs/project_log.log`. The `logs/` folder is **git-ignored**.

## Run the Scripts

Open two terminals (one for the producer, one for the consumer).


**Producer:**
source .venv/bin/activate
python3 -m producers.basic_producer_joannafarris

**Consumer:**
source .venv/bin/activate
python3 -m consumers.basic_consumer_joannafarris

## Consumer Alerts

The consumer raises alerts for special messages:

- Contains `"debugged a model"` →  
  **ALERT: Debug event detected!**
- Contains `"inspiring"` →  
  **ALERT: Inspiring moment spotted!**

---

## How It Works

- Skips lines containing `ALERT:` to avoid self-trigger loops.  
- Prints a heartbeat:  
  `Consumer running… processed N messages`  
  (updates in place, not scrolling endlessly).  
- Prints alerts to console.  
- Optionally, alerts can be written to a separate `logs/alerts.log`.

## Git Tips

Keep logs out of Git by adding these to your `.gitignore`: 

logs/  
*.log

