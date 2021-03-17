'''This program uses OS module to make changes in the files and folders.
Basic working of the program is to take folder path,.txt file whos first word 
we dont want to capitalize and all the images renamed to numbers from 1 to n .
Author - Vaibhav Rawat
Purpose - Python Problem solving'''
import os

def soldier(a,b,c):
    os.chdir(a)
    
    for i in os.listdir():
        if i.endswith('.txt') and i!=b:
            os.rename(i,i.capitalize()) 
    
    for x,y in enumerate(os.listdir()):
        if y.endswith(c):
            os.rename(y,str(x)+c)

    
if __name__=='__main__':
    path=input('Enter the drive where you want to go\n')
    if os.path.exists(path):
        reserve=input('Enter file name which you dont want to change\n')
        form=input('Who\'s file format you want to change?\n')
        soldier(path,reserve,form)
    else:
        print('This path dosent exist')
