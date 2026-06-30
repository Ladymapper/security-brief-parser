# SILVER LAYER - No AI, No API Keys
# Extract incidents into structured JSON
# ==========================================

import os
import re
import json
from datetime import datetime


def extract_silver(raw_text):
    """
    Extract security incidents from the weekly security brief.
    Returns a list of dictionaries.
    """

    incidents = []

    # Each incident starts with a bullet
    bullets = re.findall(r'•\s*(.*?)(?=\n•|\Z)', raw_text, flags=re.S)

    month_map = {
        "January":"01","February":"02","March":"03","April":"04",
        "May":"05","June":"06","July":"07","August":"08",
        "September":"09","October":"10","November":"11","December":"12"
    }

    for bullet in bullets:

        bullet = bullet.replace("\n", " ").strip()

        # ------------------------
        # Date
        # ------------------------
        date = None
        m = re.search(r'(\d{1,2})\s+([A-Za-z]+)\s+(\d{4})', bullet)

        if m:
            day, month, year = m.groups()
            month_num = month_map.get(month)
            if month_num:
                date = f"{year}-{month_num}-{int(day):02d}"

        # ------------------------
        # Time
        # ------------------------
        time = None
        m = re.search(r'(\d{4})LT', bullet)

        if m:
            t = m.group(1)
            time = f"{t[:2]}:{t[2:]}"

        # ------------------------
        # LGA
        # ------------------------
        lga = None
        m = re.search(r';\s*([^;]+LGA)\s*;', bullet)

        if m:
            lga = m.group(1).strip()

        # ------------------------
        # State
        # ------------------------
        state = None

        states = [
            "FCT Abuja",
            "Abuja FCT",
            "Kogi State",
            "Nasarawa State",
            "Kogi",
            "Nasarawa"
        ]

        for s in states:
            if s in bullet:
                state = s.replace(" State", "")
                break

        # ------------------------
        # Category
        # ------------------------
        categories = [
            "Kidnapping",
            "Armed Attack",
            "Arrest",
            "Security Operation",
            "Rescue"
        ]

        category = "Other"

        for c in categories:
            if c.lower() in bullet.lower():
                category = c
                break

        # Rescue detection
        if "rescued" in bullet.lower():
            category = "Rescue"

        # ------------------------
        # Casualties killed
        # ------------------------
        killed = 0

        m = re.search(r'killing\s+(\w+)', bullet.lower())

        if m:
            word = m.group(1)

            numbers = {
                "one":1,
                "two":2,
                "three":3,
                "four":4,
                "five":5,
                "six":6,
                "seven":7,
                "eight":8,
                "nine":9,
                "ten":10
            }

            if word.isdigit():
                killed = int(word)
            elif word in numbers:
                killed = numbers[word]

        # ------------------------
        # Casualties abducted
        # ------------------------
        abducted = 0

        m = re.search(r'abduct(?:ed|ing)\s+(\w+)', bullet.lower())

        if m:
            word = m.group(1)

            numbers = {
                "one":1,
                "two":2,
                "three":3,
                "four":4,
                "five":5,
                "six":6,
                "seven":7,
                "eight":8,
                "nine":9,
                "ten":10
            }

            if word.isdigit():
                abducted = int(word)
            elif word in numbers:
                abducted = numbers[word]

        # ------------------------
        # Summary
        # ------------------------
        summary = bullet.split(";")[-1].strip()

        incidents.append({
            "date": date,
            "time": time,
            "lga": lga,
            "state": state,
            "category": category,
            "summary": summary,
            "casualties_killed": killed,
            "casualties_abducted": abducted
        })

    return incidents
