from app.utils.bmi import calculate_bmi

test_athletes = [
    {"height_cm": 160, "weight_kg": 45},
    {"height_cm": 175, "weight_kg": 70},
    {"height_cm": 180, "weight_kg": 95},
]

for athlete in test_athletes:
    result = calculate_bmi(athlete["height_cm"], athlete["weight_kg"])
    print(f"Height: {athlete['height_cm']}, Weight: {athlete['weight_kg']} → {result}")