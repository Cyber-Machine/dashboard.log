import datetime
import json

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

#BacNet statistics
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
Ethernet_Statistics = json.dumps(Ethernet_Statistics)

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
BACnet_statistics = json.dumps(BACnet_statistics)

# Converting Device Beginning Now 
Device_Beginning_Now = {}
for i in range(len(Beginning_Now)):
    Device_Beginning_Now[i] = str(Beginning_Now[i])
Device_Beginning_Now = json.dumps(Device_Beginning_Now)

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
BACnet_Services_stats = json.dumps(BACnet_Services_stats)
