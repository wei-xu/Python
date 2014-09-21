#!C:\\python27
#Filename: getSSRAM.py

N=128
f=file('SSRAM_in.txt','w')
f.write('[SSRAM in]\n')
dataNumber='Data Cnt=%d'%N
print dataNumber
f.write(dataNumber+'\n')
f.close()
print 'done'
nf=file('SSRAM_in.txt','a')
for i in range(0,N):
    dataline='Data[%d]=[0x%04x]0x01 0x03 0x03 0x02 0x02 0x03 0x03 0x02\n'%(i,8*i+2*16*16)
    nf.write(dataline)
    print dataline
nf.close()
