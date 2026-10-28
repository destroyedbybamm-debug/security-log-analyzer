from collections import Counter
from pathlib import Path

LOG_FILE = Path("auth_sample.log")
REPORT_FILE = Path("analysis_report.txt")

def analyze_log():
    if not LOG_FILE.exists():
        print(f"Error: {LOG_FILE} was not found.")
        return

    failed_logins = []
    successful_logins = []

    with LOG_FILE.open("r", encoding="utf-8") as file:
        for line in file:
            if "Failed password" in line:
                failed_logins.append(line.strip())
            elif "Accepted password" in line:
                successful_logins.append(line.strip())

    ip_counts = Counter()

    for entry in failed_logins:
        parts = entry.split()
        if "from" in parts:
            ip_index = parts.index("from") + 1
            if ip_index < len(parts):
                ip_counts[parts[ip_index]] += 1

    report = [
        "=== Security Log Analysis Report ===",
        f"Log file analyzed: {LOG_FILE}",
        f"Failed login attempts: {len(failed_logins)}",
        f"Successful login attempts: {len(successful_logins)}",
        "",
        "Failed login attempts by source IP:",
    ]

    if ip_counts:
        for ip, count in ip_counts.most_common():
            report.append(f"{ip}: {count} failed attempt(s)")
    else:
        report.append("No failed login attempts found.")

    report.extend(["", "Failed login entries:"])
    report.extend(failed_logins or ["None"])

    report_text = "\n".join(report)

    print(report_text)
    REPORT_FILE.write_text(report_text + "\n", encoding="utf-8")
    print(f"\nReport saved to: {REPORT_FILE}")

if __name__ == "__main__":
    analyze_log()
