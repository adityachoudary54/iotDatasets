import os
def rename():  
    i=1
    for count, filename in enumerate(os.listdir()): 
        src = filename 
        if '.txt' in src:
            dst = filename[:-4] + ".csv"
            # print(dst)
            i+=1 
            os.rename(src, dst) 

rename()