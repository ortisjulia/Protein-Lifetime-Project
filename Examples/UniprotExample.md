# Protein lifetime of a protein from a Uniprot accession number

In this markdown file, I am going to explain how to use the protein lifetime tool to find out a protein's lifetime in the cell from its Uniprot accession number.

## Step 1

Open Spyder (or any other Python IDE) and run the script. This will cause a graphical user interface window to pop up. The window will look similar to the one shown in figure 1.

![ProteinLifetime](https://user-images.githubusercontent.com/70640998/111024653-3fba0280-83e0-11eb-858e-6c485913f7b5.jpg)

**Figure 1.** Graphical User Interface (GUI) of the protein lifetime tool. You can observe the different options the user can choose regarding type of organism and type of input (either a nucleotide sequence, a protein sequence or a Uniprot accession number). You can also see that there are different blank boxes to choose how to input the input sequence/accession number.

## Step 2

Now, we can proceed by choosing the options necessary to be able to analyse the protein sequence and obtain the protein lifetime. We have three different options to choose from regarding type of organism: Animal/Plant, Bacteria or Yeast, which are pretty self-descriptive. In addition to those, we also need to choose the option of Uniprot accession number as we want to use that to find out the protein lifetime. In figure 2, we can see the different combinations of options to be chosen.

![ProteinLifetimeMouseUniprot](https://user-images.githubusercontent.com/70640998/111028252-c4634b80-83f5-11eb-9cd9-a0e34c897798.jpg) ![ProteinLifetimeBacteriaUniprot](https://user-images.githubusercontent.com/70640998/111028257-c9c09600-83f5-11eb-921e-7445d339681e.jpg)  ![ProteinLifetimeYeastUniprot](https://user-images.githubusercontent.com/70640998/111028260-cf1de080-83f5-11eb-8ffd-1733c916dfc8.jpg)

**Figure 2.** In these pictures you can see the different option combinations to choose depending on whether the Uniprot accession number comes from an Animal/Plant, a Bacterial or a Yeast protein, respectively.

## Step 3

After filling in the input information, we can press the submit button. In case you want to cancel the analysis, you can press the cancel button and the tool will stop running. Upon pressing the submit button, a new window will show. This is the results window shown in figure 3. As you can observe, it tells the user the lifetime of that particular protein in the cell as well as the information found on Uniprot about that particular protein.

![ProteinLifetimeMouseUniprotResults](https://user-images.githubusercontent.com/70640998/111028265-d644ee80-83f5-11eb-8ed9-c92e736e90f7.jpg)  ![ProteinLifetimeBacteriaUniprotResults](https://user-images.githubusercontent.com/70640998/111028266-db09a280-83f5-11eb-9907-4f6f3a0dba52.jpg) ![ProteinLifetimeYeastUniprotResults](https://user-images.githubusercontent.com/70640998/111028271-e066ed00-83f5-11eb-9c62-1871754c7f2a.jpg)

**Figure 3.** Results window with the protein lifetime in the cell as well as the Uniprot information about the protein. The pictures correspond to the animal protein lifetime analysis, bacterial protein lifetime analysis and the yeast protein lifetime analysis, respectively.

## Uniprot accession numbers used in the example

Q8CJ12 -> Mus musculus, Adhesion G-protein coupled receptor G2.

P46544 -> Lactobacillus delbrueckii subsp. bulgaricus, Proline iminopeptidase.

P12688 -> Saccharomyces cerevisiae (strain ATCC 204508 / S288c) (Baker's yeast), Serine/threonine-protein kinase YPK1.

