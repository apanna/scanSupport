TOP=../..
include $(TOP)/configure/CONFIG
#----------------------------------------
#  ADD MACRO DEFINITIONS AFTER THIS LINE

#----------------------------------------------------
#  Optimization of db files using dbst (DEFAULT: NO)
#DB_OPT = YES

#----------------------------------------------------
# Create and install (or just install) into <top>/db
# databases, templates, substitutions like this
ifdef AUTOSAVE
	DB_INSTALLS += $(AUTOSAVE)/asApp/Db/save_restoreStatus.db
endif
ifdef CAPUTRECORDER
	DB_INSTALLS += $(CAPUTRECORDER)/caputRecorderApp/Db/caputPoster.db
	DB_INSTALLS += $(CAPUTRECORDER)/caputRecorderApp/Db/caputRecorder.db
endif
ifdef DEVIOCSTATS
	DB_INSTALLS += $(DEVIOCSTATS)/db/iocAdminSoft.db
endif
ifdef SSCAN
	DB_INSTALLS += $(SSCAN)/sscanApp/Db/standardScans.db
	DB_INSTALLS += $(SSCAN)/sscanApp/Db/scanProgress.db
endif
ifdef STD
	DB_INSTALLS += $(STD)/stdApp/Db/timer.db
	DB_INSTALLS += $(STD)/stdApp/Db/timeString.db
	DB_INSTALLS += $(STD)/stdApp/Db/countDownTimer.vdb
	DB_INSTALLS += $(STD)/stdApp/Db/async_pid_control.db
endif

#----------------------------------------------------
# If <anyname>.db template is not named <anyname>*.template add
# <anyname>_template = <templatename>

include $(TOP)/configure/RULES
#----------------------------------------
#  ADD RULES AFTER THIS LINE

