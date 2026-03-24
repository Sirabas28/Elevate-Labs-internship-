def export_csv(df):
    df.to_csv("output.csv")

def generate_report(brute, dos):
    with open("report.txt", "w") as f:
        f.write("=== Incident Report ===\n\n")

        f.write("Brute Force Attempts:\n")
        for ip, count in brute.items():
            f.write(f"{ip} → {count}\n")

        f.write("\nDoS Attempts:\n")
        for ip, count in dos.items():
            f.write(f"{ip} → {count}\n")
