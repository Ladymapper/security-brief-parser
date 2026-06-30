from src.bronze import save_bronze
from src.silver import extract_silver
from src.gold import build_gold

import json
import os
from datetime import datetime


# ---------------------------------------
# Paste the weekly brief here
# ---------------------------------------

raw_email_text = """
PASTE THE WEEKLY BRIEF HERE
"""


# Bronze
save_bronze(raw_email_text)


# Silver
incidents = extract_silver(raw_email_text)


# Gold
gold_summary = build_gold(incidents)


# Save outputs
os.makedirs("silver", exist_ok=True)
os.makedirs("gold", exist_ok=True)

timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

with open(f"silver/brief_{timestamp}.json", "w") as f:
    json.dump(incidents, f, indent=4)

with open(f"gold/summary_{timestamp}.json", "w") as f:
    json.dump(gold_summary, f, indent=4)

print("Pipeline completed successfully.")
