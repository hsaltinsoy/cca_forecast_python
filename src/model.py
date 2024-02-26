from datetime import datetime, date


class Entry:
    def __init__(self, data: dict):
        self.data = data
        self.date_time = datetime.fromisoformat(data["date_time"].replace('Z', '+00:00'))
        self.average_temperature = data.get("average_temperature")
        self.probability_of_rain = data.get("probability_of_rain")

    def get_day(self) -> date:
        return self.date_time.date()


class Summary:

    def __init__(self, entries):
        self.morning_temperature = []
        self.afternoon_temperature = []
        self.morning_rain = []
        self.afternoon_rain = []
        self.entries = entries

    def process(self):
        for entry in self.entries:
            # collect morning period entries
            if 6 <= entry.date_time.hour < 12:
                self.morning_temperature.append(entry.average_temperature)
                self.morning_rain.append(entry.probability_of_rain)
            # collection afternoon period entries
            elif 12 <= entry.date_time.hour < 18:
                self.afternoon_temperature.append(entry.average_temperature)
                self.afternoon_rain.append(entry.probability_of_rain)