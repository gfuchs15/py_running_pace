from flask import Flask, render_template, request, jsonify
import re

app = Flask(__name__)


def parse_time(time_str):
    """Parse time string in format HH:MM:SS, MM:SS or SS"""
    time_str = time_str.strip()
    parts = list(map(int, re.split("[:]", time_str)))

    if len(parts) == 3:
        return parts[0] * 3600 + parts[1] * 60 + parts[2]
    elif len(parts) == 2:
        return parts[0] * 60 + parts[1]
    elif len(parts) == 1:
        return parts[0]
    else:
        raise ValueError("Invalid time format")


def format_time(seconds):
    """Convert seconds to HH:MM:SS format"""
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    secs = seconds % 60
    if hours > 0:
        return f"{int(hours):02d}:{int(minutes):02d}:{int(secs):02d}"
    else:
        return f"{int(minutes):02d}:{int(secs):02d}"


def calculate_pace(distance_km, time_seconds):
    """Calculate pace in km/h and min/km"""
    if time_seconds <= 0 or distance_km <= 0:
        return None, None

    # km/h
    speed_kmh = (distance_km / time_seconds) * 3600

    # min/km
    pace_per_km = time_seconds / distance_km
    pace_formatted = format_time(int(pace_per_km))

    return round(speed_kmh, 2), pace_formatted


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/calculate_pace", methods=["POST"])
def calculate():
    try:
        time_str = request.form["time"]
        activity = request.form["activity"].lower()

        # Validate activity type
        valid_activities = ["running", "swimming", "biking"]
        if activity not in valid_activities:
            return render_template(
                "index.html", error=f"Activity must be one of {valid_activities}"
            )

        # Parse time
        total_seconds = parse_time(time_str)

        # Define standard distances for each activity (in km)
        distances = {
            "running": {"10K": 10, "HM": 21.097, "Marathon": 42.195},
            "swimming": {"100m": 0.1, "500m": 0.5, "1500m": 1.5, "10K": 10},
            "biking": {"10K": 10, "40K": 40, "100K": 100},
        }

        # Calculate paces for standard distances
        results = []
        for name, distance in distances[activity].items():
            speed, pace = calculate_pace(distance, total_seconds)
            if speed is not None:
                results.append(
                    {
                        "distance": name,
                        "distance_km": distance,
                        "time": format_time(total_seconds),
                        "speed_kmh": speed,
                        "pace_per_km": pace,
                    }
                )

        return render_template("index.html", results=results, activity=activity)

    except Exception as e:
        return render_template("index.html", error=str(e))


if __name__ == "__main__":
    app.run(debug=True)
