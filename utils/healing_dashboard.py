import json
import os
from collections import Counter
from datetime import datetime


class HealingDashboard:

    LOG_FILE = os.path.join("reports", "healing_log.json")
    OUTPUT_FILE = os.path.join("reports", "healing_dashboard.html")

    @staticmethod
    def generate():

        os.makedirs("reports", exist_ok=True)

        # -------------------------
        # Load Healing Log
        # -------------------------

        logs = []

        print("\nDashboard loading:")
        print(os.path.abspath(HealingDashboard.LOG_FILE))

        if os.path.exists(HealingDashboard.LOG_FILE):

            try:

                with open(
                        HealingDashboard.LOG_FILE,
                        "r",
                        encoding="utf-8"
                ) as f:

                    logs = json.load(f)

                print(f"Dashboard loaded {len(logs)} healing events.")

            except Exception as e:

                print("Dashboard load failed:", e)

                logs = []
        else:

            print("Dashboard log file not found.")

        # -------------------------
        # Statistics
        # -------------------------

        total = len(logs)

        sources = Counter(
            log.get("source", "Unknown")
            for log in logs
        )

        repository = sources.get("Repository", 0)
        strategy = sources.get("Strategy", 0)
        fuzzy = sources.get("Fuzzy", 0)
        ai = sources.get("AI", 0)

        # -------------------------
        # Recent Healing Rows
        # -------------------------

        rows = ""

        for log in reversed(logs[-20:]):

            rows += f"""
            <tr>
                <td>{log.get("timestamp","")}</td>
                <td>{log.get("original","")}</td>
                <td>{log.get("recovered","")}</td>
                <td>{log.get("source","")}</td>
            </tr>
            """

        # -------------------------
        # HTML
        # -------------------------

        html = f"""
<!DOCTYPE html>
<html>

<head>

<title>Self-Healing Dashboard</title>

<style>

body {{
    font-family: Arial;
    background:#f4f6f8;
    margin:40px;
}}

h1 {{
    color:#2c3e50;
}}

.card {{
    display:inline-block;
    width:180px;
    padding:20px;
    margin:10px;
    border-radius:8px;
    background:white;
    box-shadow:0 2px 6px rgba(0,0,0,.15);
    text-align:center;
}}

.number {{
    font-size:32px;
    color:#0078D7;
    font-weight:bold;
}}

table {{
    width:100%;
    border-collapse:collapse;
    margin-top:30px;
}}

th {{
    background:#0078D7;
    color:white;
    padding:10px;
}}

td {{
    border:1px solid #ddd;
    padding:10px;
}}

tr:nth-child(even){{
    background:#f2f2f2;
}}

.footer {{
    margin-top:30px;
    color:gray;
}}

</style>

</head>

<body>

<h1>Enterprise Self-Healing Dashboard</h1>

<div class="card">
<div>Total Healings</div>
<div class="number">{total}</div>
</div>

<div class="card">
<div>Repository</div>
<div class="number">{repository}</div>
</div>

<div class="card">
<div>Strategy</div>
<div class="number">{strategy}</div>
</div>

<div class="card">
<div>Fuzzy</div>
<div class="number">{fuzzy}</div>
</div>

<div class="card">
<div>AI</div>
<div class="number">{ai}</div>
</div>

<h2>Recent Healing Events</h2>

<table>

<tr>
<th>Timestamp</th>
<th>Original Locator</th>
<th>Recovered Locator</th>
<th>Recovery Source</th>
</tr>

{rows}

</table>

<div class="footer">

Generated on:
{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}

</div>

</body>

</html>
"""

        with open(
                HealingDashboard.OUTPUT_FILE,
                "w",
                encoding="utf-8"
        ) as f:

            f.write(html)

        print(
            f"\nHealing Dashboard generated : {HealingDashboard.OUTPUT_FILE}"
        )