# Configuration and troubleshooting

[Back to the index](../README.md) · [Start here](START_HERE.md)

Work from a small test with two nearby radios. Change one setting at a time and record the result.

| Symptom | First checks | Official reference |
| --- | --- | --- |
| Computer cannot see the radio | Try a known USB data cable and the flashing instructions for the exact board family. | [Getting started](https://meshtastic.org/docs/getting-started/) |
| Phone or browser cannot connect | Confirm the board's connection methods and the client's support; use the platform-specific setup instructions. | [Initial configuration](https://meshtastic.org/docs/getting-started/initial-config/) |
| Connected, but messages do not arrive | Compare region, modem preset, frequency slot and messaging channel name/key on both radios. | [LoRa settings](https://meshtastic.org/docs/configuration/radio/lora/) and [channels](https://meshtastic.org/docs/configuration/radio/channels/) |
| Delivery changes after moving the radio | Repeat the nearby test, inspect the antenna connection and compare placement. | [Antenna resources](https://meshtastic.org/docs/hardware/antennas/) |
| App reports an unexpected battery state | Check the device's documented power behavior before changing calibration or sleep settings. | [Power configuration](https://meshtastic.org/docs/configuration/radio/power/) |
| A node is missing from a public map | Check whether it reports through that map's data source. A map is not a complete inventory of the RF mesh. | [MQTT configuration](https://meshtastic.org/docs/configuration/module/mqtt/) |

## Roles and shared mesh settings

Begin with the recommended client roles in the [configuration tips](https://meshtastic.org/docs/configuration/tips/). Coordinate specialized routing roles with your local group. More rebroadcasting or a higher hop limit is not automatically better.

## Location and channel privacy

Review [position settings](https://meshtastic.org/docs/configuration/radio/position/), [channel settings](https://meshtastic.org/docs/configuration/radio/channels/) and [MQTT settings](https://meshtastic.org/docs/configuration/module/mqtt/) before sharing a node publicly. A default shared channel is not a private group. Check what position data each channel publishes; MQTT can carry mesh data beyond the local radio network.

## Backup and recovery

Use the [security documentation](https://meshtastic.org/docs/configuration/radio/security/) for configuration/key backup and restore. Keep backups private: they can contain keys. Avoid factory erasure as a first troubleshooting step.

## Ask for useful help

Include the board model, firmware and client versions, connection method, symptom, and what you tried. Remove keys, private channel QR codes and exact home coordinates from screenshots or logs. For a resource-index problem, use the repository's broken-link template; for radio behavior, contact the relevant project or local group.
