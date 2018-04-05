
# coding: utf-8

# In[27]:

# scp data between remote and local

import os
import shutil
import subprocess


# In[28]:

from subprocess import Popen, PIPE

def listdir_shell(remoteHost, rootFolder):
    p = Popen(['ssh', '-p', '8', '%s' %remoteHost, 'ls', '%s' %rootFolder], shell=False, stdout=PIPE, close_fds=True)
    return [path.rstrip('\n') for path in p.stdout.readlines()]


# In[29]:

def run():
        remoteHost = "yaocai@ohio"
        
        rootFolder = "/home/yaocai/Ab/CsPbI3/slab"
        rootFolderLocal = "/Users/yao/Google Drive/data/CsPbI3/slab"
        
        targetFolder = ["wfn","wfn_idipol","wfn_ldipol"]
        targetFile = "LOCPOT"
        
        for currentFolder in listdir_shell(remoteHost, rootFolder):
                if "slab1" in currentFolder:
                    os.mkdir(os.path.join(rootFolderLocal, currentFolder))
                    for subFolder in targetFolder:
                        remotePath = os.path.join(rootFolder, currentFolder, subFolder)
                        remoteFile = os.path.join(remotePath, targetFile)
                        localPath = os.path.join(rootFolderLocal, currentFolder, subFolder)
                        localFile = os.path.join(localPath, targetFile)
                        os.mkdir(localPath)
                        os.system('scp -P 8 "%s:%s" "%s"' % (remoteHost, remoteFile, localPath))

if __name__ == "__main__":
        run()


# In[21]:




# In[26]:




# In[ ]:



