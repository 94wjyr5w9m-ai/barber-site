# AI Automations: Starter Kit

Build your first AI automations from zero. Each step is one small Python file.
Run them in order.

## Setup (one time, about 10 minutes)

1. Install Python 3.10+ from https://python.org
2. Get an API key at https://console.anthropic.com (add about $5 of credit, which covers a lot of testing)
3. In a terminal, inside this folder:
   ```bash
   pip install -r requirements.txt
   export ANTHROPIC_API_KEY=sk-ant-...     # Windows PowerShell: $env:ANTHROPIC_API_KEY="sk-ant-..."
   ```

## The steps

| # | File | What it does | What you learn |
|---|------|--------------|----------------|
| 1 | `01_hello_ai.py` | Asks Claude one question | That your setup works |
| 2 | `02_review_replier.py` | Writes owner-style replies to Google reviews | Automating a task businesses will pay for |
| 3 | `03_lead_finder.py` | Scores local businesses and drafts personal outreach | Using AI to find customers |

```bash
python 01_hello_ai.py
python 02_review_replier.py
python 03_lead_finder.py
```

Results land in `output/` as CSV files you can open in Excel or Google Sheets.

## How every automation works

```
Input (CSV, email, form)  ->  Instructions + data sent to AI  ->  Output (reply, score, message)  ->  You approve  ->  Action
```

All the AI code lives in `ai.py`. To make your own automation, copy one of the
step files, change the `SYSTEM` instructions, and point it at a different CSV.

## Make it yours

- **Step 2:** change `SHOP_NAME` and the tone in `SYSTEM`, then paste a real shop's reviews into `data/reviews.csv`.
- **Step 3:** put real businesses into `data/leads.csv` (copy them by hand from Google Maps to start) and edit `MY_OFFER`.

## What to learn next

1. **Run it on a schedule:** a cron job, or a no-code tool like n8n or Make that calls these scripts.
2. **Connect real inputs:** Google reviews API, Gmail, website forms.
3. **Connect real outputs:** send texts (Twilio), emails, post replies.
4. **Build a chatbot:** an AI receptionist for the barber website in this repo.

## Rules that keep the business alive

- **A human approves anything sent to customers or leads,** at least until you trust the output.
- **Outreach:** send small batches of personalized messages, never mass blasts. Follow CAN-SPAM in the US and GDPR in the EU.
- **Never let the AI promise** refunds, discounts or prices you haven't approved.
