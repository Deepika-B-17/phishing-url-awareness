

# Phishing URL Awareness Checker - Test Report



## Environment



- Python Version: Python 3.13.11

- Operating System: Windows 11

- Test Date: 2026-10-31



## Test Results



| Test | Sample URL | Expected Observation | Actual Observation | Status |

|---|---|---|---|---|

| 1 | https://www.example.com/login | No listed warning signs | No listed warning signs found | PASS |

| 2 | http://192.0.2.10/account | IP address and HTTP warnings | IP address warning and HTTP warning | PASS |

| 3 | http://example.com@sample.invalid/login | @ symbol and HTTP warnings | @ symbol warning and HTTP warning | PASS |

| 4 | https://a.b.c.d.e.example.invalid/path | Many hostname segments | Many hostname segments/subdomains warning | PASS |

| 5 | https://xn--example.invalid/ | Punycode warning | Punycode-style hostname warning | PASS |

| 6 | http://[bad | Invalid URL format handled without crashing | Invalid URL message displayed; program continued | PASS |



## Implemented Improvements



1. Repeated URL checking: Users can inspect multiple sample URLs in one session and type q to quit.

2. Warning summary: The program displays the number of detected warning signs.

3. Malformed input handling: Invalid URL formats are handled without crashing the program.



## Learning Notes



1. An IP address in a URL can be a warning sign and should be inspected carefully.

2. Special characters, unusually long URLs, multiple hostname segments, and punycode can indicate suspicious URL patterns.

3. A URL with no detected warning signs is not necessarily safe. This program performs only basic text-based checks.



## Conclusion



All six test cases passed. The program successfully identified the warning signs included in the test cases and handled malformed input without crashing. It does not visit URLs or guarantee that a URL is safe.



