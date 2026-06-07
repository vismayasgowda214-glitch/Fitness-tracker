from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/report", methods=["POST"])
def report():
    name = request.form.get("name")
    age = request.form.get("age")

    # ✅ Safe conversion for height (cm) and weight (kg)
    try:
        height_cm = float(request.form.get("height", 0))
        weight = float(request.form.get("weight", 0))
    except (TypeError, ValueError):
        height_cm, weight = 0, 0

    # Convert cm → meters
    height = height_cm / 100 if height_cm > 0 else 0

    # ✅ Optional inputs
    try:
        water = float(request.form.get("water", 0))
    except (TypeError, ValueError):
        water = 0 add .

    try:
        exercise = float(request.form.get("exercise", 0))
    except (TypeError, ValueError):
        exercise = 0

    # ✅ BMI calculation
    bmi = weight / (height * height) if height > 0 else 0
    bmi = round(bmi, 1)

    # ✅ Category + Tip + Color
    if bmi < 18.5:
        category = "Underweight"
        tip = "Eat nutritious food and increase protein intake."
        color = "#3498db"  # blue
    elif bmi < 25:
        category = "Normal"
        tip = "Great job! Maintain your current lifestyle."
        color = "#2ecc71"  # green
    elif bmi < 30:
        category = "Overweight"
        tip = "Add regular exercise and control diet."
        color = "#f39c12"  # orange
    else:
        category = "Obese"
        tip = "Consult a doctor and follow a structured fitness plan."
        color = "#e74c3c"  # red

    return render_template(
        "report.html",
        name=name,
        age=age,
        bmi=bmi,
        category=category,
        water=water,
        exercise=exercise,
        tip=tip,
        color=color
    )

if __name__ == "__main__":
    app.run(debug=True)
