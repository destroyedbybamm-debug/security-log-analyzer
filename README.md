# Security Log Analyzer

## Overview
A Python-based cybersecurity tool that analyzes sample authentication logs to identify failed login attempts, count successful logins, and group failed attempts by source IP address.

## Features
- Reads authentication logs from a text file
- Counts failed and successful login attempts
- Groups failed login attempts by source IP
- Displays the analysis in the terminal
- Generates a report saved to a text file
- Handles a missing input file with an error message

## Technologies
- Python 3
- `collections.Counter`
- `pathlib`

## How to Run
1. Clone or download this repository.
2. Open a terminal in the project directory.
3. Run:

   `python3 log_analyzer.py`

The script reads `auth_sample.log` and creates `analysis_report.txt`.

## Sample Results
Using the included fictional log entries, the analyzer identifies:
- 5 failed login attempts
- 1 successful login
- 3 failed attempts from `192.168.1.50`
- 2 failed attempts from `10.0.0.8`

## Project Files
- `log_analyzer.py` — log analysis script
- `auth_sample.log` — fictional authentication log entries
- `analysis_report.txt` — generated analysis report

## Security Scope
This project uses synthetic sample data for educational purposes. Repeated failed logins can warrant investigation, but this tool does not determine whether an IP address is malicious.

## Future Improvements
- Add configurable alert thresholds
- Export reports to CSV
- Support additional log formats
- Add automated tests

## Author
Cybersecurity student building practical Python and security-analysis projects.
