def generate_explanation(categories, risk_score, decision):
    reasons = []

    if "instruction_override" in categories:
        reasons.append("Instruction override attempt detected.")

    if "system_prompt_extraction" in categories:
        reasons.append("Possible system prompt extraction attempt detected.")

    if "role_manipulation" in categories:
        reasons.append("Role manipulation pattern detected.")

    if "context_manipulation" in categories:
        reasons.append("Context manipulation pattern detected.")

    if not reasons:
        reasons.append("No known prompt injection pattern detected.")

    if risk_score >= 70:
        severity = "HIGH"
    elif risk_score >= 40:
        severity = "MEDIUM"
    else:
        severity = "LOW"

    return {
        "decision": decision,
        "severity": severity,
        "risk_score": risk_score,
        "reasons": reasons
    }