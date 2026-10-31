# Phishing URL Awareness Checker

## 1. Project Overview

The Phishing URL Awareness Checker is a Python-based command-line application that examines the visible text of a URL for selected warning signs commonly associated with suspicious links.

The project aims to improve user awareness by identifying potentially suspicious URL patterns and encouraging users to review links carefully before interacting with them.

**Important:** This tool performs basic text-based checks only. It does not open URLs, access websites, or guarantee that a URL is safe.

## 2. Features

The application checks for six URL warning signs:

1. **@ Symbol Detection:** Identifies URLs containing the `@` symbol.
2. **URL Length Check:** Flags URLs longer than 100 characters.
3. **IP Address Detection:** Identifies URLs that use an IPv4 address as the hostname.
4. **Multiple Hostname Segments:** Flags hostnames containing five or more labels.
5. **Punycode Detection:** Identifies hostnames containing the `xn--` marker.
6. **HTTP Scheme Detection:** Flags URLs that use HTTP instead of HTTPS.

Additional features:
- Repeated URL checking in one session.
- Warning summary showing the number of detected warning signs.
- Malformed URL input handling.
- Exit option using `q`, `quit`, or `exit`.

## 3. Technologies Used

- **Programming Language:** Python
- **Regular Expressions:** `re`
- **URL Parsing:** `urllib.parse`
- **Interface:** Command Line Interface (CLI)

No external Python packages are required.

## 4. Project Structure

```text
phishing-url-awareness/
|-- phishing_checker.py
|-- README.md
|-- requirements.txt
|-- tests/
|   |-- test_samples.md
|-- screenshots/
    |-- sample_run.png
    |-- test_results.png
```

## 5. Requirements

- Python 3.10 or above.
- Windows, Linux, or macOS terminal.
- No external dependencies.

## 6. How to Run

**Step 1: Clone the repository**

```bash
git clone https://github.com/Deepika-B-17/phishing-url-awareness.git
```

**Step 2: Navigate to the project folder**

```bash
cd phishing-url-awareness
```

**Step 3: Run the application**

```bash
python phishing_checker.py
```

**Step 4: Enter a sample URL**

Enter a URL when prompted. The application displays detected warning signs and a review summary.

To exit, enter:

```text
q
```

## 7. Sample Output

```text
=============================================
EWB PHISHING URL AWARENESS CHECKER
Text checks only - URLs are never opened.
=============================================

Enter a sample URL (or type sq to quit): http://192.0.2.10/account

Result:
- Uses an IP address instead of a familiar domain.
- Uses HTTP. HTTPS alone does not prove trust.

REVIEW CAREFULLY: 2 warning sign(s) found.

Never enter passwords from unexpected links.

Enter a sample URL (or type q to quit): q

Goodbye! Stay alert online.
```

## 8. Testing

The application was tested using six sample cases.

| Test | Description | Result |
|---|---|---|
| 1 | Normal HTTPS URL | PASS |
| 2 | IP address and HTTP | PASS |
| 3 | @ symbol and HTTP | PASS |
| 4 | Multiple hostname segments | PASS |
| 5 | Punycode hostname | PASS |
| 6 | Malformed URL input | PASS |

Detailed test observations are documented in `tests/test_samples.md`.

## 9. Implemented Improvements

Three improvements were implemented:

**A. Repeated URL Checking**

Users can inspect multiple URLs during one execution without restarting the program. The application exits when the user enters `q`, `quit`, or `exit`.

**B. Warning Summary**

The application displays the number of detected warning signs, helping users understand the result more clearly.

**C. Malformed Input Handling**

Invalid URL formats are handled using exception handling so that the application does not unexpectedly terminate.

## 10. Limitations

- The application uses basic URL text analysis rather than machine learning.
- It does not check website reputation or domain registration information.
- It does not access external threat intelligence databases.
- It cannot confirm whether a URL is genuinely malicious.
- A URL with no detected warning signs may still be unsafe.
- HTTPS does not guarantee that a website is trustworthy.

## 11. Ethical Use

This project is developed for educational and cybersecurity awareness purposes.

- Only sample URL strings are used for testing.
- URLs are not opened or visited.
- No personal information or login credentials are collected.
- The application does not perform website scanning or network requests.

## 12. Author

**Name:** DEEPIKA B

**Project:** Phishing URL Awareness Checker

**Language:** Python