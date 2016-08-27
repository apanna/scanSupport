#!/bin/env python

import time
import epics

# The function "_abort" is special: it's used by asTrap to abort an executing
# macro
def _abort(prefix):
	print "aborting"
	epics.caput(prefix+"AbortScans", "1")
	epics.caput(prefix+"allstop", "stop")
	epics.caput(prefix+"scaler1.CNT", "Done")

def initScan(start=0, end=1):
	epics.caput("SIM:SCAN:scan1.T1PV","SIM:SCAN:scaler1.CNT")
	epics.caput("SIM:SCAN:scan1.NPTS","21")
	epics.caput("SIM:SCAN:scan1.P1PV","SIM:SCAN:m1.VAL")
	epics.caput("SIM:SCAN:scan1.P1SP",start)
	epics.caput("SIM:SCAN:scan1.P1EP",end)
	epics.caput("SIM:SCAN:scan1.P1SM","LINEAR")
	epics.caput("SIM:SCAN:scan1.P1AR","ABSOLUTE")
	epics.caput("SIM:SCAN:scan1.PASM","STAY")
	epics.caput("SIM:SCAN:scan1.T1PV","SIM:SCAN:scaler1.CNT")
	epics.caput("SIM:SCAN:scan1.D01PV","SIM:SCAN:userCalcOut1.VAL")

def initScaler():
	epics.caput("SIM:SCAN:scaler1.CONT","OneShot")
	epics.caput("SIM:SCAN:scaler1.TP","1.000")
	epics.caput("SIM:SCAN:scaler1.TP1","1.000")
	epics.caput("SIM:SCAN:scaler1.RATE","10.000")
	epics.caput("SIM:SCAN:scaler1.DLY","0.000")
	epics.caput("SIM:SCAN:scaler1_calcEnable.VAL","ENABLE")

def initScanDo(start=0, end=1, d1=1,d2=2,d3=3,d4=4):
	epics.caput("SIM:SCAN:scan1.NPTS","21", wait=True, timeout=300)
	epics.caput("SIM:SCAN:scan1.P1PV","SIM:SCAN:m1.VAL", wait=True, timeout=300)
	epics.caput("SIM:SCAN:scan1.P1SP",start, wait=True, timeout=300)
	epics.caput("SIM:SCAN:scan1.P1EP",end, wait=True, timeout=300)
	epics.caput("SIM:SCAN:scan1.P1SM","LINEAR", wait=True, timeout=300)
	epics.caput("SIM:SCAN:scan1.P1AR","ABSOLUTE", wait=True, timeout=300)
	epics.caput("SIM:SCAN:scan1.PASM","STAY", wait=True, timeout=300)
	epics.caput("SIM:SCAN:scan1.T1PV","SIM:SCAN:scaler1.CNT", wait=True, timeout=300)
	epics.caput("SIM:SCAN:scan1.D01PV","SIM:SCAN:userCalcOut1.VAL", wait=True, timeout=300)
	epics.caput("SIM:SCAN:scan1.EXSC","1", wait=True, timeout=300)
	epics.caput("SIM:SCAN:scan1.EXSC","1", wait=True, timeout=300)

def motorscan(motor="m1", start=0, end=1, step=.1):
	epics.caput("SIM:SCAN:scan1.P1PV",("SIM:SCAN:%s.VAL" % motor), wait=True, timeout=300)
	epics.caput("SIM:SCAN:scan1.P1SP",start, wait=True, timeout=300)
	epics.caput("SIM:SCAN:scan1.P1EP",end, wait=True, timeout=300)
	epics.caput("SIM:SCAN:scan1.P1SI",step, wait=True, timeout=300)
	epics.caput("SIM:SCAN:scan1.EXSC","1", wait=True, timeout=300)

def test3():
	recordDate = "Fri Dec 19 10:44:18 2014"
	epics.caput("SIM:SCAN:scan1.P1PV","SIM:SCAN:m2.VAL", wait=True, timeout=300)
	epics.caput("SIM:SCAN:scan1.P1SP","0.00000", wait=True, timeout=300)
	epics.caput("SIM:SCAN:scan1.P1EP","1.00000", wait=True, timeout=300)
	epics.caput("SIM:SCAN:scan1.P1SI","0.10000", wait=True, timeout=300)
	epics.caput("SIM:SCAN:scan1.P1AR","ABSOLUTE", wait=True, timeout=300)
	epics.caput("SIM:SCAN:scan1.PASM","STAY", wait=True, timeout=300)
	epics.caput("SIM:SCAN:scan1.D01PV","SIM:SCAN:userCalcOut1.VAL", wait=True, timeout=300)
	epics.caput("SIM:SCAN:scan1.T1PV","SIM:SCAN:scaler1.CNT", wait=True, timeout=300)
	epics.caput("SIM:SCAN:scan1.EXSC","1", wait=True, timeout=300)

def a1():
	recordDate = "Fri Dec 19 15:33:01 2014"

def a2():
	recordDate = "Fri Dec 19 15:33:06 2014"

def a3():
	recordDate = "Fri Dec 19 15:33:10 2014"

def a4():
	recordDate = "Fri Dec 19 15:33:14 2014"

def a5():
	recordDate = "Fri Dec 19 15:33:18 2014"

def a6():
	recordDate = "Fri Dec 19 15:33:22 2014"

def a7():
	recordDate = "Fri Dec 19 15:33:25 2014"

def a8():
	recordDate = "Fri Dec 19 15:33:29 2014"

def a9():
	recordDate = "Fri Dec 19 15:33:34 2014"

def a10():
	recordDate = "Fri Dec 19 15:33:40 2014"

def a11():
	recordDate = "Fri Dec 19 15:33:49 2014"

def a12():
	recordDate = "Fri Dec 19 15:33:55 2014"

def scan_test():
	recordDate = "04/21/16 15:32:31"
	epics.caput("SIM:SCAN:scan2.PASM","PRIOR POS", wait=True, timeout=1000000.0)
	epics.caput("SIM:SCAN:scan1.PASM","PRIOR POS", wait=True, timeout=1000000.0)
	epics.caput("SIM:SCAN:scan1.P1AR","RELATIVE", wait=True, timeout=1000000.0)
	epics.caput("SIM:SCAN:scan1.P1SM","LINEAR", wait=True, timeout=1000000.0)
	epics.caput("SIM:SCAN:scan2.P1SM","LINEAR", wait=True, timeout=1000000.0)
	epics.caput("SIM:SCAN:scan3.P1SM","LINEAR", wait=True, timeout=1000000.0)

def sequence():
	recordDate = "04/21/16 15:35:41"
	epics.caput("SIM:SCAN:scan1.PASM","VALLEY POS", wait=True, timeout=1000000.0)
	epics.caput("SIM:SCAN:scan2.PASM","CNTR OF MASS", wait=True, timeout=1000000.0)
	epics.caput("SIM:SCAN:scan3.PASM","PEAK POS", wait=True, timeout=1000000.0)
	epics.caput("SIM:SCAN:scan2.P1PV","", wait=True, timeout=1000000.0)
	epics.caput("SIM:SCAN:scan1.P1PV","", wait=True, timeout=1000000.0)

