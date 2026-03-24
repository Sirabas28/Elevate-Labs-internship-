
import pandas as pd
import argparse

# IMPORTS
from parser import parse_apache, parse_ssh
from detector import detect_bruteforce, detect_dos
from visualizer import plot_top_ips
from reporter import generate_report, export_csv

# CLI arguments
parser = argparse.ArgumentParser()
parser.add_argument("--apache", default="access.log")
parser.add_argument("--ssh", default="auth.log")
args = parser.parse_args()

# Parse logs (MUST COME FIRST)
apache_df = parse_apache(args.apache)
ssh_df = parse_ssh(args.ssh)

# Convert time column
#apache_df['time'] = pd.to_datetime(
#    apache_df['time'],
#    errors='coerce'
#)

# Drop invalid rows
#apache_df = apache_df.dropna(subset=['time'])

# Set index
#apache_df.set_index('time', inplace=True)

# Resample (requests per minute)
#traffic = apache_df.resample('1min').count()

#print("\nTraffic per minute:\n", traffic['ip'])


# Detect attacks
brute = detect_bruteforce(ssh_df)
dos = detect_dos(apache_df)

print("Brute Force:\n", brute)
print("DoS:\n", dos)

# Visualization
plot_top_ips(apache_df)

# Report
generate_report(brute, dos)
export_csv(apache_df)

print("\n=== 🚨 Brute Force Attacks ===")
for ip, count in brute.items():
    print(f"[HIGH] {ip} → {count} attempts")

print("\n=== 🚨 DoS Attacks ===")
for ip, count in dos.items():
    print(f"[MEDIUM] {ip} → {count} requests")
