# -*- coding: utf-8 -*-
from Applicant import Applicant
from HashTable import HashTable
from Status import Status

class ClubHouse :
    def __init__(self):
        print("Hi")
        
    def initializeHash(self): 
        self.ApplicationRecords=HashTable()
    
    def insertAppDetails(self, name, phone, memRef, status):
             p1 = Applicant(name, phone,memRef,status)
             self.ApplicationRecords.put(p1.name,p1)
             
    def updateAppDetails(self, name, phone, memRef, status):
             p1 = Applicant(name, phone,memRef,status)
             self.ApplicationRecords.put(p1.name,p1)
                     
    def memRef(self, memRefId): 
        
        res = [] 
        for val in self.ApplicationRecords.values(): 
            if val.memberReferenceId== memRefId : 
                res.append(val)
        print(res)    
        return res
        
    def appStatus(self):
        res = [] 
        
            
        return res
    
    def destroyHash(self,ApplicationRecords): 
        self.ApplicationRecords
        
        
def main():
    c=ClubHouse()
    c.initializeHash()
    c.insertAppDetails("Bhavesh", "9619655828","ref1","Status.Applied")
    c.insertAppDetails("Bhavesh1", "9619655828","ref1","Status.Applied")
    c.insertAppDetails("Bhavesh2", "9619655828","ref1","Status.Applied")
    c.insertAppDetails("Bhavesh3", "9619655828","ref1","Status.Applied")
    c.insertAppDetails("Bhavesh4", "9619655828","ref2","Status.Applied")
    c.insertAppDetails("Bhavesh5", "9619655828","ref2","Status.Applied")
    print("hello world!")
    c.memRef("ref2")
    c.updateAppDetails("Bhavesh5", "9619655829","ref2","Status.Applied")
    c.memRef("ref2")
    
if __name__ == "__main__":
    main()   
    
         