# MultiCrab

 ### First setup the MiniTree package
 * https://github.com/ravindkv/ExLep2016Tree/blob/master/README.md
 
 #### Download and set MultiCrab ####
 * git clone git@github.com:ravindkv/ExLep2016Crab.git
 * cd ExLep2016Crab/crab
 * source /cvmfs/cms.cern.ch/crab3/crab_standalone.sh
 * voms-proxy-init -voms cms

 #### Run CRAB over single sample ####
 * crab submit oneMiniTreeCrab_cfg.py
 
 #### Run CRAB over multiple samples ####
 * python multiMiniTreeCrab_cfg.py
 
 #### Take a look at CRAB tutorial ####
 * https://twiki.cern.ch/twiki/bin/view/CMSPublic/WorkBookCRAB3Tutorial
 * https://twiki.cern.ch/twiki/bin/view/CMSPublic/CRAB3ConfigurationFile
 * https://twiki.cern.ch/twiki/bin/view/CMSPublic/CRABClientLibraryAPI#Example_submitting_multiple_task 
