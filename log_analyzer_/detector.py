import requests

# 🔹 OPTIONAL (for later use — keep but don't use now)
def check_ip_blacklist(ip):
    try:
        url = "https://api.abuseipdb.com/api/v2/check"
        headers = {
            "Key": "YOUR_API_KEY",   # replace later if needed
            "Accept": "application/json"
        }
        params = {"ipAddress": ip}

        response = requests.get(url, headers=headers, params=params, timeout=5)
        return response.json()
    except Exception as e:
        return {"error": str(e)}

# 🔹 Brute Force Detection
def detect_bruteforce(df):
    counts = df['ip'].value_counts()
    return counts[counts > 5]

# 🔹 DoS Detection
def detect_dos(df):
    counts = df['ip'].value_counts()
    return counts[counts > 20]

# 🔹 Scanning Detection
def detect_scanning(df):
    return df.groupby('ip')['url'].nunique().sort_values(ascending=False)
