#!/usr/bin/python3
'''
    Title: ProteinLifetime.py
    Date: 2021-03-12
    Author: Julia Ortis Sunyer
    Description:
        This program will calculate the protein lifetime in the cell by the N-end rule described
        by Alexander Varshavsky et al. In order to calculate the protein lifetime a protein sequence
        needs to be given, either by directly inputing the protein sequence, by giving the protein's
        Uniprot accession number or by giving the coding nucleotide sequence so that it can be translated
        to a protein sequence and its lifetime calculated.
    List of functions:
        No user defined functions are used in the program.
    List of non-standard modules:
        The non-standard modules used are the following:
            - PySimpleGUI: version 4.35.0. It is a Python graphical user interface that was developed in 2018.
            - requests: version 2.25.1. It is a simple HTTP library. It allows the user to send HTTP/1.1 requests extremely easy.
            - Biopython: version 1.78. It is a package of Python tools for computational molecular biology.
                - SeqIO: the standard Sequence Input/Output interface for BioPython 1.43 and later. 
                         It provides a simple uniform interface to input and output assorted sequence file 
                         formats (including multiple sequence alignments), but will only deal with sequences as SeqRecord objects.
                - Seq: combines a Python string with biological methods.
    Procedure:
        1. Using PySimpleGUI create the graphical user interface with all the input options needed as well as
        the output window.
        2. Depending on the organism option chosen by the user, this script is going to use the animal/plant dictionary,
        the bacterial dictionary or the yeast dictionary, that contain all the amino acids with the resulting
        half-life of the protein when they are found at the N-terminal.
        3. Depending on the input option chosen by the user, this script is going to either use the protein sequence directly
        to calculate its lifetime in the cell, translate the coding nucleotide sequence to obtain the protein sequence and
        calculate the protein lifetime or access the Uniprot database to retrieve the information related to the accession 
        number given and calculate the protein lifetime.
        4. The output is going to be displayed in a pop up window and will show the protein lifetime in either hours or minutes
        as well as the protein sequence or the Uniprot information.
    Usage:
        ./ProteinLifetime.py
'''
#Import modules
import PySimpleGUI as sg #For the graphical user interface
import requests as r #To send HTTP requests
from Bio import SeqIO #To input and output assorted sequence file formats
from io import StringIO #To create an in-memory file-like object
from Bio.Seq import Seq #To combine a Python string with biological methods

#Color scheme of the graphical user interface
sg.ChangeLookAndFeel('GreenTan')      

#Layout of the graphical user interface        
layout = [      
    
    #Title of the GUI
    [sg.Text('PROTEIN LIFETIME IN THE CELL', size=(30, 1), justification='center', font=("Helvetica", 25), relief=sg.RELIEF_RIDGE)],
    
    #Explanation text so that the user can run the program smoothly
    [sg.Text('In order to get the protein lifetime, you need to choose the organism the protein comes from' + '\n' + 'and input either the sequence or the Uniprot accession number from the protein of interest.')],
    
    #Frame with organism options that the user needs to choose from. Radio is used when only one option should be chosen
    [sg.Frame(layout=[      
    [sg.Radio('Animal or Plant', "RADIO1", size=(11,1)),  sg.Radio('Bacteria', "RADIO1"), sg.Radio('Yeast', "RADIO1")]], title='Choose an organism',title_color='black', relief=sg.RELIEF_SUNKEN, tooltip='Use these to set flags')],
    
    #Frame with input options that the user needs to choose from. Radio is used when only one option has to be chosen
    [sg.Frame(layout=[            
    [sg.Radio('Protein sequence', "RADIO2", size=(12,1)), sg.Radio('Nucleotide sequence', "RADIO2"), sg.Radio('Uniprot accession number', "RADIO2")]], title='Choose an option',title_color='black', relief=sg.RELIEF_SUNKEN, tooltip='Use these to set flags')],
    
    #To depict a separation line in the GUI    
    [sg.Text('_'  * 80)],
    
    #Text explaining what needs to be done in the following section
    [sg.Text('Copy a sequence, an accession number or choose a fasta file:', size=(60, 1))], 
    
    #Empty input box to copy a sequence as input with text indicating that that box is for the sequence input
    [sg.Text('Sequence', size=(15, 1), auto_size_text=False, justification='right'),      
        sg.InputText()],
    
    #Empty input box to copy the Uniprot accession number with text indicating that the box is for the accession number input
    [sg.Text('Accession number', size=(15, 1), auto_size_text=False, justification='right'),      
        sg.InputText()],
    
    #Empty input box to browse through the user files and upload a fasta file, with text indicating that the box is for a fasta file
    [sg.Text('Fasta file', size=(15, 1), auto_size_text=False, justification='right'),      
        sg.InputText(), sg.FileBrowse()],
    
    #Submit button to submit the input data and cancel button to cancel and exit the GUI
    [sg.Submit(tooltip='Click to submit this window'), sg.Cancel()]    
]      

#To create the GUI window with the window name and the default size
window = sg.Window('Protein lifetime', layout, default_element_size=(40, 1), grab_anywhere=False)      

#To read the events and values from the window
event, values = window.read()      

#To close the GUI window
window.close()

#Create an empty amino acid list to append the amino acids found in the sequence
aminoacid_list = []
#Make the last_aminoacid variable global so it can be used anywhere in the script
global last_aminoacid
#Make the uniprot_seqids variable global so it can be used anywhere in the script
global uniprot_seqids

#If the values[6] is not empty and the values[7] and values[8] are empty, it will mean that the input box for sequence is full and I will want to process the input data the following way
if values[6] != '' and values[7] == '' and values[8] == '':
    for element in values[6]: #Go through the elements in values[6], which is a sequence
        aminoacid_list.append(element) #Append each element to the aminoacid_list
        last_aminoacid = element #The last element on the values[6], so the last element of the sequence, will be added to a variable called last_aminoacid

#If the values[7] is not empty and the values[6] and values[8] are empty, it means that the Uniprot accession number box is full and I will want to process the input data the following way
if values[7] != '' and values[6] == '' and values[8] == '':
    cID = values[7] #The Uniprot accession number is assigned to a variable called cID
    baseUrl = "http://www.uniprot.org/uniprot/" #This is the base URL for the Uniprot website
    currentUrl = baseUrl+cID+".fasta" #The current URL is going to be the base URL plus the Uniprot accession number (cID variable) plus .fasta
    response = r.post(currentUrl) #This is used to send HTTP requests with the currentUrl. It is assigned to a variable called response
    cData = ''.join(response.text) #cData variable joins the response text
    Sequence = StringIO(cData) #Sequence is a variable that is created by using StringIO and the information on the cData variable
    pSeq = list(SeqIO.parse(Sequence,'fasta')) #pSeq is a variable which is assigned a list of the parsed sequence variable using SeqIO
    for element in pSeq: #Go through the elements in pSeq
        last_aminoacid = element[-1] #Find the last element of the pSeq, which will correspond to the last amino acid on the protein sequence found in Uniprot, and assign it to the variable called last_aminoacid

#If values[8] is not empty and values[6] and values[7] are empty, it means that the fasta file input box is full and I will want to process the input data the following way
if values[8] != '' and values[6] == '' and values[7] == '':
    with open(values[8], 'r') as protein: #Open the fasta file as protein in reading mode
        for line in protein: #Go through the file
            if line.startswith(">"): #Do nothing with the lines starting with >
                pass
            else: #The lines that do not start with > are the lines with the sequence
                for element in line.strip(): #Go through the elements in those lines while striping new line characters
                    aminoacid_list.append(element) #Append the elements of the line to the aminoacid_list
                    last_aminoacid = element #Assign the last element on the line to the variable called last_aminoacid

#If any combination other than the ones described above is selected, do nothing
else:
    pass

#The following dictionaries show the half-time life of the protein if the last residue ends with one particular element of the dictionary
#For animals and plants, the degradation half-time is in hours
animal_dict = {'V':100, 'M':30, 'G':30, 'P':20, 'I':20, 'T':7.2, 'L':5.5, 'A':4.4, 'H':3.5, 'W':2.8, 'Y':2.8, 'S':1.9, 'N':1.4, 'K':1.3, 'C':1.2, 'D':1.1, 'F':1.1, 'E':1, 'R':1, 'Q':0.8}
#For yeast, the degradation half-time is in minutes
yeast_dict = {'V':1200, 'M':1200, 'G':1200, 'P':1200, 'I':30, 'T':1200, 'L':3, 'A':1200, 'H':3, 'W':3, 'Y':10, 'S':1200, 'N':3, 'K':3, 'C':1800, 'D':3, 'F':3, 'E':30, 'R':2, 'Q':10}
#For bacteria, the degradation half-time is in minutes
bacterial_dict = {'V':600, 'M':600, 'G':600, 'P':600, 'I':600, 'T':600, 'L':2, 'A':600, 'H':600, 'W':2, 'Y':2, 'S':600, 'N':600, 'K':2, 'C':600, 'D':600, 'F':2, 'E':600, 'R':2, 'Q':600} 

#Code if option 0 is chosen, which is that the organism is an animal and option 3 is chosen, which is a protein sequence
if values[0] == True and values[3] == True:
    for key,value in animal_dict.items(): #Go through the keys and values in the animal_dict dictionary
        if key == last_aminoacid: #if the key is the same as the last_aminoacid
            time = value * 2 #I multiply the value in the dictionary by 2 because it is the half-life and I want the full degradation time
            protein_sequence = "".join(aminoacid_list) #Join the amino_acid list and assign it to a variable called protein_sequence
            sg.popup('PROTEIN LIFETIME', 'This protein half-life is ' + str(value) + ' hours.', 'This protein lifetime in the cell is ' + str(time) + ' hours.', 'The protein sequence is:' + "\n" + protein_sequence) #In a pop up window print the protein lifetime and the protein sequence as the output of the analysis
        else: #If the last_aminoacid is not the same as the key, do nothing
            pass

#Code if option 0 is chosen, which is that the organism is an animal and option 4 is chosen, which is a nucleotide sequence
if values[0] == True and values[4] == True:
    coding_dna = "".join(aminoacid_list) #Join the elements in the aminoacid_list and assign them to the variable coding_dna
    coding_dna = Seq(coding_dna) #To be able to use the coding_dna variable in biopython as a string with biological methods
    translated = coding_dna.translate(to_stop=True) #Assign the translated coding_dna information to a new variable called translated, which will contain the translated DNA sequence (the protein sequence)
    for element in translated: #Go through the elements in the variable translated
        aminoacid_list.append(element) #Append each element to the aminoacid_list
        last_aminoacid = element #Assign the last element to a variable called last_aminoacid
    for key,value in animal_dict.items(): #Go through the keys and values of the animal_dict dictonary
        if key == last_aminoacid: #If the dictionary key is the same as the last_aminoacid
            time = value * 2 #I multiply the value in the dictionary by 2 because it is the half-life and I want the full degradation time
            protein_sequence = translated #Assigned the translated variable data to protein_sequence variable
            sg.popup('PROTEIN LIFETIME', 'This protein half-life is ' + str(value) + ' hours.', 'This protein lifetime in the cell is ' + str(time) + ' hours.', 'The protein sequence is:' + "\n" + protein_sequence) #In a pop up window print the protein lifetime and the protein sequence as the output of the analysis
        else: #If the last_aminoacid is not the same as the key, do nothing
            pass

#Code if option 0 is chosen, which is that the organism is an animal and option 5 is chosen, which is a uniprot accession number
if values[0] == True and values[5] == True:
    for key,value in animal_dict.items(): #Go through the keys and values of the animal_dict dictionary
        if key == last_aminoacid: #If the key is the same as the last_aminoacid
            time = value * 2 #I multiply the value in the dictionary by 2 because it is the half-life and I want the full degradation time
            protein_sequence = "".join(aminoacid_list) #Join the amino_acid list and assign it to a variable called protein_sequence
            sg.popup('PROTEIN LIFETIME', 'This protein half-life is ' + str(value) + ' hours.', 'This protein lifetime in the cellNo docu is ' + str(time) + ' hours.', 'The Uniprot information about the protein sequence is:', pSeq) #In a pop up window print the protein lifetime and the information retrieved in the Uniprot webpage using the input Uniprot accession number
        else: #If the last_aminoacid is not the same as the key, do nothing
            pass
    

#Code if option 1 is chosen, which is that the organism is a bacteria and option 3 is chosen, which is a protein sequence
if values[1] == True and values[3] == True:
    for key,value in bacterial_dict.items(): #Go through the keys and values in the bacterial_dict dictionary
        if key == last_aminoacid: #If the key and the last_aminoacid are the same
            time = value * 2 #I multiply the value in the dictionary by 2 because it is the half-life and I want the full degradation time
            protein_sequence = "".join(aminoacid_list) #Join the amino_acid list and assign it to a variable called protein_sequence
            if time > 60: #If the variable time is bigger than 60
                time = time/60 #Divide the variable time by 60 to transform minutes to hours
                value = value/60 #Divide the variable value by 60 to transform minutes to hours
                sg.popup('PROTEIN LIFETIME', 'This protein half-life is ' + str(value) + ' hours.', 'This protein lifetime in the cell is ' + str(time) + ' hours.', 'The protein sequence is:' + '\n' + protein_sequence) #In a pop up window print the protein lifetime and the protein sequence as the output of the analysis
            else: #If the time is less than 60, leave the time units in minutes
                sg.popup('PROTEIN LIFETIME', 'This protein half-life is ' + str(value) + ' minutes.', 'This protein lifetime in the cell is ' + str(time) + ' minutes.', 'The protein sequence is:' + '\n' + protein_sequence) #In a pop up window print the protein lifetime and the protein sequence as the output of the analysis
        else: #If the last_aminoacid is not the same as the key, do nothing
            pass

#Code if option 1 is chosen, which is that the organism is a bacteria and option 4 is chosen, which is a nucelotide sequence
if values[1] == True and values[4] == True:
    coding_dna = "".join(aminoacid_list) #Join the elements in the aminoacid_list and assign them to the variable coding_dna
    coding_dna = Seq(coding_dna) #To be able to use the coding_dna variable in biopython as a string with biological methods
    translated = coding_dna.translate(to_stop=True) #Assign the translated coding_dna information to a new variable called translated, which will contain the translated DNA sequence (the protein sequence)
    for element in translated: #Go through the elements in the variable translated
        aminoacid_list.append(element) #Append each element to the aminoacid_list
        last_aminoacid = element #Assign the last element to a variable called last_aminoacid
    for key,value in bacterial_dict.items(): #Go through the keys and values in the bacterial_dict dictionary
        if key == last_aminoacid: #If the key and the last_aminoacid are the same
            time = value * 2 #I multiply the value in the dictionary by 2 because it is the half-life and I want the full degradation time
            protein_sequence = translated #Assign the translated variable to the protein_sequence variable
            if time > 60: #If the variable time is bigger than 60
                time = time/60 #Divide the variable time by 60 to transform minutes to hours
                value = value/60 #Divide the variable value by 60 to transform minutes to hours
                sg.popup('PROTEIN LIFETIME', 'This protein half-life is ' + str(value) + ' hours.', 'This protein lifetime in the cell is ' + str(time) + ' hours.', 'The protein sequence is:' + '\n' + protein_sequence) #In a pop up window print the protein lifetime and the protein sequence as the output of the analysis
            else: #If the time is less than 60, leave the time units in minutes
                sg.popup('PROTEIN LIFETIME', 'This protein half-life is ' + str(value) + ' minutes.', 'This protein lifetime in the cell is ' + str(time) + ' minutes.', 'The protein sequence is:' + '\n' + protein_sequence) #In a pop up window print the protein lifetime and the protein sequence as the output of the analysis
        else: #If the last_aminoacid is not the same as the key, do nothing
            pass

#Code if option 1 is chosen, which is that the organism is a bacteria and option 5 is chosen, which is a uniprot accession number
if values[1] == True and values[5] == True:
    for key,value in bacterial_dict.items(): #Go through the keys and values in the bacterial_dict dictionary
        if key == last_aminoacid: #If the key and the last_aminoacid are the same
            time = value * 2 #I multiply the value in the dictionary by 2 because it is the half-life and I want the full degradation time
            protein_sequence = "".join(aminoacid_list) #Join the amino_acid list and assign it to a variable called protein_sequence
            if time > 60: #If the variable time is bigger than 60
                time = time/60 #Divide the variable time by 60 to transform minutes to hours
                value = value/60 #Divide the variable value by 60 to transform minutes to hours
                sg.popup('PROTEIN LIFETIME', 'This protein half-life is ' + str(value) + ' hours.', 'This protein lifetime in the cell is ' + str(time) + ' hours.', 'The Uniprot information about the protein sequence is:', pSeq) #In a pop up window print the protein lifetime and the information retrieved in the Uniprot webpage using the input Uniprot accession number
            else: #If the time is less than 60, leave the time units in minutes
                sg.popup('PROTEIN LIFETIME', 'This protein half-life is ' + str(value) + ' minutes.', 'This protein lifetime in the cell is ' + str(time) + ' minutes.', 'The Uniprot information about the protein sequence is:', pSeq) #In a pop up window print the protein lifetime and the information retrieved in the Uniprot webpage using the input Uniprot accession number
        else: #If the last_aminoacid is not the same as the key, do nothing
            pass

#Code if option 2 is chosen, which is that the organism is a fungi and option 3 is chosen, which is a protein sequence
if values[2] == True and values[3] == True:
    for key,value in yeast_dict.items(): #Go through the keys and values in the yeast_dict dictionary
        if key == last_aminoacid: #If the key and the last_aminoacid are the same
            time = value * 2 #I multiply the value in the dictionary by 2 because it is the half-life and I want the full degradation time
            protein_sequence = "".join(aminoacid_list) #Join the amino_acid list and assign it to a variable called protein_sequence
            if time > 60: #If the variable time is bigger than 60
                time = time/60 #Divide the variable time by 60 to transform minutes to hours
                value = value/60 #Divide the variable value by 60 to transform minutes to hours
                sg.popup('PROTEIN LIFETIME', 'This protein half-life is ' + str(value) + ' hours.', 'This protein lifetime in the cell is ' + str(time) + ' hours.', 'The protein sequence is:' + '\n' + protein_sequence) #In a pop up window print the protein lifetime and the protein sequence as the output of the analysis
            else: #If the time is less than 60, leave the time units in minutes
                sg.popup('PROTEIN LIFETIME', 'This protein half-life is ' + str(value) + ' minutes.', 'This protein lifetime in the cell is ' + str(time) + ' minutes.', 'The protein sequence is:' + '\n' + protein_sequence) #In a pop up window print the protein lifetime and the protein sequence as the output of the analysis
        else: #If the last_aminoacid is not the same as the key, do nothing
            pass

#Code if option 2 is chosen, which is that the organism is a fungi and option 4 is chosen, which is a nucleotide sequence
if values[2] == True and values[4] == True:
    coding_dna = "".join(aminoacid_list) #Join the elements in the aminoacid_list and assign them to the variable coding_dna
    coding_dna = Seq(coding_dna) #To be able to use the coding_dna variable in biopython as a string with biological methods
    translated = coding_dna.translate(to_stop=True) #Assign the translated coding_dna information to a new variable called translated, which will contain the translated DNA sequence (the protein sequence)
    for element in translated: #Go through the elements in the variable translated
        aminoacid_list.append(element) #Append each element to the aminoacid_list
        last_aminoacid = element #Assign the last element to a variable called last_aminoacid
    for key,value in yeast_dict.items(): #Go through the keys and values in the yeast_dict dictionary
        if key == last_aminoacid: #If the key and the last_aminoacid are the same
            time = value * 2 #I multiply the value in the dictionary by 2 because it is the half-life and I want the full degradation time
            protein_sequence = translated #Assign the translated variable to the protein_sequence variable
            if time > 60: #If the variable time is bigger than 60
                time = time/60 #Divide the variable time by 60 to transform minutes to hours
                value = value/60 #Divide the variable value by 60 to transform minutes to hours
                sg.popup('PROTEIN LIFETIME', 'This protein half-life is ' + str(value) + ' hours.', 'This protein lifetime in the cell is ' + str(time) + ' hours.', 'The protein sequence is:' + '\n' + protein_sequence) #In a pop up window print the protein lifetime and the protein sequence as the output of the analysis
            else: #If the time is less than 60, leave the time units in minutes
                sg.popup('PROTEIN LIFETIME', 'This protein half-life is ' + str(value) + ' minutes.', 'This protein lifetime in the cell is ' + str(time) + ' minutes.', 'The protein sequence is:' + '\n' + protein_sequence) #In a pop up window print the protein lifetime and the protein sequence as the output of the analysis
        else: #If the last_aminoacid is not the same as the key, do nothing
            pass

#Code if option 2 is chosen, which is that the organism is a fungi and option 5 is chosen, which is a uniprot accession number
if values[2] == True and values[5] == True:
    for key,value in yeast_dict.items(): #Go through the keys and values in the yeast_dict dictionary
        if key == last_aminoacid: #If the key and the last_aminoacid are the same
            time = value * 2 #I multiply the value in the dictionary by 2 because it is the half-life and I want the full degradation time
            protein_sequence = "".join(aminoacid_list) #Join the amino_acid list and assign it to a variable called protein_sequence
            if time > 60: #If the variable time is bigger than 60
                time = time/60 #Divide the variable time by 60 to transform minutes to hours
                value = value/60 #Divide the variable value by 60 to transform minutes to hours
                sg.popup('PROTEIN LIFETIME', 'This protein half-life is ' + str(value) + ' hours.', 'This protein lifetime in the cell is ' + str(time) + ' hours.', 'The Uniprot information about the protein sequence is:', pSeq) #In a pop up window print the protein lifetime and the information retrieved in the Uniprot webpage using the input Uniprot accession number
            else: #If the time is less than 60, leave the time units in minutes
                sg.popup('PROTEIN LIFETIME', 'This protein half-life is ' + str(value) + ' minutes.', 'This protein lifetime in the cell is ' + str(time) + ' minutes.', 'The Uniprot information about the protein sequence is:', pSeq) #In a pop up window print the protein lifetime and the information retrieved in the Uniprot webpage using the input Uniprot accession number
        else: #If the last_aminoacid is not the same as the key, do nothing
            pass