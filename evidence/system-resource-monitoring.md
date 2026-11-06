# Linux System Resource Monitoring

## Objective
Monitor Linux system health, resource utilization,
storage, CPU, memory and running processes.

## System Information
- Operating System: Ubuntu Linux
- Environment: WSL2
- Architecture: x86_64
- CPU: Intel Core i5-7500
- CPU Cores: 4

## System Health
- Uptime: 1 hour 23 minutes
- Load Average: 0.09, 0.23, 0.23

## Memory
- Total RAM: 5.7 GiB
- Used RAM: 1.2 GiB
- Available RAM: 4.6 GiB
- Swap: 2 GiB
- Swap Used: 0

## Storage Monitoring
- Root filesystem: 1 TB
- Application volume: 740 MB
- Log volume: 236 MB
- Backup volume: 265 MB

## Monitoring Commands
- uptime
- lscpu
- free -h
- swapon --show
- df -hT
- lsblk
- ps aux --sort=-%cpu
- ps aux --sort=-%mem

## Observations
- System resource utilization was low.
- Sufficient available memory was observed.
- Swap was not being used.
- Application, log and backup volumes were mounted.
- Windows-mounted drives showed high utilization.

## Conclusion
Successfully performed Linux system health and
resource monitoring using standard administration tools.
