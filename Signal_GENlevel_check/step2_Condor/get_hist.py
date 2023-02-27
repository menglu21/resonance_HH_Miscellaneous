import ROOT
import numpy as np

import sys

inputFile = sys.argv[1]
#signal=inputFile
#signal='root://xrootd-cms.infn.it//store/mc/RunIISummer20UL17NanoAODv9/NMSSM_XToYHTo2Z2BTo2L2J2B_MX-1000_MY-600_TuneCP5_13TeV-madgraph-pythia8/NANOAODSIM/106X_mc2017_realistic_v9-v1/80000/19EA30A8-544E-B244-B74C-D3C6294D83F4.root'
signal='root://xrootd-cms.infn.it/'+inputFile
filein=ROOT.TFile.Open(signal)
treein=filein.Get('Events')

nTot=treein.GetEntriesFast()

hist_LHE_Y_mass=ROOT.TH1D('Y_mass','Y_mass',10,50,150)
hist_LHE_Y_eta=ROOT.TH1D('Y_eta','Y_eta',20,-5,5)
hist_LHE_Y_phi=ROOT.TH1D('Y_phi','Y_phi',20,-4,4)
hist_LHE_Y_pt=ROOT.TH1D('Y_pt','Y_pt',20,0,1000)
hist_LHE_h_mass=ROOT.TH1D('h_mass','h_mass',10,120,130)
hist_LHE_h_eta=ROOT.TH1D('h_eta','h_eta',20,-5,5)
hist_LHE_h_phi=ROOT.TH1D('h_phi','h_phi',20,-4,4)
hist_LHE_h_pt=ROOT.TH1D('h_pt','h_pt',20,0,1000)

hist_GEN_z1_mass=ROOT.TH1D('z1_mass','z1_mass',30,0,120)
hist_GEN_z1_pt=ROOT.TH1D('z1_pt','z1_pt',20,0,1000)
hist_GEN_z1_eta=ROOT.TH1D('z1_eta','z1_eta',20,-5,5)
hist_GEN_z1_phi=ROOT.TH1D('z1_phi','z1_phi',20,-4,4)
hist_GEN_z2_mass=ROOT.TH1D('z2_mass','z2_mass',30,0,120)
hist_GEN_z2_pt=ROOT.TH1D('z2_pt','z2_pt',20,0,1000)
hist_GEN_z2_eta=ROOT.TH1D('z2_eta','z2_eta',20,-5,5)
hist_GEN_z2_phi=ROOT.TH1D('z2_phi','z2_phi',20,-4,4)
hist_dr_z1z2=ROOT.TH1D('dr_z1z2','dr_z1z2',40,0,4)
hist_dr_b1b2=ROOT.TH1D('dr_b1b2','dr_b1b2',40,0,4)
hist_dr_b1l1=ROOT.TH1D('dr_b1l1','dr_b1l1',40,0,4)
hist_dr_b1l2=ROOT.TH1D('dr_b1l2','dr_b1l2',40,0,4)
hist_dr_b1j1=ROOT.TH1D('dr_b1j1','dr_b1j1',40,0,4)
hist_dr_b1j2=ROOT.TH1D('dr_b1j2','dr_b1j2',40,0,4)
hist_dr_b2l1=ROOT.TH1D('dr_b2l1','dr_b2l1',40,0,4)
hist_dr_b2l2=ROOT.TH1D('dr_b2l2','dr_b2l2',40,0,4)
hist_dr_b2j1=ROOT.TH1D('dr_b2j1','dr_b2j1',40,0,4)
hist_dr_b2j2=ROOT.TH1D('dr_b2j2','dr_b2j2',40,0,4)
hist_dr_l1l2=ROOT.TH1D('dr_l1l2','dr_l1l2',40,0,4)
hist_dr_l1j1=ROOT.TH1D('dr_l1j1','dr_l1j1',40,0,4)
hist_dr_l1j2=ROOT.TH1D('dr_l1j2','dr_l1j2',40,0,4)
hist_dr_l2j1=ROOT.TH1D('dr_l2j1','dr_l2j1',40,0,4)
hist_dr_l2j2=ROOT.TH1D('dr_l2j2','dr_l2j2',40,0,4)
hist_dr_j1j2=ROOT.TH1D('dr_j1j2','dr_j1j2',40,0,4)
hist_l1_pt=ROOT.TH1D('l1_pt','l1_pt',20,0,1000)
hist_l2_pt=ROOT.TH1D('l2_pt','l2_pt',20,0,1000)
hist_b1_pt=ROOT.TH1D('b1_pt','b1_pt',20,0,1000)
hist_b2_pt=ROOT.TH1D('b2_pt','b2_pt',20,0,1000)
hist_j1_pt=ROOT.TH1D('j1_pt','j1_pt',20,0,1000)
hist_j2_pt=ROOT.TH1D('j2_pt','j2_pt',20,0,1000)

z1=ROOT.TLorentzVector()
z2=ROOT.TLorentzVector()
b1=ROOT.TLorentzVector()
b2=ROOT.TLorentzVector()
l1=ROOT.TLorentzVector()
l2=ROOT.TLorentzVector()
j1=ROOT.TLorentzVector()
j2=ROOT.TLorentzVector()

for ieve in range(0,nTot):

  if ieve%1000==0:print('Processing event ', ieve)
  if ieve>10000:break
  treein.GetEntry(ieve)

  temp_gen=np.array(list(range(0,treein.nGenPart,1)))

  # obtain array id for Y
  temp_y1=np.array(treein.GenPart_pdgId)-35
  temp_y2=np.nonzero(temp_y1)[0]
  index_y=list(set(temp_gen)-set(temp_y2))

  # obtain array id for Higgs bosons
  temp_h1=np.array(treein.GenPart_pdgId)-25
  temp_h2=np.nonzero(temp_h1)[0]
  index_h=list(set(temp_gen)-set(temp_h2))
  # obtain array id for decay products for h
  temp_h_decay1=np.array(treein.GenPart_genPartIdxMother)-index_h[0]
  temp_h_decay2=np.nonzero(temp_h_decay1)[0]
  index_h_decay=list(set(temp_gen)-set(temp_h_decay2))
  b1.SetPtEtaPhiM(treein.GenPart_pt[index_h_decay[0]],treein.GenPart_eta[index_h_decay[0]],treein.GenPart_phi[index_h_decay[0]],treein.GenPart_mass[index_h_decay[0]])
  b2.SetPtEtaPhiM(treein.GenPart_pt[index_h_decay[1]],treein.GenPart_eta[index_h_decay[1]],treein.GenPart_phi[index_h_decay[1]],treein.GenPart_mass[index_h_decay[1]])

  # obtain array id for two Z bosons
  temp_z1=np.array(treein.GenPart_pdgId)-23
  temp_z2=np.nonzero(temp_z1)[0]
  index=list(set(temp_gen)-set(temp_z2))

  # obtain array id for decay products for z1/z2
  temp_z1_decay1=np.array(treein.GenPart_genPartIdxMother)-index[0]
  temp_z1_decay2=np.nonzero(temp_z1_decay1)[0]
  index_z1_decay=list(set(temp_gen)-set(temp_z1_decay2))
  temp_z2_decay1=np.array(treein.GenPart_genPartIdxMother)-index[1]
  temp_z2_decay2=np.nonzero(temp_z2_decay1)[0]
  index_z2_decay=list(set(temp_gen)-set(temp_z2_decay2))
  if abs(treein.GenPart_pdgId[index_z1_decay[0]])<10:
    l1.SetPtEtaPhiM(treein.GenPart_pt[index_z2_decay[0]],treein.GenPart_eta[index_z2_decay[0]],treein.GenPart_phi[index_z2_decay[0]],treein.GenPart_mass[index_z2_decay[0]])
    l2.SetPtEtaPhiM(treein.GenPart_pt[index_z2_decay[1]],treein.GenPart_eta[index_z2_decay[1]],treein.GenPart_phi[index_z2_decay[1]],treein.GenPart_mass[index_z2_decay[1]])
    j1.SetPtEtaPhiM(treein.GenPart_pt[index_z1_decay[0]],treein.GenPart_eta[index_z1_decay[0]],treein.GenPart_phi[index_z1_decay[0]],treein.GenPart_mass[index_z1_decay[0]])
    j2.SetPtEtaPhiM(treein.GenPart_pt[index_z1_decay[1]],treein.GenPart_eta[index_z1_decay[1]],treein.GenPart_phi[index_z1_decay[1]],treein.GenPart_mass[index_z1_decay[1]])
  else:
    j1.SetPtEtaPhiM(treein.GenPart_pt[index_z2_decay[0]],treein.GenPart_eta[index_z2_decay[0]],treein.GenPart_phi[index_z2_decay[0]],treein.GenPart_mass[index_z2_decay[0]])
    j2.SetPtEtaPhiM(treein.GenPart_pt[index_z2_decay[1]],treein.GenPart_eta[index_z2_decay[1]],treein.GenPart_phi[index_z2_decay[1]],treein.GenPart_mass[index_z2_decay[1]])
    l1.SetPtEtaPhiM(treein.GenPart_pt[index_z1_decay[0]],treein.GenPart_eta[index_z1_decay[0]],treein.GenPart_phi[index_z1_decay[0]],treein.GenPart_mass[index_z1_decay[0]])
    l2.SetPtEtaPhiM(treein.GenPart_pt[index_z1_decay[1]],treein.GenPart_eta[index_z1_decay[1]],treein.GenPart_phi[index_z1_decay[1]],treein.GenPart_mass[index_z1_decay[1]])

  hist_LHE_Y_mass.Fill(treein.GenPart_mass[index_y[0]])
  hist_LHE_Y_pt.Fill(treein.GenPart_pt[index_y[0]])
  hist_LHE_Y_eta.Fill(treein.GenPart_eta[index_y[0]])
  hist_LHE_Y_phi.Fill(treein.GenPart_phi[index_y[0]])
  hist_LHE_h_mass.Fill(treein.GenPart_mass[index_h[0]])
  hist_LHE_h_pt.Fill(treein.GenPart_pt[index_h[0]])
  hist_LHE_h_eta.Fill(treein.GenPart_eta[index_h[0]])
  hist_LHE_h_phi.Fill(treein.GenPart_phi[index_h[0]])

  if treein.GenPart_mass[index[0]]>treein.GenPart_mass[index[1]]:
    z1.SetPtEtaPhiM(treein.GenPart_pt[index[0]],treein.GenPart_eta[index[0]],treein.GenPart_phi[index[0]],treein.GenPart_mass[index[0]])
    z2.SetPtEtaPhiM(treein.GenPart_pt[index[1]],treein.GenPart_eta[index[1]],treein.GenPart_phi[index[1]],treein.GenPart_mass[index[1]])
    hist_GEN_z1_mass.Fill(treein.GenPart_mass[index[0]])
    hist_GEN_z1_pt.Fill(treein.GenPart_pt[index[0]])
    hist_GEN_z1_eta.Fill(treein.GenPart_eta[index[0]])
    hist_GEN_z1_phi.Fill(treein.GenPart_phi[index[0]])
    hist_GEN_z2_mass.Fill(treein.GenPart_mass[index[1]])
    hist_GEN_z2_pt.Fill(treein.GenPart_pt[index[1]])
    hist_GEN_z2_eta.Fill(treein.GenPart_eta[index[1]])
    hist_GEN_z2_phi.Fill(treein.GenPart_phi[index[1]])
    hist_dr_z1z2.Fill(z1.DeltaR(z2))
  else:
    z2.SetPtEtaPhiM(treein.GenPart_pt[index[0]],treein.GenPart_eta[index[0]],treein.GenPart_phi[index[0]],treein.GenPart_mass[index[0]])
    z1.SetPtEtaPhiM(treein.GenPart_pt[index[1]],treein.GenPart_eta[index[1]],treein.GenPart_phi[index[1]],treein.GenPart_mass[index[1]])
    hist_GEN_z1_mass.Fill(treein.GenPart_mass[index[1]])
    hist_GEN_z1_pt.Fill(treein.GenPart_pt[index[1]])
    hist_GEN_z1_eta.Fill(treein.GenPart_eta[index[1]])
    hist_GEN_z1_phi.Fill(treein.GenPart_phi[index[1]])
    hist_GEN_z2_mass.Fill(treein.GenPart_mass[index[0]])
    hist_GEN_z2_pt.Fill(treein.GenPart_pt[index[0]])
    hist_GEN_z2_eta.Fill(treein.GenPart_eta[index[0]])
    hist_GEN_z2_phi.Fill(treein.GenPart_phi[index[0]])
    hist_dr_z1z2.Fill(z1.DeltaR(z2))
  
  hist_dr_b1b2.Fill(b1.DeltaR(b2))
  hist_dr_b1l1.Fill(b1.DeltaR(l1))
  hist_dr_b1l2.Fill(b1.DeltaR(l2))
  hist_dr_b1j1.Fill(b1.DeltaR(j1))
  hist_dr_b1j2.Fill(b1.DeltaR(j2))
  hist_dr_b2l1.Fill(b2.DeltaR(l1))
  hist_dr_b2l2.Fill(b2.DeltaR(l2))
  hist_dr_b2j1.Fill(b2.DeltaR(j1))
  hist_dr_b2j2.Fill(b2.DeltaR(j2))
  hist_dr_l1l2.Fill(l1.DeltaR(l2))
  hist_dr_l1j1.Fill(l1.DeltaR(j1))
  hist_dr_l1j2.Fill(l1.DeltaR(j2))
  hist_dr_l2j1.Fill(l2.DeltaR(j1))
  hist_dr_l2j2.Fill(l2.DeltaR(j2))
  hist_dr_j1j2.Fill(j1.DeltaR(j2))
  hist_l1_pt.Fill(l1.Pt())
  hist_l2_pt.Fill(l2.Pt())
  hist_b1_pt.Fill(b1.Pt())
  hist_b2_pt.Fill(b2.Pt())
  hist_j1_pt.Fill(j1.Pt())
  hist_j2_pt.Fill(j2.Pt())
#  print 'b1:',b1.Pt(),b1.Eta(),b1.Phi(),b1.M()
#  print 'b2:',b2.Pt(),b2.Eta(),b2.Phi(),b2.M()
#  print 'l1:',l1.Pt(),l1.Eta(),l1.Phi(),l1.M()
#  print 'l2:',l2.Pt(),l2.Eta(),l2.Phi(),l2.M()
#  print 'j1:',j1.Pt(),j1.Eta(),j1.Phi(),j1.M()
#  print 'j2:',j2.Pt(),j2.Eta(),j2.Phi(),j2.M()
output_name=inputFile.split('/')[4].split('_')[2]+'_'+inputFile.split('/')[4].split('_')[3]+'_check.root'
fileout=ROOT.TFile.Open(output_name,'recreate')
fileout.cd()

hist_LHE_h_mass.Write()
hist_LHE_h_pt.Write()
hist_LHE_h_eta.Write()
hist_LHE_h_phi.Write()
hist_LHE_Y_mass.Write()
hist_LHE_Y_pt.Write()
hist_LHE_Y_eta.Write()
hist_LHE_Y_phi.Write()

hist_GEN_z1_mass.Write()
hist_GEN_z1_pt.Write()
hist_GEN_z1_eta.Write()
hist_GEN_z1_phi.Write()
hist_GEN_z2_mass.Write()
hist_GEN_z2_pt.Write()
hist_GEN_z2_eta.Write()
hist_GEN_z2_phi.Write()
hist_dr_z1z2.Write()
hist_dr_b1b2.Write()
hist_dr_b1l1.Write()
hist_dr_b1l2.Write()
hist_dr_b1j1.Write()
hist_dr_b1j2.Write()
hist_dr_b2l1.Write()
hist_dr_b2l2.Write()
hist_dr_b2j1.Write()
hist_dr_b2j2.Write()
hist_dr_l1l2.Write()
hist_dr_l1j1.Write()
hist_dr_l1j2.Write()
hist_dr_l2j1.Write()
hist_dr_l2j2.Write()
hist_dr_j1j2.Write()
hist_l1_pt.Write()
hist_l2_pt.Write()
hist_b1_pt.Write()
hist_b2_pt.Write()
hist_j1_pt.Write()
hist_j2_pt.Write()

fileout.Close()
