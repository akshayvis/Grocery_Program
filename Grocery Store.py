# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 11:39:32 2019

@author: Akshay Viswanathan
"""

# Importing the libraries
from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
import random
import itertools

class Customer:
    def __init__(self,ctype):
        self._ctype = ctype
        
    def isdiscounteligible(self):
        if self.ctype == 'Senior Citizen':
            print('Eligible for 10% Discount')
        elif self.ctype == 'Staff':
            print('Eligible for 20% Discount')
        else:
            print('No discount available')
        
class Itemcategory:
    def __init__(self, category):
        self.category = category
        
class Item(Itemcategory):
    itemobj = {}       #Dictionary to store all item objects
    itemlst = []
    chkitemlst = []
    def __init__(self,category,iname,iquantity,iprice):
        super().__init__(category)
        self._iname = iname    #Protected
        self._stock = iquantity    #Protected
        self._iquantity = iquantity    #Protected
        self._iprice = iprice    #Protected
        
    #Add item function
    def additem(category,name,quantity,price):
        if (name in Item.itemobj.keys()):
            messagebox.showwarning("Warning","Item already exists!")
        else:
            Item.itemobj[name] = Item(category,name,quantity,float(price))
            messagebox.showinfo("Information","Item added successfully")
    
    #AddItemApplication
    def iaddfunc():
        additemwindow = Toplevel(mainwindow)
        additemwindow.title("Add Item") 
        additemwindow.geometry('600x500')
        
        Label(additemwindow, text='Enter Category').grid(column=0,row=0, padx=10, pady=5)
        
        categorye1 = Entry(additemwindow)
        categorye1.grid(column=2, row=0, padx=10, pady=5)
        
        Label(additemwindow, text='Enter Item Name').grid(column=0,row=2, padx=10, pady=5)
        iteme1 = Entry(additemwindow)
        iteme1.grid(column=2, row=2, padx=10, pady=5)
        
        Label(additemwindow, text='Enter Quantity').grid(column=0,row=4)
        quantitye1 = Entry(additemwindow)
        quantitye1.grid(column=2, row=4, padx=10, pady=5)
        
        Label(additemwindow, text='Enter Price per Item').grid(column=0,row=6)
        pricee1 = Entry(additemwindow)
        pricee1.grid(column=2, row=6, padx=10, pady=5)
        
        
        additembtn = Button(additemwindow, text = "Add Item", command = lambda: Item.additem(categorye1.get(),iteme1.get(),quantitye1.get(),pricee1.get()))
        additembtn.grid(column=1, row=8, padx=10, pady=5)
        
        additemwclosebtn = Button(additemwindow, text="Close", command = additemwindow.destroy)
        additemwclosebtn.grid(column=1, row=10, padx=10, pady=5)
         
#        additemwindow.mainloop()
    
    #Combobox event    
    def ItemBoxUpdate(catupdate,ibox):
        itemlst = []
        for obj in Item.itemobj.values():
            if obj.category == catupdate :
                itemlst.append(obj._iname)
        ibox['values']= itemlst
        ibox.current(0)
                
    #Values of category box
    def clstfunc():
        catlst = []
        for obj in Item.itemobj.values():
            if obj.category not in catlst:
                catlst.append(obj.category)
        return list(set(catlst))
    
    #Remove Item Function
    def removeitem(rvitem):
        temp = Item.itemobj[rvitem]._iname
        del Item.itemobj[rvitem]
        messagebox.showinfo("Information",f"{temp} is deleted successfully!")
        
            
        
    #RemoveItemApplication
    def iremovefunc():
        remitemwindow = Toplevel(mainwindow)
        remitemwindow.title("Remove Item") 
        remitemwindow.geometry('600x500')
        
        Label(remitemwindow, text='Select Category').grid(column=0,row=0, padx=10, pady=5)
        categlst = Item.clstfunc()
        remcategorybox = Combobox(remitemwindow)
        remcategorybox['values']= categlst
        remcategorybox.grid(column=2, row=0, padx=10, pady=5)
        
        
        Label(remitemwindow, text='Select Item').grid(column=0,row=2, padx=10, pady=5)
        itembox = Combobox(remitemwindow)
        itembox['values']= Item.itemlst
        itembox.grid(column=2, row=2, padx=10, pady=5)
        
        remcategorybox.bind("<<ComboboxSelected>>", lambda _ : Item.ItemBoxUpdate(remcategorybox.get(),itembox))
        
        remitembtn = Button(remitemwindow, text = "Remove Item", command = lambda: Item.removeitem(itembox.get()))
        remitembtn.grid(column=1, row=4, padx=10, pady=5)
        
        remitemwclosebtn = Button(remitemwindow, text="Close", command = remitemwindow.destroy)
        remitemwclosebtn.grid(column=1, row=10, padx=10, pady=5)
         

    
    #Apply Discount Function
    def appdisfunc(discat, disitemcat,disitem,dispercent):    
        for obj in Item.itemobj.values():
            if (obj.category == disitemcat):
                if (discat == 'Category') :
                    obj._iprice = (float(obj._iprice) - (float(obj._iprice) * (float(dispercent)/100)))
                    messagebox.showinfo("Information",f"{dispercent}% Discount applied on {discat}!")
                elif(obj._iname == disitem):
                    obj._iprice = (float(obj._iprice) - (float(obj._iprice) * (float(dispercent)/100)))
                    messagebox.showinfo("Information",f"{dispercent}% Discount applied on {disitem}!")
                else:
                    pass
            else:
                pass
        
        
    #Apply Discount Application
    def iappdisfunc():
        appdiswindow = Toplevel(mainwindow)
        appdiswindow.title("Apply Discount") 
        appdiswindow.geometry('600x500')
        
        Label(appdiswindow, text='Select Discount Type').grid(column=0,row=0, padx=10, pady=5)
        
        discategorybox = Combobox(appdiswindow)
        discategorybox['values']= ['Category','Item'] 
        discategorybox.grid(column=2, row=0, padx=10, pady=5)
        
        Label(appdiswindow, text='Select Category').grid(column=0,row=2, padx=10, pady=5)
        categlst = Item.clstfunc()
        disitemcatebox = Combobox(appdiswindow)
        disitemcatebox['values']= categlst
        disitemcatebox.grid(column=2, row=2, padx=10, pady=5)
        disitemcatebox.current(0)
        
        
        Label(appdiswindow, text='Select Item').grid(column=0,row=4, padx=10, pady=5)
        disitembox = Combobox(appdiswindow)
        disitemlst = []

        disitembox['values']= disitemlst  
        disitembox.grid(column=2, row=4, padx=10, pady=5)
        
        disitemcatebox.bind("<<ComboboxSelected>>", lambda _ : Item.ItemBoxUpdate(disitemcatebox.get(),disitembox))
        
        Label(appdiswindow, text='Enter Discount Value (%)').grid(column=0,row=6, padx=10, pady=5)
        dispricee1 = Entry(appdiswindow)
        dispricee1.grid(column=2, row=6)
        dispricee1.insert(END, '0')
        
        appdisbtn = Button(appdiswindow, text = "Apply Discount", command = lambda: Item.appdisfunc(discategorybox.get(),disitemcatebox.get(),disitembox.get(),dispricee1.get()))
        appdisbtn.grid(column=1, row=8, padx=10, pady=5)
        
        appdismwclosebtn = Button(appdiswindow, text="Close", command = appdiswindow.destroy)
        appdismwclosebtn.grid(column=1, row=10, padx=10, pady=5)

        
    #Inventory
    
    def vinventoryfunc():
        inventorywindow = Toplevel(mainwindow)
        inventorywindow.title("Inventory") 
        inventorywindow.geometry('1000x500')
    
        Label(inventorywindow, text='Category').grid(column=0,row=2, padx=10, pady=5)
        Label(inventorywindow, text='Item').grid(column=2,row=2, padx=10, pady=5)
        Label(inventorywindow, text='Stock').grid(column=4,row=2, padx=10, pady=5)
        Label(inventorywindow, text='Price').grid(column=6,row=2, padx=10, pady=5)
        for f,g in enumerate(Item.itemobj.values(),3):
            Label(inventorywindow, text=g.category).grid(column=0,row=f, padx=10, pady=5)
            Label(inventorywindow, text=g._iname).grid(column=2,row=f, padx=10, pady=5)
            Label(inventorywindow, text=g._iquantity).grid(column=4,row=f, padx=10, pady=5)
            Label(inventorywindow, text=g._iprice).grid(column=6,row=f, padx=10, pady=5)
    

        
class Billing(Item,Customer):
    bills = {}   #Dictionary to store all billing objects
    bnumlst = []
    def __init__(self,billnum,inamelst,iquantitylst,gt,ctype):    #Bill Number
         Customer.__init__(self,ctype)
         self.__billnum = billnum   #Private
         self.__inamelst = inamelst    #Private
         self.__iquantitylst = iquantitylst    #Private
         self.__gt = gt    #Private
         
    #Total sales
    def totsales():
        totsaleswin = Toplevel(mainwindow)
        totsaleswin.title('Sales')
        totsaleswin.geometry('500x600')
        Label(totsaleswin, text = 'Item Name').grid(column=0,row=0,padx=10,pady=5)
        Label(totsaleswin, text = 'Original Stock').grid(column=2,row=0,padx=10,pady=5)
        Label(totsaleswin, text = 'Stock Sold').grid(column=4,row=0,padx=10,pady=5)
        Label(totsaleswin, text = 'Stock Remaining').grid(column=6,row=0,padx=10,pady=5)
        for f,obj in enumerate(Item.itemobj.values(),1):
            Label(totsaleswin, text=obj._iname).grid(column=0,row=f, padx=10, pady=5)
            Label(totsaleswin, text=obj._stock).grid(column=2,row=f, padx=10, pady=5)
            Label(totsaleswin, text=(int(obj._stock)-int(obj._iquantity))).grid(column=4,row=f, padx=10, pady=5)
            Label(totsaleswin, text=obj._iquantity).grid(column=6,row=f, padx=10, pady=5)
        totalsales = 0
        for billobj in Billing.bills.values():
            totalsales += int(billobj.__gt)
        messagebox.showinfo("Information",f"Total Sales for the day is {totalsales}!")
            
         
    #Price Update Function
    def PriceUpdate(chkibox,chkqbox, q, chkoutwin):
        ipr = float(Item.itemobj[chkibox]._iprice) * int(chkqbox)
        Label(chkoutwin, text = ipr).grid(column = 6, row=q+3, padx=10, pady=5)
        

    #Bill Generator Function
        
    def spldisfunc(bitemlst,bquantitylst,noi):
        
        def genbillfunc(bitemlst,bquantitylst,noi,discountfactor):
            
            
            bnum = random.randint(1,10000)
            while(bnum in Billing.bnumlst):
                bnum = random.randint(1,1000000)
            Billing.bnumlst.append(bnum)
            billwindow = Toplevel(mainwindow)
            billwindow.title("Bill")
            Label(billwindow, text='Bill Number').grid(column=0, row=0, padx = 10, pady=5)
            Label(billwindow, text=bnum).grid(column=1, row=0, padx = 10, pady=5)
            Label(billwindow, text='Thank You. Visit Again.').grid(column=4, row=0, padx = 10, pady=5)
            Label(billwindow, text='Item Name').grid(column=0,row=1, padx=10, pady=5)
            Label(billwindow, text='Quantity').grid(column=2,row=1, padx=10, pady=5)
            Label(billwindow, text='Item Price').grid(column=4,row=1, padx=10, pady=5)
            bpricelst = []
            for j in range(noi):
                bpricelst.append((float(Item.itemobj[bitemlst[j]]._iprice)) * (int (bquantitylst[j])))
                
            grandtot = sum(bpricelst)
            flag = 0
                
            if(discountfactor == 'Senior Citizen'):
                grandtot -= (grandtot * 0.1)
                flag = 1
            elif(discountfactor == 'Staff'):
                grandtot -= (grandtot * 0.2)
                flag = 2
            
            for num in range(noi):
                Label(billwindow, text= bitemlst[num]).grid(column=0,row=num+2, padx=10, pady=5)
                Label(billwindow, text= bquantitylst[num]).grid(column=2,row=num+2, padx=10, pady=5)
                Label(billwindow, text= bpricelst[num]).grid(column=4,row=num+2, padx=10, pady=5)
                
                
            Label(billwindow, text='Grand Total').grid(column=3,row=noi+3, padx=10, pady=5)
            Label(billwindow, text=grandtot).grid(column=5,row=noi+3, padx=10, pady=5)
            
            Billing.bills[bnum] = Billing(bnum,bitemlst,bquantitylst,grandtot,discountfactor)
            
            for (it,qu) in zip(bitemlst,bquantitylst):
                Item.itemobj[it]._iquantity = int(Item.itemobj[it]._iquantity) - int(qu)

            
        ctypewindow = Toplevel(mainwindow)
        ctypewindow.title("Special Discount")
        Label(ctypewindow, text="Avail Special Discount?").grid(column=0,row=0,padx=10,pady=5)
        distypebox = Combobox(ctypewindow)
        distypebox['values'] = ['None', 'Staff', 'Senior Citizen']
        distypebox.grid(column=6, row=0, padx=10, pady=5)
        distypebox.current(0)
        
        disconfirmbtn = Button(ctypewindow, text="Confirm", command = lambda : genbillfunc(bitemlst,bquantitylst,noi,distypebox.get()))
        disconfirmbtn.grid(column = 3, row = 2, padx = 10, pady = 5)  
        
        
    
    #CheckoutApplication
    def checkoutfunc():
        checkoutwindow = Toplevel(mainwindow)
        checkoutwindow.title("Checkout") 
        checkoutwindow.geometry('1000x500')
        
        Label(checkoutwindow, text='Select Register').grid(column=1,row=0, padx=10, pady=5)
        
        registerbox = Combobox(checkoutwindow)
        registerbox['values']= [i for i in range(1,nreg+1)] 
        registerbox.grid(column=2, row=0, padx=10, pady=5)
        
        Label(checkoutwindow, text='Enter the number of items').grid(column=0,row=1,padx=10, pady=5)
        noitemse1 = Entry(checkoutwindow)
        noitemse1.insert(END, '0')
        noitemse1.grid(column=1, row=1, padx=10, pady=5)
        
        def chkadditems(n):
            Label(checkoutwindow, text='Select Item Category').grid(column=0,row=2, padx=10, pady=5)
            Label(checkoutwindow, text='Select Item').grid(column=2,row=2, padx=10, pady=5)
            Label(checkoutwindow, text='Select Quantity').grid(column=4,row=2, padx=10, pady=5)
            Label(checkoutwindow, text='Price').grid(column=6,row=2, padx=10, pady=5)
            chkitemcatbox = []            
            chkitembox = []
            chkquantitybox = []
            chkprice = []
            
            
            for i in range(n):
                
                chkitemcatbox.append(Combobox(checkoutwindow))
                chkitemcatbox[i]['values']= list(set([x.category for x in Item.itemobj.values()])) 
                chkitemcatbox[i].grid(column=0, row=i+3, padx=10, pady=5)
                chkitemcatbox[i].current(0)
                
                chkitembox.append(Combobox(checkoutwindow))
                chkitembox[i]['values']= Item.chkitemlst
                chkitembox[i].grid(column=2, row=i+3, padx=10, pady=5)
                chkitemcatbox[i].bind("<<ComboboxSelected>>", lambda e , catindex=i : Item.ItemBoxUpdate(chkitemcatbox[catindex].get(),chkitembox[catindex]))
                
                chkquantitybox.append(Combobox(checkoutwindow))
                chkquantitybox[i]['values']= [k for k in range(1,21)] 
                chkquantitybox[i].grid(column=4, row=i+3, padx=10, pady=5)
                chkquantitybox[i].current(0)
            
                #add price box
                chkprice.append(Label(checkoutwindow).grid(column = 6, row=i+3, padx=10, pady=5))

                chkquantitybox[i].bind("<<ComboboxSelected>>", lambda e, priceindex = i : Billing.PriceUpdate(chkitembox[priceindex].get(),chkquantitybox[priceindex].get(),priceindex,checkoutwindow))
                
    
            genbillbtn = Button(checkoutwindow, text = "Generate Bill", command = lambda: Billing.spldisfunc([chkitembox[bnindex].get() for bnindex in range(n)],[chkquantitybox[bqindex].get() for bqindex in range(n)],n))
            genbillbtn.grid(column=6, row=0, padx=10, pady=5)
            
  
        #add item btn
        additemsbtn = Button(checkoutwindow, text="Add items", command = lambda: chkadditems(int(noitemse1.get())))
        additemsbtn.grid(column=2, row=1,padx=10, pady=5)  
           
#Driver Function
nreg = int(input('Enter the number of registers: '))

#MainApplication
mainwindow = Tk() 
mainwindow.title("Welcome") 
mainwindow.geometry('600x500')

addbtn = Button(mainwindow, text = "Add Item", command = lambda: Item.iaddfunc())
addbtn.grid(column=0, row=1, padx=10, pady=5)

rembtn = Button(mainwindow, text="Remove Item", command = lambda: Item.iremovefunc())
rembtn.grid(column=2, row=1, padx=10, pady=5)

appdisbtn = Button(mainwindow, text="Apply Discount", command = lambda: Item.iappdisfunc()) 
appdisbtn.grid(column=1, row=2, padx=10, pady=5)


checkoutbtn = Button(mainwindow, text="Checkout", command = lambda: Billing.checkoutfunc()) 
checkoutbtn.grid(column=1, row=3, padx=10, pady=5)

inventorybtn = Button(mainwindow, text="View Inventory", command = lambda: Item.vinventoryfunc())
inventorybtn.grid(column=1, row=4, padx=10, pady=5)

totsalesbtn = Button(mainwindow, text="Total Sales amount", command = lambda: Billing.totsales())
totsalesbtn.grid(column=1, row=5, padx=10, pady=5)

mwclosebtn = Button(mainwindow, text="Close", command = mainwindow.destroy)
mwclosebtn.grid(column=1, row=6, padx=10, pady=5)

mainwindow.mainloop()