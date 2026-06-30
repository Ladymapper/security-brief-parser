# Bronze layer : save raw inout
import json
from datetime import datetime

def save_bronze(raw_text, folder="bronze"):
    """
    Saves the raw weekly brief to the Bronze layer.
    """

    os.makedirs(folder, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    filepath = os.path.join(folder, f"brief_raw_{timestamp}.txt")

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(raw_text)

    print(f"Bronze saved: {filepath}")

    return filepath
