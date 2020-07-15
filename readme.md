# Seyyed & Amin Network Simulator
Computer Networking Project number 2 - Shahid Beheshti University

Simple Network Simulator with python

## Requirements
Any version of Python 3


## Discription
This program uses Bellmanford algorithm as routing mechanism to simulate network distances from each other.


## Usage

### Initiation

To run:

`python main.py`

You're asked to enter network size. i.e. `5` (in secs.)


Then you should enter network properties. i.e.

First the graph size. then the name of the routers and topology of Networks.
As default the graph names will be R_0 to R_n-1 (n: the graph size). Or you can choose your names instead.

The topology of network is in this form `Router_name1 Router_name2 Network_Address`

### Report

After finishing the initialization, you can get report of the distances from one specific network to the others by choosing the `report` mode, and the network name.

### Add

You can add new networks by selecting this mode.

### Remove

Also Removing a network is possbile.

### Change Interval

The Bellmanfordd algorithm runs peridocally to cover possible changes (Like real networks). This value is asked in the first place, but it can be changed using this mode.

### Quit

And you can close the simulation by sending quit order.

## Algorithm

networks with the toplogy explained by the user will run Bellmanford algorithm to find the shortest path through the routers. This algorithm runs periodically to update in coordination with the possible changes each `refresh_interval` seconds.
