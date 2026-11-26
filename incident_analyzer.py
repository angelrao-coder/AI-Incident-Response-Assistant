
def analyze_incident(description):

    text = description.lower()

    categories = {
        "Phishing": [
            "phishing", "suspicious email",
            "fake link", "fake website"
        ],

        "Malware": [
            "malware", "virus", "trojan",
            "infected"
        ],

        "Ransomware": [
            "ransomware", "encrypted files",
            "ransom"
        ],

        "Unauthorized Access": [
            "unauthorized login", "unknown login",
            "account hacked", "unknown device"
        ],

        "Data Breach": [
            "data breach", "data leak",
            "stolen data", "exposed data"
        ],

        "Denial of Service": [
            "ddos", "dos attack",
            "traffic overload"
        ]
    }

    matches = {}

    for category, keywords in categories.items():
        matches[category] = sum(
            word in text for word in keywords
        )

    if max(matches.values()) == 0:
        return "Unknown Incident"

    return max(matches, key=matches.get)
