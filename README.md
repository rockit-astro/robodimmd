## ING RoboDIMM daemon

Part of the observatory software for the Warwick La Palma telescopes.

`robodimmd` is a Pyro frontend that proxies queries to the ING RoboDIMM API.

`robodimm` is a commandline utility that shows the ING RoboDIMM seeing.

See [Software Infrastructure](https://github.com/warwick-one-metre/docs/wiki/Software-Infrastructure) for an overview of the observatory software architecture and instructions for developing and deploying the code.

### Software setup
After installing `observatory-robodimm-server`, the `robodimmd` must be enabled using:
```
sudo systemctl enable robodimmd.service
```

The service will automatically start on system boot, or you can start it immediately using:
```
sudo systemctl start robodimmd.service
```

Finally, open a port in the firewall so that other machines on the network can access the daemon:
```
sudo firewall-cmd --zone=public --add-port=9026/tcp --permanent
sudo firewall-cmd --reload
```
