import json
import os

def load_attempts():
    if os.path.exists("attempts.json"):
        with open("attempts.json", "r") as file:
            return json.load(file)
    return []

def save_attempts(attempts):
    with open("attempts.json", "w") as file:
        json.dump(attempts, file, indent=4)

def summary_data(difficulty, total_attempts, correct_guess, total_time, attempt_datetime):
    return {
        'difficulty': difficulty,
        'total_attempts': total_attempts,
        'correct_number': correct_guess,
        'total_time': round(total_time, 2),
        'attempt_datetime': attempt_datetime
    }

def sorted_score_list(score_list):
    return sorted(score_list, key=lambda x: x['total_attempts'])