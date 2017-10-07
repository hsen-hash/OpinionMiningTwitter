import opinionFunctions

def printResultChoice():
    userChoice = str(input ('\nDo you want to print the result on output window ?(Y/n):'))
    if(userChoice == 'Y' or userChoice=='y'):
        return True
    else:
        return False

_FolderName='Data\\Trump\\'
file = _FolderName+'Trump.txt'
_ReviewDataset=file
_PreProcessedData=_FolderName+'1.PreProcessedData.txt'
_TokenizedReviews=_FolderName+'2.TokenizedReviews.txt'
_PosTaggedReviews=_FolderName+'3.PosTaggedReviews.txt'
_Aspects=_FolderName+'4.Aspects.txt'
_Opinions=_FolderName+'5.Opinions.txt'

print("\nWELCOME TO OPINION MINING SYSTEM  ")
print("-------------------------------------------------------------")
input("Please Enter any key to continue...")
print("\n\n\n\n\n\nPREPROCESSING DATA")
omsFunctions.preProcessing(_ReviewDataset,_PreProcessedData,printResultChoice())
print("\n\n\n\n\n\nREADING REVIEW COLLECTION...")
omsFunctions.tokenizeReviews(_ReviewDataset,_TokenizedReviews,printResultChoice())
print("\n\n\n\n\n\nPART OF SPEECH TAGGING...")
omsFunctions.posTagging(_TokenizedReviews,_PosTaggedReviews,printResultChoice())
print("\nThis function will list all the nouns as aspect")
omsFunctions.aspectExtraction(_PosTaggedReviews,_Aspects,printResultChoice())
print("\n\n\n\n\n\nIDENTIFYING OPINION WORDS...")
omsFunctions.identifyOpinionWords(_PosTaggedReviews,_Aspects,_Opinions,printResultChoice())
