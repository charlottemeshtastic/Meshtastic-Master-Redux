# Awesome Meshtastic — Master Redux

A consolidated community resource index maintained by charlottemeshtastic. Start with the official documentation, then explore tools, projects, hardware and local groups.

Meshtastic® is a registered trademark of Meshtastic LLC. This community index is not affiliated with, endorsed, or sponsored by Meshtastic LLC.

## Start here

Follow the [first-message path](docs/START_HERE.md), solve a problem with [troubleshooting](docs/TROUBLESHOOTING.md), or plan a [fixed/solar deployment](docs/DEPLOYMENT.md). For computer-based nodes, see [Linux and Raspberry Pi](docs/LINUX.md).

[Searchable directory: build and preview](site/README.md)

## Contents

- [Official resources](#official-resources)
- [Configuration and troubleshooting](#configuration-and-troubleshooting)
- [Deployment resources](#deployment-resources)
- [Linux and Raspberry Pi](#linux-and-raspberry-pi)
- [Guides and learning](#guides-and-learning)
- [Clients and local tools](#clients-and-local-tools)
- [Maps and diagnostics](#maps-and-diagnostics)
- [Servers and integrations](#servers-and-integrations)
- [Source code and developer tools](#source-code-and-developer-tools)
- [Hardware and experiments](#hardware-and-experiments)
- [Hardware stores](#hardware-stores)
- [Related LoRa projects](#related-lora-projects)
- [Community directory](COMMUNITIES.md)
- [Contribute](CONTRIBUTING.md)
- [Maintenance and automated checks](docs/MAINTENANCE.md)
- [Attribution and license](ATTRIBUTION.md)
- [Audit and unresolved links](audit/REPORT.md)

Checked on 2026-10-09 (America/New_York). A reachable page is not an endorsement or a guarantee that a project is maintained. **Verification pending** means automated checks were blocked or inconclusive; **Membership not verified** means a public social page was reachable but group membership/invite validity was not tested.

## Official resources

Use [Meshtastic documentation](https://meshtastic.org/) as the authority for configuration, supported hardware and current applications. Android and Apple clients have separate platform support; consult the official downloads page.

- [All Downloads](https://meshtastic.org/downloads/)
- [Android App](https://play.google.com/store/apps/details?id=com.geeksville.mesh)
- [Donate to Meshtastic](https://opencollective.com/meshtastic) - Support the Meshtastic project and development on OpenCollective
- [Firmware on Github](https://github.com/meshtastic/firmware)
- [iOS App](https://apps.apple.com/us/app/meshtastic/id1586432531)
- [Meshtastic.org](https://meshtastic.org/) - The homepage & official documentation
- [Official Android App on F-Droid](https://f-droid.org/packages/com.geeksville.mesh/)
- [Official Android App Sideloading via GitHub](https://github.com/meshtastic/Meshtastic-Android/releases/latest)
- [Web App](https://client.meshtastic.org/)
- [Web Flasher](https://flasher.meshtastic.org/)

## Configuration and troubleshooting

Use the [troubleshooting guide](docs/TROUBLESHOOTING.md) to choose a reference for your symptom.

- [Channel configuration](https://meshtastic.org/docs/configuration/radio/channels/) — Messaging channels and key settings.
- [Configuration tips](https://meshtastic.org/docs/configuration/tips/) — Roles, hop counts and position-sharing guidance.
- [Flashing firmware](https://meshtastic.org/docs/getting-started/flashing-firmware/) — Instructions by board family.
- [Getting started](https://meshtastic.org/docs/getting-started/) — Preparation and first setup.
- [Initial configuration](https://meshtastic.org/docs/getting-started/initial-config/) — Client connections and regional setup.
- [LoRa configuration](https://meshtastic.org/docs/configuration/radio/lora/) — Radio region, presets and frequency-slot settings.
- [MQTT configuration](https://meshtastic.org/docs/configuration/module/mqtt/) — Internet bridging and module settings.
- [Position configuration](https://meshtastic.org/docs/configuration/radio/position/) — Position sources and reporting settings.
- [Region by country](https://meshtastic.org/docs/configuration/region-by-country/) — Navigation to the project's country/region guidance.
- [Security and backups](https://meshtastic.org/docs/configuration/radio/security/) — Device keys, access and recovery documentation.

## Deployment resources

Use [deployment planning](docs/DEPLOYMENT.md) for antenna placement, solar sizing, enclosures and field-test notes. Related experiments remain under hardware and experiments.

- [Antenna selection and testing](https://meshtastic.org/docs/hardware/antennas/) — Official antenna resource hub.
- [Power configuration](https://meshtastic.org/docs/configuration/radio/power/) — Advanced device power behavior; consult device roles first.
- [Supported hardware](https://meshtastic.org/docs/hardware/) — Official board documentation.

## Linux and Raspberry Pi

See the [Linux guide](docs/LINUX.md) to distinguish a connected-radio client from a computer running a node.

- [MeshtasticD](https://meshtastic.org/docs/meshtasticd/) — Native node software for supported radio interfaces on Linux and macOS.
- [mPWRD-OS](https://meshtastic.org/docs/software/mpwrd-os/) — Linux images and setup guidance for supported single-board computers.
- [Python CLI documentation](https://meshtastic.org/docs/software/python/cli/) — Configure and communicate with an existing radio.

## Guides and learning

- ["Getting Started with Meshtastic" by The Comms Channel (YouTube)](https://www.youtube.com/playlist?list=PLshzThxhw4O5JTOACGHzYSSd3soDhoXKK)
- ["How does it Work" by AustinMesh](https://www.austinmesh.org/learn/#about) - Some suggested settings are AustinMesh specific, but in general it's useful for anyone
- ["What is Meshtastic and why should you care?" (YouTube)](https://www.youtube.com/watch?v=P9G9hR3T4po) - A short video about the core concepts of Meshtastic
- [Antenna Reports](https://github.com/meshtastic/antenna-reports) - Official Meshtastic community antenna reports
- [Disaster Comms with Meshtastic + MeshCore](https://pamfinds.com/guides/disaster-comms-meshtastic-meshcore/) — Community guide comparing household LoRa mesh deployments. Configuration and range advice is context dependent.
- [How to Visualize Meshtastic Telemetry on Grafana](https://hackaday.io/project/202156-how-to-visualize-meshtastic-telemetry-on-grafana) - Integrates Meshtastic telemetry data with Grafana through Telemetry Harbor, enabling real-time visualization and analysis of device metrics and location data.
- [Meshtastic for Makers](https://www.youtube.com/watch?v=qjJIVBOWvfc&list=PLPK2l9Knytg6jzOfcqk5y0iBH48ZATVVD) — Video course covering Meshtastic setup, sensors, hardware control and MQTT.
- [Meshtastic Quick-Start Video Guide (iOS)](https://www.youtube.com/watch?v=IoaoYbrdtlU) - Short video showing radio setup and basic functions on iOS App
- [Meshtastic RF Connector Types](https://pole1.co.uk/blog/5/) - Visual dictionary of RF connector types commonly found on Meshtastic radios and antennas. Many detailed macro photos.

## Clients and local tools

- [CheckTastic on Google Play](https://play.google.com/store/apps/details?id=com.specfive.checkers)
- [Connect](https://github.com/pdxlocations/connect) — Python MQTT client for Meshtastic; formerly Meshtastic-MQTT-Connect.
- [Contact - A Console UI for Meshtastic](https://github.com/pdxlocations/contact) - A terminal-based Python chat and configuration client for Meshtastic devices.
- [Mesh-Client by Colorado-Mesh](https://github.com/Colorado-Mesh/mesh-client) — Community desktop client for Meshtastic and MeshCore.
- [Mesh-Tac-Toe on Google Play](https://play.google.com/store/apps/details?id=com.specfive.meshtactoe)
- [MeshChess on Google Play](https://play.google.com/store/apps/details?id=com.specfive.chess)
- [Meshlink](https://github.com/Murturtle/MeshLink) — Meshtastic and Discord bridge.
- [MeshSense](https://affirmatech.com/meshsense) - Windows/Mac/Linux app for using a node over Wi-Fi or Bluetooth
- [MeshStation](https://github.com/IronGiu/MeshStation) - Multi-platform SDR analyzer and desktop GUI for decoding and visualizing Meshtastic traffic using RTL-SDR or other SDR hardware
- [Meshtastic Plugin for Pidgin](https://github.com/dadecoza/pidgin-meshtastic) - A plugin to enable you to use Meshtastic with Pidgin (a multiplatform chat client)
- [Meshtastic python scripts by N7IW](https://github.com/N7IW/Meshtastic) - Various Meshtastic python scripts for experimentation
- [Meshtastic Visualizer](https://github.com/antlas0/meshtastic_visualizer) - Python PyQT desktop app to interface with local nodes, or subscribing to MQTT servers
- [meshtastic-go by lmatte7](https://github.com/lmatte7/meshtastic-go) - A meshtastic CLI written in GoLang
- [Meshtastic-SAME-EAS-Alerter by RCGV1](https://github.com/RCGV1/Meshtastic-SAME-EAS-Alerter) - A tool to receive alerts from the National Weather Service and broadcast them on Meshtastic
- [Meshtastic-SDR](https://gitlab.com/crankylinuxuser/meshtastic_sdr) — GNU Radio and Python experiments for receiving Meshtastic traffic with SDR hardware.
- [MeshTenna](https://github.com/OE3JGW/MeshTenna) - Windows/Android app for comparing the performance of different antennas and locations
- [MultiMesh](https://github.com/paulocode/multimesh) - A cross-platform Meshtastic client based on Flutter
- [Red Grid MGRS](https://redgridtactical.com/mgrs) — Tactical mapping application with Meshtastic integration; check current platform support.
- [WeatherStation2Meshtastic](https://github.com/iz0kew/WeatherStation2Meshtastic) — Weather-sensor telemetry bridge for Meshtastic.


## Maps and diagnostics

Public maps show reported nodes and do not establish complete RF coverage or real-time reachability.

- [Bay Area Meshview](https://meshview.bayme.sh/map)
- [Florida Mesh Map](https://map.areyoumeshingwith.us/?lat=28.258786255470607&lng=278.89892578125006&zoom=8)
- [Meshmap.net](https://meshmap.net/) - [Source code](https://github.com/brianshea2/meshmap.net)
- [MeshSense Global Map](https://meshsense.affirmatech.com/) - [Source code](https://github.com/Affirmatech/MeshSense)
- [MeshSight](https://ranfty.github.io/meshsight/) - Terrain-aware RF coverage planner for mapping predicted LoRa signal reach before deploying nodes.
- [Meshtastic Map](https://meshtastic.liamcottle.net/) by Liam Cottle - [Source code](https://github.com/liamcottle/meshtastic-map)
- [PotatoMesh](https://potatomesh.net/) - [Source code](https://github.com/l5yth/potato-mesh)

## Servers and integrations

- [bayme.sh-bot by ppicazo](https://github.com/baymesh/ratm-meshtastic-discord-bot) - An MQTT to Discord logger bot for local meshes.
- [Frozen BBS](https://github.com/kstrauser/frozenbbs) - Another BBS Implementation (written in Rust)
- [Mesh Metrics](https://github.com/cordelster/mesh-metrics) - Poll Meshtastic repeaters over the mesh network without internet access, using this script with Prometheus-compatible monitoring setups.
- [Meshinfo by kevinelliott](https://github.com/MeshAddicts/meshinfo) - A project written in Python and connects to an MQTT server that is receiving Meshtastic messages for the purpose of visualizing and inspecting traffic. [Example on Central Valley Mesh](https://meshinfo.cvme.sh/)
- [MeshLink (Beta)](https://gitHub.com/Murturtle/MeshLinkBeta) — Beta Meshtastic and Discord bridge; distinct repository from MeshLink.
- [Meshmonitor](https://meshmonitor.org/) — Web application for monitoring Meshtastic nodes over IP.
- [MeshSat](https://github.com/meshsat/meshsat) — Bridge between Meshtastic and external transports; see its documentation for hardware and supported integrations.
- [Meshtastic Web API](https://github.com/bmswens/Meshtastic-Web-API) - A RESTful interface to interact with a Meshtastic node via a serial connection.
- [meshtastic-ha-entity-builder](https://github.com/pdxlocations/ha-entity-builder-for-meshtastic) - Builds entities from stored nodes using the [Meshtastic Home Assistant Integration](https://meshtastic.org/docs/software/integrations/mqtt/home-assistant/)
- [Meshtastic-Matrix-Relay](https://github.com/jeremiah-k/meshtastic-matrix-relay) - Meshtastic to Matrix Relay
- [meshtastic-new-node-processing by StevoKeano](https://github.com/StevoKeano/meshtastic-new-node-processing/) - Created by the AustinMesh team to welcome new users to the public mesh and direct them to help/resources.
- [Meshview by pablorevilla](https://github.com/pablorevilla-meshtastic/meshview) - A project watches a MQTT topic for meshtastic messages, imports them to a database and has a web UI to view them. [Example on BayMesh](https://meshview.bayme.sh/)
- [Node-RED Messages Node](https://github.com/danpeig/node-red-meshtastic-msg) - It allows sending and receiving packets to a Meshtastic mesh network thru a device connected via HTTP.
- [TC2-BBS-mesh by TheCommsChannel](https://github.com/TheCommsChannel/TC2-BBS-mesh) - Do you miss the good old days of dial up BBS? Now you can have one via mesh!
- [The Harbor Meshtastic Integration](https://github.com/HarborScale/harbor-meshtastic) — Telemetry Harbor integration for Meshtastic.

## Source code and developer tools

Repositories hosted by the Meshtastic organization; archived components are labeled. Each linked project keeps its own license.

- [api](https://github.com/meshtastic/api) - Meshtastic Website API.
- [c-sharp](https://github.com/meshtastic/c-sharp) - C#/.NET command-line interface and library for Meshtastic.
- [enclosures](https://github.com/meshtastic/enclosures) - 3D models for enclosures used in Meshtastic devices.
- [ETHClass2](https://github.com/meshtastic/ETHClass2) - Provides ETHClass2 integration for Meshtastic, originally from LilyGO T-ETH series.
- [firmware-ota](https://github.com/meshtastic/firmware-ota) - BLE-OTA Mini firmware for Meshtastic devices.
- [firmware-ota-wifi](https://github.com/meshtastic/firmware-ota-wifi) - WiFi-based OTA (Over The Air) firmware updates for Meshtastic devices.
- [home-assistant](https://github.com/meshtastic/home-assistant) - Home Assistant integration for Meshtastic.
- [i2c-sensor](https://github.com/meshtastic/i2c-sensor) - Arduino boilerplate for creating custom I2C sensors for Meshtastic.
- [meshtastic](https://github.com/meshtastic/meshtastic) - Meshtastic project website and documentation.
- [Meshtastic-Android](https://github.com/meshtastic/Meshtastic-Android) - Android app for Meshtastic.
- [Meshtastic-Apple](https://github.com/meshtastic/Meshtastic-Apple) - iOS, iPadOS & macOS Clients for Meshtastic.
- [Meshtastic-arduino](https://github.com/meshtastic/Meshtastic-arduino) - Arduino drivers for interfacing with Meshtastic nodes over WiFi and Serial.
- [meshtastic-site-planner](https://github.com/meshtastic/meshtastic-site-planner) - Site planning tool based on RF analysis using SPLAT! software.
- [meshtasticator](https://github.com/meshtastic/meshtasticator) - Simulator for Meshtastic, supporting discrete-event and interactive simulations.
- [meshTestic](https://github.com/meshtastic/meshTestic) - End-to-end test suite for Meshtastic devices.
- [mqtt](https://github.com/meshtastic/mqtt) - MQTT broker boilerplate designed for Meshtastic's native packet-aware MQTT support.
- [network-management-client](https://github.com/meshtastic/network-management-client) - Desktop client for offline deployment and mesh network management.
- [node-red-contrib-meshtastic](https://github.com/meshtastic/node-red-contrib-meshtastic) - Node-RED integration for Meshtastic.
- [nrf52_factory_erase](https://github.com/meshtastic/nrf52_factory_erase) - Firmware for factory erasing the nRF52 chips used in Meshtastic devices.
- [protobufs](https://github.com/meshtastic/protobufs) - Protobuf definitions for Meshtastic.
- [python](https://github.com/meshtastic/python) - Python CLI and API for interacting with Meshtastic devices.
- [RadioHead](https://github.com/meshtastic/RadioHead) - A fork of the RadioHead library, with custom fixes for Meshtastic devices.
- [rust](https://github.com/meshtastic/rust) - A Rust library for interacting with Meshtastic radios.
- [web](https://github.com/meshtastic/web) - Meshtastic Web Client.
- [web-flasher](https://github.com/meshtastic/web-flasher) - Online flasher for Meshtastic device firmware.

## Hardware and experiments

- [A Major Solution to a Miner Problem](https://meshtastic.org/blog/a-major-solution-to-a-miner-problem/) - How to repurpose an unused LoRa-based cryptocurrency mining device into functional Meshtastic node.
- [Harbor Breeze Meshtastic Hack](https://hackaday.io/project/194509-harbor-breeze-meshtastic-hack) — Solar-light enclosure project for a WisBlock-based Meshtastic node.
- [Meshpipe by Armooo](https://github.com/armooo/meshpipe) - An attempt to slurp packets out of one radio and chuck them out another (POC for a conceptual meshtastic backhaul)
- [Meshtastic or Helium Ultrasonic WX Station](https://hackaday.io/project/196990-meshtastic-or-helium-ultrasonic-wx-station) - Transforms the Ecowitt WS85 weather station into a Meshtastic-enabled device by modifying its hardware to output serial data, enabling it to transmit weather telemetry over a LoRa mesh network.
- [Meshtastic Solar Buoy](https://www.instructables.com/Meshtastic-Solar-Buoy/) - Converts a waterproof solar fishing buoy lamp into a rugged, solar-powered Meshtastic node for long-range mesh communication.
- [Meshtastic-Experiments by HarukiToreda](https://github.com/HarukiToreda/Meshtastic-Experiments) - A low level collection & comparison of various Meshtastic hardware.
- [MeshTIEstick: The Wearable LoRa Meshtastic Node](https://www.youtube.com/watch?v=2Wf6BcZS3AY) - Turning a necktie into a fully functional mesh node.

## Hardware stores

Vendor links are a directory, not a quality ranking or certification. Check radio region, supported device model and current stock.

- [AT Labs](https://at-labs.tech) — Hardware vendor; check current device compatibility and availability.
- [B&Q Consulting](https://shop.uniteng.com) — Hardware vendor; check current device compatibility and availability.
- [Canary Radio](https://canaryradio.io) — Hardware vendor; check current device compatibility and availability.
- [CommsForAll](https://commsforall.com) — Hardware vendor; check current device compatibility and availability.
- [HELTEC®](https://heltec.org) — Hardware vendor; check current device compatibility and availability.
- [LILYGO Official Site](https://www.lilygo.cc/collections/lora-or-gps) — Hardware vendor; check current device compatibility and availability.
- [LILYGO on AliExpress](https://lilygo.aliexpress.com/store/1101195566) — Hardware vendor; check current device compatibility and availability.
- [Neil Hao on Tindie](https://www.tindie.com/stores/neilhao/) — Hardware vendor; check current device compatibility and availability. **[Verification pending]**
- [PileupDX](https://pileupdx.com/product-category/brands/meshtastic/) — Hardware vendor; check current device compatibility and availability.
- [RAK®](https://store.rakwireless.com) — Hardware vendor; check current device compatibility and availability.
- [Rokland](https://store.rokland.com/pages/meshtastic-hardware-rak-lilygo) — Hardware vendor; check current device compatibility and availability.
- [Seeed Studio®](https://www.seeedstudio.com) — Hardware vendor; check current device compatibility and availability.
- [Spec5](https://specfive.com) — Hardware vendor; check current device compatibility and availability.
- [YetiWurks](https://www.yetiwurks.com/product-category/communication/) — Hardware vendor; check current device compatibility and availability.

## Related LoRa projects

Related inspiration; these projects are not necessarily Meshtastic compatible.

- [ARMAWATCH & ARMACHAT - long range radio messengers](https://hackaday.io/project/171790-armawatch-armachat-long-range-radio-messengers) - Long-range radio communicator featuring a QWERTY keyboard, LoRa connectivity, and a color display, designed for off-grid messaging and disaster resilience.

## Communities

Browse the [community directory](COMMUNITIES.md), organized by country and region.

## License and credit

The index is released under [CC0 1.0 Universal](LICENSE). See [attribution](ATTRIBUTION.md) for both source snapshots and upstream maintainers. Linked software, media and trademarks retain their own licenses and rights.
