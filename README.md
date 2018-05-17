# MatrixCircEvolutions
An evolutionary algorithm for automatic analog circuit topology synthesis. 

INTRODUCTION
Let us imagine the typical work-flow of an analog circuit designer. He or she has to:
  1. Figure out desired circuit specifications,
  2. choose a suitable topology to perform a task,
  3. find the physical sizes (numerical parameters) of choosen electrical building-blocks,
  4. evaluate and confirm the design. 
  
It is often a time consuming and ambiguous task, specially for un-experienced designer.

This software is build to to help you with owerall analog circuit design. This software basically joins steps 2 and 3 together and makes possible for a designer to jump from the 1st step directly to the 4th step. 

INPUTS-OUTPUTS
There are two main inputs to this process. The first is a fixed bank of electrical building blocks (SPICE models) you want to be used in the final design. There can be more than needed, but certainly not less than needed. The second input is a high-level definition of the desired circuit behaviour. That is, for example, how much gain do we want, the bandwidth, dumping, allowed THD, etc.
The output is simply a netlist (or a set of netlists) that represent the resulting circuit (topology+parameters). 

IDEA
The main idea behing this software is to take the building-blocks bank and connect terminals together using special binary-connection matrix. Altering the setup of the binary matrix provides changes in the topology. We modify those matrices utilizing the artificial evolution process. Please read REFERENCES to fully understand the main core of this procedure. 

WARNING
Do not expect miracles. They might come, but do not count on it. When designing a circuit, firstly make sure that you know, what you are doing. This sofware can indeed find novel topologies and even return an optimized solution - but only when high-level circuit definition is defined well. WYWIWYG!

USAGE
Run main.py for single-objective search.
Run main_moea.py for multi-objective search.

REFERENCES
[1] Ž. Rojec, Á. Bűrmen and I. Fajfar, "An evolution-driven analog circuit topology synthesis," 2016 IEEE Symposium Series on Computational Intelligence (SSCI), Athens, 2016, pp. 1-6.
doi: 10.1109/SSCI.2016.7850184
http://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=7850184&isnumber=7849361

[2] 

[3]

