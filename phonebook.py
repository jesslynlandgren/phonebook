from sys import exit
import pickle
import os

def phoneApp():
    try:
        f = open('phonebook.pickle', 'r')
        dic = pickle.load(f)
        print 'Entries Loaded'
        phonebook(dic)
    except:
        print 'No entries to load!'
        dic = {}
        phonebook(dic)

#Prompts user with option list and calls function based on choice
def phonebook(dic):
    print '\nElectronic Phone Book'
    print '====================='
    print '1. Look up an entry'
    print '2. Set an entry'
    print '3. Delete an entry'
    print '4. List all entries'
    print '5. Save entries'
    print '6. Clear ALL entries'
    print '7. Quit'

    choice = choose()

    if choice == 1:
        lookUpEntry(dic)
    elif choice == 2:
        setEntry(dic)
    elif choice == 3:
        deleteEntry(dic)
    elif choice == 4:
        listEntries(dic)
    elif choice == 5:
        saveEntries(dic)
    elif choice == 6:
        clearEntries()
    else:
        return dic
        quitPhonebook()
    return dic

#Enforces valid choices for app options 1-5
def choose():
    choice = int(raw_input('Please choose an option (1-8): \n'))
    if choice not in range(1,8):
        print "Only enter 1-8!"
        choose()
    else:
        return choice

#Ask to go back to 1-5 option menu if current option returns error
def goBack():
    back = raw_input('Go back? (y/n) ')
    if back == 'y' or back == 'n':
        if back == 'n':
            return False
        else:
            return True
    else:
        print "Only enter 'y' or 'n'!"
        goBack()

#Functions for phonebook methods
def lookUpEntry(dic):
    name = raw_input('Name: ')
    try:
        print '\nFound entry for {0}: \n work: {1}\n home: {2} cell: {3}'.format(name, dic[name]['work'],dic[name]['home'],dic[name]['cell'])
        phonebook(dic)
    except:
        print 'That person is not in the phonebook!'
        out = False
        while not out:
            out = goBack()
            if not out:
                lookUpEntry(dic)
            else:
                break
        phonebook(dic)

def setEntry(dic):
    name = raw_input('Name: ')
    print 'Enter phone numbers: '
    print '(if none, press enter)'
    work = raw_input('work: ')
    home = raw_input('home: ')
    cell = raw_input('cell: ')
    try:
        numDict = {'work': work, 'home': home, 'cell': cell}
        dic[name] = numDict
        print 'Entry stored for {0}: work: {1}  home: {2}  cell: {3}'.format(name, numDict['work'], numDict['home'], numDict['cell'])
        phonebook(dic)
    except:
        print 'Invalid entry! - try again'
        out = False
        while not out:
            out = goBack()
            if not out:
                setEntry(dic)
            else:
                break
        phonebook(dic)

def deleteEntry(dic):
    name = raw_input('Name: ')
    try:
        del dic[name]
        print 'Deleted entry for {0}\n'.format(name)
        phonebook(dic)
    except:
        print 'That person is not in the phonebook!'
        out = False
        while not out:
            out = goBack()
            if not out:
                lookUpEntry(dic)
            else:
                break
        phonebook(dic)

def listEntries(dic):
    print ''
    if len(dic) > 0:
        for key, value in sorted(dic.items(),key = lambda x: x[0]):
            print 'Found entry for {0}: work: {1}  home: {2}  cell: {3}'.format(key, value['work'], value['home'], value['cell'])
        phonebook(dic)
    else:
        print 'No entries yet!\n'
        phonebook(dic)

def saveEntries(dic):
    f = open('phonebook.pickle', 'w')
    pickle.dump(dic, f)
    f.close
    print 'Entries Saved!'
    phonebook(dic)

def clearEntries(dic):
    os.remove('phonebook.pickle')
    phoneApp()

def quitPhonebook(dic):
    f = open('phonebook.pickle', 'w')
    pickle.dump(dic, f)
    f.close
    print 'Entries Saved! - GOODBYE\n'
    exit(0)

phoneApp()
