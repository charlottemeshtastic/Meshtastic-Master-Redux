# Linux and Raspberry Pi

[Back to the index](../README.md) · [Deployment planning](DEPLOYMENT.md)

These options serve different purposes. Choose based on whether the computer connects to an existing radio or runs the node itself.

| Option | Purpose | Documentation |
| --- | --- | --- |
| Python CLI/API | Configure and communicate with a connected Meshtastic radio. | [Official Python documentation](https://meshtastic.org/docs/software/python/cli/) |
| meshtasticd | Run Meshtastic node software on a computer with supported radio hardware; the official documentation covers Linux and macOS. | [MeshtasticD](https://meshtastic.org/docs/meshtasticd/) |
| mPWRD-OS | Use a Linux image for a supported single-board computer with meshtasticd and setup tools included. Check the board-support table before choosing an image. | [mPWRD-OS](https://meshtastic.org/docs/software/mpwrd-os/) |

A Raspberry Pi on its own is not a LoRa radio. Verify the radio interface, board pinout, power supply and image compatibility in the selected project's documentation.

For an always-on deployment, test restart behavior and remote access before installing the node in a difficult-to-reach location. Keep the project's own update and recovery instructions alongside your deployment notes.
