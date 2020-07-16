# Seyyed & Amin Network Simulator
Computer Networking Project number 2 - Shahid Beheshti University - Summer 1399

Simple Network Simulator with python

## Requirements
Any version of Python 3


## Description
This program uses Bellman-Ford algorithm as routing mechanism to simulate network distances from each other.


## Usage

### Initiation

To run:

`python main.py`

You're asked to enter network size. i.e. `5` (in secs.)


Then you should enter network properties:

First the graph size. i.e. `4` . then the name of the routers and topology of Networks.
As default the graph names will be R_0 to R_n-1 (n: the graph size). Or you can choose your names instead.
Then you enter number of connections between routers and finally you should enter connections.

The topology of network connections is in this form `Router_name1 Router_name2 Port_number1 Port_number2 Network_Address`. i.e. `R1 R2 2002 3003 10.10.10.10`

### Report

After finishing the initialization, you can get report of the distances from one specific network to the other routers by choosing the `report` mode. Then you asked to enter the network name i.e. `10.10.10.2`.

### Add

You can add new networks by selecting this mode. The input form of adding connection was explained before.

### Change Interval

The Bellman Ford algorithm runs periodically to cover possible changes (Like real networks). This value is asked in the first place, but it can be changed using this mode.

### Report Router

You can get report of the distances from one specific router to all networks by choosing the `report router` mode. Then you asked to enter the router name i.e. `R0`.

### Quit

And you can close the simulation by sending `quit` command.

## Algorithm

networks with the topology explained by the user will run Bellman-Ford algorithm to find the shortest path through the routers. This algorithm runs periodically to update in coordination with the possible changes each `refresh_interval` seconds.
