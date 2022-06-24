# Keywords 
# ETHERNET Statistics, Bacnet  statistics , Memory Usage , Device Beginning Now 
from re import A
from matplotlib.font_manager import json_dump
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime
import altair as alt
import json 

# Setting Homepage title & icon
st.set_page_config(page_title='Home')

## Some random name Logline , Logview , smartlog , logboard , dashlog , datalog , logdex
st.markdown('''
    # Logboard
     Start dashboarding your log by uploading your log file in sideBar.
     



''')

# Data 
# SideBar 
# Taking log file from user
with st.sidebar.header('Upload .log file'):
    uploaded_file = st.sidebar.file_uploader("Drag and drop your log file")

if uploaded_file is not None :  
    
     # ETHERNET
    times = []
    Rx_Bytes = []
    Tx_Bytes = []
    Rx_Drop = []
    Tx_Drop = []
    Rx_Error = []
    Tx_Error = []
    Rx_Packets = []
    Tx_Packets = []

    #BacNet statistics at TIME 
    Bacnet_Time = []
    ALQ_totalrecordsadded = []
    ALQ_totalrecordsdropped = []
    ALQ_usedrecordscount = []
    ALQ_readindex = []
    ALQ_currentindex = []

    NLQ0_totalrecordsadded = []
    NLQ0_totalrecordsdropped = []
    NLQ0_totalrecordscount = []
    NLQ0_usedrecordscount = []
    NLQ0_readindex = []
    NLQ0_currentindex = []
    NLQ0_freecount = []
    NLQ0_dropiam = []
    NLQ0_nlqloadpctlimit = []

    NLQ1_totalrecordsadded = []
    NLQ1_totalrecordsdropped = []
    NLQ1_totalrecordscount = []
    NLQ1_usedrecordscount = []
    NLQ1_readindex = []
    NLQ1_currentindex = []
    NLQ1_freecount = []
    NLQ1_dropiam = []
    NLQ1_nlqloadpctlimit = []

    NLQ2_totalrecordsadded = []
    NLQ2_totalrecordsdropped = []
    NLQ2_totalrecordscount = []
    NLQ2_usedrecordscount = []
    NLQ2_readindex = []
    NLQ2_currentindex = []
    NLQ2_freecount = []
    NLQ2_dropiam = []
    NLQ2_nlqloadpctlimit = []

    NLQ3_totalrecordsadded = []
    NLQ3_totalrecordsdropped = []
    NLQ3_totalrecordscount = []
    NLQ3_usedrecordscount = []
    NLQ3_readindex = []
    NLQ3_currentindex = []
    NLQ3_freecount = []
    NLQ3_dropiam = []
    NLQ3_nlqloadpctlimit = []


    # BACnet Services stats at TIME
    BACnet_server_time = []
    kkeys = ['total_time' ,'no_of_packets' , 'individual_packet_time' ]
    whois = dict([(key, []) for key in kkeys])
    iam = dict([(key, []) for key in kkeys])
    rpm = dict([(key, []) for key in kkeys])
    rp = dict([(key, []) for key in kkeys])
    rr = dict([(key, []) for key in kkeys])
    almack = dict([(key, []) for key in kkeys])
    uncovnt = dict([(key, []) for key in kkeys])
    getevsum = dict([(key, []) for key in kkeys])
    baddlist = dict([(key, []) for key in kkeys])
    bgetinfo = dict([(key, []) for key in kkeys])
    butctimsync = dict([(key, []) for key in kkeys])

    #MEMORY_LIMIT
    Memory_Usage_Time = []
    Total_System_Memory = []
    Available_System_Memory = []

    # Times system restarted 
    Beginning_Now = []

    
    lines = list(map(lambda x : x.decode('UTF-8') ,uploaded_file.readlines()))

    for line in lines:
            if("Device Beginning Now" in line):
                Beginning_Now.append(datetime.datetime.fromtimestamp(int(line.split()[4],16)))
            if("Ethernet Statistics at TIME: " in line):
                times.append(line[-2:-10:-1][::-1])
            if("Rx_Bytes " in line):
                Rx_Bytes.append(line[9:-1])
            if("Tx_Bytes " in line):
                Tx_Bytes.append(line[9:-1])
            if("Rx_Drop " in line):
                Rx_Drop.append(line[8:-1])
            if("Tx_Drop " in line):
                Tx_Drop.append(line[8:-1])
            if("Rx_Error" in line):
                Rx_Error.append(line[9:-1])
            if("Tx_Error" in line):
                Tx_Error.append(line[9:-1])
            if("Rx_Packets" in line):
                Rx_Packets.append(line[11:-1])
            if("Tx_Packets" in line):
                Tx_Packets.append(line[11:-1])
            

            # Bacnet statistics at TIME 
            if("BACnet statistics at TIME" in line):
                Bacnet_Time.append(line[-2:-10:-1][::-1])
            if("ALQ : totalrecordsadded" in line) :
                l = line.split(" ")
                ALQ_totalrecordsadded.append(int(l[4][:-1]))
                ALQ_totalrecordsdropped.append(int(l[7]))
            if("ALQ : usedrecordscount" in line):
                l = line.split(" ")
                ALQ_usedrecordscount.append(int(l[4][:-1]))
                ALQ_readindex.append(int(l[7][:-1]))
                ALQ_currentindex.append(int(l[10]))


            # NLQ0
            if("NLQ0 : totalrecordsadded" in line):
                l = line.split(" ")
                NLQ0_totalrecordsadded.append(int(l[4][:-1]))
                NLQ0_totalrecordsdropped.append(int(l[7]))
            if("NLQ0 : usedrecordscount" in line):
                l = line.split()
                NLQ0_usedrecordscount.append(int(l[4][:-1]))
                NLQ0_readindex.append(int(l[7][:-1]))
                NLQ0_currentindex.append(int(l[10]))
            if("NLQ0 : freecount" in line):
                l = line.split()
                NLQ0_freecount.append(int(l[4][:-1]))
                NLQ0_dropiam.append(int(l[7]))
                NLQ0_nlqloadpctlimit.append(int(l[10]))
            
            #NLQ1
            if("NLQ1 : totalrecordsadded" in line):
                l = line.split(" ")
                NLQ1_totalrecordsadded.append(int(l[4][:-1]))
                NLQ1_totalrecordsdropped.append(int(l[7]))
            if("NLQ1 : usedrecordscount" in line):
                l = line.split()
                NLQ1_usedrecordscount.append(int(l[4][:-1]))
                NLQ1_readindex.append(int(l[7][:-1]))
                NLQ1_currentindex.append(int(l[10]))
            if("NLQ1 : freecount" in line):
                l = line.split()
                NLQ1_freecount.append(int(l[4][:-1]))
                NLQ1_dropiam.append(int(l[7]))
                NLQ1_nlqloadpctlimit.append(int(l[10]))
            
            #NLQ2
            if("NLQ2 : totalrecordsadded" in line):
                l = line.split(" ")
                NLQ2_totalrecordsadded.append(int(l[4][:-1]))
                NLQ2_totalrecordsdropped.append(int(l[7]))
            if("NLQ2 : usedrecordscount" in line):
                l = line.split()
                NLQ2_usedrecordscount.append(int(l[4][:-1]))
                NLQ2_readindex.append(int(l[7][:-1]))
                NLQ2_currentindex.append(int(l[10]))
            if("NLQ2 : freecount" in line):
                l = line.split()
                NLQ2_freecount.append(int(l[4][:-1]))
                NLQ2_dropiam.append(int(l[7]))
                NLQ2_nlqloadpctlimit.append(int(l[10]))
            
            # NLQ3 
            if("NLQ3 : totalrecordsadded" in line):
                l = line.split(" ")
                NLQ3_totalrecordsadded.append(int(l[4][:-1]))
                NLQ3_totalrecordsdropped.append(int(l[7]))
            if("NLQ3 : usedrecordscount" in line):
                l = line.split()
                NLQ3_usedrecordscount.append(int(l[4][:-1]))
                NLQ3_readindex.append(int(l[7][:-1]))
                NLQ3_currentindex.append(int(l[10]))
            if("NLQ3 : freecount" in line):
                l = line.split()
                NLQ3_freecount.append(int(l[4][:-1]))
                NLQ3_dropiam.append(int(l[7]))
                NLQ3_nlqloadpctlimit.append(int(l[10]))
            
            # BACnet Services stats 
            if("BACnet Services stats" in line) :
                BACnet_server_time.append(line[-2:-10:-1][::-1])
            if(line.startswith("WHOIS")) :
                l = line.split()
                for i in range(3):
                    temp = whois[kkeys[i]]
                    temp.append(float(l[i+1]))
                    whois[kkeys[i]] = temp
            if(line.startswith("IAM")) :
                l = line.split()
                for i in range(3):
                    temp = iam[kkeys[i]]
                    temp.append(float(l[i+1]))
                    iam[kkeys[i]] = temp

            if("RPM" in line.split()):
                l = line.split()
                for i in range(3):
                    temp = rpm[kkeys[i]]
                    temp.append(float(l[i+1]))
                    rpm[kkeys[i]] = temp
                    
            # if("SUBCOVP" in line.split()):
            #     l = line.split()

            if("RP" in line.split()) :
                l = line.split()
                for i in range(3):
                    temp = rp[kkeys[i]]
                    temp.append(float(l[i+1]))
                    rp[kkeys[i]] = temp
            
            if("RR" in line.split()) :
                l = line.split()
                for i in range(3):
                    temp = rr[kkeys[i]]
                    temp.append(float(l[i+1]))
                    rr[kkeys[i]] = temp

            if("AlmAck" in line.split()) :
                l = line.split()
                for i in range(3):
                    temp = almack[kkeys[i]]
                    temp.append(float(l[i+1]))
                    almack[kkeys[i]] = temp

            if("getEvSum" in line.split()) :
                l = line.split()
                for i in range(3):
                    temp = getevsum[kkeys[i]]
                    temp.append(float(l[i+1]))
                    getevsum[kkeys[i]] = temp
            if("BADDLIST" in line.split()) :
                l = line.split()
                for i in range(3):
                    temp = baddlist[kkeys[i]]
                    temp.append(float(l[i+1]))
                    baddlist[kkeys[i]] = temp

            if("BGETINFO" in line.split()) :
                l = line.split()
                for i in range(3):
                    temp = bgetinfo[kkeys[i]]
                    temp.append(float(l[i+1]))
                    bgetinfo[kkeys[i]] = temp

            if("BUTCTIMSYNC" in line.split()) :
                l = line.split()
                for i in range(3):
                    temp = butctimsync[kkeys[i]]
                    temp.append(float(l[i+1]))
                    butctimsync[kkeys[i]] = temp

            
            # Memory Usage 
            if("Memory Usage at TIME:" in line):
                Memory_Usage_Time.append(line[-2:-10:-1][::-1])
            if(" Total System Memory" in line):
                Total_System_Memory.append(int((line.replace(" Total System Memory            :  ","").strip())[:-3]))
            if(" Available System Memory" in line):
                Available_System_Memory.append(int((line.replace(" Available System Memory        : ","").strip())[:-3]))

    # From HEX to timedate.datetime
    times = list(map(lambda x : datetime.datetime.fromtimestamp(int(x,16)) , times))
    Memory_Usage_Time =  list(map(lambda x : datetime.datetime.fromtimestamp(int(x,16)) , Memory_Usage_Time))
    Bacnet_Time =  list(map(lambda x : datetime.datetime.fromtimestamp(int(x,16)) , Bacnet_Time))
    BACnet_server_time = list(map(lambda x : datetime.datetime.fromtimestamp(int(x,16)) , BACnet_server_time))


    # Converting Memory Usuage to JSON
    Memory_Usage = {}
    for i in range(len(Memory_Usage_Time)):
        n = {}
        n["time"] = str(Memory_Usage_Time[i])
        n["tot_mem"] = Total_System_Memory[i]
        n["avail_mem"] = Available_System_Memory[i]
        Memory_Usage[i] = n
    
    Memory_Usage = json.dumps(Memory_Usage)
    # st.json(Memory_Usage)

    # Converting Ethernet Statistics to JSON
    Ethernet_Statistics = {}
    for i in range(len(times)):
        es = {}
        es["time"] = str(times[i])
        es["Rx_Bytes"] = Rx_Bytes[i]
        es["Tx_Bytes"] = Tx_Bytes[i]
        es["Rx_Drop"] = Rx_Drop[i]
        es["Tx_Drop"] = Tx_Drop[i]
        es["Rx_Error"] = Rx_Error[i]
        es["Tx_Error"] = Tx_Error[i]
        es["Rx_Packets"] = Rx_Packets[i]
        es["Tx_Packets"] = Tx_Packets[i]
        Ethernet_Statistics[i] = es
    # Ethernet_Statistics = json.dumps(Ethernet_Statistics)
    # st.json(Ethernet_Statistics)

    # Converting BACnet statistics 
    BACnet_statistics = {}
    for i in range(len(Bacnet_Time)):
        bn = {}
        bn['time'] = str(Bacnet_Time[i])
        alq = {}
        alq["totalrecodsadded"] = ALQ_totalrecordsadded[i]
        alq["totalrecordsdropped"] = ALQ_totalrecordsdropped[i]
        alq["usedrecordscount"] = ALQ_usedrecordscount[i]
        alq["readindex"] = ALQ_readindex[i]
        alq["currentindex"] = ALQ_currentindex[i]

        nlq0 = {}
        nlq0["totalrecodsadded"] =    NLQ0_totalrecordsadded[i]
        nlq0["totalrecordsdropped"] = NLQ0_totalrecordsdropped[i]
        nlq0["usedrecordscount"] =    NLQ0_usedrecordscount[i]
        nlq0["readindex"] =           NLQ0_readindex[i]
        nlq0["currentindex"] =        NLQ0_currentindex[i]
        nlq0["freecount"] =           NLQ0_freecount[i]
        nlq0["dropiam"] =             NLQ0_dropiam[i]
        nlq0["nlqloadpctlimit"] =     NLQ0_nlqloadpctlimit[i]
       
        nlq1 = {}
        nlq1["totalrecodsadded"] =    NLQ1_totalrecordsadded[i]
        nlq1["totalrecordsdropped"] = NLQ1_totalrecordsdropped[i]
        nlq1["usedrecordscount"] =    NLQ1_usedrecordscount[i]
        nlq1["readindex"] =           NLQ1_readindex[i]
        nlq1["currentindex"] =        NLQ1_currentindex[i]
        nlq1["freecount"] =           NLQ1_freecount[i]
        nlq1["dropiam"] =             NLQ1_dropiam[i]
        nlq1["nlqloadpctlimit"] =     NLQ1_nlqloadpctlimit[i]
       
        nlq2 = {}
        nlq2["totalrecodsadded"] =    NLQ2_totalrecordsadded[i]
        nlq2["totalrecordsdropped"] = NLQ2_totalrecordsdropped[i]
        nlq2["usedrecordscount"] =    NLQ2_usedrecordscount[i]
        nlq2["readindex"] =           NLQ2_readindex[i]
        nlq2["currentindex"] =        NLQ2_currentindex[i]
        nlq2["freecount"] =           NLQ2_freecount[i]
        nlq2["dropiam"] =             NLQ2_dropiam[i]
        nlq2["nlqloadpctlimit"] =     NLQ2_nlqloadpctlimit[i]
       

        nlq3 = {}
        nlq3["totalrecodsadded"] =    NLQ3_totalrecordsadded[i]
        nlq3["totalrecordsdropped"] = NLQ3_totalrecordsdropped[i]
        nlq3["usedrecordscount"] =    NLQ3_usedrecordscount[i]
        nlq3["readindex"] =           NLQ3_readindex[i]
        nlq3["currentindex"] =        NLQ3_currentindex[i]
        nlq3["freecount"] =           NLQ3_freecount[i]
        nlq3["dropiam"] =             NLQ3_dropiam[i]
        nlq3["nlqloadpctlimit"] =     NLQ3_nlqloadpctlimit[i]
       
        bn["ALQ"] = alq
        bn['NLQ0'] = nlq0
        bn['NLQ1'] = nlq1
        bn['NLQ2'] = nlq2
        bn['NLQ3'] = nlq3

        BACnet_statistics[i] = bn
    # BACnet_statistics = json.dumps(BACnet_statistics)
    # st.json(BACnet_statistics)

    # Converting Device Beginning Now 
    Device_Beginning_Now = {}
    for i in range(len(Beginning_Now)):
        Device_Beginning_Now[i] = str(Beginning_Now[i])
    Device_Beginning_Now = json.dumps(Device_Beginning_Now)
    # st.json(Device_Beginning_Now)

    # Converting BACnet_services
    BACnet_Services_stats = {}
    for i in range(len(BACnet_server_time)) :
        bn = {}
        bn["time"] = str(BACnet_server_time[i])
        li = [whois,iam,rpm,rp,rr,almack,getevsum,baddlist,bgetinfo,butctimsync]

        name = ["WHOIS","IAM","RPM" , "RP" , "RR" , "AlmAck"  , "getEvSum" , "BADDLIST" , "BGETINFO" , "BUTCTIMSYNC"]

        for k in range(len(li)):
            bn[name[k]] = dict()
            for j in range(3):
                lis = li[k][kkeys[j]]
                bn[name[k]][kkeys[j]] = lis[i]
        BACnet_Services_stats[i] = bn
    # BACnet_Services_stats = json.dumps(BACnet_Services_stats)
    
    # Total available memory vs time
    Time_df = pd.DataFrame()
    Time_df["Total System"] = Total_System_Memory
    Time_df["Available Memory"] = Available_System_Memory
    Time_df["Memory_Usage_Time"] = Memory_Usage_Time
    # Time_df["Memory_Usage_Time"] =  Time_df['Memory_Usage_Time'].apply(lambda x: x.value)//10**9
    # temp = Time_df["Memory_Usage_Time"][0]
    # Time_df["Memory_Usage_Time"] = Time_df['Memory_Usage_Time'].apply(lambda x: x - temp)
    Time_df["Memory_Usage_Time"] = Time_df["Memory_Usage_Time"].apply(lambda x : x.ctime()) 
    # Time_df["Memory_Usage_Time"] = Time_df.datetime.values.astype(np.int64) // 10 ** 9
    Time_df["Used_Memory"] = Time_df['Total System'] - Time_df["Available Memory"]
    Time_df.drop(["Available Memory"] , axis= 1 , inplace= True)
    Time_df = Time_df.set_index("Memory_Usage_Time")
    if(len(Beginning_Now)!=0):
        col1 , col2 = st.columns(2)
        col1.metric("Device Reboots" , len(Beginning_Now) )
        for t in range(len(Beginning_Now)) :
            time = Beginning_Now[t]
            Beginning_Now[t] = time.strftime("%d %B, %Y, %H:%M:%S")
        print(Beginning_Now)
        Beginning_Now = pd.DataFrame(data= Beginning_Now , columns= ["Time"])
        col2.dataframe(Beginning_Now)
    st.header("Memory Usage")
    chart = alt.Chart(Time_df.reset_index()).mark_area().encode(
        x=alt.X('Memory_Usage_Time', axis=alt.Axis(labelOverlap="greedy",grid=False)),
        y=alt.Y('Used_Memory'),color = alt.value('orange') )
    sys = alt.Chart(Time_df.reset_index()).mark_area().encode(
        x=alt.X('Memory_Usage_Time', axis=alt.Axis(labelOverlap="greedy",grid=False)),
        y=alt.Y('Total System'))
        
    chart = alt.layer(sys,chart)
    st.altair_chart(chart, use_container_width=True)
  
    Rx_Bytes = list(map(lambda x : int(x,16)//1000, Rx_Bytes))
    Tx_Bytes = list(map(lambda x : int(x,16)//1000 , Tx_Bytes))
    Time_byte = pd.DataFrame()
    Time_byte['Time']= times
    Time_byte ["Time"] = Time_byte["Time"].apply(lambda x : x.ctime()) 
    Time_byte = Time_byte.set_index("Time")
    Time_byte["Received Bytes"] = Rx_Bytes
    Time_byte["Transmitted Bytes"] = Tx_Bytes
    Time_byte["Received Packets"] = list(map(lambda x : int(x,16),Rx_Packets))
    Time_byte["Transmitted Packets"] = list(map(lambda x : int(x,16),Tx_Packets))
    if(len(Time_byte["Transmitted Packets"])>20):
        val = []
        i = 0
        while i < (len(Time_byte["Transmitted Bytes"])):
            val.append(i)
            i+=5
        Time_byte = Time_byte.iloc[val , 0:]

    st.markdown('''
    ## Ethernet Statistics
    #### Bytes Received and Transmitted
    ''')
    
    st.bar_chart(Time_byte[["Received Bytes","Transmitted Bytes"]])
    E_Bytes = pd.DataFrame()
    E_Bytes["Times"] = times
    E_Bytes["Times"]=E_Bytes["Times"].apply(lambda x : x.ctime())
    # E_Bytes["Received Bytes"]

    st.subheader("Packets")
    st.line_chart(Time_byte[["Received Packets", "Transmitted Packets"]])
    st.subheader("Drop in Bytes")
    col1,col2 = st.columns(2)
    col1.metric("Drop in Received Bytes",Rx_Drop[0])    
    col2.metric("Drop in Transmitted Bytes", Tx_Drop[0])

    # Time_byte["Rx_Error"] = Rx_Error
    # Time_byte['Tx_Error'] = Tx_Error
    
    st.subheader("Errors in Receiving and transmitting")
    col1,col2 = st.columns(2)
    col1.metric("Error in Receiving Bytes",Rx_Error[0])
    col2.metric("Error in Transmitted Bytes", Tx_Error[0])

    st.header("BacNet Statistics")
    Bac_byte_ALQ = pd.DataFrame()
    Bac_byte_ALQ["totalrecodsadded"] = ALQ_totalrecordsadded
    Bac_byte_ALQ["totalrecordsdropped"] = ALQ_totalrecordsdropped
    Bac_byte_ALQ["usedrecordscount"] = ALQ_usedrecordscount
    Bac_byte_ALQ["readindex"] = ALQ_readindex
    Bac_byte_ALQ["currentindex"] = ALQ_currentindex
    # st.dataframe(Bac_byte_ALQ)
    Bac_byte_ALQ['Time'] = times    
    Bac_byte_ALQ['Time']=Bac_byte_ALQ["Time"].apply(lambda x : x.strftime("%d %B, %Y, %H:%M"))
    Bac_byte_ALQ=Bac_byte_ALQ.set_index('Time')
    # st.write(Bac_byte_ALQ['Time'])
    options = st.multiselect("Filter by params",list(Bac_byte_ALQ.columns),list(Bac_byte_ALQ.columns))
    st.line_chart(Bac_byte_ALQ[options])

    options = st.multiselect("Select NLQ" ,["NLQ0","NLQ1","NLQ2","NLQ3"])
    if("NLQ0" in options):
        Bac_byte_NLQ0 = pd.DataFrame()
        Bac_byte_NLQ0["totalrecodsadded"] =    NLQ0_totalrecordsadded
        Bac_byte_NLQ0["totalrecordsdropped"] = NLQ0_totalrecordsdropped
        Bac_byte_NLQ0["usedrecordscount"] =    NLQ0_usedrecordscount
        Bac_byte_NLQ0["readindex"] =           NLQ0_readindex
        Bac_byte_NLQ0["currentindex"] =        NLQ0_currentindex
        Bac_byte_NLQ0["freecount"] =           NLQ0_freecount
        Bac_byte_NLQ0["dropiam"] =             NLQ0_dropiam
        Bac_byte_NLQ0["nlqloadpctlimit"] =     NLQ0_nlqloadpctlimit
        Bac_byte_NLQ0['Time'] = times    
        Bac_byte_NLQ0['Time']=Bac_byte_NLQ0["Time"].apply(lambda x : x.strftime("%d %B, %Y, %H:%M"))
        Bac_byte_NLQ0=Bac_byte_NLQ0.set_index('Time')
        st.line_chart(Bac_byte_NLQ0)
        # st.dataframe(Bac_byte_NLQ0)
    if("NLQ1" in options):
        Bac_byte_NLQ1 = pd.DataFrame()
        Bac_byte_NLQ1["totalrecodsadded"] =    NLQ1_totalrecordsadded
        Bac_byte_NLQ1["totalrecordsdropped"] = NLQ1_totalrecordsdropped
        Bac_byte_NLQ1["usedrecordscount"] =    NLQ1_usedrecordscount
        Bac_byte_NLQ1["readindex"] =           NLQ1_readindex
        Bac_byte_NLQ1["currentindex"] =        NLQ1_currentindex
        Bac_byte_NLQ1["freecount"] =           NLQ1_freecount
        Bac_byte_NLQ1["dropiam"] =             NLQ1_dropiam
        Bac_byte_NLQ1["nlqloadpctlimit"] =     NLQ1_nlqloadpctlimit
        Bac_byte_NLQ1['Time'] = times    
        Bac_byte_NLQ1['Time']=Bac_byte_NLQ1["Time"].apply(lambda x : x.strftime("%d %B, %Y, %H:%M"))
        Bac_byte_NLQ1=Bac_byte_NLQ1.set_index('Time')
        st.line_chart(Bac_byte_NLQ1)
        # st.dataframe(Bac_byte_NLQ1)
    if("NLQ2" in options):
        Bac_byte_NLQ2 = pd.DataFrame()
        Bac_byte_NLQ2["totalrecodsadded"] =    NLQ2_totalrecordsadded
        Bac_byte_NLQ2["totalrecordsdropped"] = NLQ2_totalrecordsdropped
        Bac_byte_NLQ2["usedrecordscount"] =    NLQ2_usedrecordscount
        Bac_byte_NLQ2["readindex"] =           NLQ2_readindex
        Bac_byte_NLQ2["currentindex"] =        NLQ2_currentindex
        Bac_byte_NLQ2["freecount"] =           NLQ2_freecount
        Bac_byte_NLQ2["dropiam"] =             NLQ2_dropiam
        Bac_byte_NLQ2["nlqloadpctlimit"] =     NLQ2_nlqloadpctlimit
        Bac_byte_NLQ2['Time'] = times    
        Bac_byte_NLQ2['Time']=Bac_byte_NLQ2["Time"].apply(lambda x : x.strftime("%d %B, %Y, %H:%M"))
        Bac_byte_NLQ2=Bac_byte_NLQ2.set_index('Time')
        st.line_chart(Bac_byte_NLQ2)
        # st.dataframe(Bac_byte_NLQ2)
    if("NLQ3" in options):
        Bac_byte_NLQ3 = pd.DataFrame()
        Bac_byte_NLQ3["totalrecodsadded"] =    NLQ3_totalrecordsadded
        Bac_byte_NLQ3["totalrecordsdropped"] = NLQ3_totalrecordsdropped
        Bac_byte_NLQ3["usedrecordscount"] =    NLQ3_usedrecordscount
        Bac_byte_NLQ3["readindex"] =           NLQ3_readindex
        Bac_byte_NLQ3["currentindex"] =        NLQ3_currentindex
        Bac_byte_NLQ3["freecount"] =           NLQ3_freecount
        Bac_byte_NLQ3["dropiam"] =             NLQ3_dropiam
        Bac_byte_NLQ3["nlqloadpctlimit"] =     NLQ3_nlqloadpctlimit
        Bac_byte_NLQ3['Time'] = times    
        Bac_byte_NLQ3['Time']=Bac_byte_NLQ3["Time"].apply(lambda x : x.strftime("%d %B, %Y, %H:%M"))
        Bac_byte_NLQ3=Bac_byte_NLQ3.set_index('Time')
        st.line_chart(Bac_byte_NLQ3)
        # st.dataframe(Bac_byte_NLQ3)
    
    st.header('BACnet Service Statistics')
    options = st.multiselect("Select params" , ['total time' ,'no of packets' , 'individual packet time' ])
    if('no of packets' in options):
        bacnet_service = pd.DataFrame()
        li = [whois,iam,rpm,rp,rr,almack,getevsum,baddlist,bgetinfo,butctimsync]

        name = ["WHOIS","IAM","RPM" , "RP" , "RR" , "AlmAck"  , "getEvSum" , "BADDLIST" , "BGETINFO" , "BUTCTIMSYNC"]
        bacnet_service["time"] = BACnet_server_time
        for k in range(len(li)):
            lis = li[k]['no_of_packets']
            bacnet_service[name[k]] = lis
        bacnet_service["time"] = bacnet_service['time'].apply(lambda x : x.strftime("%d %B, %Y, %H:%M"))
        bacnet_service = bacnet_service.set_index('time')
        st.write('Total no of packets')
        st.line_chart(bacnet_service)
    if('total time' in options):
        bacnet_service = pd.DataFrame()
        li = [whois,iam,rpm,rp,rr,almack,getevsum,baddlist,bgetinfo,butctimsync]
    
        name = ["WHOIS","IAM","RPM" , "RP" , "RR" , "AlmAck"  , "getEvSum" , "BADDLIST" , "BGETINFO" , "BUTCTIMSYNC"]
        bacnet_service["time"] = BACnet_server_time
        for k in range(len(li)):
            lis = li[k]['total_time']
            bacnet_service[name[k]] = lis
        bacnet_service["time"] = bacnet_service['time'].apply(lambda x : x.strftime("%d %B, %Y, %H:%M"))
        bacnet_service = bacnet_service.set_index('time')
        st.write('total time')
        st.line_chart(bacnet_service)
        

    if('individual packet time' in options):
        bacnet_service = pd.DataFrame()
        st.write('individual packet time')
        li = [whois,iam,rpm,rp,rr,almack,getevsum,baddlist,bgetinfo,butctimsync]
    
        name = ["WHOIS","IAM","RPM" , "RP" , "RR" , "AlmAck"  , "getEvSum" , "BADDLIST" , "BGETINFO" , "BUTCTIMSYNC"]
        bacnet_service["time"] = BACnet_server_time
        for k in range(len(li)):
            lis = li[k]['individual_packet_time']
            bacnet_service[name[k]] = lis
        bacnet_service["time"] = bacnet_service['time'].apply(lambda x : x.strftime("%d %B, %Y, %H:%M"))
        bacnet_service = bacnet_service.set_index('time')
        st.line_chart(bacnet_service)
      
else :
    # ETHERNET
    times = []
    Rx_Bytes = []
    Tx_Bytes = []
    Rx_Drop = []
    Tx_Drop = []
    Rx_Error = []
    Tx_Error = []
    Rx_Packets = []
    Tx_Packets = []

    #BacNet statistics at TIME 
    Bacnet_Time = []
    ALQ_totalrecordsadded = []
    ALQ_totalrecordsdropped = []
    ALQ_usedrecordscount = []
    ALQ_readindex = []
    ALQ_currentindex = []

    NLQ0_totalrecordsadded = []
    NLQ0_totalrecordsdropped = []
    NLQ0_totalrecordscount = []
    NLQ0_usedrecordscount = []
    NLQ0_readindex = []
    NLQ0_currentindex = []
    NLQ0_freecount = []
    NLQ0_dropiam = []
    NLQ0_nlqloadpctlimit = []

    NLQ1_totalrecordsadded = []
    NLQ1_totalrecordsdropped = []
    NLQ1_totalrecordscount = []
    NLQ1_usedrecordscount = []
    NLQ1_readindex = []
    NLQ1_currentindex = []
    NLQ1_freecount = []
    NLQ1_dropiam = []
    NLQ1_nlqloadpctlimit = []

    NLQ2_totalrecordsadded = []
    NLQ2_totalrecordsdropped = []
    NLQ2_totalrecordscount = []
    NLQ2_usedrecordscount = []
    NLQ2_readindex = []
    NLQ2_currentindex = []
    NLQ2_freecount = []
    NLQ2_dropiam = []
    NLQ2_nlqloadpctlimit = []

    NLQ3_totalrecordsadded = []
    NLQ3_totalrecordsdropped = []
    NLQ3_totalrecordscount = []
    NLQ3_usedrecordscount = []
    NLQ3_readindex = []
    NLQ3_currentindex = []
    NLQ3_freecount = []
    NLQ3_dropiam = []
    NLQ3_nlqloadpctlimit = []


    # BACnet Services stats at TIME
    BACnet_server_time = []
    kkeys = ['total_time' ,'no_of_packets' , 'individual_packet_time' ]
    whois = dict([(key, []) for key in kkeys])
    iam = dict([(key, []) for key in kkeys])
    rpm = dict([(key, []) for key in kkeys])
    rp = dict([(key, []) for key in kkeys])
    rr = dict([(key, []) for key in kkeys])
    almack = dict([(key, []) for key in kkeys])
    uncovnt = dict([(key, []) for key in kkeys])
    getevsum = dict([(key, []) for key in kkeys])
    baddlist = dict([(key, []) for key in kkeys])
    bgetinfo = dict([(key, []) for key in kkeys])
    butctimsync = dict([(key, []) for key in kkeys])

    #MEMORY_LIMIT
    Memory_Usage_Time = []
    Total_System_Memory = []
    Available_System_Memory = []

    # Times system restarted 
    Beginning_Now = []

    with open("Diagnostics_Text_Logs/EverestA9_2.log",'r') as f :
        lines = f.readlines();
        for line in lines:
            if("Device Beginning Now" in line):
                Beginning_Now.append(datetime.datetime.fromtimestamp(int(line.split()[4],16)))
            if("Ethernet Statistics at TIME: " in line):
                times.append(line[-2:-10:-1][::-1])
            if("Rx_Bytes " in line):
                Rx_Bytes.append(line[9:-1])
            if("Tx_Bytes " in line):
                Tx_Bytes.append(line[9:-1])
            if("Rx_Drop " in line):
                Rx_Drop.append(line[8:-1])
            if("Tx_Drop " in line):
                Tx_Drop.append(line[8:-1])
            if("Rx_Error" in line):
                Rx_Error.append(line[9:-1])
            if("Tx_Error" in line):
                Tx_Error.append(line[9:-1])
            if("Rx_Packets" in line):
                Rx_Packets.append(line[11:-1])
            if("Tx_Packets" in line):
                Tx_Packets.append(line[11:-1])
            

            # Bacnet statistics at TIME 
            if("BACnet statistics at TIME" in line):
                Bacnet_Time.append(line[-2:-10:-1][::-1])
            if("ALQ : totalrecordsadded" in line) :
                l = line.split(" ")
                ALQ_totalrecordsadded.append(int(l[4][:-1]))
                ALQ_totalrecordsdropped.append(int(l[7]))
            if("ALQ : usedrecordscount" in line):
                l = line.split(" ")
                ALQ_usedrecordscount.append(int(l[4][:-1]))
                ALQ_readindex.append(int(l[7][:-1]))
                ALQ_currentindex.append(int(l[10]))


            # NLQ0
            if("NLQ0 : totalrecordsadded" in line):
                l = line.split(" ")
                NLQ0_totalrecordsadded.append(int(l[4][:-1]))
                NLQ0_totalrecordsdropped.append(int(l[7]))
            if("NLQ0 : usedrecordscount" in line):
                l = line.split()
                NLQ0_usedrecordscount.append(int(l[4][:-1]))
                NLQ0_readindex.append(int(l[7][:-1]))
                NLQ0_currentindex.append(int(l[10]))
            if("NLQ0 : freecount" in line):
                l = line.split()
                NLQ0_freecount.append(int(l[4][:-1]))
                NLQ0_dropiam.append(int(l[7]))
                NLQ0_nlqloadpctlimit.append(int(l[10]))
            
            #NLQ1
            if("NLQ1 : totalrecordsadded" in line):
                l = line.split(" ")
                NLQ1_totalrecordsadded.append(int(l[4][:-1]))
                NLQ1_totalrecordsdropped.append(int(l[7]))
            if("NLQ1 : usedrecordscount" in line):
                l = line.split()
                NLQ1_usedrecordscount.append(int(l[4][:-1]))
                NLQ1_readindex.append(int(l[7][:-1]))
                NLQ1_currentindex.append(int(l[10]))
            if("NLQ1 : freecount" in line):
                l = line.split()
                NLQ1_freecount.append(int(l[4][:-1]))
                NLQ1_dropiam.append(int(l[7]))
                NLQ1_nlqloadpctlimit.append(int(l[10]))
            
            #NLQ2
            if("NLQ2 : totalrecordsadded" in line):
                l = line.split(" ")
                NLQ2_totalrecordsadded.append(int(l[4][:-1]))
                NLQ2_totalrecordsdropped.append(int(l[7]))
            if("NLQ2 : usedrecordscount" in line):
                l = line.split()
                NLQ2_usedrecordscount.append(int(l[4][:-1]))
                NLQ2_readindex.append(int(l[7][:-1]))
                NLQ2_currentindex.append(int(l[10]))
            if("NLQ2 : freecount" in line):
                l = line.split()
                NLQ2_freecount.append(int(l[4][:-1]))
                NLQ2_dropiam.append(int(l[7]))
                NLQ2_nlqloadpctlimit.append(int(l[10]))
            
            # NLQ3 
            if("NLQ3 : totalrecordsadded" in line):
                l = line.split(" ")
                NLQ3_totalrecordsadded.append(int(l[4][:-1]))
                NLQ3_totalrecordsdropped.append(int(l[7]))
            if("NLQ3 : usedrecordscount" in line):
                l = line.split()
                NLQ3_usedrecordscount.append(int(l[4][:-1]))
                NLQ3_readindex.append(int(l[7][:-1]))
                NLQ3_currentindex.append(int(l[10]))
            if("NLQ3 : freecount" in line):
                l = line.split()
                NLQ3_freecount.append(int(l[4][:-1]))
                NLQ3_dropiam.append(int(l[7]))
                NLQ3_nlqloadpctlimit.append(int(l[10]))
            
            # BACnet Services stats 
            if("BACnet Services stats" in line) :
                BACnet_server_time.append(line[-2:-10:-1][::-1])
            if(line.startswith("WHOIS")) :
                l = line.split()
                for i in range(3):
                    temp = whois[kkeys[i]]
                    temp.append(float(l[i+1]))
                    whois[kkeys[i]] = temp
            if(line.startswith("IAM")) :
                l = line.split()
                for i in range(3):
                    temp = iam[kkeys[i]]
                    temp.append(float(l[i+1]))
                    iam[kkeys[i]] = temp

            if("RPM" in line.split()):
                l = line.split()
                for i in range(3):
                    temp = rpm[kkeys[i]]
                    temp.append(float(l[i+1]))
                    rpm[kkeys[i]] = temp
                    
            # if("SUBCOVP" in line.split()):
            #     l = line.split()

            if("RP" in line.split()) :
                l = line.split()
                for i in range(3):
                    temp = rp[kkeys[i]]
                    temp.append(float(l[i+1]))
                    rp[kkeys[i]] = temp
            
            if("RR" in line.split()) :
                l = line.split()
                for i in range(3):
                    temp = rr[kkeys[i]]
                    temp.append(float(l[i+1]))
                    rr[kkeys[i]] = temp

            if("AlmAck" in line.split()) :
                l = line.split()
                for i in range(3):
                    temp = almack[kkeys[i]]
                    temp.append(float(l[i+1]))
                    almack[kkeys[i]] = temp

            if("getEvSum" in line.split()) :
                l = line.split()
                for i in range(3):
                    temp = getevsum[kkeys[i]]
                    temp.append(float(l[i+1]))
                    getevsum[kkeys[i]] = temp
            if("BADDLIST" in line.split()) :
                l = line.split()
                for i in range(3):
                    temp = baddlist[kkeys[i]]
                    temp.append(float(l[i+1]))
                    baddlist[kkeys[i]] = temp

            if("BGETINFO" in line.split()) :
                l = line.split()
                for i in range(3):
                    temp = bgetinfo[kkeys[i]]
                    temp.append(float(l[i+1]))
                    bgetinfo[kkeys[i]] = temp

            if("BUTCTIMSYNC" in line.split()) :
                l = line.split()
                for i in range(3):
                    temp = butctimsync[kkeys[i]]
                    temp.append(float(l[i+1]))
                    butctimsync[kkeys[i]] = temp

            
            # Memory Usage 
            if("Memory Usage at TIME:" in line):
                Memory_Usage_Time.append(line[-2:-10:-1][::-1])
            if(" Total System Memory" in line):
                Total_System_Memory.append(int((line.replace(" Total System Memory            :  ","").strip())[:-3]))
            if(" Available System Memory" in line):
                Available_System_Memory.append(int((line.replace(" Available System Memory        : ","").strip())[:-3]))

    # From HEX to timedate.datetime
    times = list(map(lambda x : datetime.datetime.fromtimestamp(int(x,16)) , times))
    Memory_Usage_Time =  list(map(lambda x : datetime.datetime.fromtimestamp(int(x,16)) , Memory_Usage_Time))
    Bacnet_Time =  list(map(lambda x : datetime.datetime.fromtimestamp(int(x,16)) , Bacnet_Time))
    BACnet_server_time = list(map(lambda x : datetime.datetime.fromtimestamp(int(x,16)) , BACnet_server_time))


    # Converting Memory Usuage to JSON
    Memory_Usage = {}
    for i in range(len(Memory_Usage_Time)):
        n = {}
        n["time"] = str(Memory_Usage_Time[i])
        n["tot_mem"] = Total_System_Memory[i]
        n["avail_mem"] = Available_System_Memory[i]
        Memory_Usage[i] = n
    
    Memory_Usage = json.dumps(Memory_Usage)
    # st.json(Memory_Usage)

    # Converting Ethernet Statistics to JSON
    Ethernet_Statistics = {}
    for i in range(len(times)):
        es = {}
        es["time"] = str(times[i])
        es["Rx_Bytes"] = Rx_Bytes[i]
        es["Tx_Bytes"] = Tx_Bytes[i]
        es["Rx_Drop"] = Rx_Drop[i]
        es["Tx_Drop"] = Tx_Drop[i]
        es["Rx_Error"] = Rx_Error[i]
        es["Tx_Error"] = Tx_Error[i]
        es["Rx_Packets"] = Rx_Packets[i]
        es["Tx_Packets"] = Tx_Packets[i]
        Ethernet_Statistics[i] = es
    # Ethernet_Statistics = json.dumps(Ethernet_Statistics)
    # st.json(Ethernet_Statistics)

    # Converting BACnet statistics 
    BACnet_statistics = {}
    for i in range(len(Bacnet_Time)):
        bn = {}
        bn['time'] = str(Bacnet_Time[i])
        alq = {}
        alq["totalrecodsadded"] = ALQ_totalrecordsadded[i]
        alq["totalrecordsdropped"] = ALQ_totalrecordsdropped[i]
        alq["usedrecordscount"] = ALQ_usedrecordscount[i]
        alq["readindex"] = ALQ_readindex[i]
        alq["currentindex"] = ALQ_currentindex[i]

        nlq0 = {}
        nlq0["totalrecodsadded"] =    NLQ0_totalrecordsadded[i]
        nlq0["totalrecordsdropped"] = NLQ0_totalrecordsdropped[i]
        nlq0["usedrecordscount"] =    NLQ0_usedrecordscount[i]
        nlq0["readindex"] =           NLQ0_readindex[i]
        nlq0["currentindex"] =        NLQ0_currentindex[i]
        nlq0["freecount"] =           NLQ0_freecount[i]
        nlq0["dropiam"] =             NLQ0_dropiam[i]
        nlq0["nlqloadpctlimit"] =     NLQ0_nlqloadpctlimit[i]
       
        nlq1 = {}
        nlq1["totalrecodsadded"] =    NLQ1_totalrecordsadded[i]
        nlq1["totalrecordsdropped"] = NLQ1_totalrecordsdropped[i]
        nlq1["usedrecordscount"] =    NLQ1_usedrecordscount[i]
        nlq1["readindex"] =           NLQ1_readindex[i]
        nlq1["currentindex"] =        NLQ1_currentindex[i]
        nlq1["freecount"] =           NLQ1_freecount[i]
        nlq1["dropiam"] =             NLQ1_dropiam[i]
        nlq1["nlqloadpctlimit"] =     NLQ1_nlqloadpctlimit[i]
       
        nlq2 = {}
        nlq2["totalrecodsadded"] =    NLQ2_totalrecordsadded[i]
        nlq2["totalrecordsdropped"] = NLQ2_totalrecordsdropped[i]
        nlq2["usedrecordscount"] =    NLQ2_usedrecordscount[i]
        nlq2["readindex"] =           NLQ2_readindex[i]
        nlq2["currentindex"] =        NLQ2_currentindex[i]
        nlq2["freecount"] =           NLQ2_freecount[i]
        nlq2["dropiam"] =             NLQ2_dropiam[i]
        nlq2["nlqloadpctlimit"] =     NLQ2_nlqloadpctlimit[i]
       

        nlq3 = {}
        nlq3["totalrecodsadded"] =    NLQ3_totalrecordsadded[i]
        nlq3["totalrecordsdropped"] = NLQ3_totalrecordsdropped[i]
        nlq3["usedrecordscount"] =    NLQ3_usedrecordscount[i]
        nlq3["readindex"] =           NLQ3_readindex[i]
        nlq3["currentindex"] =        NLQ3_currentindex[i]
        nlq3["freecount"] =           NLQ3_freecount[i]
        nlq3["dropiam"] =             NLQ3_dropiam[i]
        nlq3["nlqloadpctlimit"] =     NLQ3_nlqloadpctlimit[i]
       
        bn["ALQ"] = alq
        bn['NLQ0'] = nlq0
        bn['NLQ1'] = nlq1
        bn['NLQ2'] = nlq2
        bn['NLQ3'] = nlq3

        BACnet_statistics[i] = bn
    # BACnet_statistics = json.dumps(BACnet_statistics)
    # st.json(BACnet_statistics)

    # Converting Device Beginning Now 
    Device_Beginning_Now = {}
    for i in range(len(Beginning_Now)):
        Device_Beginning_Now[i] = str(Beginning_Now[i])
    Device_Beginning_Now = json.dumps(Device_Beginning_Now)
    # st.json(Device_Beginning_Now)

    # Converting BACnet_services
    BACnet_Services_stats = {}
    for i in range(len(BACnet_server_time)) :
        bn = {}
        bn["time"] = str(BACnet_server_time[i])
        li = [whois,iam,rpm,rp,rr,almack,getevsum,baddlist,bgetinfo,butctimsync]

        name = ["WHOIS","IAM","RPM" , "RP" , "RR" , "AlmAck"  , "getEvSum" , "BADDLIST" , "BGETINFO" , "BUTCTIMSYNC"]

        for k in range(len(li)):
            bn[name[k]] = dict()
            for j in range(3):
                lis = li[k][kkeys[j]]
                bn[name[k]][kkeys[j]] = lis[i]
        BACnet_Services_stats[i] = bn
    # BACnet_Services_stats = json.dumps(BACnet_Services_stats)
    
    # Total available memory vs time
    Time_df = pd.DataFrame()
    Time_df["Total System"] = Total_System_Memory
    Time_df["Available Memory"] = Available_System_Memory
    Time_df["Memory_Usage_Time"] = Memory_Usage_Time
    # Time_df["Memory_Usage_Time"] =  Time_df['Memory_Usage_Time'].apply(lambda x: x.value)//10**9
    # temp = Time_df["Memory_Usage_Time"][0]
    # Time_df["Memory_Usage_Time"] = Time_df['Memory_Usage_Time'].apply(lambda x: x - temp)
    Time_df["Memory_Usage_Time"] = Time_df["Memory_Usage_Time"].apply(lambda x : x.ctime()) 
    # Time_df["Memory_Usage_Time"] = Time_df.datetime.values.astype(np.int64) // 10 ** 9
    Time_df["Used_Memory"] = Time_df['Total System'] - Time_df["Available Memory"]
    Time_df.drop(["Available Memory"] , axis= 1 , inplace= True)
    Time_df = Time_df.set_index("Memory_Usage_Time")
    if(len(Beginning_Now)!=0):
        col1 , col2 = st.columns(2)
        col1.metric("Device Reboots" , len(Beginning_Now) )
        for t in range(len(Beginning_Now)) :
            time = Beginning_Now[t]
            Beginning_Now[t] = time.strftime("%d %B, %Y, %H:%M:%S")
        print(Beginning_Now)
        Beginning_Now = pd.DataFrame(data= Beginning_Now , columns= ["Time"])
        col2.dataframe(Beginning_Now)
    st.header("Memory Usage")
    st.area_chart(Time_df)
    Rx_Bytes = list(map(lambda x : int(x,16)//1000, Rx_Bytes))
    Tx_Bytes = list(map(lambda x : int(x,16)//1000 , Tx_Bytes))
    Time_byte = pd.DataFrame()
    Time_byte['Time']= times
    Time_byte ["Time"] = Time_byte["Time"].apply(lambda x : x.ctime()) 
    Time_byte = Time_byte.set_index("Time")
    Time_byte["Received Bytes"] = Rx_Bytes
    Time_byte["Transmitted Bytes"] = Tx_Bytes



    st.markdown('''
    ## Ethernet Statistics
    #### Bytes Received and Transmitted
    ''')
    st.bar_chart(Time_byte)
    E_Bytes = pd.DataFrame()
    E_Bytes["Times"] = times
    E_Bytes["Times"]=E_Bytes["Times"].apply(lambda x : x.ctime())
    # E_Bytes["Received Bytes"]

    st.subheader("Packets")
    Time_byte["Received Packets"] = list(map(lambda x : int(x,16),Rx_Packets))
    Time_byte["Transmitted Packets"] = list(map(lambda x : int(x,16),Tx_Packets))
    st.line_chart(Time_byte[["Received Packets", "Transmitted Packets"]])
    st.subheader("Drop in Bytes")
    col1,col2 = st.columns(2)
    col1.metric("Drop in Received Bytes",Rx_Drop[0])    
    col2.metric("Drop in Transmitted Bytes", Tx_Drop[0])

    Time_byte["Rx_Error"] = Rx_Error
    Time_byte['Tx_Error'] = Tx_Error
    
    st.subheader("Errors in Receiving and transmitting")
    col1,col2 = st.columns(2)
    col1.metric("Error in Receiving Bytes",Rx_Error[0])
    col2.metric("Error in Transmitted Bytes", Tx_Error[0])

    st.header("BacNet Statistics")
    Bac_byte_ALQ = pd.DataFrame()
    Bac_byte_ALQ["totalrecodsadded"] = ALQ_totalrecordsadded
    Bac_byte_ALQ["totalrecordsdropped"] = ALQ_totalrecordsdropped
    Bac_byte_ALQ["usedrecordscount"] = ALQ_usedrecordscount
    Bac_byte_ALQ["readindex"] = ALQ_readindex
    Bac_byte_ALQ["currentindex"] = ALQ_currentindex
    # st.dataframe(Bac_byte_ALQ)
    Bac_byte_ALQ['Time'] = times    
    Bac_byte_ALQ['Time']=Bac_byte_ALQ["Time"].apply(lambda x : x.strftime("%d %B, %Y, %H:%M"))
    Bac_byte_ALQ=Bac_byte_ALQ.set_index('Time')
    # st.write(Bac_byte_ALQ['Time'])
    options = st.multiselect("Filter by params",list(Bac_byte_ALQ.columns),list(Bac_byte_ALQ.columns))
    st.line_chart(Bac_byte_ALQ[options])

    options = st.multiselect("Select NLQ" ,["NLQ0","NLQ1","NLQ2","NLQ3"])
    if("NLQ0" in options):
        Bac_byte_NLQ0 = pd.DataFrame()
        Bac_byte_NLQ0["totalrecodsadded"] =    NLQ0_totalrecordsadded
        Bac_byte_NLQ0["totalrecordsdropped"] = NLQ0_totalrecordsdropped
        Bac_byte_NLQ0["usedrecordscount"] =    NLQ0_usedrecordscount
        Bac_byte_NLQ0["readindex"] =           NLQ0_readindex
        Bac_byte_NLQ0["currentindex"] =        NLQ0_currentindex
        Bac_byte_NLQ0["freecount"] =           NLQ0_freecount
        Bac_byte_NLQ0["dropiam"] =             NLQ0_dropiam
        Bac_byte_NLQ0["nlqloadpctlimit"] =     NLQ0_nlqloadpctlimit
        Bac_byte_NLQ0['Time'] = times    
        Bac_byte_NLQ0['Time']=Bac_byte_NLQ0["Time"].apply(lambda x : x.strftime("%d %B, %Y, %H:%M"))
        Bac_byte_NLQ0=Bac_byte_NLQ0.set_index('Time')
        st.line_chart(Bac_byte_NLQ0)
        # st.dataframe(Bac_byte_NLQ0)
    if("NLQ1" in options):
        Bac_byte_NLQ1 = pd.DataFrame()
        Bac_byte_NLQ1["totalrecodsadded"] =    NLQ1_totalrecordsadded
        Bac_byte_NLQ1["totalrecordsdropped"] = NLQ1_totalrecordsdropped
        Bac_byte_NLQ1["usedrecordscount"] =    NLQ1_usedrecordscount
        Bac_byte_NLQ1["readindex"] =           NLQ1_readindex
        Bac_byte_NLQ1["currentindex"] =        NLQ1_currentindex
        Bac_byte_NLQ1["freecount"] =           NLQ1_freecount
        Bac_byte_NLQ1["dropiam"] =             NLQ1_dropiam
        Bac_byte_NLQ1["nlqloadpctlimit"] =     NLQ1_nlqloadpctlimit
        Bac_byte_NLQ1['Time'] = times    
        Bac_byte_NLQ1['Time']=Bac_byte_NLQ1["Time"].apply(lambda x : x.strftime("%d %B, %Y, %H:%M"))
        Bac_byte_NLQ1=Bac_byte_NLQ1.set_index('Time')
        st.line_chart(Bac_byte_NLQ1)
        # st.dataframe(Bac_byte_NLQ1)
    if("NLQ2" in options):
        Bac_byte_NLQ2 = pd.DataFrame()
        Bac_byte_NLQ2["totalrecodsadded"] =    NLQ2_totalrecordsadded
        Bac_byte_NLQ2["totalrecordsdropped"] = NLQ2_totalrecordsdropped
        Bac_byte_NLQ2["usedrecordscount"] =    NLQ2_usedrecordscount
        Bac_byte_NLQ2["readindex"] =           NLQ2_readindex
        Bac_byte_NLQ2["currentindex"] =        NLQ2_currentindex
        Bac_byte_NLQ2["freecount"] =           NLQ2_freecount
        Bac_byte_NLQ2["dropiam"] =             NLQ2_dropiam
        Bac_byte_NLQ2["nlqloadpctlimit"] =     NLQ2_nlqloadpctlimit
        Bac_byte_NLQ2['Time'] = times    
        Bac_byte_NLQ2['Time']=Bac_byte_NLQ2["Time"].apply(lambda x : x.strftime("%d %B, %Y, %H:%M"))
        Bac_byte_NLQ2=Bac_byte_NLQ2.set_index('Time')
        st.line_chart(Bac_byte_NLQ2)
        # st.dataframe(Bac_byte_NLQ2)
    if("NLQ3" in options):
        Bac_byte_NLQ3 = pd.DataFrame()
        Bac_byte_NLQ3["totalrecodsadded"] =    NLQ3_totalrecordsadded
        Bac_byte_NLQ3["totalrecordsdropped"] = NLQ3_totalrecordsdropped
        Bac_byte_NLQ3["usedrecordscount"] =    NLQ3_usedrecordscount
        Bac_byte_NLQ3["readindex"] =           NLQ3_readindex
        Bac_byte_NLQ3["currentindex"] =        NLQ3_currentindex
        Bac_byte_NLQ3["freecount"] =           NLQ3_freecount
        Bac_byte_NLQ3["dropiam"] =             NLQ3_dropiam
        Bac_byte_NLQ3["nlqloadpctlimit"] =     NLQ3_nlqloadpctlimit
        Bac_byte_NLQ3['Time'] = times    
        Bac_byte_NLQ3['Time']=Bac_byte_NLQ3["Time"].apply(lambda x : x.strftime("%d %B, %Y, %H:%M"))
        Bac_byte_NLQ3=Bac_byte_NLQ3.set_index('Time')
        st.line_chart(Bac_byte_NLQ3)
        # st.dataframe(Bac_byte_NLQ3)
    
    st.header('BACnet Service Statistics')
    options = st.multiselect("Select params" , ['total time' ,'no of packets' , 'individual packet time' ])
    if('no of packets' in options):
        bacnet_service = pd.DataFrame()
        li = [whois,iam,rpm,rp,rr,almack,getevsum,baddlist,bgetinfo,butctimsync]

        name = ["WHOIS","IAM","RPM" , "RP" , "RR" , "AlmAck"  , "getEvSum" , "BADDLIST" , "BGETINFO" , "BUTCTIMSYNC"]
        bacnet_service["time"] = BACnet_server_time
        for k in range(len(li)):
            lis = li[k]['no_of_packets']
            bacnet_service[name[k]] = lis
        bacnet_service["time"] = bacnet_service['time'].apply(lambda x : x.strftime("%d %B, %Y, %H:%M"))
        bacnet_service = bacnet_service.set_index('time')
        st.write('Total no of packets')
        st.line_chart(bacnet_service)
    if('total time' in options):
        bacnet_service = pd.DataFrame()
        li = [whois,iam,rpm,rp,rr,almack,getevsum,baddlist,bgetinfo,butctimsync]
    
        name = ["WHOIS","IAM","RPM" , "RP" , "RR" , "AlmAck"  , "getEvSum" , "BADDLIST" , "BGETINFO" , "BUTCTIMSYNC"]
        bacnet_service["time"] = BACnet_server_time
        for k in range(len(li)):
            lis = li[k]['total_time']
            bacnet_service[name[k]] = lis
        bacnet_service["time"] = bacnet_service['time'].apply(lambda x : x.strftime("%d %B, %Y, %H:%M"))
        bacnet_service = bacnet_service.set_index('time')
        st.write('total time')
        st.line_chart(bacnet_service)
        

    if('individual packet time' in options):
        bacnet_service = pd.DataFrame()
        st.write('individual packet time')
        li = [whois,iam,rpm,rp,rr,almack,getevsum,baddlist,bgetinfo,butctimsync]
    
        name = ["WHOIS","IAM","RPM" , "RP" , "RR" , "AlmAck"  , "getEvSum" , "BADDLIST" , "BGETINFO" , "BUTCTIMSYNC"]
        bacnet_service["time"] = BACnet_server_time
        for k in range(len(li)):
            lis = li[k]['individual_packet_time']
            bacnet_service[name[k]] = lis
        bacnet_service["time"] = bacnet_service['time'].apply(lambda x : x.strftime("%d %B, %Y, %H:%M"))
        bacnet_service = bacnet_service.set_index('time')
        st.line_chart(bacnet_service)
        