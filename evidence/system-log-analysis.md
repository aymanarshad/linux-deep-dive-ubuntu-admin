# Linux System Logging and Monitoring

## Objective
Investigate Linux system logs, journal entries,
authentication events and service errors.

## Log Sources Investigated
- /var/log/
- /var/log/auth.log
- /var/log/syslog
- /var/log/kern.log
- systemd journal

## Investigation Results
- System journal size: 112 MB.
- Reviewed recent system errors.
- Investigated authentication and sudo activity.
- Examined recent system events.
- Identified historical ReportApp service failure.
- Identified historical backup service execution failure.
- Observed WSL graphics-related kernel errors.
- Observed Chrony clock synchronization warnings.

## Findings and Troubleshooting
ReportApp previously failed because of invalid
Python syntax. The application source was corrected,
and its service was subsequently verified active.

The backup service previously encountered an
Exec format error due to a script execution issue.
The shebang was corrected.

## Security Relevance
Authentication logs provide an audit trail of
privileged commands and administrative sessions.

System journals help administrators investigate
service failures, application errors and kernel events.

## Conclusion
Successfully investigated Linux logging mechanisms,
reviewed system errors and identified historical
service failures using journalctl and /var/log.
