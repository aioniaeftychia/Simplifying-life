def split(string:str,char:str=":",splits:int=1):
    a,b=string.split(char,splits)
    return int(a),int(b)
def time(hour, minute, hadd, madd):
    if (hour+hadd>24):
        hour+=hadd-24
    else: hour+=hadd
    if (minute+madd>60):
        while madd>60:
            if (hour+1>23):
                hour=0
            else: 
                hour+=1
            madd-=60
            
        minute+=madd-60
        if (hour+1>23):
            hour=0
        else: hour+=1
    else: minute+=madd
    hour=str(hour)
    minute=str(minute)
    while (len(hour)<2):
        hour="0"+hour
    while (len(minute)<2):
        minute="0"+minute
    return hour, minute
def difference(tinit, tfinal):
    hour = int(tfinal[0]) - int(tinit[0])
    minute = int(tfinal[1]) - int(tinit[1])
    return hour, minute
def run(runoption):
    global hr,mn
    if runoption==1:
        tadd = input("Enter time progressed as hh:mm")
        while (tadd!="-1"):
            hradd,mnadd=split(tadd)
            hr,mn=time(int(hr),int(mn),hradd,mnadd)
            print(str(hr)+":"+str(mn))
            tadd = input("Enter time progressed as hh:mm")
        print("Terminated")
    if runoption== 2:
        tadd = input("Enter time progressed as mm")
        while (tadd!="-1"):
            mnadd=int(tadd)
            hr,mn=time(int(hr),int(mn),0,mnadd)
            print(str(hr)+":"+str(mn))
            tadd = input("Enter time progressed as mm")
        print("Terminated")
    #if runoption==3: #option three is for subtracting time
    #    tadd = input("Enter time progressed as mm:")
    #    while (tadd!="-1"):
    #        mnadd=int(tadd)
    #        hr,mn=time(int(hr),int(mn),0,mnadd)
    #        print(str(hr)+":"+str(mn))
    #        tadd = input("Enter time progressed as mm:")
    #    print("Terminated")      
    #option four is for adding minutes and giving the hh:mm equivalent  
    if runoption==4: #option to calculate how many given study sessions can fit in a time period
        tinit = split(input("Enter initial time as hh:mm: "))
        tfinal = split(input("Enter final time as hh:mm: "))
        tstudy = int(input("Enter length of one study session as mm: "))
        tbreak = int(input("Enter length of one break as mm: "))
        tdif = difference(tinit, tfinal)
        tdifmin = tdif[0]*60 + tdif[1]
        tsession = (tstudy+tbreak)
        tstudysessions = tdifmin//tsession
        tbreaksessions = tstudysessions
        tleftover = tdifmin-(tsession*tstudysessions)
        if tleftover >= tstudy:
            tstudysessions+=1
            tleftover-=tstudy
        print(str(tstudysessions) + " study sessions and " + str(tbreaksessions) + " break sessions" + "\nTime left over: " + str(tleftover)+" minutes\nTerminated.")
    runoption = int(input("Select running mode(1=hh:mm,2=mm,-1=end):"))
    if runoption!=-1:
        run(runoption)
    else: print("Ended.")
runoption=int(input("Select running mode(1=hh:mm,2=mm):"))
if runoption == -1:
    print("Ended.")
else:
    if runoption!=4:
        hr,mn = split(input("Enter time as hh:mm:"))
    run(runoption)

        
    
    