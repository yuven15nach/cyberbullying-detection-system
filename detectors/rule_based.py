import re


INSULT_WORDS = [
    "stupid",
    "idiot",
    "idiots",
    "dumb",
    "moron",
    "loser",
    "ugly",
    "worthless",
    "useless",
    "bitch",
    "whore",
    "fool"
]

HATE_WORDS = [
    "hate",
    "racist",
    "sexist",
    "terrorist",
    "terrorism"
]

IDENTITY_TERMS = [
    "muslim",
    "muslims",
    "islam",
    "islamic",
    "christian",
    "black",
    "white",
    "gay",
    "girls",
    "women",
    "nigger",
    "niggers"
]

EXCLUSION_PHRASES = [
    "nobody likes you",
    "no one likes you",
    "go away",
    "no one wants you",
    "nobody wants you",
    "you do not belong",
    "you don't belong"
]


def contains_word(text, word):
    pattern = r"\b" + re.escape(word) + r"\b"
    return re.search(pattern, text) is not None


def classify_rule_based(text):
    text = text.lower()

    score = 0
    detected_type = "not_cyberbullying"

    # Direct insult detection
    for word in INSULT_WORDS:
        if contains_word(text, word):
            score += 2
            detected_type = "other_cyberbullying"

    # Hate-related words
    for word in HATE_WORDS:
        if contains_word(text, word):
            score += 2
            detected_type = "other_cyberbullying"

    # Exclusion phrases
    for phrase in EXCLUSION_PHRASES:
        if phrase in text:
            score += 3
            detected_type = "other_cyberbullying"

    # Identity-related terms
    for word in IDENTITY_TERMS:
        if contains_word(text, word):
            score += 1

            if word in ["muslim", "muslims", "islam", "islamic", "christian"]:
                detected_type = "religion"

            elif word in ["black", "white", "nigger", "niggers"]:
                detected_type = "ethnicity"

            elif word in ["gay", "girls", "women"]:
                detected_type = "gender"

    if score >= 2:
        return {
            "bullying": "Yes",
            "type": detected_type
        }

    return {
        "bullying": "No",
        "type": "not_cyberbullying"
    }