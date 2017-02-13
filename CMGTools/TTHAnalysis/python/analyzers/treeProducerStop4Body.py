from CMGTools.TTHAnalysis.analyzers.treeProducerSusyCore import *
from CMGTools.TTHAnalysis.analyzers.ntupleTypes import *

susyStop4Body_globalVariables = susyCore_globalVariables + [
            ## ------- HT from LHE event, needed for merging HT binned samples (requires LHE analyzer to have run)  ---------------------------------- #
            NTupleVariable("lheHT", lambda ev : getattr(ev,"lheHT",-999), mcOnly=True, help="H_{T} computed from quarks and gluons in Heppy LHEAnalyzer"),
            NTupleVariable("lheHTIncoming", lambda ev : getattr(ev,"lheHTIncoming",-999), mcOnly=True, help="H_{T} computed from quarks and gluons in Heppy LHEAnalyzer (only LHE status<0 as mothers)"),
            NTupleVariable("LHEweight_original", lambda ev: getattr(ev, "LHE_originalWeight", 0), mcOnly=True, help="original LHE weight"),
            # ---------------------------------------------------------------------------------------------------------------------------------------- #
            #ISR jet counting for SUSY reweighting
            NTupleVariable("nIsr", lambda ev : getattr(ev,"nIsr",-999) , help="Number of ISR jets not matched to gen particles"),
            # ---------------------------------------------------------------------------------------------------------------------------------------- #
            NTupleVariable("nJet20", lambda ev: sum([j.pt() > 20 for j in ev.cleanJets]), int, help="Number of jets with pt > 20, |eta|<2.4"),
            NTupleVariable("nJet20a", lambda ev: sum([j.pt() > 20 for j in ev.cleanJetsAll]), int, help="Number of jets with pt > 20, |eta|<4.7"),
            NTupleVariable("nBJetLoose20", lambda ev: sum([j.btagWP("CSVv2IVFL") for j in ev.cleanJets if j.pt() > 20]), int, help="Number of jets with pt > 20 passing CSV loose"),
            NTupleVariable("nBJetMedium20", lambda ev: sum([j.btagWP("CSVv2IVFM") for j in ev.bjetsMedium if j.pt() > 20]), int, help="Number of jets with pt > 20 passing CSV medium"),
            NTupleVariable("nBJetTight20", lambda ev: sum([j.btagWP("CSVv2IVFT") for j in ev.bjetsMedium if j.pt() > 20]), int, help="Number of jets with pt > 20 passing CSV tight"),

            ##-------- custom jets ------------------------------------------
            NTupleVariable("htJet25", lambda ev : ev.htJet25, help="H_{T} computed from leptons and jets (with |eta|<2.4, pt > 25 GeV)"),
            NTupleVariable("mhtJet25", lambda ev : ev.mhtJet25, help="H_{T}^{miss} computed from leptons and jets (with |eta|<2.4, pt > 25 GeV)"),
            NTupleVariable("htJet40j", lambda ev : ev.htJet40j, help="H_{T} computed from only jets (with |eta|<2.4, pt > 40 GeV)"),
            NTupleVariable("htJet40ja", lambda ev : ev.htJet40ja, help="H_{T} computed from only jets (with |eta|<4.7, pt > 40 GeV)"),
            NTupleVariable("htJet40", lambda ev : ev.htJet40, help="H_{T} computed from leptons and jets (with |eta|<2.4, pt > 40 GeV)"),
            NTupleVariable("htJet40a", lambda ev : ev.htJet40a, help="H_{T} computed from leptons and jets (with |eta|<4.7, pt > 40 GeV)"),
            NTupleVariable("mhtJet40", lambda ev : ev.mhtJet40, help="H_{T}^{miss} computed from leptons and jets (with |eta|<2.4, pt > 40 GeV)"),
            NTupleVariable("mhtJet40a", lambda ev : ev.mhtJet40a, help="H_{T}^{miss} computed from leptons and jets (with |eta|<4.7, pt > 40 GeV)"),

            NTupleVariable("htJet20", lambda ev : ev.htJet20, help="H_{T} computed from leptons and jets (with |eta|<2.4, pt > 20 GeV)"),
            NTupleVariable("htJet20j", lambda ev : ev.htJet20j, help="H_{T} computed from only jets (with |eta|<2.4, pt > 20 GeV)"),
            NTupleVariable("mhtJet20", lambda ev : ev.mhtJet20, help="H_{T}^{miss} computed from leptons and jets (with |eta|<2.4, pt > 20 GeV)"),

            NTupleVariable("htJet30j", lambda ev : ev.htJet30j, help="H_{T} computed from only jets (with |eta|<2.4, pt > 30 GeV)"),
            NTupleVariable("htJet30", lambda ev : ev.htJet30, help="H_{T} computed from leptons and jets (with |eta|<2.4, pt > 30 GeV)"),
            NTupleVariable("mhtJet30", lambda ev : ev.mhtJet30, help="H_{T}^{miss} computed from leptons and jets (with |eta|<2.4, pt > 30 GeV)"),

            ##
            NTupleVariable("nSoftBJetLoose20",  lambda ev: sum([(sv.mva>0.3 and (sv.jet == None or sv.jet.pt() < 20)) for sv in ev.ivf]) + len(ev.bjetsMedium), int, help="Exclusive sum of jets with pt > 20 passing CSV medium and SV from ivf with loose sv mva"),
            NTupleVariable("nSoftBJetMedium20", lambda ev: sum([(sv.mva>0.7 and (sv.jet == None or sv.jet.pt() < 20)) for sv in ev.ivf]) + len(ev.bjetsMedium), int, help="Exclusive sum of jets with pt > 20 passing CSV medium and SV from ivf with medium sv mva"),
            NTupleVariable("nSoftBJetTight20",  lambda ev: sum([(sv.mva>0.9 and (sv.jet == None or sv.jet.pt() < 20)) for sv in ev.ivf]) + len(ev.bjetsMedium), int, help="Exclusive sum of jets with pt > 20 passing CSV medium and SV from ivf with tight sv mva"),

            ##
            NTupleVariable("nSoftBJetLoose25",  lambda ev: sum([(sv.mva>0.3 and (sv.jet == None or sv.jet.pt() < 25)) for sv in ev.ivf]) + len(ev.bjetsMedium), int, help="Exclusive sum of jets with pt > 25 passing CSV medium and SV from ivf with loose sv mva"),
            NTupleVariable("nSoftBJetMedium25", lambda ev: sum([(sv.mva>0.7 and (sv.jet == None or sv.jet.pt() < 25)) for sv in ev.ivf]) + len(ev.bjetsMedium), int, help="Exclusive sum of jets with pt > 25 passing CSV medium and SV from ivf with medium sv mva"),
            NTupleVariable("nSoftBJetTight25",  lambda ev: sum([(sv.mva>0.9 and (sv.jet == None or sv.jet.pt() < 25)) for sv in ev.ivf]) + len(ev.bjetsMedium), int, help="Exclusive sum of jets with pt > 25 passing CSV medium and SV from ivf with tight sv mva"),

            ##
            NTupleVariable("nSoftBJetLoose30",  lambda ev: sum([(sv.mva>0.3 and (sv.jet == None or sv.jet.pt() < 30)) for sv in ev.ivf]) + len(ev.bjetsMedium), int, help="Exclusive sum of jets with pt > 30 passing CSV medium and SV from ivf with loose sv mva"),
            NTupleVariable("nSoftBJetMedium30", lambda ev: sum([(sv.mva>0.7 and (sv.jet == None or sv.jet.pt() < 30)) for sv in ev.ivf]) + len(ev.bjetsMedium), int, help="Exclusive sum of jets with pt > 30 passing CSV medium and SV from ivf with medium sv mva"),
            NTupleVariable("nSoftBJetTight30",  lambda ev: sum([(sv.mva>0.9 and (sv.jet == None or sv.jet.pt() < 30)) for sv in ev.ivf]) + len(ev.bjetsMedium), int, help="Exclusive sum of jets with pt > 30 passing CSV medium and SV from ivf with tight sv mva"),

            ##
            #NTupleVariable("nJet25NoTau", lambda ev: sum([ (j.pt() > 25 and not j.taus ) for j in ev.cleanJets]), int, help="Number of jets with pt > 25, not matched with taus"),
            #NTupleVariable("nBJetLoose25NoTau", lambda ev: sum([(j.btagWP("CSVv2IVFL") and not j.taus) for j in ev.cleanJets]), int, help="Number of jets with pt > 25 passing CSV loose, not matched with taus"),
            #NTupleVariable("nBJetMedium25NoTau", lambda ev: sum([(j.btagWP("CSVv2IVFM") and not j.taus) for j in ev.bjetsMedium]), int, help="Number of jets with pt > 25 passing CSV medium, not matched with taus"),
            #NTupleVariable("nBJetCMVALoose25", lambda ev: sum([j.btagWP("CMVAL") for j in ev.cleanJets]), int, help="Number of jets with pt > 25 passing CMVA Loose"),
            #NTupleVariable("nBJetCMVAMedium25", lambda ev: sum([j.btagWP("CMVAM") for j in ev.cleanJets]), int, help="Number of jets with pt > 25 passing CMVA Medium"),
            #NTupleVariable("nBJetCMVATight25", lambda ev: sum([j.btagWP("CMVAT") for j in ev.cleanJets]), int, help="Number of jets with pt > 25 passing CMVA Tight"),
            #NTupleVariable("nSoftBLoose25",  lambda ev: sum([(sv.mva>0.3 and (sv.jet == None or sv.jet.pt() < 25)) for sv in ev.ivf]), int, help="SV from ivf with loose sv mva not matched to a jet with pt > 25 GeV"),
            #NTupleVariable("nSoftBMedium25", lambda ev: sum([(sv.mva>0.7 and (sv.jet == None or sv.jet.pt() < 25)) for sv in ev.ivf]), int, help="SV from ivf with medium sv mva not matched to a jet with pt > 25 GeV"),
            #NTupleVariable("nSoftBTight25",  lambda ev: sum([(sv.mva>0.9 and (sv.jet == None or sv.jet.pt() < 25)) for sv in ev.ivf]), int, help="SV from ivf with tight sv mva not matched to a jet with pt > 25 GeV"),
            ##

            #NTupleVariable("nJet30NoTau", lambda ev: sum([ (j.pt() > 30 and not j.taus ) for j in ev.cleanJets]), int, help="Number of jets with pt > 30, not matched with taus"),
            #NTupleVariable("nBJetLoose30NoTau", lambda ev: sum([(j.btagWP("CSVv2IVFL") and not j.taus) for j in ev.cleanJets if j.pt() > 30]), int, help="Number of jets with pt > 30 passing CSV loose, not matched with taus"),
            #NTupleVariable("nBJetMedium30NoTau", lambda ev: sum([(j.btagWP("CSVv2IVFM") and not j.taus) for j in ev.bjetsMedium if j.pt() > 30]), int, help="Number of jets with pt > 30 passing CSV medium, not matched with taus"),
            ##

            #NTupleVariable("nJet40NoTau", lambda ev: sum([ (j.pt() > 40 and not j.taus ) for j in ev.cleanJets]), int, help="Number of jets with pt > 40, not matched with taus"),
            #NTupleVariable("nBJetLoose40NoTau", lambda ev: sum([(j.btagWP("CSVv2IVFL") and not j.taus) for j in ev.cleanJets if j.pt() > 40]), int, help="Number of jets with pt > 40 passing CSV loose, not matched with taus"),
            #NTupleVariable("nBJetMedium40NoTau", lambda ev: sum([(j.btagWP("CSVv2IVFM") and not j.taus) for j in ev.bjetsMedium if j.pt() > 40]), int, help="Number of jets with pt > 40 passing CSV medium, not matched with taus"),
            #NTupleVariable("nBJetCMVALoose40", lambda ev: sum([j.btagWP("CMVAL") for j in ev.cleanJets if j.pt() > 40]), int, help="Number of jets with pt > 40 passing CMVA Loose"),
            #NTupleVariable("nBJetCMVAMedium40", lambda ev: sum([j.btagWP("CMVAM") for j in ev.cleanJets if j.pt() > 40]), int, help="Number of jets with pt > 40 passing CMVA Medium"),
            #NTupleVariable("nBJetCMVATight40", lambda ev: sum([j.btagWP("CMVAT") for j in ev.cleanJets if j.pt() > 40]), int, help="Number of jets with pt > 40 passing CMVA Tight"),
            ##------------------------------------------------

            ##-------- type1 MET systematics ------------------------------------------
            NTupleVariable("metNoHF_rawPt", lambda ev : ev.metNoHF.uncorPt() if  hasattr(ev,'metNoHF') else  0, help="raw noHF met p_{T}"),
            NTupleVariable("metNoHF_rawPhi", lambda ev : ev.metNoHF.uncorPhi() if  hasattr(ev,'metNoHF') else  0, help="raw noHF met phi"),
            NTupleVariable("metNoHF_rawSumEt", lambda ev : ev.metNoHF.uncorSumEt() if hasattr(ev,'metNoHF') else 0, help="raw noHF met sumEt"),
            NTupleVariable("met_caloPt", lambda ev : ev.met.caloMETPt(), help="calo met p_{T}"),
            NTupleVariable("met_caloPhi", lambda ev : ev.met.caloMETPhi(), help="calo met phi"),
            NTupleVariable("met_caloSumEt", lambda ev : ev.met.caloMETSumEt(), help="calo met sumEt"),

            NTupleVariable("met_JetEnUp_Pt", lambda ev : ev.met.shiftedPt(ev.met.JetEnUp), help="type1, JetEnUp, pt"),
            NTupleVariable("met_JetEnUp_Phi", lambda ev : ev.met.shiftedPhi(ev.met.JetEnUp), help="type1, JetEnUp, phi"),
            NTupleVariable("met_JetResUp_Pt", lambda ev : ev.met.shiftedPt(ev.met.JetResUp), help="type1, JetResUp, pt"),
            NTupleVariable("met_JetResUp_Phi", lambda ev : ev.met.shiftedPhi(ev.met.JetResUp), help="type1, JetResUp, phi"),
            #NTupleVariable("met_JetResUpSmear_Pt", lambda ev : ev.met.shiftedPt(ev.met.JetResUpSmear), help="type1, JetResUpSmear, pt"),
            #NTupleVariable("met_JetResUpSmear_Phi", lambda ev : ev.met.shiftedPhi(ev.met.JetResUpSmear), help="type1, JetResUpSmear, phi"),
            NTupleVariable("met_MuonEnUp_Pt", lambda ev : ev.met.shiftedPt(ev.met.MuonEnUp), help="type1, MuonEnUp, pt"),
            NTupleVariable("met_MuonEnUp_Phi", lambda ev : ev.met.shiftedPhi(ev.met.MuonEnUp), help="type1, MuonEnUp, phi"),
            NTupleVariable("met_ElectronEnUp_Pt", lambda ev : ev.met.shiftedPt(ev.met.ElectronEnUp), help="type1, ElectronEnUp, pt"),
            NTupleVariable("met_ElectronEnUp_Phi", lambda ev : ev.met.shiftedPhi(ev.met.ElectronEnUp), help="type1, ElectronEnUp, phi"),
            NTupleVariable("met_TauEnUp_Pt", lambda ev : ev.met.shiftedPt(ev.met.TauEnUp), help="type1, TauEnUp, pt"),
            NTupleVariable("met_TauEnUp_Phi", lambda ev : ev.met.shiftedPhi(ev.met.TauEnUp), help="type1, TauEnUp, phi"),
            NTupleVariable("met_UnclusteredEnUp_Pt", lambda ev : ev.met.shiftedPt(ev.met.UnclusteredEnUp), help="type1, UnclusteredEnUp, pt"),
            NTupleVariable("met_UnclusteredEnUp_Phi", lambda ev : ev.met.shiftedPhi(ev.met.UnclusteredEnUp), help="type1, UnclusteredEnUp, phi"),
            NTupleVariable("met_ElectronEnUp_Pt", lambda ev : ev.met.shiftedPt(ev.met.ElectronEnUp), help="type1, ElectronEnUp, pt"),
            NTupleVariable("met_ElectronEnUp_Phi", lambda ev : ev.met.shiftedPhi(ev.met.ElectronEnUp), help="type1, ElectronEnUp, phi"),

            NTupleVariable("met_JetEnDown_Pt", lambda ev : ev.met.shiftedPt(ev.met.JetEnDown), help="type1, JetEnDown, pt"),
            NTupleVariable("met_JetEnDown_Phi", lambda ev : ev.met.shiftedPhi(ev.met.JetEnDown), help="type1, JetEnDown, phi"),
            NTupleVariable("met_JetResDown_Pt", lambda ev : ev.met.shiftedPt(ev.met.JetResDown), help="type1, JetResDown, pt"),
            NTupleVariable("met_JetResDown_Phi", lambda ev : ev.met.shiftedPhi(ev.met.JetResDown), help="type1, JetResDown, phi"),
            #NTupleVariable("met_JetResDownSmear_Pt", lambda ev : ev.met.shiftedPt(ev.met.JetResDownSmear), help="type1, JetResDownSmear, pt"),
            #NTupleVariable("met_JetResDownSmear_Phi", lambda ev : ev.met.shiftedPhi(ev.met.JetResDownSmear), help="type1, JetResDownSmear, phi"),
            NTupleVariable("met_MuonEnDown_Pt", lambda ev : ev.met.shiftedPt(ev.met.MuonEnDown), help="type1, MuonEnDown, pt"),
            NTupleVariable("met_MuonEnDown_Phi", lambda ev : ev.met.shiftedPhi(ev.met.MuonEnDown), help="type1, MuonEnDown, phi"),
            NTupleVariable("met_ElectronEnDown_Pt", lambda ev : ev.met.shiftedPt(ev.met.ElectronEnDown), help="type1, ElectronEnDown, pt"),
            NTupleVariable("met_ElectronEnDown_Phi", lambda ev : ev.met.shiftedPhi(ev.met.ElectronEnDown), help="type1, ElectronEnDown, phi"),
            NTupleVariable("met_TauEnDown_Pt", lambda ev : ev.met.shiftedPt(ev.met.TauEnDown), help="type1, TauEnDown, pt"),
            NTupleVariable("met_TauEnDown_Phi", lambda ev : ev.met.shiftedPhi(ev.met.TauEnDown), help="type1, TauEnDown, phi"),
            NTupleVariable("met_UnclusteredEnDown_Pt", lambda ev : ev.met.shiftedPt(ev.met.UnclusteredEnDown), help="type1, UnclusteredEnDown, pt"),
            NTupleVariable("met_UnclusteredEnDown_Phi", lambda ev : ev.met.shiftedPhi(ev.met.UnclusteredEnDown), help="type1, UnclusteredEnDown, phi"),
            NTupleVariable("met_ElectronEnDown_Pt", lambda ev : ev.met.shiftedPt(ev.met.ElectronEnDown), help="type1, ElectronEnDown, pt"),
            NTupleVariable("met_ElectronEnDown_Phi", lambda ev : ev.met.shiftedPhi(ev.met.ElectronEnDown), help="type1, ElectronEnDown, phi"),

            #NTupleVariable("metNoHF_JetEnUp_Pt", lambda ev : ev.metNoHF.shiftedPt(ev.met.JetEnUp) if hasattr(ev,'metNoHF') else -999, help="type1 noHF , JetEnUp, pt"),
            #NTupleVariable("metNoHF_JetEnUp_Phi", lambda ev : ev.metNoHF.shiftedPhi(ev.met.JetEnUp) if hasattr(ev,'metNoHF') else -999, help="type1 noHF , JetEnUp, phi"),
            #NTupleVariable("metNoHF_JetEnDown_Pt", lambda ev : ev.metNoHF.shiftedPt(ev.met.JetEnDown) if hasattr(ev,'metNoHF') else -999, help="type1 noHF , JetEnDown, pt"),
            #NTupleVariable("metNoHF_JetEnDown_Phi", lambda ev : ev.metNoHF.shiftedPhi(ev.met.JetEnDown) if hasattr(ev,'metNoHF') else -999, help="type1 noHF , JetEnDown, phi"),

            ##-------- custom quantities ------------------------------------------
            NTupleVariable("mtw", lambda ev: ev.mtw, help="mt(l,met)"),
            NTupleVariable("mtw1", lambda ev: ev.mtw1, help="1- 80*80/2*met*pt"),
            NTupleVariable("mtw2", lambda ev: ev.mtw2, help="cos (phi)"),

            ##-------- MET filter information ------------------------------------------
            #NTupleVariable("Flag_HBHENoiseFilter_fix", lambda ev: getattr(ev, "ev.hbheFilterNew", 0), help="HBEHE baseline temporary filter decision"),
            #NTupleVariable("Flag_HBHEIsoNoiseFilter_fix", lambda ev: getattr(ev, "ev.hbheFilterIso", 0), help="HBEHE isolation temporary filter decision"),
            NTupleVariable("Flag_badChargedHadronFilter", lambda ev: ev.badChargedHadron, help="bad charged hadron filter decision"),
            NTupleVariable("Flag_badMuonFilter", lambda ev: ev.badMuon, help="bad muon filter decision"),

]

susyStop4Body_globalObjects = susyCore_globalObjects.copy()
susyStop4Body_globalObjects.update({
            # put more here
})

susyStop4Body_collections = susyCore_collections.copy()
susyStop4Body_collections.update({
            "genParticles"       : NTupleCollection("genPartAll", genParticleWithMotherId,    200,              help="all pruned genparticles"),
            #"genParticles"       : NTupleCollection("genPartAll", genParticleWithMotherIndex, 200,              help="all pruned genparticles"),
            "gentopquarks"       : NTupleCollection("GenTop",     genParticleType,              2,              help="Generated top quarks from hard scattering (needed separately for top pt reweighting)"),
            ## ---------------------------------------------
            "selectedTaus"       : NTupleCollection("TauGood",    tauTypeSusy,                  8,              help="Taus after the preselection"),
            #"otherTaus"          : NTupleCollection("TauOther",   tauTypeSusy,                  8,              help="Taus after the preselection not selected"),
            "selectedLeptons"    : NTupleCollection("LepGood",    leptonTypeSusyExtraLight,     8,              help="Leptons after the preselection"),
            "otherLeptons"       : NTupleCollection("LepOther",   leptonTypeSusyExtraLight,     8,              help="Leptons after the preselection"),
            ## ---------------------------------------------
            "cleanJetsAll"       : NTupleCollection("Jet",        jetTypeSusy,                 30,              help="Cental jets after full selection and cleaning, sorted by pt"),
            ## ---------------------------------------------
            "ivf"                : NTupleCollection("SV",         svType,                      20,              help="SVs from IVF"),
            ## ---------------------------------------------
            "selectedIsoTrack"   : NTupleCollection("isoTrack",   isoTrackType,                50,              help="isoTrack, sorted by pt"),
            ## ---------------------------------------------
            "LHE_weights"        : NTupleCollection("LHEweight",  weightsInfoType,           1000, mcOnly=True, help="LHE weight info"),
})

