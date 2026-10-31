
import re
from urllib.parse import urlparse


def inspect_url(raw_url):
    """Check visible URL text for selected warning signs."""
    url = raw_url.strip()
    findings = []

    if not url:
        return ["No URL entered."]

    candidate = url if "://" in url else "http://" + url

    try:
        parsed = urlparse(candidate)
        host = (parsed.hostname or "").lower()
    except ValueError:
        return ["This text is not a valid URL format."]

    if not host:
        return ["Could not identify a hostname."]

    if "@" in candidate:
        findings.append("Contains an @ symbol; inspect carefully.")

    if len(url) > 100:
        findings.append("Unusually long URL (over 100 characters).")

    if re.fullmatch(r"(?:\d{1,3}\.){3}\d{1,3}", host):
        findings.append(
            "Uses an IP address instead of a familiar domain."
        )

    labels = [part for part in host.split(".") if part]
    if len(labels) >= 5:
        findings.append(
            "Contains many hostname segments/subdomains."
        )

    if "xn--" in host:
        findings.append("Contains a punycode-style hostname.")

    if parsed.scheme.lower() == "http":
        findings.append(
            "Uses HTTP. HTTPS alone does not prove trust."
        )

    if not findings:
        findings.append(
            "No listed warning signs found. This does NOT prove safety."
        )

    return findings


def has_warnings(findings):
    """Identify whether the result contains warning signs."""
    info_messages = (
        "No URL entered.",
        "Could not identify a hostname.",
        "This text is not a valid URL format.",
        "No listed warning signs found."
    )

    return not any(
        findings[0].startswith(message)
        for message in info_messages
    )


def main():
    print("=" * 45)
    print("EWB PHISHING URL AWARENESS CHECKER")
    print("Text checks only - URLs are never opened.")
    print("=" * 45)

    while True:
        raw_url = input(
            "\nEnter a sample URL (or type q to quit): "
        )

        if raw_url.strip().lower() in ("q", "quit", "exit"):
            print("\nGoodbye! Stay alert online.")
            break

        findings = inspect_url(raw_url)

        print("\nResult:")
        for item in findings:
            print("- " + item)

        if findings[0] in (
            "No URL entered.",
            "Could not identify a hostname.",
            "This text is not a valid URL format."
        ):
            print("\nInput could not be assessed. Please check the URL format.")

        elif has_warnings(findings):
            print(
                f"\nREVIEW CAREFULLY: "
                f"{len(findings)} warning sign(s) found."
            )

        else:
            print("\nNo warning signs were detected by these checks.")
            print("This does NOT prove that the URL is safe.")


if __name__ == "__main__":
    main()
