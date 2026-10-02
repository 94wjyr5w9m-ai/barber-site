"""Step 2: a real automation you could sell.

Reads customer reviews from data/reviews.csv, writes a reply to each one in the
shop owner's voice, and saves them to output/review_replies.csv for approval.
"""
import csv
from pathlib import Path

from ai import ask

SHOP_NAME = "Blade & Crown Barbershop"
SYSTEM = f"""You reply to Google reviews on behalf of {SHOP_NAME}.
Write like a friendly, professional shop owner: warm, short (2-4 sentences), no emojis.
Thank the reviewer by first name. For positive reviews, mention a specific detail they liked.
For negative reviews, apologize sincerely without making excuses, say what you'll do
better, and invite them to contact the shop directly. Never offer refunds or discounts.
Output only the reply text."""

rows = list(csv.DictReader(open("data/reviews.csv")))
Path("output").mkdir(exist_ok=True)

with open("output/review_replies.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["reviewer", "stars", "review", "suggested_reply"])
    writer.writeheader()
    for row in rows:
        reply = ask(f"{row['stars']}-star review from {row['reviewer']}:\n{row['review']}", system=SYSTEM)
        writer.writerow({**row, "suggested_reply": reply})
        print(f"\n[{row['stars']}*] {row['reviewer']}: {row['review']}\n  -> {reply}")

print("\nSaved to output/review_replies.csv - review before posting.")
