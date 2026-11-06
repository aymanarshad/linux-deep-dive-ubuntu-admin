# ReportApp Service Troubleshooting and Recovery

## Objective
Diagnose and recover a failed Python application managed by systemd.

## Initial Problem
- Service: reportapp.service
- Initial state: Failed
- Exit status: 1/FAILURE
- Root cause: Invalid Python syntax in app.py.
- Accidental text was present in the first seven lines.

## Troubleshooting
- Inspected systemd service status and journal logs.
- Examined application source code.
- Ran Python syntax validation.
- Created a backup of the corrupted application.
- Removed the seven invalid leading lines.
- Revalidated Python syntax successfully.

## Recovery Verification
- Python compilation: Passed
- systemd service: Active
- Health endpoint: HTTP 200
- Reports endpoint: HTTP 200

## API Testing

### Health Endpoint
GET /health

Response:
{"status": "ok", "host": "AayanPC"}

### Reports Endpoint
GET /reports

Response:
{"reports": ["headcount.csv", "sales-2025-q1.csv", "sales-2025-q2.csv"]}

## Conclusion
Successfully diagnosed and recovered the ReportApp
Python application service using Linux troubleshooting,
Python syntax validation, systemd and curl.
