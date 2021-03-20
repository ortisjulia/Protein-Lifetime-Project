# Protein lifetime of a protein from protein sequence

In this markdown file, I am going to explain several examples on the possible options to obtain the protein lifetime of a protein from a protein sequence. In this case, the protein sequence is not found in a fasta file but directly copied to the input box.

## Step 1

Open Spyder (or any other Python IDE) and run the script. Alternatively you can also run the script from the command line using: `python ProteinLifetime.py`. This will cause a graphical user interface window to pop up. The window will look similar to the one shown in figure 1.

![ProteinLifetime](https://user-images.githubusercontent.com/70640998/111024653-3fba0280-83e0-11eb-858e-6c485913f7b5.jpg)

**Figure 1.** Graphical User Interface (GUI) of the protein lifetime tool. You can observe the different options the user can choose regarding type of organism and type of input (either a nucleotide sequence, a protein sequence or a Uniprot accession number). You can also see that there are different blank boxes to choose how to input the input sequence/accession number.

## Step 2

Now, we can proceed by choosing the options necessary to be able to analyse the protein sequence and obtain the protein lifetime. We have three different options to choose from regarding type of organism: Animal/Plant, Bacteria or Yeast, which are pretty self-descriptive. In addition to those, we also need to choose if our input is going to be a protein or a nucleotide (coding DNA sequence). In this example, we are going to choose the protein sequence option as we are going to paste a protein sequence to the empty sequence box below. In figure 2, you can see the different option combinations you can choose depending on the organism the protein sequence comes from.

![ProteinLifetimePlantProtSeq](https://user-images.githubusercontent.com/70640998/111027216-18b6fd00-83ef-11eb-90e3-7a0a9f4087a6.jpg) ![ProteinLifetimeBacteriaProtSeq](https://user-images.githubusercontent.com/70640998/111027218-1ce31a80-83ef-11eb-9016-9fe945b968d6.jpg)  ![ProteinLifetimeYeastProtSeq](https://user-images.githubusercontent.com/70640998/111027224-21a7ce80-83ef-11eb-9405-6f3e041626e6.jpg)

**Figure 2.** In these pictures you can see the different option combinations to choose depending on whether the protein sequence comes from Animal/Plant, Bacteria or Yeast, respectively.

## Step 3

After filling in the input information, we can press the submit button. In case you want to cancel the analysis, you can press the cancel button and the tool will stop running. Upon pressing the submit button, a new window will show. This is the results window shown in figure 3. As you can observe, it tells the user the lifetime of that particular protein in the cell as well as the protein sequence that was input.

![ProteinLifetimePlantProtSeqResults](https://user-images.githubusercontent.com/70640998/111027242-59167b00-83ef-11eb-8719-5d5cd2f90612.jpg)  ![ProteinLifetimeBacteriaProtSeqResults](https://user-images.githubusercontent.com/70640998/111027245-5d429880-83ef-11eb-8d00-0bcbcf49e39e.jpg) ![ProteinLifetimeYeastProtSeqResults](https://user-images.githubusercontent.com/70640998/111027248-65023d00-83ef-11eb-8d88-b977b2018121.jpg)

**Figure 3.** Results window with the protein lifetime in the cell as well as the protein sequence that was input. The pictures correspond to the plant protein lifetime analysis, bacterial protein lifetime analysis and the yeast protein lifetime analysis, respectively. 

## Sequences used in the example

**>ADX23525.1 DOG1, partial [Arabidopsis thaliana]**
MGSSSKNIEQAQDSYLEWMSLQSQRIPELKQLLAQRRSHGDEDNDNKLRKLTGKIIGDFKNYAAKRADLAHRCSSNYYAPTWNSPLENALIWMGGCRPSSFFRLVYALCGSQTEIRVTQFLRNIDGYESS

**>AAL20871.1 flagellar biosynthesis; flagellin [Salmonella enterica subsp. enterica serovar Typhimurium str. LT2]**
MAQVINTNSLSLLTQNNLNKSQSALGTAIERLSSGLRINSAKDDAAGQAIANRFTANIKGLTQASRNAND
GISIAQTTEGALNEINNNLQRVRELAVQSANSTNSQSDLDSIQAEITQRLNEIDRVSGQTQFNGVKVLAQ
DNTLTIQVGANDGETIDIDLKQINSQTLGLDTLNVQQKYKVSDTAATVTGYADTTIALDNSTFKASATGL
GGTDQKIDGDLKFDDTTGKYYAKVTVTGGTGKDGYYEVSVDKTNGEVTLAGGATSPLTGGLPATATEDVK
NVQVANADLTEAKAALTAAGVTGTASVVKMSYTDNNGKTIDGGLAVKVGDDYYSATQNKDGSISINTTKY
TADDGTSKTALNKLGGADGKTEVVSIGGKTYAASKAEGHNFKAQPDLAEAAATTTENPLQKIDAALAQVD
TLRSDLGAVQNRFNSAITNLGNTVNNLTSARSRIEDSDYATEVSNMSRAQILQQAGTSVLAQANQVPQNV
LSLLR

**>NP_594716.1 Cdc14 family protein phosphatase Clp1 [Schizosaccharomyces pombe]**
MDYQDDGLGEMIEFLEDKLYYTSLSQPPKAELYPHMHFFTIDDELIYNPFYHDFGPLNVSHLIRFAVIVH
GIMGKHRQAKKSKAIVLYSSTDTRLRANAACLLACYMVLVQNWPPHLALAPLAQAEPPFLGFRDAGYAVS
DYYITIQDCVYGLWRARESSILNIRNIDVHDYETYERVENGDFNWISPKFIAFASPIQAGWNHASTRPKK
LPQPFAIVLDYFVANKVKLIVRLNGPLYDKKTFENVGIRHKEMYFEDGTVPELSLVKEFIDLTEEVEEDG
VIAVHCKAGLGRTGCLIGAYLIYKHCFTANEVIAYMRIMRPGMVVGPQQHWLHINQVHFRAYFYEKAMGR
AIQQATAAEPLATPPRHPLNATNGTSQSNISTPLPEPTPGQPRKVSGHNPPSARRLPSASSVKFNEKLKN
ASKQSIQNENKASYSSYEDSEIQNDDETRTVGTPTETISVVRLRRSSSQSNIEPNGVRSPTSSPTGSPIR
RTSGNRWSSGSSHSKKSAQRSVSMSSLNNTSNGRVAKPKPSKSRLIS

