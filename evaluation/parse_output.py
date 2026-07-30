def normalize_type(value):
    value = value.lower().strip()

    allowed_types = [
        "not_cyberbullying",
        "gender",
        "religion",
        "age",
        "ethnicity",
        "other_cyberbullying"
    ]

    # Convert common Gemini outputs
    if value == "other":
        return "other_cyberbullying"

    if value == "not bullying" or value == "non-bullying":
        return "not_cyberbullying"

    # If Gemini returns multiple labels, choose the first valid one
    # Example: "religion, ethnicity" -> "religion"
    for label in allowed_types:
        if label in value:
            return label

    return "Unknown"


def parse_prediction(output):

    result = {
        "bullying": "Unknown",
        "type": "Unknown",
        "severity": "Unknown"
    }

    lines = output.split("\n")

    for line in lines:
        line = line.strip()

        if line.lower().startswith("bullying:"):
            value = line.split(":", 1)[1].strip().lower()

            if value in ["yes", "y"]:
                result["bullying"] = "Yes"
            elif value in ["no", "n"]:
                result["bullying"] = "No"
            else:
                result["bullying"] = "Unknown"

        elif line.lower().startswith("type:"):
            value = line.split(":", 1)[1].strip().lower()
            result["type"] = normalize_type(value)

        elif line.lower().startswith("severity:"):
            result["severity"] = line.split(":", 1)[1].strip().capitalize()

    return result