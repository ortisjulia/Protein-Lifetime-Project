# Protein lifetime of a protein from nucleotide sequence

In this markdown file, I am going to explain several examples on the possible options to obtain the protein lifetime of a protein from a coding DNA nucleotide sequence. In this case, the nucleotide sequence is not found in a fasta file but directly copied to the input box. However, it needs to be said that as the nucleotide sequences tend to be longer than protein sequences it is better to use the fasta file function of the tool instead of copying the nucleotide sequence directly to the input box.

## Step 1

Open Spyder (or any other Python IDE) and run the script. Alternatively you can also run the script from the command line using: `python ProteinLifetime.py`. This will cause a graphical user interface window to pop up. The window will look similar to the one shown in figure 1.

![ProteinLifetime](https://user-images.githubusercontent.com/70640998/111024653-3fba0280-83e0-11eb-858e-6c485913f7b5.jpg)

**Figure 1.** Graphical User Interface (GUI) of the protein lifetime tool. You can observe the different options the user can choose regarding type of organism and type of input (either a nucleotide sequence, a protein sequence or a Uniprot accession number). You can also see that there are different blank boxes to choose how to input the input sequence/accession number.

## Step 2

Now, we can proceed by choosing the options necessary to be able to analyse the coding DNA nucleotide sequence and obtain the protein lifetime. We have three different options to choose from regarding type of organism: Animal/Plant, Bacteria or Yeast, which are pretty self-descriptive. In addition to those, we also need to choose if our input is going to be a protein or a nucleotide (coding DNA sequence). In this example, we are going to choose the nucleotide sequence option as we are going to paste a nucleotide sequence to the empty sequence box below. In figure 2, you can see the different option combinations you can choose depending on the organism the nucleotide sequence comes from.

![ProteinLifetimeHumanNtSeq](https://user-images.githubusercontent.com/70640998/111027745-8153a900-83f2-11eb-8f7a-bd46b93d3dfe.jpg) ![ProteinLifetimeBacteriaNtSeq](https://user-images.githubusercontent.com/70640998/111027820-f921d380-83f2-11eb-8c76-2f224a6404f7.jpg)  ![ProteinLifetimeYeastNtSeq](https://user-images.githubusercontent.com/70640998/111027826-ffb04b00-83f2-11eb-97c6-39603f1b4995.jpg)

**Figure 2.** In these pictures you can see the different option combinations to choose depending on whether the nucelotide sequence comes from Animal/Plant, Bacteria or Yeast, respectively.

## Step 3

After filling in the input information, we can press the submit button. In case you want to cancel the analysis, you can press the cancel button and the tool will stop running. Upon pressing the submit button, a new window will show. This is the results window shown in figure 3. As you can observe, it tells the user the lifetime of that particular protein in the cell as well as the protein sequence that was obtained from the input nucleotide sequence.

![ProteinLifetimeHumanNtSeqResults](https://user-images.githubusercontent.com/70640998/111027748-84e73000-83f2-11eb-8f09-da755a65d316.jpg)

**Figure 3.** Results window with the protein lifetime in the cell as well as the protein sequence that was input. This result picture corresponds to the human protein lifetime analysis. 

## Sequence used in the example

**>AB046569.1 Homo sapiens ace2 mRNA, complete cds**
TTTTTAGTCTAGGGAAAGTCATTCAGTGGATGTGATCTTGGCTCACAGGGGACGATGTCAAGCTCTTCCT
GGCTCCTTCTCAGCCTTGTTGCTGTAACTGCTGCTCAGTCCACCATTGAGGAACAGGCCAAGACATTTTT
GGACAAGTTTAACCACGAAGCCGAAGACCTGTTCTATCAAAGTTCACTTGCTTCTTGGAATTATAACACC
AATATTACTGAAGAGAATGTCCAAAACATGAATAACGCTGGGGACAAATGGTCTGCCTTTTTAAAGGAAC
AGTCCACACTTGCCCAAATGTATCCACTACAAGAAATTCAGAATCTCACAGTCAAGCTTCAGCTGCAGGC
TCTTCAGCAAAATGGGTCTTCAGTGCTCTCAGAAGACAAGAGCAAACGGTTGAACACAATTCTAAATACA
ATGAGCACCATCTACAGTACTGGAAAAGTTTGTAACCCAGATAATCCACAAGAATGCTTATTACTTGAAC
CAGGTTTGAATGAAATAATGGCAAACAGTTTAGACTACAATGAGAGGCTCTGGGCTTGGGAAAGCTGGAG
ATCTGAGGTCGGCAAGCAGCTGAGGCCATTATATGAAGAGTATGTGGTCTTGAAAAATGAGATGGCAAGA
GCAAATCATTATGAGGACTATGGGGATTATTGGAGAGGAGACTATGAAGTAAATGGGGTAGATGGCTATG
ACTACAGCCGCGGCCAGTTGATTGAAGATGTGGAACATACCTTTGAAGAGATTAAACCATTATATGAACA
TCTTCATGCCTATGTGAGGGCAAAGTTGATGAATGCCTATCCTTCCTATATCAGTCCAATTGGATGCCTC
CCTGCTCATTTGCTTGGTGATATGTGGGGTAGATTTTGGACAAATCTGTACTCTTTGACAGTTCCCTTTG
GACAGAAACCAAACATAGATGTTACTGATGCAATGGTGGACCAGGCCTGGGATGCACAGAGAATATTCAA
GGAGGCCGAGAAGTTCTTTGTATCTGTTGGTCTTCCTAATATGACTCAAGGATTCTGGGAAAATTCCATG
CTAACGGACCCAGGAAATGTTCAGAAAGCAGTCTGCCATCCCACAGCTTGGGACCTGGGGAAAGGCGACT
TCAGGATCCTTATGTGCACAAAGGTGACAATGGACGACTTCCTGACAGCTCATCATGAGATGGGGCATAT
TCAGTATGATATGGCATATGCTGCACAACCTTTTCTGCTAAGAAATGGAGCTAATGAAGGATTCCATGAA
GCTGTTGGGGAAATCATGTCACTTTCTGCAGCCACACCTAAGCATTTAAAATCCATTGGTCTTCTGTCAC
CCGATTTTCAAGAAGACAATGAAACAGAAATAAACTTCCTGCTCAAACAAGCACTCACGATTGTTGGGAC
TCTGCCATTTACTTACATGTTAGAGAAGTGGAGGTGGATGGTCTTTAAAGGGGAAATTCCCAAAGACCAG
TGGATGAAAAAGTGGTGGGAGATGAAGCGAGAGATAGTTGGGGTGGTGGAACCTGTGCCCCATGATGAAA
CATACTGTGACCCCGCATCTCTGTTCCATGTTTCTAATGATTACTCATTCATTCGATATTACACAAGGAC
CCTTTACCAATTCCAGTTTCAAGAAGCACTTTGTCAAGCAGCTAAACATGAAGGCCCTCTGCACAAATGT
GACATCTCAAACTCTACAGAAGCTGGACAGAAACTGTTCAATATGCTGAGGCTTGGAAAATCAGAACCCT
GGACCCTAGCATTGGAAAATGTTGTAGGAGCAAAGAACATGAATGTAAGGCCACTGCTCAACTACTTTGA
GCCCTTATTTACCTGGCTGAAAGACCAGAACAAGAATTCTTTTGTGGGATGGAGTACCGACTGGAGTCCA
TATGCAGACCAAAGCATCAAAGTGAGGATAAGCCTAAAATCAGCTCTTGGAGATAGAGCATATGAATGGA
ACGACAATGAAATGTACCTGTTCCGATCATCTGTTGCATATGCTATGAGGCAGTACTTTTTAAAAGTAAA
AAATCAGATGATTCTTTTTGGGGAGGAGGATGTGCGAGTGGCTAATTTGAAACCAAGAATCTCCTTTAAT
TTCTTTGTCACTGCACCTAAAAATGTGTCTGATATCATTCCTAGAACTGAAGTTGAAAAGGCCATCAGGA
TGTCCCGGAGCCGTATCAATGATGCTTTCCGTCTGAATGACAACAGCCTAGAGTTTCTGGGGATACAGCC
AACACTTGGACCTCCTAACCAGCCCCCTGTTTCCATATGGCTGATTGTTTTTGGAGTTGTGATGGGAGTG
ATAGTGGTTGGCATTGTCATCCTGATCTTCACTGGGATCAGAGATCGGAAGAAGAAAAATAAAGCAAGAA
GTGGAGAAAATCCTTATGCCTCCATCGATATTAGCAAAGGAGAAAATAATCCAGGATTCCAAAACACTGA
TGATGTTCAGACCTCCTTTTAGAAAAATCTATGTTTTTCCTCTTGAGGTGATTTTGTTGTATGTAAATGT
TAATTTCATGGTATAGAAAATATAAGATGATAAAAATATCATTAAATGTCAAAACTATGACTCTGTTCAG
AAAAAAAAA
