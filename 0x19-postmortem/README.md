POSTMOTERM

Postmortem: Authentication Service Outage
Issue Summary
On May 15, 2024, from 14:30 to 16:45 UTC, our authentication service experienced a critical outage. This incident affected 73% of our users, preventing them from logging into their accounts across all our web applications. The root cause was identified as an unexpected surge in database connections due to a misconfigured connection pool in a recent deployment.
Timeline

14:30 UTC - Issue detected through automated monitoring alert showing a spike in failed login attempts
14:35 UTC - Engineering team began investigating the authentication service and database logs
14:50 UTC - Initial assumption: DDoS attack due to the sudden increase in traffic
15:10 UTC - Security team engaged to analyze potential DDoS patterns
15:25 UTC - DDoS hypothesis ruled out; focus shifted to recent deployments
15:40 UTC - DevOps team identified misconfiguration in the latest deployment
16:00 UTC - Senior backend engineer escalated to assist with database connection issues
16:30 UTC - Fix implemented: connection pool reconfigured and service restarted
16:45 UTC - Service fully restored and stable

Root Cause and Resolution
The root cause was traced to a misconfiguration in the database connection pool settings introduced in the latest deployment. The maximum number of connections was inadvertently set too low, causing connection exhaustion under normal load. This led to a cascading failure as connection requests 
