import numpy as np
import struct

path = '/Users/Jonathan/Documents/PhD /Data/2015'
foldername = '/2015_01/'
folderpath = path+foldername
filename = '2015_01_14_isteps.DAT'
filepath = fpath+'/2015_01_14_isteps.DAT'
#savepath = folderpath+'converted/'+filename[:-4]
savepath = folderpath+filename[:-4]

bytes = []
data = []

first = True
channel_number = 4
fs = 20000
acq_len = 1 # in seconds 
sweep_number = 30

bytes_per_sweep = fs*4*channel_number

byte_indexes = [(bytes_per_sweep*i) +611+(29*i) for i in range(sweep_number)]
for sweep_index in range(sweep_number):
    with open(filepath, "rb") as f:
        wastebyte = f.read(byte_indexes[sweep_index])
        data = []
        for i in range(80000): # channel*sampling
            byte = f.read(4)
            bytes.append(byte)
            try:
                x = struct.unpack('>f',byte)
                data.append(x)
            except:
                print 'Error', Exception
        if first:
            dArray = np.ravel(np.array([data]))
            first = False
        else:
            vals = np.ravel(np.array([data]))
            dArray = np.vstack([dArray,vals])

dArray = dArray.transpose()
# rows are time, columns sweeps, depth is channels
if channel_number == 4:
    temp0 = dArray[0::4]
    temp1 = dArray[1::4]
    temp2 = dArray[2::4]
    temp3 = dArray[3::4]
    dArray = np.dstack([temp0,temp1,temp2,temp3])

if channel_number ==2:
    temp0 = dArray[0::2]
    temp1 = dArray[1::2]
    dArray = np.dstack([temp0,temp1])

np.save(savepath,dArray)
