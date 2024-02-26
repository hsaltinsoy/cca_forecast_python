from collections import defaultdict

from src.model import Entry, Summary


def summarize_forecast(data):
    group_day = defaultdict(list)
    summaries = {}

    # Group entries by day
    for datum in data:
        entry = Entry(data=datum)
        group_day[entry.get_day()].append(entry)

    # Process each day
    for day, entries in group_day.items():
        summary = Summary(entries)
        summary.process()
        all_temperatures = [entry.average_temperature for entry in entries]

        summary = {
            # if no morning data, report insufficient data
            "morning_average_temperature": "Insufficient forecast data" if not summary.morning_temperature else round(
                sum(summary.morning_temperature) / len(summary.morning_temperature)),
            "morning_chance_of_rain": "Insufficient forecast data" if not summary.morning_rain else round(
                sum(summary.morning_rain) / len(summary.morning_rain), 2),
            # if no afternoon data, report insufficient data
            "afternoon_average_temperature": "Insufficient forecast data" if not summary.afternoon_temperature else round(
                sum(summary.afternoon_temperature) / len(summary.afternoon_temperature)),
            "afternoon_chance_of_rain": "Insufficient forecast data" if not summary.afternoon_rain else round(
                sum(summary.afternoon_rain) / len(summary.afternoon_rain), 2),
            "high_temperature": max(all_temperatures),
            "low_temperature": min(all_temperatures)
        }

        # format reader-friendly date
        day_name = day.strftime("%A %B %d").replace(" 0", " ")

        summaries[day_name] = summary

    return summaries

