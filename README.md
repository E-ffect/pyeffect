<div align="center">
  <a href="https://e-ffect.fr">
    <img src="https://media.alors-la.center/s/16hqhl6h.svg"/>
  </a>
</div>

<div align="center"><h1>PyEffect</h1></div>

<div align="center">
<h4>Python package ready to use for the E-ffect Bridge</h4>
</div>

<div align="center">
<img src="https://img.shields.io/badge/Language-Python-blueviolet" />
<img src="https://img.shields.io/badge/Interface-Zigbee-blue" />
</div>

<div align="center">
<img src="https://img.shields.io/badge/version-0.0.4-green" /> 
</div>

## How to install

```sh

pip install git+https://github.com/antonin-alves/pyeffect

```

## How to use 

```python

from pyeffect import zigbee

# Change Pedal color
zigbee.changePedalLedColor("EF-EC-01-23-45", 255, 255, 255)

# Ping a Pedal
zigbee.pingPedal("EF-EC-01-23-45")


```
