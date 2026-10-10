# Antennas, power and deployment planning

[Back to the index](../README.md) · [Troubleshooting](TROUBLESHOOTING.md)

Use this as a planning worksheet, with the linked device and project documentation for construction details.

## Antenna selection and placement

Match the antenna to the radio band and connector. Compare candidate locations with the same hardware and settings, and record actual message delivery. Consult [official antenna resources](https://meshtastic.org/docs/hardware/antennas/) and the [community antenna reports](https://github.com/meshtastic/antenna-reports).

## Solar power worksheet

Measure your configured node's average power rather than borrowing another board's runtime claim.

| Quantity | Planning calculation |
| --- | --- |
| Daily load | Average measured watts × 24 hours = Wh/day |
| Required usable battery energy | Wh/day × target days without charging |
| Battery's nominal energy | Battery voltage × amp-hours = nominal Wh; usable energy depends on the battery and system |
| Expected daily solar energy | Panel watts × local equivalent sun hours × a measured/justified system efficiency factor |

Compare daily generation against load and recovery needs. Record seasonal shading, temperature limits and charging-controller compatibility. These arithmetic estimates do not certify an electrical design. Use the board, battery and charger manufacturers' specifications. See [power configuration](https://meshtastic.org/docs/configuration/radio/power/) for firmware behavior.

Existing project examples include the [Harbor Breeze enclosure](https://hackaday.io/project/194509-harbor-breeze-meshtastic-hack) and [solar buoy](https://www.instructables.com/Meshtastic-Solar-Buoy/). Their parts and construction methods are examples to evaluate for your conditions.

## Enclosures and weatherproofing

Record the enclosure rating, cable-entry method, drainage/condensation plan, temperature exposure and a way to service the device. A printed enclosure or a repurposed lamp does not automatically retain a weatherproof rating after modification. Browse the [Meshtastic enclosure designs](https://github.com/meshtastic/enclosures) for ideas and verify each design's license before reproducing it.

## Coverage planning and field tests

Use the [Meshtastic site planner](https://github.com/meshtastic/meshtastic-site-planner), [MeshSight](https://ranfty.github.io/meshsight/) and [maps in the index](../README.md#maps-and-diagnostics) to explore placement. Predicted coverage and publicly reported node locations are starting points for a field test, not guaranteed connectivity.

Record installation height, terrain/obstructions, antenna/cable, firmware, settings, battery measurements, test locations, successful deliveries and the check date. Coordinate shared mesh roles using the [configuration tips](https://meshtastic.org/docs/configuration/tips/).
