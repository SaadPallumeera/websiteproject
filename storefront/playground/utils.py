import re

import matplotlib.pyplot as plt
import base64
from io import BytesIO
import math

def get_graph():
    buffer = BytesIO()
    plt.savefig(buffer,format = 'png',dpi = 200)
    buffer.seek(0)
    image_png = buffer.getvalue()
    graph = base64.b64encode(image_png)
    graph = graph.decode('utf-8')
    buffer.close()
    return (graph)

def get_plot(Ph,x):
    y=str(x)
    a = 0
    l1=[]
    while(a<=14):
        l1.append(a)
        a+=1
    Ph = float(Ph)
    l2 = [ Ph*i for i in l1]
    plt.switch_backend('AGG')
    plt.title(y)
    plt.plot(l1,l2)
    plt.tight_layout()
    graph = get_graph()
    return (graph)

def titrationS(Macid,volAcid,Mbase):
    molAcid = Macid * volAcid/1000
    y = molAcid/Mbase * 2 *1000
    l1=[]
    l2 = []
    x=0
    while (x<y+.0001):
        l1.append(x)
        x+= y/1000
    x=0
    while (x<len(l1)):
        if(l1[x]<((molAcid/Mbase*1000))):
            H = (molAcid - (Mbase*l1[x]/1000))/(l1[x]/1000+volAcid/1000)
            Ph = -1* math.log(H,10)
            l2.append(Ph)
        else:
            OH = (-1*molAcid + (Mbase*l1[x]/1000))/(l1[x]/1000+volAcid/1000)
            Ph = 14 + 1*math.log(OH,10)
            l2.append(Ph)
        x+=1
        
    l2[int(len(l2)/2)] = 7
    plt.cla()
    plt.plot(l1,l2)

    plt.annotate("Equivalance point\nPH: " + str(l2[int(len(l2)/2)]) ,(l1[int(len(l1)/2)],l2[int(len(l2)/2)]),textcoords="offset points",xytext=(10,0))
    plt.title("Strong base vs Strong Acid")
    plt.xlabel("ml of base added")
    plt.ylabel("PH")
    plt.xlim(left = 0, right = l1[len(l1)-1])
    plt.scatter(l1[int(len(l1)/2)],l2[int(len(l2)/2)])
    plt.grid() 
    graph = get_graph()
    return(graph)

def titrationW(Pka,Macid,volAcid,Mbase):
    molAcid = Macid * volAcid/1000
    y = molAcid/Mbase * 2 *1000
    l1=[]
    l2 = []
    x=0
    while (x<y+.0001):
        l1.append(x)
        x+=.01
    x=0
    while (x<len(l1)):
        if(l1[x]<(molAcid/Mbase*1000)):
            H = (molAcid - (Mbase*l1[x]/1000))/(l1[x]/1000+volAcid/1000)
            Ph = -1*math.log(H,10)
            l2.append(Ph)
        
        if(l1[x]>=(molAcid/Mbase*1000)):
            OH = (-1*molAcid + (Mbase*l1[x]/1000))/(l1[x]/1000+volAcid/1000)
            Ph = 14 + 1*math.log(OH,10)
            l2.append(Ph)
        x+=1
    O = (.1**(14-Pka))**.5
    l2[int(len(l2)/2)] = 14-O
    plt.cla()
    plt.plot(l1,l2)
    plt.title("Strong base vs Weak Acid")
    plt.xlabel("ml of base added")
    plt.ylabel("PH")
    plt.grid()
    plt.tight_layout()
    plt.axes.Axes.set_facecolor(color="blue")
    plt.scatter(l1[int(len(l1)/2)],l2[int(len(l2)/2)])



class Chemistry():

    Symbols = ["H","He",
            "Li","Be","B","C","N","O","F","Ne",
            "Na","Mg","Al","Si","P","S","Cl","Ar",
            "K","Ca","Sc","Ti","V","Cr","Mn","Fe","Co","Ni","Cu","Zn","Ga","Ge","As","Se","Br","Kr",
            "Rb","Sr","Y","Zr","Nb","Mo","Tc","Ru","Rh","Pd","Ag","Cd","In","Sn","Sb","Te","I","Xe",
            "Cs","Ba","La","Ce","Pr","Nd","Pm","Sm","Eu","Gd","Tb","Dy","Ho","Er","Tm","Yb","Lu"
            ,"Hf","Ta","W","Re","Os","Ir","Pt","Au","Hg","Ti","Pb","Bi","Po","At","Rn",
            "Fr","Ra","Ac","Th","Pa","U","Np","Pu","Am","Cm","Bk","Cf","Es","Fm","Md","No","Lr",
            "Rf","Db","Sg","Bh","Hs","Mt","Ds","Rg","Cn","Nh","Fl","Mc","Lv","Ts","Og"]
    
    Names = ["Hydrogen","Helium",
             "Lithium","Beryllium","Boron","Carbon","Nitrogen","Oxygen","Fluorine","Neon",
             "Sodium","Magnesium","Aluminum","Silicon","Phosphorus","Sulfur","Chlorine","Argon","Potassium","Calcium","Scandium","Titanium","Vanadium","Chromium","Manganese","Iron","Cobalt","Nickel","Copper","Zinc","Gallium","Germanium","Arsenic","Selenium","Bromine","Krypton",
             "Rubidium","Strontium","Yttrium","Zirconium","Niobium","Molybdenum","Technetium","Ruthenium","Rhodium","Palladium","Silver","Cadmium","Indium","Tin","Antimony","Tellurium","Iodine","Xenon",
             "Cesium","Barium","Lanthanum","Cerium","Praseodymium","Neodymium","Promethium","Samarium","Europium","Gadolinium","Terbium","Dysprosium","Holmium","Erbium","Thulium","Ytterbium","Lutetium",
             "Hafnium","Tantalum","Tungsten","Rhenium","Osmium","Iridium","Platinum","Gold","Mercury","Thallium","Lead","Bismuth","Polonium","Astatine","Radon","Francium","Radium",
             "Actinium","Thorium","Protactinium","Uranium","Neptunium","Plutonium","Americium","Curium","Berkelium","Californium","Einsteinium","Fermium","Mendelevium","Nobelium","Lawrencium",
             "Rutherfordium","Dubnium","Seaborgium","Bohrium","Hassium","Meitnerium","Ununnilium","Unununium","Ununbium","Ununtrium","Ununquadium","Ununpentium","Ununhexium","Ununseptium","Ununoctium"]
    
    Amu = [1.00794,4.002602,
           6.941,9.01218,10.811,12.011,14.00674,15.9994,18.998403,20.1797,22.989768,24.305,26.981539,28.0855,30.973762,32.066,35.4527,39.948,39.0983,40.078,44.95591,47.88,50.9415,51.9961,54.93805,55.847,58.9332,58.6934,63.546,65.39,69.723,72.61,74.92159,78.96,79.904,83.8,85.4678,87.62,88.90585,91.224,92.90638,95.94,97.9072,101.07,102.9055,106.42,107.8682,112.411,114.818,118.71,121.76,127.6,126.90447,131.29,132.90543,137.327,138.9055,140.115,140.90765,144.24,144.9127,150.36,151.965,157.25,158.92534,162.5,164.93032,167.26,168.93421,173.04,174.967,178.49,180.9479,183.84,186.207,190.23,192.22,195.08,196.96654,200.59,204.3833,207.2,208.98037,208.9824,209.9871,222.0176,223.0197,226.0254,227.0278,232.0381,231.03588,238.0289,237.048,244.0642,243.0614,247.0703,247.0703,251.0796,252.083,257.0951,258.1,259.1009,262.11, [261], [262], [266], [264], [269], [268], [269], [272], [277], None, [289], None, None, None, None]

    def getAmu(element):
        if (len(element)<=2):
            x = Chemistry.Symbols.index(element)
            return(Chemistry.Amu[x])
        if (len(element)>2):
            x = Chemistry.Names.index(element)
            return(Chemistry.Amu[x])
        
    def molarMass():
        print("Write element symbol then quantity. to Stop enter stop ")
        
        x = ""
        mm = 0
        while (x!="stop"):
            sym = input("input symbol: ")
            if (sym == "stop"):
                break
            q = input ("input [quantity]: ")
            q = int(q)
            mm+= q*Chemistry.getAmu(sym)
        print(mm)
        
    def mm(mol):
        mol1 = mol
        mol = list(mol)
        element = list()
        quantity = list()
        seperate = list()
       
        x = 0
        a = -1
        while (x < len(mol)):
            if (mol[x].isupper()):
                element.append(mol[x])
                a+=1
            if(mol[x].islower()):
                element[a]+=mol[x]
            x+=1
        y = 0
        z=-1

        l1 = re.sub( r"([A-Z])", r" \1", mol1).split()
        s1 = list();
        
        for i in l1:
            if(i[len(i)-1:len(i)].isnumeric()):
                temp = ([int(s) for s in re.findall(r'\d+', i)])
                s1.append(temp[0])
            else:
                s1.append(1)
        ans = 0
        d=0
        while (d<len(element)):
            ans+= s1[d]*Chemistry.getAmu(element[d])
            d+=1
        return(ans)

    def percentMass(mol):
        mol1 = mol
        mol = list(mol)
        element = list()
        quantity = list()
        seperate = list()
       
        x = 0
        a = -1
        while (x < len(mol)):
            if (mol[x].isupper()):
                element.append(mol[x])
                a+=1
            if(mol[x].islower()):
                element[a]+=mol[x]
            x+=1
        y = 0
        z=-1

        l1 = re.sub( r"([A-Z])", r" \1", mol1).split()
        s1 = list();
        
        for i in l1:
            if(i[len(i)-1:len(i)].isnumeric()):
                temp = ([int(s) for s in re.findall(r'\d+', i)])
                s1.append(temp[0])
            else:
                s1.append(1)
        ans = 0
        d=0
        while (d<len(element)):
            ans+= s1[d]*Chemistry.getAmu(element[d])
            d+=1
        count = 0
        answer = ""
        while (count<len(element)):
            add = ""
            add += str(element[count])
            add += str(s1[count])
            num = Chemistry.mm(add)
            percent = round(num/ans * 100,4)
            answer += "Percent mass composition of " + Chemistry.Names[Chemistry.Symbols.index(element[count])] + " is " + str(percent) + "%. \n"
            count+=1
        return(answer) 
    


    




