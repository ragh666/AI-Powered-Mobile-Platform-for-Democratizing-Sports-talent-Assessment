def calculate_bmi(height_cm: float, weight_kg: float) -> dict:
    """
    Calculates BMI and categorizes it.

    Args:
        height_cm (float): Height in centimeters
        weight_kg (float): Weight in kilograms

    Returns:
        dict: {
            "bmi": float,
            "category": str
        }
    """
    if height_cm <= 0 or weight_kg <= 0:
        raise ValueError("Height and weight must be greater than zero.")

    # Convert height from cm to meters
    height_m = height_cm / 100

    # BMI formula
    bmi = weight_kg / (height_m ** 2)
    bmi = round(bmi, 2)

    # BMI category
    if bmi < 18.5:
        category = "Underweight"
    elif bmi < 25:
        category = "Normal weight"
    elif bmi < 30:
        category = "Overweight"
    else:
        category = "Obese"

    return {
        "bmi": bmi,
        "category": category
    }