# Docker Backblaze B2 rclone scheduler

## Required files

### rclone.conf
this file can be generated through the `rclone config` terminal command.
The generated config will be found in its config file. Pleasae see rclone documentation for up-to-date details.
```
[config-name]
type = b2
account = <account>
key = <key>

[other-config-name]
type = b2
account = <account>
key = <key>
```

### config.json
`time` is in 24-hour format.
```
{
  "config-name": {
    "bucket": "b2-bucket-name",
    "time": "03:00",
    "location": "/container/path/to/data"
  },
  "other-config-name": {
    "bucket": "other-b2-bucket-name",
    "time": "03:00",
    "location": "/container/path/to/other/data"
  }
}
```

## Example configuration
```
version: 3
services:
  app:
    image: davidstur/rclone
    volumes:
      - /local/path/to/config.json:/config.json:ro
      - /local/path/to/rclone.conf:/rclone.conf:ro
      - /local/path/to/data:/container/path/to/data:ro
      - /local/path/to/other/data:/container/path/to/other/data:ro
```