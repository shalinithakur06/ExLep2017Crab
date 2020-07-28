
#///////////////////////////////////////////////////
#                                                  #
# CRAB configuration to run over Multiple samples  #
#                                                  #
#///////////////////////////////////////////////////

#------------------ Setup CRAB -------------------------------#
#execme("source /cvmfs/cms.cern.ch/crab3/crab_standalone.sh")
#execme("cmsenv")
#execme("voms-proxy-init --voms cms")
#-------------------------------------------------------------#

import os
import sys
import datetime

import FWCore.ParameterSet.Config as cms
#IMPORT MODULES FROM OTHER DIR
sys.path.insert(0, os.getcwd().replace("crab","sample"))
from dataMiniAOD import dataSampDict as data
from mcMiniAOD import mcSampDict as mc
sys.path.insert(0, os.getcwd().replace("crab","module"))
from sampleKeyVal import *
from multiCrab import *

def execme(cmd):
    print "\033[01;32m"+ "Excecuting: "+ "\033[00m",  cmd
    os.system(cmd)

#------------------------------------------
#Check availability of samples on DAS
#------------------------------------------
def getSummaryFromDAS(dataset_name):
     das_command = "dasgoclient --limit=1 --query=\"summary dataset=%s\"" %dataset_name
     #print "\033[01;32m"+ "Excecuting: "+ "\033[00m",  das_command
     das_summary = os.popen(das_command).read()
     return das_summary

#------------------------------------------
#Check availability of samples on DAS
#------------------------------------------
#toPrint("Total MC samples",len(mc))
for n in range(len(mc)):
    dataset_key = getMCKey(mc, n)
    dataset_name = getMCVal(mc, n)
    ###dataset_summary = getSummaryFromDAS(dataset_name)
    ###print '{:<20}  {:<30}'.format(dataset_key, dataset_summary)

#toPrint("Total single muon DATA samples",len(data))
for n in range(len(data)):
    dataset_key = getMCKey(data, n)
    dataset_name = getMCVal(data, n)
    #dataset_summary = getSummaryFromDAS(dataset_name)
    #print '{:<30}  {:<30}'.format(dataset_key, dataset_summary)

#------------------------------------------
#USER INPUTS
#------------------------------------------
#muon channel
isMC = True
isData = False 
range_mc = len(mc)
range_data = len(data)

#------------------------------------------
#CRAB PARAMETERS
#------------------------------------------
#https://twiki.cern.ch/twiki/bin/view/CMSPublic/CRAB3ConfigurationFile#CRAB_configuration_parameters
from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

#default CRAB parameters
config.General.transferOutputs = True
config.General.transferLogs = False
config.JobType.allowUndistributedCMSSW = True
config.JobType.pluginName = 'Analysis'
#config.JobType.disableAutomaticOutputCollection = True
config.Data.inputDBS = 'global'
##config.Data.inputDBS = 'phys03'
config.Data.allowNonValidInputDataset = True
config.JobType.maxMemoryMB = 2000
#config.Data.ignoreLocality = True
config.Site.storageSite = 'T2_IN_TIFR'
config.JobType.inputFiles = ["../../ExLep2017Tree/Selection/test/Fall17_V3_MC_PtResolution_AK8PF.txt","../../ExLep2017Tree/Selection/test/Fall17_V3_MC_SF_AK8PF.txt"]

date = str(datetime.date.today()).replace("-","")
execme("mkdir -p "+date+"/config")
mc_T2Paths_ = open(date+"/ntupleT2Paths_mc"+ date +".txt", 'w')
data_T2Paths_ = open(date+"/ntupleT2Paths_data"+ date +".txt", 'w')
all_T2Paths = open(date+"/ntupleT2Paths_"+ date +".txt", 'w')

#------------------------------------------
#MUON CHANNEL
#------------------------------------------
mc_T2Paths = ["MC:"]
data_T2Paths = ["DATA:"]
mcDirT2 = "ntuple_for2017MC_"+date
dataDirT2 = "ntuple_for2017Data_"+date
if isMC:
    for m in range(range_mc):
        mcTime = "MC_"+ date
        config.Data.splitting = 'FileBased'
        config.Data.unitsPerJob = 10
        createMCpsetFile(mcTime, "../../ExLep2017Tree/Selection/test/produceTree_cfg.py", mc, m, date)
        config.General.requestName = getMCKey(mc, m) +"_"+mcTime
        config.General.workArea = 'Crab' +mcTime
        config.JobType.psetName = date+'/config/'+config.General.requestName+ "_cfg.py"
        config.Data.inputDataset = getMCVal(mc, m)
        config.Data.outLFNDirBase = getLFNDirBaseMC(mcTime, mc, m, mcDirT2)
        multiCrabSubmit(config, config.Data.outLFNDirBase)
        mc_T2Paths.append(getNtupleT2Paths(mcTime, mc, m, mcDirT2))

if isData:
    for d in range(range_data):
    ##for d in range(1):
        dataTime = "Data_"+ date
        config.Data.unitsPerJob = 500
        config.Data.splitting = 'LumiBased'
        config.Data.allowNonValidInputDataset = True
        createDatapsetFile(dataTime, "../../ExLep2017Tree/Selection/test/produceTree_cfg.py",data, d, date)
        config.General.requestName = getDataKey(data, d) +"_"+dataTime
        config.General.workArea = 'Crab'+dataTime
        config.JobType.psetName = date+'/config/'+config.General.requestName+ "_cfg.py"
	config.Data.lumiMask = "https://cms-service-dqm.web.cern.ch/cms-service-dqm/CAF/certification/Collisions17/13TeV/ReReco/Cert_294927-306462_13TeV_EOY2017ReReco_Collisions17_JSON_v1.txt"
	config.Data.inputDataset = getDataVal(data, d)
        config.Data.outLFNDirBase = getLFNDirBaseData(dataTime, data, d, dataDirT2)
        multiCrabSubmit(config, config.Data.outLFNDirBase)
        data_T2Paths.append(getNtupleT2Paths(dataTime, data, d, dataDirT2))
mc_T2Paths_.write(str(mc_T2Paths)+",\n\n")
all_T2Paths.write(str(mc_T2Paths)+",\n\n")
data_T2Paths_.write(str(data_T2Paths)+",\n\n")
all_T2Paths.write(str(data_T2Paths)+",\n\n")

