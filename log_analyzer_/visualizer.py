import matplotlib.pyplot as plt

def plot_top_ips(df):
    top_ips = df['ip'].value_counts().head(10)

    if top_ips.empty:
        print("[!] No data available for plotting")
        return

    plt.figure(figsize=(10,5))
    top_ips.plot(kind='bar')
    plt.title("Top IPs")
    plt.xlabel("IP")
    plt.ylabel("Requests")

    plt.savefig("graph.png")   # ✅ save file (important)
    plt.show()                 # ✅ show graph
