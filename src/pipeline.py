from src.bronze import save_bronze
from src.silver import extract_silver
from src.gold import build_gold


def run_pipeline(raw_text):
    """
    Run the complete Bronze → Silver → Gold pipeline.
    """

    bronze = save_bronze(raw_text)

    incidents = extract_silver(raw_text)

    gold = build_gold(incidents)

    return bronze, incidents, gold
