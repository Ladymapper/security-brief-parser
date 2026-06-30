import os
import json
import pandas as pd
from datetime import datetime


def build_gold(incidents):
    """
    Create summary statistics from the Silver layer.
    """

    df = pd.DataFrame(incidents)

    # Ensure expected columns exist
    expected_columns = [
        "state",
        "category",
        "casualties_killed",
        "casualties_abducted"
    ]

    for col in expected_columns:
        if col not in df.columns:
            df[col] = 0 if "casualties" in col else "Unknown"

    gold = {
        "total_incidents": len(df),

        "by_state":
            df["state"].value_counts().to_dict(),

        "by_category":
            df["category"].value_counts().to_dict(),

        "total_killed":
            int(df["casualties_killed"].fillna(0).sum()),

        "total_abducted":
            int(df["casualties_abducted"].fillna(0).sum()),

        "high_priority":
            df[df["category"].isin(["Kidnapping", "Armed Attack"])]
            .to_dict("records"),

        "arrests_and_ops":
            df[df["category"].isin(
                ["Arrest", "Security Operation", "Rescue"]
            )]
            .to_dict("records"),

        "generated_at":
            datetime.now().isoformat()
    }

    return gold
