from datetime import datetime

def save_bronze(raw_text):
    """
    Bronze layer:
    Store the raw text in memory instead of writing to disk.
    """

    bronze_data = {
        "timestamp": datetime.now().isoformat(),
        "raw_text": raw_text
    }

    return bronze_data
