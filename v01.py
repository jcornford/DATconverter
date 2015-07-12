import struct as st
#2015_01_14_s2c1_i75.DAT
#'/2015_01_14_isteps.DAT'
bytes = []
data = []
first = True

byte_indexes = [611, 320640,640669, 960698 ]
sweep_number = 4
for sweep_index in range(sweep_number):
    print sweep_index, 'sweep_index'
    with open(fpath+'/2015_01_14_isteps.DAT', "rb") as f:
        wastebyte = f.read(byte_indexes[sweep_index])
        data = []

        for i in range(80000): # channel*sampling
            byte = f.read(4)
            bytes.append(byte)
            try:
                x = st.unpack('>f',byte)
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
print dArray.shape


plt.figure(figsize = (12,6))
plt.subplot(1,2,1)
plt.plot(dArray[0::4,:])
plt.axis('off')
plt.subplot(1,2,2)
plt.plot(dArray[2::4], 'k')
plt.axis('off')
