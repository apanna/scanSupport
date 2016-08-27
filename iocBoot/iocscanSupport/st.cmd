############################################################################
< envPaths

# For deviocstats
epicsEnvSet("ENGINEER", "Alireza Panna")
epicsEnvSet("LOCATION", "B1D521D DT-SMLIN112")
epicsEnvSet("STARTUP","$(TOP)/iocBoot/$(IOC)")
epicsEnvSet("ST_CMD","st.cmd")

# For stream proto file
epicsEnvSet "STREAM_PROTOCOL_PATH" "$(TOP)/db"

# Change this according to set-up
epicsEnvSet "P" "$(P=SIM:SCAN)"
epicsEnvSet "CONFIG" "$(CONFIG=scan)"
epicsEnvSet "EPICS_IOC_LOG_INET" "192.168.1.5"
epicsEnvSet "EPICS_IOC_LOG_PORT" "7004"
############################################################################
# Increase size of buffer for error logging from default 1256
errlogInit(20000)
############################################################################
# Register all support components
cd $(TOP)
dbLoadDatabase "dbd/scanSupport.dbd"
scanSupport_registerRecordDeviceDriver pdbbase
############################################################################
# Load save_restore.cmd
cd $(IPL_SUPPORT)
< save_restore.cmd
set_requestfile_path("$(TOP)", "scanSupportApp/Db")
set_requestfile_path("$(CAPUTRECORDER)", "caputRecorderApp/Db")
############################################################################
# Load record instances 
cd $(TOP)
dbLoadRecords("db/iocAdminSoft.db","IOC=$(P)")
dbLoadRecords("db/timer.db","P=$(P), N=1")
dbLoadRecords("db/timeString.db","P=$(P)")
dbLoadRecords("db/countDownTimer.vdb","P=$(P), N=1")
dbLoadRecords("db/standardScans.db","P=$(P):,MAXPTS1=2000,MAXPTS2=1000,MAXPTS3=1000,MAXPTS4=10,MAXPTSH=2000")
dbLoadRecords("db/scanProgress.db","P=$(P):scanProgress:")
dbLoadRecords("$(CAPUTRECORDER)/caputRecorderApp/Db/caputPoster.db","P=$(P):,N=300")
dbLoadRecords("$(CAPUTRECORDER)/caputRecorderApp/Db/caputRecorder.db","P=$(P):,N=100")
asSetFilename("$(IPL_SUPPORT)/security.acf")
############################################################################
# Start EPICS IOC
cd $(STARTUP)
iocInit
############################################################################
# Start up the autosave task and tell it what to do.
create_monitor_set("auto_positions.req", 5, "P=$(P):")
create_monitor_set("auto_settings.req", 30, "P=$(P):")

# Handle autosave 'commands' contained in loaded databases
# Searches through the EPICS database for info nodes named 'autosaveFields' 
# and 'autosaveFields_pass0' and write the PV names to the files 
# 'info_settings.req' and 'info_positions.req'
makeAutosaveFiles()
create_monitor_set("info_positions.req",5,"P=$(P):")
create_monitor_set("info_settings.req",30,"P=$(P):")

# For configMenu
create_manual_set("scanMenu.req","P=$(P):,CONFIG=$(CONFIG),CONFIGMENU=1")
############################################################################
# Start EPICS IOC log server
iocLogInit()
setIocLogDisable(0)
############################################################################
# Turn on caPutLogging:
# Log values only on change to the iocLogServer:
caPutLogInit("$(EPICS_IOC_LOG_INET):$(EPICS_IOC_LOG_PORT)",1)
caPutLogShow(2)
############################################################################
# Write all PV names to local text file
dbl > records.txt
############################################################################
# startup SNL programs to monitor scan
#seq &scanProgress ("S=$(P):, P=$(P):scanProgress:")
registerCaputRecorderTrapListener("$(P):caputRecorderCommand")
############################################################################
# print the time our boot was finished
date
############################################################################