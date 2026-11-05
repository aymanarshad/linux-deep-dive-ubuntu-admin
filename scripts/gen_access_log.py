

#!/usr/bin/env python3
"""Generate a deterministic ReportApp access log (one day) for analysis practice."""
import random
import sys
import time

START = 1741564800  # 2025-03-10 00:00:00 UTC

NORMAL = [
    ("10.20.1.15", "GET", "/reports", 200, 512, "Mozilla/5.0 (X11; Linux x86_64) Firefox/123.0", 1200),
    ("10.20.1.22", "GET", "/health", 200, 34, "monitoring-agent/2.1", 800),
    ("10.20.3.7", "GET", "/reports", 200, 512, "python-requests/2.31.0", 450),
    ("10.20.3.7", "POST", "/reports/upload", 201, 64, "python-requests/2.31.0", 100),
    ("192.0.2.66", "GET", "/admin", 404, 22, "sqlmap/1.7.2", 180),
    ("192.0.2.66", "GET", "/wp-login.php", 404, 22, "sqlmap/1.7.2", 120),
    ("198.51.100.23", "GET", "/.env", 404, 22, "curl/7.88.1", 50),
]
INCIDENT = ("10.20.2.40", "GET", "/reports/export", 500, 87, "Mozilla/5.0 (Windows NT 10.0) Edge/122.0", 150)


def fmt(ts, ip, method, path, status, size, agent):
    stamp = time.strftime("%d/%b/%Y:%H:%M:%S +0000", time.gmtime(ts))
    return '%s - - [%s] "%s %s HTTP/1.1" %d %d "-" "%s"' % (ip, stamp, method, path, status, size, agent)


rng = random.Random(2025)
normal = []
for ip, method, path, status, size, agent, count in NORMAL:
    normal.extend([(ip, method, path, status, size, agent)] * count)
rng.shuffle(normal)

events = [(START + i * 29, rec) for i, rec in enumerate(normal)]
ip, method, path, status, size, agent, count = INCIDENT
events += [(START + 14 * 3600 + i * 12, (ip, method, path, status, size, agent)) for i in range(count)]
events.sort(key=lambda e: e[0])

out = sys.argv[1] if len(sys.argv) > 1 else "access-sample.log"
with open(out, "w", encoding="utf-8") as fh:
    for ts, rec in events:
        fh.write(fmt(ts, *rec) + "\n")
print("wrote %d lines to %s" % (len(events), out))
