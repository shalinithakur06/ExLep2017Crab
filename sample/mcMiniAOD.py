import FWCore.ParameterSet.Config as cms
from collections import OrderedDict

# MC Samples of Excited Lepton & Bkg at 13 TeV
RUN = "RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14"
M = "MINIAODSIM"
#### Both channel
##mcSampDict_ = {"DYJetsToLL_M50":"/DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8/"+RUN+"_ext1-v1/"+M}
#mcSampDict_["DYJetsToLL_Pt50To100"]="/DYJetsToLL_Pt-50To100_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/"+RUN+"-v3/"+M
#mcSampDict_["DYJetsToLL_Pt100To250"]="/DYJetsToLL_Pt-100To250_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/"+RUN+"-v2/"+M
#mcSampDict_["DYJetsToLL_Pt250To400"]="/DYJetsToLL_Pt-250To400_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/"+RUN+"-v1/"+M
#mcSampDict_["DYJetsToLL_Pt400To650"]="/DYJetsToLL_Pt-400To650_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/"+RUN+"-v1/"+M
#mcSampDict_["DYJetsToLL_Pt650ToInf"]="/DYJetsToLL_Pt-650ToInf_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/"+RUN+"-v1/"+M
##mcSampDict_["TT"]="/TTJets_TuneCP5_13TeV-amcatnloFXFX-pythia8/"+RUN+"-v1/"+M
##mcSampDict_["WJetsToLNu"]="/WJetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/"+RUN+"_ext1-v2/"+M
##mcSampDict_["WW"]="/WW_TuneCP5_13TeV-pythia8/"+RUN+"-v1/"+M
##mcSampDict_["WZ"]="/WZ_TuneCP5_13TeV-pythia8/"+RUN+"-v1/"+M
##mcSampDict_["ZZ"]="/ZZ_TuneCP5_13TeV-pythia8/"+RUN+"-v1/"+M

mcSampDict_ = {"ExLepMuMuZ_M250":"/ExcitedLepton_MuMuZ-250_TuneCP5_13TeV_pythia8/"+RUN+"-v1/"+M}
mcSampDict_["ExLepMuMuZ_M250"]="/ExcitedLepton_MuMuZ-250_TuneCP5_13TeV_pythia8/"+RUN+"-v1/"+M
mcSampDict_["ExLepMuMuZ_M500"]="/ExcitedLepton_MuMuZ-500_TuneCP5_13TeV-pythia8/"+RUN+"-v1/"+M
mcSampDict_["ExLepMuMuZ_M750"]="/ExcitedLepton_MuMuZ-750_TuneCP5_13TeV-pythia8/"+RUN+"-v1/"+M
mcSampDict_["ExLepMuMuZ_M1000"]="/ExcitedLepton_MuMuZ-1000_TuneCP5_13TeV-pythia8/"+RUN+"-v1/"+M
mcSampDict_["ExLepMuMuZ_M1250"]="/ExcitedLepton_MuMuZ-1250_TuneCP5_13TeV-pythia8/"+RUN+"-v1/"+M
mcSampDict_["ExLepMuMuZ_M1500"]="/ExcitedLepton_MuMuZ-1500_TuneCP5_13TeV-pythia8/"+RUN+"-v1/"+M
mcSampDict_["ExLepMuMuZ_M1750"]="/ExcitedLepton_MuMuZ-1750_TuneCP5_13TeV-pythia8/"+RUN+"-v1/"+M
mcSampDict_["ExLepMuMuZ_M2000"]="/ExcitedLepton_MuMuZ-2000_TuneCP5_13TeV-pythia8/"+RUN+"-v1/"+M
mcSampDict_["ExLepMuMuZ_M2500"]="/ExcitedLepton_MuMuZ-2500_TuneCP5_13TeV-pythia8/"+RUN+"-v1/"+M
mcSampDict_["ExLepMuMuZ_M3000"]="/ExcitedLepton_MuMuZ-3000_TuneCP5_13TeV-pythia8/"+RUN+"-v1/"+M
mcSampDict_["ExLepMuMuZ_M3500"]="/ExcitedLepton_MuMuZ-3500_TuneCP5_13TeV-pythia8/"+RUN+"-v1/"+M
mcSampDict_["ExLepMuMuZ_M4000"]="/ExcitedLepton_MuMuZ-4000_TuneCP5_13TeV-pythia8/"+RUN+"-v1/"+M
mcSampDict_["ExLepMuMuZ_M4500"]="/ExcitedLepton_MuMuZ-4500_TuneCP5_13TeV-pythia8/"+RUN+"-v1/"+M
mcSampDict_["ExLepMuMuZ_M5000"]="/ExcitedLepton_MuMuZ-5000_TuneCP5_13TeV-pythia8/"+RUN+"-v1/"+M

mcSampDict_["ExLepEEZ_M250"]="/ExcitedLepton_EEZ-250_TuneCP5_13TeV-pythia8/"+RUN+"-v1/"+M
mcSampDict_["ExLepEEZ_M500"]="/ExcitedLepton_EEZ-500_TuneCP5_13TeV-pythia8/"+RUN+"-v1/"+M
mcSampDict_["ExLepEEZ_M750"]="/ExcitedLepton_EEZ-750_TuneCP5_13TeV-pythia8/"+RUN+"-v1/"+M
mcSampDict_["ExLepEEZ_M1000"]="/ExcitedLepton_EEZ-1000_TuneCP5_13TeV-pythia8/"+RUN+"-v1/"+M
mcSampDict_["ExLepEEZ_M1250"]="/ExcitedLepton_EEZ-1250_TuneCP5_13TeV-pythia8/"+RUN+"-v1/"+M
mcSampDict_["ExLepEEZ_M1500"]="/ExcitedLepton_EEZ-1500_TuneCP5_13TeV-pythia8/"+RUN+"-v1/"+M
mcSampDict_["ExLepEEZ_M1750"]="/ExcitedLepton_EEZ-1750_TuneCP5_13TeV-pythia8/"+RUN+"-v1/"+M
mcSampDict_["ExLepEEZ_M2000"]="/ExcitedLepton_EEZ-2000_TuneCP5_13TeV-pythia8/"+RUN+"-v1/"+M
mcSampDict_["ExLepEEZ_M2500"]="/ExcitedLepton_EEZ-2500_TuneCP5_13TeV-pythia8/"+RUN+"-v1/"+M
mcSampDict_["ExLepEEZ_M3000"]="/ExcitedLepton_EEZ-3000_TuneCP5_13TeV-pythia8/"+RUN+"-v1/"+M
mcSampDict_["ExLepEEZ_M3500"]="/ExcitedLepton_EEZ-3500_TuneCP5_13TeV-pythia8/"+RUN+"-v1/"+M
mcSampDict_["ExLepEEZ_M4000"]="/ExcitedLepton_EEZ-4000_TuneCP5_13TeV-pythia8/"+RUN+"-v1/"+M
mcSampDict_["ExLepEEZ_M4500"]="/ExcitedLepton_EEZ-4500_TuneCP5_13TeV-pythia8/"+RUN+"-v1/"+M
mcSampDict_["ExLepEEZ_M5000"]="/ExcitedLepton_EEZ-5000_TuneCP5_13TeV-pythia8/"+RUN+"-v1/"+M

# Sort dictionaly w.r.t the keys
mcSampDict= OrderedDict(sorted(mcSampDict_.items(), key=lambda t: t[0]))

