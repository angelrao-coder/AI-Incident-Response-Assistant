
def assess_risk(incident_type):

    risk_data = {

        "Phishing": (
            "MEDIUM",
            "Credential theft and financial fraud"
        ),

        "Malware": (
            "HIGH",
            "System compromise and data loss"
        ),

        "Ransomware": (
            "CRITICAL",
            "Loss of access to important files"
        ),

        "Unauthorized Access": (
            "HIGH",
            "Account compromise and privacy loss"
        ),

        "Data Breach": (
            "CRITICAL",
            "Exposure of confidential information"
        ),

        "Denial of Service": (
            "HIGH",
            "Service disruption and downtime"
        )
    }

    return risk_data.get(
        incident_type,
        ("UNKNOWN", "Further investigation required")
    )

