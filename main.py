
from incident_analyzer import analyze_incident
from risk_assessment import assess_risk
from prompt_engine import generate_prompt
from ai_engine import generate_ai_report


def main():

    print("=" * 60)
    print("    AI CYBERSECURITY INCIDENT RESPONSE ASSISTANT")
    print("=" * 60)
    print("Python | Cybersecurity | Prompt Engineering")
    print("Powered by Ollama and Llama 3.2")
    print("=" * 60)

    print("\nUse fictional incident descriptions only.")
    print("Do not enter confidential information.")

    while True:

        description = input(
            "\nDescribe the cybersecurity incident: "
        )

        if description.lower() == "exit":
            print("Thank you for using the assistant!")
            break

        if not description.strip():
            print("Please enter an incident description.")
            continue

        incident = analyze_incident(description)

        severity, risk = assess_risk(incident)

        print("\n" + "=" * 60)
        print("PRELIMINARY INCIDENT ANALYSIS")
        print("=" * 60)

        print("Incident Type:", incident)
        print("Estimated Severity:", severity)
        print("Potential Risk:", risk)

        prompt = generate_prompt(
            description,
            incident,
            severity,
            risk
        )

        print("\n" + "=" * 60)
        print("PROMPT ENGINEERING MODULE")
        print("=" * 60)

        print(prompt)

        print("\nGenerating AI response...")
        print("Please wait...\n")

        report = generate_ai_report(prompt)

        print("=" * 60)
        print("AI INCIDENT RESPONSE REPORT")
        print("=" * 60)

        print(report)

        print("\n" + "=" * 60)
        print("Educational advice only.")
        print("AI recommendations require human review.")
        print("Enter another incident or type exit.")
        print("=" * 60)


if __name__ == "__main__":
    main()

