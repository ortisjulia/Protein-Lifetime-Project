# Protein-Lifetime-Project
This python script allows the user to get the protein lifetime in the cell following the N-end rule, by which the protein half-life is calculated by the last aminoacid in the protein sequence.

## Background
The N-end rule was first described by Alexander Varshavsky and his team in the ninties. It relates the in vivo half-life of a protein to the indentity of its N-terminal residue. He concluded that similar but distinct versions of the N-end rule operate in all organisms, from mammals, to yeast to bacteria. Therefore, according to this, it should be possible to calculate the half-life of a protein from a protein sequence and estimate the life-time of the protein in the cell using a bioinformatic approach.

## Code
This code was developed using Python3 version 3.8 using Spyder version 4.2.3, which is a Python development environment. Spyder can be downloaded using the cross-platform Anaconda distribution.

### Anaconda

In order to download Anaconda and, therefore, Spyder, you can go to the Anaconda website and follow their [installation protocol](https://docs.anaconda.com/anaconda/install/).

### Python Modules
Before using this script it is recommended to install the following Python modules:

1. **PySimpleGUI version 4.35.0.** It is a Python graphical user interface that was developed in 2018. More information and the user manual can be found on their [website](https://pysimplegui.readthedocs.io/en/latest/). You can install this module by either using `pip install pysimplegui` or by using `conda install -c conda-forge pysimplegui`.
2. **Requests version 2.25.1.** It is a simple HTTP library. It allows the user to send HTTP/1.1 requests extremely easy. You can install this module by using `python -m pip install requests`. More information on this module can be found on their [website](https://requests.readthedocs.io/en/master/).
3. **Biopython version 1.78.** It is a package of Python tools for computational molecular biology. It can be installed by either using `pip install biopython` or by `conda install -c conda-forge biopython`. More information and the documentation for biopython can be found on their [website](https://biopython.org/wiki/Documentation). From this package I am going to use the module SeqIO, which is the standard Sequence Input/Output interface for BioPython 1.43 and later. It provides a simple uniform interface to input and output assorted sequence file formats (including multiple sequence alignments), but will only deal with sequences as SeqRecord objects. Moreover, I also used the Seq module. The Seq object essentially combines a Python string with biological methods.
4. **Io version 3.3.** This module provides Python's main facilities for dealing with various types of I/O. This module is part of the standard library, so there is no need to install it separately. Specifically, I used the StringIO module, which creates an in-memory file-like object. This object can be used as input or output to the most function that would expect a standard file object. More information on io module can be found on their [website](https://docs.python.org/3/library/io.html).

### Usage
This script can be run from the command line by using the following command: `python ProteinLifetime.py`. It can also be run from any Python development environment such as Spyder.

When the code is run, a graphical user interface will pop up. There, the user has to choose the organism from which the protein sequence comes from (either Animal/Plant, Bacteria or Yeast) and whether the input is a protein sequence, a coding DNA nucleotide sequence or a Uniprot accession number. Below this, the user can paste the sequence (either protein or coding DNA nucleotide), the accession number or browse for a fasta file on their computer. If the cancel button is pressed, the program stops running while if the submit button is pressed all the information is submitted for analysis.

![ProteinLifetime](https://user-images.githubusercontent.com/70640998/110923803-93b1e200-8321-11eb-87d8-59c57ea976c9.jpg)

**Figure 1.** Protein lifetime in the cell input window. In here the user can choose the organism and whether the input is going to be a protein sequence, a nucleotide sequence or a Uniprot accession number. Then, the user copies the sequence, the Uniprot accession number or browses their computer for a fasta file.

When all the information is input you can press the submit button. A new window will appear, in which the information of the protein lifetime in the cell will be shown in addition to the protein sequence if you input a fasta file, or a protein or nucleotide sequence. If a Uniprot accession number was given, the output will be the protein lifetime and the information on the Uniprot webpage about the protein.

![ProteinLifetimeResults](https://user-images.githubusercontent.com/70640998/110923837-9f050d80-8321-11eb-9e95-ca51455c8d9e.jpg)

**Figure 2.** Example of an output window. This window contains the results of the protein lifetime analysis. In this case, it tells the user the protein lifetime and also outputs the protein sequence.

## Examples

In this repository, you can find a folder named Examples, with several data files and well explained examples to learn how to use this tool with all possible inputs and the expected outputs that will be generated.
