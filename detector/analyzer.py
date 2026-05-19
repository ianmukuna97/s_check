import re
from dataclasses import dataclass, field

SCAM_PATTERNS = {
    "urgency_pressure": {
        "weight": 25,
        "patterns": [
            r"act now", r"limited time", r"expires today",
            r"urgent", r"immediately", r"don't delay", r"last chance"
        ]
    },
    "financial_lure": {
        "weight": 30,
        "patterns": [
            r"you('ve| have) won", r"claim your (prize|reward|money)",
            r"free money", r"send (ksh|usd|kes|money)",
            r"mpesa", r"wire transfer", r"bitcoin", r"crypto wallet",
            r"bank details", r"account number"
        ]
    },
    "impersonation": {
        "weight": 25,
        "patterns": [
            r"safaricom", r"kenya revenue authority", r"kra",
            r"your bank", r"paypal security", r"verify your account",
            r"confirm your (pin|password|details)"
        ]
    },
    "personal_info_harvest": {
        "weight": 20,
        "patterns": [
            r"id number", r"national id", r"send (your|ur) (pin|password)",
            r"otp", r"verification code", r"share the code",
            r"click this link", r"login here"
        ]
    },
    "too_good_to_be_true": {
        "weight": 30,
        "patterns": [
            r"\d{4,} (ksh|dollars|usd|kes)", r"million",
            r"lottery", r"inheritance", r"you are selected",
            r"congratulations"
        ]
    },
}

SAFE_SIGNALS = [
    r"invoice attached", r"meeting at", r"please find",
    r"regards", r"sincerely",
    r"thank you for your (order|purchase)"
]


@dataclass
class AnalysisResult:
    score: int = 0
    risk_level: str = "safe"
    flags: list = field(default_factory=list)
    explanation: str = ""
    is_scam: bool = False


def analyze_message(text: str) -> AnalysisResult:
    result = AnalysisResult()
    text_lower = text.lower()
    
    safe_hits = sum(1 for p in SAFE_SIGNALS if re.search(p, text_lower))
    score = max(0, -10 * safe_hits)
    
    for category, data in SCAM_PATTERNS.items():
        hits = [p for p in data['patterns'] if re.search(p, text_lower)]
        if hits:
            score += data['weight'] * len(hits)
            result.flags.append({
                "category": category.replace("_", " ").title(),
                "matched": hits[:3],
                "severity": "high" if data["weight"] >= 25 else "medium"
            })
    
    result.score = min(score, 100)
    
    if result.score >= 70:
        result.risk_level = "scam"
        result.is_scam = True
        result.explanation = "High probability scam. Do not respond or send any money."
    elif result.score >= 40:
        result.risk_level = "suspicious"
        result.explanation = "Suspicious. Verify through official channels."
    elif result.score >= 15:
        result.risk_level = "caution"
        result.explanation = "Mild warning signs. Proceed carefully."
    else:
        result.risk_level = "safe"
        result.explanation = "No obvious scam patterns detected."
    
    return result
