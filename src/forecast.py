from datetime import datetime
from collections import defaultdict


def summarize_forecast(data):
    grp_day = defaultdict(list)
    summaries = {}

    # Group entries by day
    for entry in data:
        entry_time = datetime.fromisoformat(entry["date_time"].replace('Z', '+00:00'))
        key = entry_time.date()
        grp_day[key].append(entry)

    # Process each day
    for day, entries in grp_day.items():
        morning_temperature, morning_rain, afternoon_temperature, afternoon_rain = [], [], [], []
        all_temperatures = [entry["average_temperature"] for entry in entries]

        for entry in entries:
            entry_time = datetime.fromisoformat(entry["date_time"].replace('Z', '+00:00'))
            # collect morning period entries
            if 6 <= entry_time.hour < 12:
                morning_temperature.append(entry["average_temperature"])
                morning_rain.append(entry["probability_of_rain"])
            # collection afternoon period entries
            elif 12 <= entry_time.hour < 18:
                afternoon_temperature.append(entry["average_temperature"])
                afternoon_rain.append(entry["probability_of_rain"])

        summary = {
            # if no morning data, report insufficient data
            "morning_average_temperature": "Insufficient forecast data" if not morning_temperature else round(
                sum(morning_temperature) / len(morning_temperature)),
            "morning_chance_of_rain": "Insufficient forecast data" if not morning_rain else round(
                sum(morning_rain) / len(morning_rain), 2),
            # if no afternoon data, report insufficient data
            "afternoon_average_temperature": "Insufficient forecast data" if not afternoon_temperature else round(
                sum(afternoon_temperature) / len(afternoon_temperature)),
            "afternoon_chance_of_rain": "Insufficient forecast data" if not afternoon_rain else round(
                sum(afternoon_rain) / len(afternoon_rain), 2),
            "high_temperature": max(all_temperatures),
            "low_temperature": min(all_temperatures)
        }

        # format reader-friendly date
        day_name = day.strftime("%A %B %d").replace(" 0", " ")

        summaries[day_name] = summary

    return summaries

