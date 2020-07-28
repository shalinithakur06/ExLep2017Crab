import FWCore.ParameterSet.Config as cms
from collections import OrderedDict

#All Data Samples at 13 TeV
dataSampDict_ ={
        "MuRunB2v2": "/SingleMuon/Run2017B-31Mar2018-v1/MINIAOD",
        "MuRunCv1":  "/SingleMuon/Run2017C-31Mar2018-v1/MINIAOD",
        "MuRunDv1":  "/SingleMuon/Run2017D-31Mar2018-v1/MINIAOD",
        "MuRunEv1":  "/SingleMuon/Run2017E-31Mar2018-v1/MINIAOD",
        "MuRunFv1":  "/SingleMuon/Run2017F-31Mar2018-v1/MINIAOD",
        "EleRunBver2v2": "/SingleElectron/Run2017B-31Mar2018-v1/MINIAOD",
        "EleRunCv1":     "/SingleElectron/Run2017C-31Mar2018-v1/MINIAOD",
        "EleRunDv1": 	 "/SingleElectron/Run2017D-31Mar2018-v1/MINIAOD",
        "EleRunEv1": 	 "/SingleElectron/Run2017E-31Mar2018-v1/MINIAOD",
        "EleRunFv1": 	 "/SingleElectron/Run2017F-31Mar2018-v1/MINIAOD"
         }
dataSampDict= OrderedDict(sorted(dataSampDict_.items(), key=lambda t: t[0]))

