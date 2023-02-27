import os

os.system(r'dasgoclient --query="files dataset=/NMSSM_XToYHTo2Z2BTo2L2J2B_MX-*_MY-*_TuneCP5_13TeV-madgraph-pythia8/*20UL17*/NANOAODSIM" > process_list')

pros_name=[]
fin=open("process_list", 'r')
line=fin.readline().strip()
while line:
  pros_name.append(line)
  line=fin.readline().strip()

for ipro in range(0,len(pros_name)):
  os.system(r'dasgoclient --query="file dataset=%s" >> samples_list'%(pros_name[ipro]))
