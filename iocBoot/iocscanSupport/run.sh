#!/bin/sh
chmod +x st.cmd
sh start_putrecorder.sh
procServ --allow -n "SCAN" -p pid.txt -L log.txt --logstamp -i ^D^C 2000 ../../bin/$EPICS_HOST_ARCH/scanSupport st.cmd
sleep 10