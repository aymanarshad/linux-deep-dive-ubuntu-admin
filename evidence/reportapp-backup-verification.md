# ReportApp Automated Backup Verification

## Objective
Implement and verify automated backups using Bash,
rsync, tar, SHA-256 and systemd.

## Backup Configuration
- Backup location: /srv/backup
- Mirror method: rsync
- Archive format: tar.gz
- Backup schedule: Daily at 02:30
- Retention policy: 5 archives
- Integrity verification: SHA-256
- Service: reportapp-backup.service
- Timer: reportapp-backup.timer

## Verification Results
- Backup filesystem mount verified.
- Application files successfully mirrored.
- Compressed backup archive created.
- Archive integrity verified.
- SHA-256 checksums validated successfully.
- Retention policy executed successfully.
- Older archives removed automatically.
- systemd service completed successfully.

## Initial Troubleshooting
The service initially failed with status 203/EXEC
because the installed script lacked a valid shebang.

The script execution issue was corrected and the
backup service subsequently completed successfully.

## Conclusion
Successfully implemented and tested an automated
backup solution with archive integrity verification,
checksum validation and retention management.
