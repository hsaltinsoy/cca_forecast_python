from datetime import datetime, date


class Entry:
    def __init__(self, data: dict):
        self.data = data
        self.date_time = datetime.fromisoformat(data["date_time"].replace('Z', '+00:00'))
        self.average_temperature = data.get("average_temperature")
        self.probability_of_rain = data.get("probability_of_rain")

    def get_day(self) -> date:
        return self.date_time.date()
