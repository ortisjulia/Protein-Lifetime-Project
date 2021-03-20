# Protein lifetime of an animal DNA coding sequence

In this example, I am going to show you how to use the protein lifetime tool to obtain the protein lifetime of a DNA coding sequence obtained from a fasta file stored in your computer.

## Step 1

Open Spyder (or any other Python IDE) and run the script. Alternatively you can also run the script from the command line using: `python ProteinLifetime.py`. This will cause a graphical user interface window to pop up. The window will look similar to the one shown in figure 1.

![ProteinLifetime](https://user-images.githubusercontent.com/70640998/111024653-3fba0280-83e0-11eb-858e-6c485913f7b5.jpg)

**Figure 1.** Graphical User Interface (GUI) of the protein lifetime tool. You can observe the different options the user can choose regarding type of organism and type of input (either a nucleotide sequence, a protein sequence or a Uniprot accession number). You can also see that there are different blank boxes to choose how to input the input sequence/accession number.

## Step 2

Now, we are going to proceed with filling the necessary options to obtain the correct protein lifetime. In this case, we have a human coding DNA sequence, which means that the user needs to select the Animal/Plant option in choose an organism and the nucleotide sequence in choose an option. Moreover, we want to use a fasta file found in our computer. For this reason, we are going to fill the third box named fasta file. This allows the user to browse through the files in the computer and choose the one that needs to be analysed. You can see the options chosen in this case in figure 2.

![ProteinLifetimeHLA](https://user-images.githubusercontent.com/70640998/111024821-033ad680-83e1-11eb-83f2-76a7f74d4e8b.jpg)

**Figure 2.** Options chosen to be able to obtain the protein sequence and protein lifetime of an animal (in this case human) DNA coding sequence.

## Step 3

After filling in the input information, we can press the submit button. In case you want to cancel the analysis, you can press the cancel button and the tool will stop running. Upon pressing the submit button, a new window will show. This is the results window shown in figure 3. As you can observe, it tells the user the lifetime of that particular protein in the cell as well as the protein sequence obtained from the coding DNA sequence.

![ProteinLifetimeHLAResults](https://user-images.githubusercontent.com/70640998/111024941-983dcf80-83e1-11eb-99eb-415e29bf1dbf.jpg)

**Figure 3.** Results window with the protein lifetime in the cell as well as the protein sequence obtained from the coding DNA sequence that was input.
