# Protein-Lifetime-Project
This python script allows the user to get the protein lifetime in the cell following the N-end rule, by which the protein half-life is calculated by the last aminoacid in the protein sequence.

## Background
The N-end rule was first described by Alexander Varshavsky and his team in the ninties. It relates the in vivo half-life of a protein to the indentity of its N-terminal residue. He concluded that similar but distinct versions of the N-end rule operate in all organisms, from mammals, to fungi to bacteria. Therefore, according to this, it should be possible to calculate the half-life of a protein from a protein sequence and estimate the life-time of the protein in the cell using a bioinformatic approach.

## Code
This code was developed using Python3 version 3.8 using Spyder version 4.2.3, which is a Python development environment. Spyder can be downloaded using the cross-platform Anaconda distribution.

### Python Modules
Before using this script it is recommended to install the following Python modules using the Anaconda Prompt:

1. PySimpleGUI version 4.35.0. It is a Python graphical user interface that was developed in 2018. More information and the user manual can be found on their [website](https://pysimplegui.readthedocs.io/en/latest/). You can install this module by either using `pip install pysimplegui` or by using `conda install -c conda-forge pysimplegui`.
2. Requests version 2.25.1. It is a simple HTTP library. It allows the user to send HTTP/1.1 requests extremely easy. You can install this module by using `python -m pip install requests`. More information on this module can be found on their [website](https://requests.readthedocs.io/en/master/).
3. Biopython version 1.78. It is a package of Python tools for computational molecular biology. It can be installed by either using `pip install biopython` or by `conda install -c conda-forge biopython`. More information and the documentation for biopython can be found on their [website](https://biopython.org/wiki/Documentation). From this package I am going to use the module SeqIO, which is the standard Sequence Input/Output interface for BioPython 1.43 and later. It provides a simple uniform interface to input and output assorted sequence file formats (including multiple sequence alignments), but will only deal with sequences as SeqRecord objects. Moreover, I also used the Seq module. The Seq object essentially combines a Python string with biological methods.
4. Io version 3.3. This module provides Python's main facilities for dealing with various types of I/O. This module is part of the standard library, so there is no need to install it separately. Specifically, I used the StringIO module, which creates an in-memory file-like object. This object can be used as input or output to the most function that would expect a standard file object. More information on io module can be found on their [website](https://docs.python.org/3/library/io.html).
