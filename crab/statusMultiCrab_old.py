
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
from dataMiniAOD import muDataSampDict as muData
from dataMiniAOD import eleDataSampDict as elemc
from mcMiniAOD import mcSampDict as mc
from sampleKeyVal import *

#Check availability of samples on DAS
def execme(cmd):
    #toPrint("\033[01;32m"+ "Excecuting: "+ "\033[00m",  cmd)
    os.system(cmd)

#USERS INPUTS
isMu = True
isMuMC = True
isMuData = True
range_MuMC = len(mc)
range_muData = len(muData)

isEle = True
isEleMC = True
isEleData = True 
range_EleMC = len(mc)
range_eleData = len(eleData)

def statusMuMC(mc, m):
    crab_dir = "CrabMC_20191029"
    crab_subdir = "crab_"+getMCKey(mc, m)+"_MuMC_"+crab_dir.split("_")[1]
    execme("echo  ")
    execme("echo +++++++++++++++++++++++++++++++++++++++++++++++")
    execme("echo NEXT SAMPLE : "+crab_subdir)
    execme("echo +++++++++++++++++++++++++++++++++++++++++++++++")
    ##execme("crab status "+crab_dir+"/"+crab_subdir)
    execme("crab status --verboseErrors "+crab_dir+"/"+crab_subdir)
    #execme("crab resubmit "+crab_dir+"/"+crab_subdir)
    #execme("crab kill -d "+crab_dir+"/"+crab_subdir)

def statusMuData(muData, d):
    crab_dir = "CrabData_20191029"
    crab_subdir = "crab_"+getDataKey(muData, d)+"_MuData_"+crab_dir.split("_")[1]
    execme("echo +++++++++++++++++++++++++++++++++++++++++++++++")
    execme("echo NEXT SAMPLE : "+crab_subdir)
    execme("echo +++++++++++++++++++++++++++++++++++++++++++++++")
    #execme("crab kill -d "+crab_dir+"/"+crab_subdir)
    ##execme("crab status "+crab_dir+"/"+crab_subdir)
    execme("crab status --verboseErrors "+crab_dir+"/"+crab_subdir)
    #execme("crab resubmit "+crab_dir+"/"+crab_subdir)
    #execme("export PATH=$HOME/.local/bin:/afs/cern.ch/cms/lumi/brilconda-1.1.7/bin:$PATH")
    ##execme("crab report "+crab_dir+"/"+crab_subdir)
    ##execme("brilcalc lumi -i "+crab_dir+"/"+crab_subdir+"/results/lumisToProcess.json")
    ##execme("brilcalc lumi -i "+crab_dir+"/"+crab_subdir+"/results/processedLumis.json")
    ##execme("brilcalc lumi -i "+crab_dir+"/"+crab_subdir+"/results/notFinishedLumis.json")

def statusEleMC(mc, m):
    crab_dir = "CrabMC_20191029"
    crab_subdir = "crab_"+getMCKey(mc, m)+"_EleMC_"+crab_dir.split("_")[1]
    execme("echo +++++++++++++++++++++++++++++++++++++++++++++++")
    execme("echo NEXT SAMPLE : "+crab_subdir)
    execme("echo +++++++++++++++++++++++++++++++++++++++++++++++")
    execme("crab status --verboseErrors "+crab_dir+"/"+crab_subdir)
    #execme("crab status --verboseErrors "+crab_dir+"/"+crab_subdir)
    #execme("crab resubmit -d "+crab_dir+"/"+crab_subdir)

def statusEleData(eleData, d):
    crab_dir = "CrabData_20191029"
    crab_subdir = "crab_"+getDataKey(eleData, d)+"_EleData_"+crab_dir.split("_")[1]
    execme("echo +++++++++++++++++++++++++++++++++++++++++++++++")
    execme("echo NEXT SAMPLE : "+crab_subdir)
    execme("echo +++++++++++++++++++++++++++++++++++++++++++++++")
    #execme("crab status "+crab_dir+"/"+crab_subdir)
    execme("crab status --verboseErrors "+crab_dir+"/"+crab_subdir)
    #execme("crab resubmit -d "+crab_dir+"/"+crab_subdir)
    #execme("crab report "+crab_dir+"/"+crab_subdir)
    ######execme("brilcalc lumi -i "+crab_dir+"/"+crab_subdir+"/results/lumisToProcess.json")
    #execme("brilcalc lumi -i "+crab_dir+"/"+crab_subdir+"/results/processedLumis.json")
    ######execme("brilcalc lumi -i "+crab_dir+"/"+crab_subdir+"/results/notFinishedLumis.json")
    #execme("brilcalc lumi -b \"STABLE BEAMS\" --normtag /afs/cern.ch/user/l/lumipro/public/normtag_file/normtag_DATACERT.json -u /fb -i "+crab_dir+"/"+crab_subdir+"/results/lumisToProcess.json")
    execme("brilcalc lumi -b \"STABLE BEAMS\" --normtag /afs/cern.ch/user/l/lumipro/public/normtag_file/normtag_DATACERT.json -u /fb -i "+crab_dir+"/"+crab_subdir+"/results/processedLumis.json")
    #execme("brilcalc lumi -b \"STABLE BEAMS\" --normtag /afs/cern.ch/user/l/lumipro/public/normtag_file/normtag_DATACERT.json -u /fb -i "+crab_dir+"/"+crab_subdir+"/results/notFinishedLumi.json")
if isMu:
    if isMuMC:
        toPrint("Total MC samples",len(mc))
        for m in range(range_MuMC):
            statusMuMC(mc, m)
            #statusEleMC(mc, m)
    if isMuData:
        toPrint("Total SingleMuon Data samples",len(muData))
        for d in range(range_muData):
            statusMuData(muData, d)
if isEle:
    if isEleMC:
        toPrint("Total MC samples",len(mc))
        for m in range(range_EleMC):
            statusEleMC(mc, m)
            #statusEleMC(mc, m)
    if isEleData:
        toPrint("Total SingleElectron Data samples",len(eleData))
        for d in range(range_eleData):
            statusEleData(eleData, d)
