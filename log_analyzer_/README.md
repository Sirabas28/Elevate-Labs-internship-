# 🔐 Log File Analyzer for Intrusion Detection

## 📌 Overview
This project is a Python-based log analyzer designed to detect suspicious activities from system logs such as Apache access logs and SSH authentication logs.

It identifies potential security threats like:
- Brute-force login attempts
- Denial-of-Service (DoS) attacks

---

## 🎯 Objective
To build a lightweight intrusion detection tool that:
- Parses log files
- Detects abnormal patterns
- Visualizes traffic behavior
- Generates reports for analysis

---

## ⚙️ Technologies Used
- Python 3
- pandas
- matplotlib
- regex (re module)

---

## 🚀 Features
- ✅ Parse Apache and SSH logs  
- ✅ Detect brute-force attacks  
- ✅ Detect DoS patterns based on request frequency  
- ✅ Visualize top IP addresses  
- ✅ Export results to CSV  
- ✅ Generate incident reports (TXT)  

---

## 📂 Project Structure

```

log_analyzer/
│── main.py
│── parser.py
│── detector.py
│── visualizer.py
│── reporter.py
│── access.log
│── auth.log
│── graph.png
│── report.txt
│── output.csv
│── README.md

````

---

## ▶️ How to Run

### 1. Activate virtual environment
```bash
source logenv/bin/activate
````

### 2. Run the program

```bash
python main.py
```

---

## 📊 Output

After execution, the following outputs are generated:

* 📌 Terminal alerts (detected attacks)
* 📈 `graph.png` → Visualization of top IPs
* 📄 `report.txt` → Incident report
* 📊 `output.csv` → Processed log data


---

## 🧠 Methodology

1. Collect logs (Apache & SSH)
2. Parse logs using regex
3. Convert data into structured format (pandas)
4. Detect suspicious patterns:

   * Repeated login failures → Brute Force
   * High request frequency → DoS
5. Visualize traffic patterns
6. Generate reports

---

## 📌 Limitations

* Time-based analysis is simplified
* Detection thresholds are static
* No real-time monitoring (batch processing)

---

## 🚀 Future Improvements

* Real-time log monitoring
* Integration with threat intelligence APIs
* Geo-location of IP addresses
* Web-based dashboard

---

## 🏁 Conclusion

This project demonstrates a basic intrusion detection system that analyzes logs, detects threats, and provides actionable insights using Python.

---

## 👨‍💻 Author

Mohammed Nihal

````

---

