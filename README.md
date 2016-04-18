# Traffic Simulator

![Traffic Simulation Graph](https://raw.githubusercontent.com/katjackson/traffic-simulation/master/traffic.png)


## Introduction
## ------------

The traffic simulation program was designed to accurately model the flow of cars on a road to determine conditions that cause traffic jams and also to determine what speed limit maximizes the flow of traffic.

The program creates cars and runs them around a circular track, occasionally decreasing their speed slightly to mimic the real world. The cars are designed in such a way that they can't pass other cars, so small slowdowns may turn into full stops in the traffic. Plotting the speeds and positions of the cars makes it possible to understand how the model functions.


### Files

The simulator module runs the car and road files to generate. A test file is provided for debugging purposes. Additionally, a Jupyter notebook file provides a means to run and view graphical output from the main program.

The simulation files may be found on GitHub at:
[Traffic Simulator at GitHub][arbitrary case-insensitive reference text]

[arbitrary case-insensitive reference text]: <https://github.com/katjackson/traffic-simulation.git>


## Requirements
## ------------

This module requires importing numpy and matplotlib, as well as the random default class. The graphs in the Jupyter notebook were also created using the seaborn module.

The simulator module has no external dependancies.


## Installation
## ------------

There is no installation required for this module. Running simulator.py from the terminal is sufficient to interact with the base program. Using the Jupyter notebook file is a stand-alone way to create output graphs from the data accumulated by the base program.


## Configuration
## -------------

This module has no menu or modifiable settings. There are no special configuration requirements. Make sure that the car and road modules are in the same directory as the simulator file.
