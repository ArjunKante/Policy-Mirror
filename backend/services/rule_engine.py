def budget_impact(user):
    impact = {}
    explanation = []

    age = user.age
    income = user.income
    status = user.status

    # Tax logic
    if income <= 700000:
        impact["tax_impact"] = "No tax liability"
        impact["financial_savings"] = "₹15,000–₹25,000/year"
        explanation.append("Income below ₹7L qualifies for full tax rebate")
    else:
        impact["tax_impact"] = "Standard tax applies"
        impact["financial_savings"] = "Minimal direct savings"

    # Education logic
    if status == "student" and 17 <= age <= 25:
        impact["education_benefit"] = "+22%"
        explanation.append("Student benefits from increased education allocation")
    else:
        impact["education_benefit"] = "No direct education benefit"

    # Health logic
    if age >= 60:
        impact["health_risk"] = "Medium"
        explanation.append("Senior citizens receive increased healthcare focus")
    else:
        impact["health_risk"] = "Low"

    return impact, explanation
