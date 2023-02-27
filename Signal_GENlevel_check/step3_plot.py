import ROOT
from ROOT import gROOT
import sys 
import os
from os import walk
gROOT.ProcessLine( "gErrorIgnoreLevel = 1001;")
ROOT.TH2.AddDirectory(False)

mass={
'240': [60,70,80,90,100],
'280': [60,70,80,90,100,125,150],
'300': [60,70,80,90,100,125,150],
'320': [60,70,80,90,100,125,150],
'360': [60,70,80,90,100,125,150],
'400': [60,70,80,90,100,125,150,250],
'450': [60,70,80,90,100,125,150,250,300],
'500': [60,70,80,90,100,125,150,250,300],
'550': [60,70,80,90,100,125,150,250,300,400],
'600': [60,70,80,90,100,125,150,250,300,400],
'650': [60,70,80,90,100,125,150,250,300,400,500],
'700': [60,70,80,90,100,125,150,250,300,400,500],
'750': [60,70,80,90,100,125,150,250,300,400,500,600],
'800': [60,70,80,90,100,125,150,250,300,400,500,600],
'850': [60,70,80,90,100,125,150,250,300,400,500,600,700],
'900': [60,70,80,90,100,125,150,250,300,400,500,600,700],
'950': [60,70,80,90,100,125,150,250,300,400,500,600,700,800],
'1000': [60,70,80,90,100,125,150,250,300,400,500,600,700,800],
'1100': [60,70,80,90,100,125,150,250,300,400,500,600,700,800,900],
'1200': [60,70,80,90,100,125,150,250,300,400,500,600,700,800,900,1000],
'1300': [60,70,80,90,100,125,150,250,300,400,500,600,700,800,900,1000,1100],
'1400': [60,70,80,90,100,125,150,250,300,400,500,600,700,800,900,1000,1100,1200],
'1500': [60,70,80,90,100,125,150,250,300,400,500,600,700,800,900,1000,1100,1200,1300],
'1600': [60,70,80,90,100,125,150,250,300,400,500,600,700,800,900,1000,1100,1200,1300,1400],
'1700': [60,70,80,90,100,125,150,250,300,400,500,600,700,800,900,1000,1100,1200,1300,1400],
'1800': [60,70,80,90,100,125,150,250,300,400,500,600,700,800,900,1000,1100,1200,1300,1400,1600],
'1900': [60,70,80,90,100,125,150,250,300,400,500,600,700,800,900,1000,1100,1200,1300,1400,1600],
'2000': [60,70,80,90,100,125,150,250,300,400,500,600,700,800,900,1000,1100,1200,1300,1400,1600,1800],
'2500': [60,70,80,90,100,125,150,250,300,400,500,600,700,800,900,1000,1100,1200,1300,1400,1600,1800,2000,2200],
'3000': [60,70,80,90,100,125,150,250,300,400,500,600,700,800,900,1000,1100,1200,1300,1400,1600,1800,2000,2200,2400,2500,2600,2800],
'3500': [60,70,80,90,100,125,150,250,300,400,500,600,700,800,900,1000,1100,1200,1300,1400,1600,1800,2000,2200,2400,2500,2600,2800],
'4000': [60,70,80,90,100,125,150,250,300,400,500,600,700,800,900,1000,1100,1200,1300,1400,1600,1800,2000,2200,2400,2500,2600,2800]
}

color=[2,3,4,6,7,8,9,12,28,30,28,41,42,46]

def plot(value_name):
  for key in mass:
    c1=ROOT.TCanvas() 
    hist_array=[]
    hist_name=[]
    max_temp=[]
  
    for idir in range(0,len(mass[key])):
    
      inputFile='Input_root/'+'MX-'+str(key)+'_'+'MY-'+str(mass[key][idir])+'_check.root'
      if not os.path.exists(inputFile):continue
      f1=ROOT.TFile.Open(inputFile)
      which_name='dr_'+value_name
      h1=f1.Get(which_name)
      h1.SetStats(0)
      max_temp.append(h1.GetMaximum())
      hist_array.append(h1.Clone())
      hist_name.append('MY-'+str(mass[key][idir]))
      f1.Close()
  
    max_final=max(max_temp)
    for ia in range(0,len(hist_array)):
      c1.cd()
      if len(hist_array)<10:
        hist_array[ia].SetLineColor(color[ia])
        hist_array[ia].SetLineWidth(2)
        hist_array[ia].SetLineStyle(1)
        if ia==0:
          hist_array[ia].SetMaximum(1.3*max_final)
          title_temp='#DeltaR_{'+value_name+'} of MX '+key+' GeV'
          hist_array[ia].SetTitle(title_temp)
          hist_array[ia].GetXaxis().SetTitle('#DeltaR')
          hist_array[ia].GetYaxis().SetTitle('A.U.')
          hist_array[ia].Draw('h')
        else:hist_array[ia].Draw('h same')
      elif len(hist_array)<20:
        count_temp=int(round(0.5*len(hist_array)))
        for ia in range(0,count_temp):
          hist_array[ia].SetLineColor(color[ia])
          hist_array[ia].SetLineWidth(2)
          hist_array[ia].SetLineStyle(1)
          if ia==0:
            hist_array[ia].SetMaximum(1.3*max_final)
            title_temp='#DeltaR_{'+value_name+'} of MX '+key+' GeV'
            hist_array[ia].SetTitle(title_temp)
            hist_array[ia].GetXaxis().SetTitle('#DeltaR')
            hist_array[ia].GetYaxis().SetTitle('A.U.')
            hist_array[ia].Draw('h')
          else:hist_array[ia].Draw('h same')
        for ia in range(count_temp,len(hist_array)):
          hist_array[ia].SetLineColor(color[ia-count_temp])
          hist_array[ia].SetLineWidth(2)
          hist_array[ia].SetLineStyle(2)
          hist_array[ia].Draw('h same')
      else:
        count_temp=int(round(0.5*len(hist_array)))
        for ia in range(0,count_temp):
          hist_array[ia].SetLineColor(color[ia])
          hist_array[ia].SetLineWidth(2)
          hist_array[ia].SetLineStyle(1)
          if ia==0:
            hist_array[ia].SetMaximum(1.3*max_final)
            title_temp='#DeltaR_{'+value_name+'} of MX '+key+' GeV'
            hist_array[ia].SetTitle(title_temp)
            hist_array[ia].GetXaxis().SetTitle('#DeltaR')
            hist_array[ia].GetYaxis().SetTitle('A.U.')
            hist_array[ia].Draw('h')
          else:hist_array[ia].Draw('h same')
        for ia in range(count_temp,len(hist_array)):
          hist_array[ia].SetLineColor(color[ia-count_temp])
          hist_array[ia].SetLineWidth(2)
          hist_array[ia].SetLineStyle(2)
          hist_array[ia].Draw('h same')
          
    t1=ROOT.TLegend(0.75,0.3,0.9,0.89)
    t1.SetBorderSize(0)
    t1.SetFillStyle(0)
    t2=ROOT.TLegend(0.6,0.3,0.75,0.89)
    t2.SetBorderSize(0)
    t2.SetFillStyle(0)
    t3=ROOT.TLegend(0.45,0.3,0.6,0.89)
    t3.SetBorderSize(0)
    t3.SetFillStyle(0)
    if len(hist_array)<10:
      for ia in range(0,len(hist_array)):
        t1.AddEntry(hist_array[ia],hist_name[ia])
      t1.Draw()
    elif len(hist_array)<20:
      count_temp=int(round(0.5*len(hist_array)))
      for ia in range(0,count_temp):
        t1.AddEntry(hist_array[ia],hist_name[ia])
      for ia in range(count_temp,len(hist_array)):
        t2.AddEntry(hist_array[ia],hist_name[ia])
      t1.Draw()
      t2.Draw('same')
    else:
      count_temp=int(round(0.333*len(hist_array)))
      for ia in range(0,count_temp):
        t1.AddEntry(hist_array[ia],hist_name[ia])
      for ia in range(count_temp,2*count_temp):
        t2.AddEntry(hist_array[ia],hist_name[ia])
      for ia in range(2*count_temp,len(hist_array)):
        t3.AddEntry(hist_array[ia],hist_name[ia])
      t1.Draw()
      t2.Draw('same')
      t3.Draw('same')
    c1.Update()
    c1_name='MX-'+key+'_dR'+value_name+'.png'
    c1_namepdf='MX-'+key+'_dR'+value_name+'.pdf'
    c1.SaveAs(c1_name)
    c1.SaveAs(c1_namepdf)

value_list=['b1b2','b1l1','b1l2','b1j1','b1j2','b2l1','b2l2','b2j1','b2j2','l1l2','l1j1','l1j2','l2j1','l2j2','j1j2']
for ii in value_list:
  os.mkdir(ii)
  plot(ii)
  os.system(r'mv *.png *.pdf %s'%(ii))
  
