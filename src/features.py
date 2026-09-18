import re
from .preprocessing import normalized_for_model

RULES = {
    "instruction_override": [
        r"\bignore\s+(all\s+)?(previous|prior|above)\s+instructions?\b",
        r"\bdisregard\s+(all\s+)?(previous|prior|above)\b",
        r"\bnew\s+instructions?\b",
        r"\binstructions?\s+(are|have been)\s+(updated|replaced|cancelled)\b",
    ],
    "system_prompt_extraction": [
        r"\breveal\b.*\bsystem\s+prompt\b",
        r"\bshow\b.*\bsystem\s+prompt\b",
        r"\brepeat\b.*\bsystem\s+prompt\b",
        r"\bexact\s+instructions?\b",
    ],
    "role_manipulation": [
        r"\byou\s+are\s+now\b",
        r"\bdeveloper\s+mode\b",
        r"\bunrestricted\s+mode\b",
        r"\bdo\s+anything\s+now\b",
    ],
    "context_manipulation": [
    r"\btreat\s+(this|the following)\s+(text|message|content)\s+as\s+(trusted|system)\b",
    r"\btrusted\s+system\s+instructions?\b",
    r"\bhigher\s+priority\s+than\s+(previous|earlier)\s+instructions?\b",
    r"\boverride\s+(the|all)\s+(previous|existing)\s+instructions?\b",
    r"\bignore\s+the\s+original\s+(rules|instructions?)\b",
    ],
    "indirect_injection": [
        r"<\s*(script|img|div)\b",
        r"\[document\s+start\]",
        r"\[email\s+body\]",
        r"\bhidden\s+(text|instruction)\b",
        r"\bsearch\s+result\s+snippet\b",
    ],
    "obfuscation": [
        r"\bbase64\b", r"\bdecode\b", r"\batob\s*\(", r"\bfromhex\b",
    ],
}

def rule_hits(text: str):
    normalized = normalized_for_model(text)
    hits = []
    categories = []
    for category, patterns in RULES.items():
        for pattern in patterns:
            if re.search(pattern, normalized, flags=re.I | re.S):
                hits.append(pattern)
                categories.append(category)
                break
    return sorted(set(categories)), hits
