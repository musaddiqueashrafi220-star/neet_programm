import numpy as np 
neet_data=np.genfromtxt(
    "neet_data.csv",
    delimiter=",",
    skip_header=1,
    dtype="str",
    encoding="utf-8"
)
#print(neet_data)
years=neet_data[:,-1].astype(int)
yearcount=[]
c1=0
c2=0
c3=0
c4=0

for i in years:
    if i==2023:
        c1+=1
    elif i==2024:
        c2+=1
    elif i==2025:
        c3+=1
    else:
        c4+=1

yearcount=[c1,c2,c3,c4]
#print(yearcount)

attempt=neet_data[:,3].astype(int)
attempt_count=[]
a1=0
a2=0
a3=0
a4=0

for i in attempt:
    if i==1:
        a1+=1
    elif i==2:
        a2+=1
    elif i==3:
        a3+=1
    else:
        a4+=1

attempt_count=[a1,a2,a3,a4]
print(attempt_count)

state=neet_data[:,5].astype(str)
state_wise=[]
b1=0
b2=0
b3=0
b4=0
b5=0
b6=0

for i in state:
    if i=="Maharashtra":
        b1+=1
    elif i=="Delhi":
        b2+=1
    elif i=="Tamil Nadu":
        b3+=1
    elif i=="Karnataka":
        b4+=1
    elif i=="West Bengal":
        b5+=1
    else:
        b6+=1

state_wise=[b1,b2,b3,b4]
print(state_wise)
