# Logrotate Verification

## Configuration
- Configuration file: configs/reportapp
- Rotation policy: daily, 7 rotations
- Maximum log size: 50 MB
- Compression: enabled, with delaycompress
- Rotation method: copytruncate
- Empty logs: not rotated (notifempty)
- Ownership: reportapp:reportapp

## Test Results
- Forced rotation successfully created test.log.1.
- Both test entries were preserved in test.log.1.
- The original test.log was truncated to 0 bytes.
- Both files retained reportapp:reportapp ownership.
- A subsequent forced rotation skipped the empty test.log, as expected.

## Conclusion
The test verified copytruncate behavior, ownership handling,
and the notifempty setting.
