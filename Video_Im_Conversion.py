import os
from scipy import *
from numpy import *
import re
import Image
import matplotlib.pyplot as plt
#import subprocess

dirc='/Videos/'
# Directory to read vidoes

save_dirc='/Converted/';
# Directory to save the converted images

# Specific videos for conversion
file_prefix='P_NEESmacroroughness2.E_Scenario1_Run3.T_Trial';
prefix='S1R3T'
#trial=[11,12,13,14,16,17,18,20,21,24,27,28,38,39,40,41,46,47,49,50,52,53,55] #CBR1
#trial=[2,3,4,5,6,9,11,14,15,17,19,20,22,26,31,33,38,39,40,42,45,48,51,53,61] #CBR3
#trial=[8,9,10,14,17,18,19,22,29,31,32,33,43,44,45,47,48,51,52,55] #S7R1
#trial=[3,4,6,8,9,15,16,17,18,24,25,26,27,28,33,38,40,42,43,47,48,51,52,54,57] #S7R2
#trial=[2,3,5,6,9,11,12,18,19,20,33,36,37,39,40,41,43,45,46,49,52,53,54] #S7R3
#trial=[5,6,8,9,15,17,20,21,22,24,26,27,28,34,35,36,37,38,40,43,44,45,46,47,49,50,52,53,54,55,56] #S8R3
#trial=[2,22,23,24,33,34,35,41,43,44,46,49,52,54,55] #S8R1
#trial=[7,8,18,23,30,35,36,38,39,42,45,48,52,54,56] #S8R2
#trial=[3,4,8,11,12,15,17,20,21,23,24,27,28,33,35,37,38,39,40,41,42,44,47,48,50,51,54] #S6R2
#trial=[3,5,9,11,18,19,20,30,31,48,51,53,21,24,26,28] #S6R1 randomly pick[21,24,26,28];
#trial=[3,4,10,11,25,27,34,36,42,43,47,54,32,45,51,52,53,55] #S6R3 randomly pick[32,45,51,52,53,55]
trial=[24]#12,15,16,21,23,26,30,31,34,38,40,49]; #S1R3 (randomly pick [12,15,16,21,23,26,29,30,31,34,38,40,49])

rate = 59.94

for i in range(size(trial)):
    run_num = '00' + str(trial[i])

    os.chdir(dirc+file_prefix + str(run_num[len(run_num)-2:]) + '/derived_data')
    if not os.path.exists(prefix + str(trial[i])) or \
    len(os.listdir(prefix+str(trial[i])))<360: 
        os.system('mkdir ' + prefix+str(trial[i]))
    #os.mkdir gets error and stops when file exists
    os.system('cp *.txt '+prefix+str(trial[i])+'.txt')
    
    os.system('cp ' + prefix+str(trial[i])+'.txt ' + './' + prefix + \
    str(trial[i]) + '/' + prefix + str(trial[i]) + '.txt')
        
    myfile = open(prefix + str(trial[i]) + '.txt', 'r')
    
    for s in myfile.readlines():
        li = re.findall('start_time_from_wmstart=', s)         
        if len(li) > 0:
            print s[s.index('=')+1:]
            sync_time = float(s[s.index('=')+1:])
            break
            
    start_time = int( floor( 30 - (sync_time - 0.5) ) )
    
    if len(os.listdir(prefix+str(trial[i])))<360:
        start_t='0'+str(start_time)
        os.popen('/opt/local/bin/ffmpeg -i *.mp4 -ss 00:00:' + start_t[len(start_t)-2:] + ' -t 00:00:06 ./'
        + prefix + str(trial[i]) + '/'+prefix + str(trial[i]) + '_%5d.png')
        
    start_frame=int( rate * ( 1 - ( (sync_time - 0.5) - floor(sync_time-0.5) ) ) )
    
    print start_frame
    
    plt.figure()
    fig_num='000000'+str(start_frame)
    pic =plt.imread(prefix+str(trial[i])+'/'+prefix+str(trial[i])+'_'+fig_num[len(fig_num)-5:]+'.png')    
    plt.imshow(pic)
    plt.show()    
    os.system('cp -rf '+ prefix+str(trial[i]) + ' ' + save_dirc +'/')
    myfile.close()

#ffmpeg_command = "/opt/local/bin/ffmpeg -i AB_058_060.composite.mp4 -ss 00:00:00 -t 00:00:01 test_%5d.png" 
#f_ffmpeg=os.popen(ffmpeg_command);
#os.system() will work as well
