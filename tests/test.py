from pysimstudy import *


# Test addColumns
print("Testing for addColumns")
dtx =  defData(varname = "xNr", dist = "nonrandom", formula = 7, idx = "idnum")
dtx =  defData(dtx, varname = "xUni", dist = "uniform", formula = "10,20") 

dt =  genData(10, dtx)

def2 = defDataAdd(varname = "y1", formula = 10, variance = 3)
def2 = defDataAdd(def2, varname = "y2", formula = .5, dist = "binary")

dt = addColumns(def2, dt)
print("addColumns works")