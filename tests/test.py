from pysimstudy import *

# add_data.py
# Test addColumns
print("Testing for addColumns")
dtx =  defData(varname = "xNr", dist = "nonrandom", formula = 7, idx = "idnum")
dtx =  defData(dtx, varname = "xUni", dist = "uniform", formula = "10,20") 

dt =  genData(10, dtx)

def2 = defDataAdd(varname = "y1", formula = 10, variance = 3)
def2 = defDataAdd(def2, varname = "y2", formula = .5, dist = "binary")

dt = addColumns(def2, dt)
print("addColumns works")

# addCondition
# addMarkov
# addMultiFac
# addSynthetic
#
#asserts
#o tests found in R version of script
#
#define_data
# defCondition
# defData
# defDataAdd
# defRepeat
# defRepeatAdd
# defRead
# defReadAdd
# dfReadCond
# defSurv
# evalDef
#
#generate_correlated_data
# genCorData
# genCorFlex
# genCorGen
# genCorMat
#
#generate_data
# genData
# genDummy
# genFactor
# genFormula
# genMarkov
# genMultiFac
# genOrdCat
# genSpline
# genSurv
# genSynthetic
#
#generate_dist
#no tests found in R version of script
#
#group_data
# addPeriods
# genCluster
# genNthEvent
# trtAssign
# trtObserve
# trtStepWedge
#
#utility
# genMixFormula
# betaGetShapes
# genCatFormula
# delColumns
# gammaGetShapeRate
# iccRE
# mergeData
# negbinomGetSizeProb
# trimData
# updateDef
# updateDefAdd
# viewBasis
# viewSplines
# survGetParams
# survParamPlot
# addCompRisk