# Linux Access Control Lists (ACL) Management

## Objective
Practice granular file and directory permissions using Linux ACLs.

## Environment
- Directory: /srv/acl-lab
- File: /srv/acl-lab/project.txt
- Owner: ayman
- Group: analysts
- Additional user: dave

## ACL Configuration
- Dave was granted execute-only access to the directory.
- Dave was granted read-only access to project.txt.
- The ACL mask was verified.

## Access Verification
Command:
sudo -u dave cat /srv/acl-lab/project.txt

Result:
Successfully read the confidential project information.

## Conclusion
Successfully implemented and tested user-specific ACL permissions,
allowing Dave to access the directory and read the file without
granting additional write permissions.
