# User and Group Administration

## Objective
Practice Linux user and group administration on Ubuntu.

## Groups
The following departmental groups were created or verified:

- analysts
- devops
- auditors

## User Accounts
The following accounts were created or verified:

- alice - DevOps administrator
- bob - Analyst
- carol - Contract analyst
- dave - Auditor

## Group Memberships

| User | Supplementary Groups |
|------|----------------------|
| alice | analysts, devops |
| bob | analysts |
| carol | analysts |
| dave | auditors |

Each human user has an individual primary group.

## Account Management
- Alice's supplementary group membership was modified.
- Carol's account was locked and subsequently unlocked.
- Carol's current password status was verified as P (password set).
- The reportapp system account was verified.

## Verification Commands

```bash
getent group analysts devops auditors
id alice
id bob
id carol
id dave
sudo passwd -S carol
id reportapp

### Step 3 — Check the document

Run:

```bash
cat evidence/user-group-administration.md
git status --short
