#!/usr/bin/python
#Filename: addressbook.py

import cPickle as c
dataname = 'personlist.data'
class Person:
    '''Representing a person.'''
    population = 0
    def __init__(self,name,email,phone):
        self.name=name
        self.email=email
        self.phone=phone
        Person.population +=1
    def __del__(self):
        '''deleting %s from the addressbook.''' % self.name
        Person.population -= 1
        print '%s is deleted from the addressbook.' % self.name

def saveAddressBook():
    f = file(dataname,'w')
    c.dump(personlist,f)#dump the personlist to a file
    print 'successfully save personlist'
    f.close()

def loadAddressBook():
    f = file(dataname)
    print 'this is before loading'
    global personlist
    personlist = c.load(f)
    ##if personlist is not defined as global, the program will delete everything after loading,
    ##don't know why
    print 'successfully load personlist'

def search(name):
    if personlist.has_key(name):
        print '%s\'s email is %s and phone is %s' %(name, personlist[name].email, personlist[name].phone)
    else:
        print '%s is not in your addressbook.' % name

def addPerson(name,email='undocumented',phone='undocumented'):
    if email=='':
        email='undocumented'
    if phone=='':
        phone='undocumanted'
    personlist[name]=Person(name,email,phone)
    print 'successfully add person %s' % name

def printBook():
    print 'we have:'
    for name, person in personlist.items():
        print '%s\'s email is %s and phone is %s' %(name, person.email, person.phone)

#p = Person('xiaoqiang','123@55.com','1234567')

loadAddressBook()
##f = file(dataname)
##personlist=c.load(f)

##addPerson('xiaoqiang')
##addPerson('xiaohong')
##addPerson('xiaoxiao')
newname = raw_input('Enter a new name:')
newemail = raw_input('and email:')
newphone = raw_input('and phone:')
addPerson(newname,newemail,newphone)
search(newname)
printBook()
saveAddressBook()
