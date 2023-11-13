#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_pet_labels.py
#                                                                             
# PROGRAMMER: Yuzana Win
# DATE CREATED: 11-05-2023                              
# REVISED DATE: 
# PURPOSE: Create the function get_pet_labels that creates the pet labels from 
#          the image's filename. This function inputs: 
#           - The Image Folder as image_dir within get_pet_labels function and 
#             as in_arg.dir for the function call within the main function. 
#          This function creates and returns the results dictionary as results_dic
#          within get_pet_labels function and as results within main. 
#          The results_dic dictionary has a 'key' that's the image filename and
#          a 'value' that's a list. This list will contain the following item
#          at index 0 : pet image label (string).
#
##
# Imports python modules
from os import listdir

# TODO 2: Define get_pet_labels function below please be certain to replace None
#       in the return statement with results_dic dictionary that you create 
#       with this function
# 
def get_pet_labels(image_dir):
    """
    Creates a dictionary of pet labels (results_dic) based upon the filenames 
    of the image files. These pet image labels are used to check the accuracy 
    of the labels that are returned by the classifier function, since the 
    filenames of the images contain the true identity of the pet in the image.
    Be sure to format the pet labels so that they are in all lower case letters
    and with leading and trailing whitespace characters stripped from them.
    (ex. filename = 'Boston_terrier_02259.jpg' Pet label = 'boston terrier')
    Parameters:
     image_dir - The (full) path to the folder of images that are to be
                 classified by the classifier function (string)
    Returns:
      results_dic - Dictionary with 'key' as image filename and 'value' as a 
      List. The list contains for following item:
         index 0 = pet image label (string)
    """

    filename_list = listdir(image_dir)
    results_dic = dict()

    for idx in range(0, len(filename_list), 1):

        #If file is already in result dictionary "results_dic"
        if filename_list[idx] in results_dic:
            print("** Warning: Key=", filename_list[idx], "already exists in results_dic with value =", 
               results_dic[filename_list[idx]])
        #If file is not in result dictionary "results_dic" yet
        else: 
            #Checking if the file name starts with '.'
            if filename_list[idx][0] != ".":
                #format into lowercase
                raw_petImg = filename_list[idx].lower()
       
                #split the raw_petName into list
                raw_petImg = raw_petImg.split("_")
        
                #initializing petName as empty string
                petName = ""

                #iterate through the word list and if alphabet, concatenate into petName 
                for word in raw_petImg:
                    if word.isalpha():
                        petName = petName + word + " "

                #remove leading and ending white spaces
                petName = petName.strip()

                #adding the petName list into the result dictionary
                results_dic[filename_list[idx]] = [petName]
      

        
    # Replace None with the results_dic dictionary that you created with this
    return results_dic
