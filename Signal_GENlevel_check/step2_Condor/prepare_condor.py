import os

if __name__ == "__main__":
  PWD=os.getcwd()
  fin=open("samples_list", 'r')
  line=fin.readline().strip()
  isam=0
  while line:
    line_temp=line.replace('/','dummy')
    dir_temp='sample_'+str(isam)
    os.mkdir(dir_temp)
    os.chdir(dir_temp)
    os.system(r'cp ../wrapper.sh .')
    os.system(r'sed -i "s/DUMMY/%s/g" wrapper.sh'%(line_temp))
    os.system(r'sed -i "s/dummy/\//g" wrapper.sh')
    os.chdir(PWD)
    isam=isam+1
    line=fin.readline().strip()
