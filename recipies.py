#Logan Scholfield
#Recipes code
#December 3, 2019
#This code lets the user save recipies, look at them, and delete them.




#constants used to call difforent functions based on what the user wants to do
EDIT = 'e'
LOOK = 'l'
DELETE = 'd'
ADD = 'a'

#import function used to delete files
import os

#Main function
def main():
    print('what would you like to do?')
    command = ''
    #while loop makes sure the user 
    while command != 'l'and command != 'e' and command != 'a' and command != 'd':
        print('to edit a file(e) to look at recipies(l) to add a new recipe(a) to delete all your recipies(d)')
        command = input('What would you like: ')
        if command != 'l'and command != 'e' and command != 'a' and command != 'd':
            print('nothing was choosen')
        else:
            one = 1
    #calls the function the user wants to go to    
    if command == EDIT:
        edit()
    elif command == LOOK:
        look()
    elif command == ADD:
        add()
    elif command == DELETE:
        delete()
    else:
        print('more options expected soon')




#edit a file function
def edit():
    
        #open recipe file and temporary file 
        file_recipies = open('recipies.txt', 'r')
        line = file_recipies.readline()
        file_temporary = open('newfile.txt', 'w')

        #looks through the titles of the code and asks the user if they want to keep that recipe  
        while line != '':
            if line.startswith('t'):
                print('Do you want to remove this recipe? (remove) means yes')
                print(line[1:])
                remove = input('do you want to remove this recipe?: ')
                #if use wants to remove it, the code transfers no lines to the temporary file
                if remove == 'remove':
                    line = file_recipies.readline()
                    line = file_recipies.readline()
                else:
                    #if the user wants to keep the recipe the code transwers the three lines of that recipe into the temporary file
                    file_temporary.write(line)
                    line = file_recipies.readline()
                    another_line = 'true'
                    while another_line == 'true':
                        if line.startswith('i'):
                            file_temporary.write(line)
                            another_line = 'false'
                        else:
                            line = file_recipies.readline()
                    line = file_recipies.readline()
                    another_line = 'true'
                    while another_line == 'true':
                        if line.startswith('h'):
                            file_temporary.write(line)
                            another_line = 'false'
                        else:
                            line = file_recipies.readline()
            else:
                line = file_recipies.readline()
        #closes both files     
        file_recipies.close()
        file_temporary.close()
        os.remove('recipies.txt')        
        #deletesthe recipies file
        file_temporary = open('newfile.txt', 'r')
        file_recipies = open('recipies.txt', 'w')
      #opens the files back up
       
        #transfers contents of temporary file into recipie file
        line = file_temporary.readline()
        while line:
            file_recipies.write(line)
            line = file_temporary.readline()
        file_recipies.close()
        file_temporary.close()
        #closes the files and provides the contents that have been saved 



        
        print('Here are you remaining reipies')
        print('------------------------------')
        file_recipies = open('recipies.txt', 'r')
        line = file_recipies.readline()
        count = 1
        #prints the remaining recipies out while numbering them
        while line:
            if line.startswith('t'):
                print(count,')',line[1:])
                count += 1
            else:
                one = 1
            
            line = file_recipies.readline()
        print('------------------------------')
        file_recipies.close()
        file_temporary.close()
        #deletes the temporary file so that it can be used to edit more files
        os.remove('newfile.txt')
        more = input('do you want to do more? (yes) means yes: ')
        if more == 'yes':
            main()
        else:
            print('Ok, have a nice day')
        
        
   
    

        
#function that lets the user look at recipies
#Most of this function is putting the information in a better format
def look():
    try:
        infile = open('recipies.txt', 'r')
        #looks to see how many lines are in the file for later use
        amount = 0
        line = infile.readline()
        while line != '':
            amount += 1
            line = infile.readline()
        infile.close()



        infile = open('recipies.txt', 'r')
        dic = { }
        count = 0
        #puts the file lines into a dictionary using the thing being made as the
        #key and the ingrediants and instructions as the values
        while amount != count:
            line = infile.readline()
            if line.startswith('t'):
                #these few lines change the set up of the way the information on the line is presented.
                #most importants the one letter at the start of each line letting the code known what type of information the line it and what to do with it.
                title = line
                title = title.rstrip()
                title = title[1:]
                line = infile.readline()
                if line.startswith('i'):
                    for i in line:
                        if i.isalpha() or i.isdigit():
                            one = 1
                        else:
                            
                            line = line.replace(i,' ')
                    
                    ing = line
                    ing = ing.rstrip()
                    ing = ing[1:]
                    
                    line = infile.readline()
                    if line.startswith('h'):
                        how = line
                        how = how.rstrip()
                        how = how[1:]
                    else:
                        one = 1
                else:
                    one = 1
            else:
                one = 1   
            dic[title] = ing, how
            count += 1
        infile.close()
        

        #prints the recipie titles to allow the user to choose one to
        #see the details
        print('Here are your recipies')
        print('-----------------------')
        counter = 1
        for key in dic:
            print(counter,')', key)
            counter += 1
        print('-----------------------')
        not_a_recipe = 'true'
        while not_a_recipe == 'true':
            recipe = input('which recipe do you want to look at: ')
            if recipe in dic.keys():
                not_a_recipe = 'false'
                        
             #prints the chosen recipe followed by its concents       
                print(' ')
                
                print(recipe.upper())
                
                #used to give names to the lines in the dictionary for later use
                for i in dic[recipe]:
                    how = i
                ing = ' '
                for i in dic[recipe]:
                    if ing == ' ':
                        ing = i
                    else:
                        one = 1
                ing = ing.strip()
                ing = ing.split()
                count = 1
                #prints the ingrediants and instructions to the choosen recipe
                for i in ing:
                    print(count,')',i)
                    count += 1
                
                print(' ')
                print('Instructions:')
                print('\t',how)
                #asks the user if they want to look at another recipe
                another_recipe = input('do you want to look at another recipe?(yes) means yes: ')
                if another_recipe == 'yes':
                    look()
                else:
                    print(' ')
                    
            else:
                print('that is not a recipe')


            more = input('do you want to do more? (yes) means yes: ')
            if more == 'yes':
                main()
            else:
                print('Ok, have a nice day')
    #allows use to go back to the main() function
    except:
        print('you have no recipies in your recipe book')
        more = input('do you want to do more? (yes) means yes: ')
        if more == 'yes':
            main()
        else:
            print('Ok, have a nice day')
   
       

    

#function lets user add new recipies to the file
def add():
    more_recipies = 'yes'
    while more_recipies == 'yes':
        

    
        title = input('What is the recipe for? ')   
        ing = 'D'
        ingr = [ ]
        #while loop to let user add multiple items to the recipe
        while ing != '':
            
            ing = input('what is a needed ingrediant(ENTER to stop adding things): ')
            if ing.isalpha() == True:
                ingr.append(ing)
            else:
                ing = ''
        ingr = str(ingr)
        how = input('how do you make it? ')


        #writes the inputed information onto the file the "t" or "i" or "h" is used for the code while in the look and edit functions
        outfile = open('recipies.txt' ,'a')
        outfile.write('t' + title + '\n')
        outfile.write('i' + ingr + '\n')
        outfile.write('h' + how + '\n')
        outfile.close()
        print("To add another recipe type 'yes'")
        more_recipies = input('do you want to add another recipe?: ')
        
    more = input('do you want to do more? (yes) means yes: ')
    if more == 'yes':
        main()
    else:
        print('Ok, have a nice day')
    
    


#delete the file function
#this function was mostly used in the creation of this code, but it is left in incase the user wants to refresh all there recipies.
def delete():
    delete = input('are you sure you want to delete all recipies?(yes) for yes: ')
    if delete == 'yes':
        os.remove('recipies.txt')
        print('all recipies have been deleted!')
    else:
        print('good call')


    more = input('do you want to do more? (yes) means yes: ')
    if more == 'yes':
        main()
    else:
        print('Ok, have a nice day')








#at the end of each function the user is given the same question, letting them go back to the main() function if they want to
            #this helps the user not have to restart the code each time if they are trying to do multiple things while on the code.
#calls main function
main()
