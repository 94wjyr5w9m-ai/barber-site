"""Step 3: let AI help find customers.

Reads local businesses from data/leads.csv, scores how much each one needs help,
and drafts a personalized first message for the good leads. Results are saved
to output/leads_scored.csv. You review and send them yourself, so you stay
in control and avoid spam problems.
"""
import csv
from pathlib import Path

from pydantic import BaseModel

from ai import ask_structured

MY_OFFER = """I set up AI automations for barbershops: a website with online booking,
an AI assistant that answers texts/DMs 24/7, and automatic replies to Google reviews.
$149/month, first two weeks free."""


class LeadScore(BaseModel):
    score: int            # 1-10, how much they need the offer
    reason: str           # one sentence explaining the score
    problems_spotted: list[str]
    outreach_message: str  # short, personal first message (empty if score < 6)


SYSTEM = f"""You are a sales researcher for a small AI automation agency.
The offer: {MY_OFFER}
Score each business 1-10 on how much it would benefit, based ONLY on the facts given.
If the score is 6 or higher, write a friendly first message (under 80 words) that mentions
one specific problem you noticed, offers to help, and ends with a low-pressure question.
No hype, no fake claims, no made-up facts. If the score is below 6, leave the message empty."""

leads = list(csv.DictReader(open("data/leads.csv")))
Path("output").mkdir(exist_ok=True)

results = []
for lead in leads:
    facts = "\n".join(f"{k}: {v or '(none)'}" for k, v in lead.items())
    s = ask_structured(facts, LeadScore, system=SYSTEM)
    results.append({**lead, "score": s.score, "reason": s.reason,
                    "problems": "; ".join(s.problems_spotted), "outreach_message": s.outreach_message})
    print(f"\n{lead['business']}: {s.score}/10 - {s.reason}")
    if s.outreach_message:
        print(f"  Draft: {s.outreach_message}")

results.sort(key=lambda r: r["score"], reverse=True)
with open("output/leads_scored.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=list(results[0].keys()))
    writer.writeheader()
    writer.writerows(results)

print("\nSaved to output/leads_scored.csv (best leads first).")
