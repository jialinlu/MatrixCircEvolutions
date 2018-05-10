"""
buildingBlocksBank.py
Ziga Rojec, EDA group, Faculty of Electrical Engineering, University of Ljubljana, Slovenia. Jan 2018.

This script is a starting point in which you tell the topology synthesis process WHICH and HOW MANY electronic devices shall be used in the search algorithm and therefore in the final solution. 
You can also set  MIN and MAX values for certain electronic devices parameters in paramBounds. 
This script is in strong relation to method makeNetlist from reproduction.py (! NOTE when changing the software !). 

Note that including many ('Quantity') elements will result in a huge (sum of every 'Quantity' times 'NofPins' in buildBlocks) connection matrix. This can result in longer "matrix to netlist" conversion time and can also widen the algorithm search space, which can - on one hand - increase possibilities of reaching an optimum solution - but on the other hand - significantly increase the time to find a solution. 

My advice - before you trigger the run, make sure you know, what kind of a circuit are you looking for. 
"""
#NOTE: Set Quantity, do not touch others.
buildBlocks =  [
      {	#Simple resistor
	'Element': 'Rs',
	'Quantity': 2, #<---NOTE
	'NofPins':  2,
	'Model': '',
	'NofParameters': 1,
	'ParamTypes': ['r'],
	  },
      {	#Simple capacitor
	'Element':'Cs',
	'Quantity': 0,#<---NOTE
	'NofPins':  2,
	'Model': '',
	'NofParameters': 1,
	'ParamTypes': ['c'],     
	  },
      {	#Simple inductor
	'Element':'Ls',
	'Quantity': 0,#<---NOTE
	'NofPins':  2,
	'Model': '',
	'NofParameters': 1,
	'ParamTypes': ['l'],     
	  },
      {	#Zener diode
	'Element':'ZDs',
	'Quantity': 0,#<---NOTE
	'NofPins':  2,
	'Model': 'zd4v7',
	'NofParameters': 0,
	'ParamTypes': [],     
	  },
      {	#NPN BJ Transistor
	'Element':'NPNs',
	'Quantity': 0,#<---NOTE
	'NofPins':  3,
	'Model': 'bc238b',
	'NofParameters': 0,
	'ParamTypes': [],     
	  },
      {	#Subcircuit with three parallel PNPs
	'Element':'3PNPs',
	'Quantity': 2,#<---NOTE
	'NofPins':  3,
	'Model': 'par3pnp',
	'NofParameters': 0,
	'ParamTypes': [],     
	  },
      {	#PNP BJ Transistor
	'Element':'PNPs',
	'Quantity': 1,#<---NOTE
	'NofPins':  3,
	'Model': 'BC308B',
	'NofParameters': 0,
	'ParamTypes': [],     
	  },
      {	#NMos transistor
	'Element':'NMOSs',
	'Quantity': 4,#<---NOTE
	'NofPins':  3,
	'Model': 'submodn',
	'NofParameters': 2,
	'ParamTypes': ['mos_w', 'mos_l'],     
	  },
      {	#PMos transistor
	'Element':'PMOSs',
	'Quantity': 6,#<---NOTE
	'NofPins':  3,
	'Model': 'submodp',
	'NofParameters': 2,
	'ParamTypes': ['mos_w', 'mos_l'],     
	  },
      
      {	#Opamp
	'Element':'OPAMPSs',
	'Quantity': 0,#<---NOTE
	'NofPins':  3,
	'Model': 'LM348T_plus',
	'NofParameters': 0,
	'ParamTypes': [],     
	  },
      {	#PMosCurrSrc1stg 				1.
	'Element':'PMosCurrSrc1stg',
	'Quantity': 0,#<---NOTE
	'NofPins':  3,
	'Model': 'PMosCurrSrc1stg',
	'NofParameters': 2,
	'ParamTypes': ['mos_w', 'mos_l'],     
	  },
      {	#CascPMosCurrSrc1stg				2.
	'Element':'CascPMosCurrSrc1stg',
	'Quantity': 0,#<---NOTE
	'NofPins':  3,
	'Model': 'CascPMosCurrSrc1stg',
	'NofParameters': 2,
	'ParamTypes': ['mos_w', 'mos_l'],     
	  },      
      {	#NMosAmp1ResOnSrc				3.
	'Element':'NMosAmp1ResOnSrc',
	'Quantity': 0,#<---NOTE
	'NofPins':  3,
	'Model': 'NMosAmp1ResOnSrc',
	'NofParameters': 3,
	'ParamTypes': ['mos_w', 'mos_l', 'r'],     
	  },   
      {	#BJTNPNCurrSink					4.
	'Element':'BJTNPNCurrSink',
	'Quantity': 0,#<---NOTE
	'NofPins':  4,
	'Model': 'BJTNPNCurrSink',
	'NofParameters': 0,
	'ParamTypes': [],     
	  },
      {	#BJTPNPCurrSrc					5.
	'Element':'BJTPNPCurrSrc',
	'Quantity': 0,#<---NOTE
	'NofPins':  4,
	'Model': 'BJTPNPCurrSrc',
	'NofParameters': 0,
	'ParamTypes': [],     
	  }, 
      {	#NMosCurrMirr					6.
	'Element':'NMosCurrMirr',
	'Quantity': 0,#<---NOTE
	'NofPins':  4,
	'Model': 'NMosCurrMirr',
	'NofParameters': 2,
	'ParamTypes': ['mos_w', 'mos_l'],     
	  },
      {	#CascNMosCurrMirr				7.
	'Element':'CascNMosCurrMirr',
	'Quantity': 0,#<---NOTE
	'NofPins':  4,
	'Model': 'CascNMosCurrMirr',
	'NofParameters': 2,
	'ParamTypes': ['mos_w', 'mos_l'],
	  },
      {	#PMosCurrSrc2Stg				8.
	'Element':'PMosCurrSrc2Stg',
	'Quantity': 0,#<---NOTE
	'NofPins':  4,
	'Model': 'PMosCurrSrc2Stg',
	'NofParameters': 4,
	'ParamTypes': ['mos_w', 'mos_l', 'mos_w', 'mos_l'],     
	  },
      {	#CascPMosCurrSrc2Stg				9.
	'Element':'CascPMosCurrSrc2Stg',
	'Quantity': 0,#<---NOTE
	'NofPins':  4,
	'Model': 'CascPMosCurrSrc2Stg',
	'NofParameters': 4,
	'ParamTypes': ['mos_w', 'mos_l', 'mos_w', 'mos_l'],     
	  },
      {	#PMosCascode					10.
	'Element':'PMosCascode',
	'Quantity': 0,#<---NOTE
	'NofPins':  4,
	'Model': 'PMosCascode',
	'NofParameters': 4,
	'ParamTypes': ['mos_w', 'mos_l', 'mos_w', 'mos_l'],     
	  },      
      {	#NMosCascode					11.
	'Element':'NMosCascode',
	'Quantity': 0,#<---NOTE
	'NofPins':  4,
	'Model': 'NMosCascode',
	'NofParameters': 4,
	'ParamTypes': ['mos_w', 'mos_l', 'mos_w', 'mos_l'],     
	  },  
]

paramBounds = {
  'r':{'min': 1e3,#Spremenjeno 6.9.2017
       'max': 1e7,
       'scale': 96,	#---not used--------scales (E):	96, 	48, 	24, 	12,	None for linear
	 },		#---------------------------	1%	2%	5%	10%
  'c':{'min': 1e-12,
       'max': 1e-6,
       'scale': 12,
	 },
  'l':{'min': 1e-9,
       'max': 1e-3,
       'scale': None,
	 },
  'mos_w':{'min': 1.8e-07,
       'max': 0.0001,
       'scale': None,
	 },
  'mos_l':{'min': 1.8e-07,
       'max': 4e-06,
       'scale': None,
	 },

  }
    
  #TODO: multiplication parameter (mos)
  #TODO: parameter values based on standard scale
	# add "standard scale" as option
	# problem for PSADE - optimizes continiousely
