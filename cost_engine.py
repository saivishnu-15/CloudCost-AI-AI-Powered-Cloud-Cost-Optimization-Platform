from models import Resource


def detect_waste(db):
    resources = db.query(Resource).all()

    results = []

    for r in resources:

        # Idle resource detection
        if r.cpu_utilization < 10:
            results.append({
                "name": r.name,
                "issue": "Idle Resource",
                "suggestion": "Terminate instance",
                "savings": float(round(r.cost_per_month * 0.7, 2)),
                "predicted_next_month_cost": float(round(r.cost_per_month * 1.1, 2)),
                "ai": f"{r.name} is flagged as Idle Resource. Consider optimizing to reduce cost."
            })

        # Underutilized resource detection
        elif r.cpu_utilization < 30:
            results.append({
                "name": r.name,
                "issue": "Underutilized",
                "suggestion": "Right size instance",
                "savings": float(round(r.cost_per_month * 0.3, 2)),
                "predicted_next_month_cost": float(round(r.cost_per_month * 1.05, 2)),
                "ai": f"{r.name} is flagged as Underutilized. Consider optimizing to reduce cost."
            })

    return results