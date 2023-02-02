# Why doesn't docker    compose reload fastapi server on file changes?

The problem is in the utility that fastapi uses to view files for changes - **watchfiles**

This utility does not see changes to files in the docker container, because starting from the second version, docker does not use the notification daemon when modifying files

The solution to the problem is to add an environment variable to the service with docker compose, which tell watchfiles to force the polling:

```dockerfile
environment:
  - WATCHFILES_FORCE_POLLING=true
```

