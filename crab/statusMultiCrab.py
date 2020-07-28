#///////////////////////////////////////////////////
#                                                  #
# CRAB status of multiple samples                  #
#                                                  #
#///////////////////////////////////////////////////

import FWCore.ParameterSet.Config as cms
import os
import sys
import datetime

#IMPORT MODULES FROM OTHER DIR
sys.path.insert(0, os.getcwd().replace("crab","sample"))
from dataMiniAOD import dataSampDict as data
from mcMiniAOD import mcSampDict as mc
sys.path.insert(0, os.getcwd().replace("crab","module"))
from sampleKeyVal import *

#Check availability of samples on DAS
def execme(cmd):
    #toPrint("\033[01;32m"+ "Excecuting: "+ "\033[00m",  cmd)
    os.system(cmd)

#USERS INPUTS
isMC = False
isData = True
rangeMC = len(mc)
rangeData = len(data)

def getStatusMC(mc, m):
    crab_dir = "CrabMC_20191116"
    crab_subdir = "crab_"+getMCKey(mc, m)+"_MC_"+crab_dir.split("_")[1]
    execme("echo  ")
    execme("echo +++++++++++++++++++++++++++++++++++++++++++++++")
    execme("echo NEXT SAMPLE : "+crab_subdir)
    execme("echo +++++++++++++++++++++++++++++++++++++++++++++++")
    ##execme("crab status "+crab_dir+"/"+crab_subdir)
    execme("crab status --verboseErrors "+crab_dir+"/"+crab_subdir)
    #execme("crab resubmit "+crab_dir+"/"+crab_subdir)
    ##execme("crab kill -d "+crab_dir+"/"+crab_subdir)

def getStatusData(eleData, d):
    crab_dir = "CrabData_20191101"
    crab_subdir = "crab_"+getDataKey(eleData, d)+"_Data_"+crab_dir.split("_")[1]
    execme("echo +++++++++++++++++++++++++++++++++++++++++++++++")
    execme("echo NEXT SAMPLE : "+crab_subdir)
    execme("echo +++++++++++++++++++++++++++++++++++++++++++++++")
    #execme("crab status "+crab_dir+"/"+crab_subdir)
    execme("crab status --verboseErrors "+crab_dir+"/"+crab_subdir)
    #execme("crab resubmit -d "+crab_dir+"/"+crab_subdir)
    #execme("crab kill -d "+crab_dir+"/"+crab_subdir)
    execme("crab report "+crab_dir+"/"+crab_subdir)
    execme("brilcalc lumi -b \"STABLE BEAMS\" --normtag /afs/cern.ch/user/l/lumipro/public/normtag_file/normtag_DATACERT.json -u /fb -i "+crab_dir+"/"+crab_subdir+"/results/lumisToProcess.json")
    execme("brilcalc lumi -b \"STABLE BEAMS\" --normtag /afs/cern.ch/user/l/lumipro/public/normtag_file/normtag_DATACERT.json -u /fb -i "+crab_dir+"/"+crab_subdir+"/results/processedLumis.json")
    execme("brilcalc lumi -b \"STABLE BEAMS\" --normtag /afs/cern.ch/user/l/lumipro/public/normtag_file/normtag_DATACERT.json -u /fb -i "+crab_dir+"/"+crab_subdir+"/results/notFinishedLumi.json")
   #execme("brilcalc lumi -i "+crab_dir+"/"+crab_subdir+"/results/lumisToProcess.json")
   #execme("brilcalc lumi -i "+crab_dir+"/"+crab_subdir+"/results/processedLumis.json")
   #execme("brilcalc lumi -i "+crab_dir+"/"+crab_subdir+"/results/notFinishedLumis.json")
  
if isMC:
    toPrint("Total MC samples",len(mc))
    for m in range(rangeMC):
        getStatusMC(mc, m)
if isData:
    toPrint("Total data samples",len(data))
    for d in range(rangeData):
        getStatusData(data, d)
