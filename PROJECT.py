# -*- coding: utf-8 -*-
"""
Created on Sat Feb 27 18:41:40 2016

@author: MEET SHAH
"""

####ANALYSIS OF EVAPORATIVE LOSSES OF GASOLINE DURING ITS HANDLING AND TRANSPORTATION####
'''
Evaporative emissions from the transportation and marketing of petroleum liquids may be
considered, by storage equipment and mode of transportation used, in four categories:
1. Rail tank cars, tank trucks, and marine vessels: loading, transit, and ballasting losses.
2. Service stations: bulk fuel drop losses and underground tank breathing losses.
3. Motor vehicle tanks: refueling losses.
4. Large storage tanks: breathing, working, and standing storage losses.
'''
d=0.75 ##density of gasoline in kg/L
a=0.4536 ##Conversion factor for pound(lb) to kg
b=3.785 ##conversion factor for gal to litres
Pe=int(input('HOW MUCH PETROL TO BE FUELLED IN YOUR CAR, SIR (litres) ='))##petrol to be filled in his car
Stock=int(input('STOCK ORDERED BY BHARAT PETROLEUM (litres) = ')) ##Owner asks for This amount of stock in litres
'''
OBJECTIVE: Consider that user asks for certain amount of fuel to be filled in his car say 1L 
but in actual he gets some volume less say 20mL. This less volume depends on losses suffered to petrol
owner during transportation and handling and he decdides amount of petrol deduction per litre to compensate
for his loss and in order to achieve expected profit
TOTAL LOSS= LOADING LOSS + BREATHING LOSS + UNLOADING LOSS + EVAPORATIVE EMISSIONS
''' 
####1.ANALYSIS OF LOADING LOSSES###
'''
Emissions from loading petroleum liquid can be estimated (with a probable error of ±30 percent)4
using the following expression:
where:
LL = loading loss, pounds per 1000 gallons (lb/103 gal) of liquid loaded
S = a saturation factor (see Table 5.2-1)
P = true vapor pressure of liquid loaded, pounds per square inch absolute (psia)
(see Section 7.1, "Organic Liquid Storage Tanks")
M = molecular weight of vapors, pounds per pound-mole (lb/lb-mole) (see Section 7.1, "Organic
Liquid Storage Tanks")
T = temperature of bulk liquid loaded, °R (°F + 460)
'''
##HUMAN LOSSES - CONTROLLABLE##
Vol1=0.0095*Stock ## DIP METHOD CANNOT NOTICE ERROR OF ABOUT 100L SO REFINERS GIVES 0.95%less as per intake ordered by owner
##THERMODYNAMIC LOSSES- UNCONTROLLABLE
S=1;
M=66;
eff=94;
P=6.6;
t=int(input('PRODUCT GASOLINE OUTLET TEMPERATURE IN FARENHEIT=')) ###(PRODUCT TEMPERATURE WHICH IS LOADED IN FARENHEIT)
T=t+460
LL=10*(12.46*S*P*M*(1-eff/100.0))/T ## lb/1000gal
L=LL*a/(1000*b) ## Loss in kg/l
Ma=L*Stock  ##MASS LOSS ACCORINGLY AS ORDER GIVEN BY PETROL OWNER
Vol2=Ma/d;
print 'CONTROLLABLE LOSS-SET BY REFINERIES = ',Vol1;
'''S = saturation factor (see Table 5.2-1) - 1.00
P = true vapor pressure of gasoline = 6.6 psia
M = molecular weight of gasoline vapors = 66
T = temperature of gasoline = 540°R
eff = overall reduction efficiency (95 percent control x 98.7 percent collection) = 94 percent
Vapor recovery efficiency is 95 percent
Vapor collection efficiency is 98.7 percent (NSPS-level annual leak test
'''
print 'LOADING LOSS AT REFINERY = ', Vol2;
Vol=Vol1+Vol2;
Cost=65 ##Cost per litre of petrol in RS
Err= Vol*1000/Stock;
Terr=Err*Pe/1000; ## less volume offered to consumer per liter
R=Cost*Terr
Amt=Cost*Pe
Per=R*100/Amt
print 'VOlUME lOSS FOR CONSUMER (in ml) per liter =' ,Err;
print 'TOTAL VOLUME LOSS FOR PETROL OWNER= ',Vol;
print 'TOTAL VOLUME LOSS FOR CONSUMER (in liters) = ' ,Terr;
print 'LOSS TO CONSUMER (in RS)=',R;
print 'ACTUAL AMT PAID BY CONSUMER (in RS)= ',Amt;
print 'PERCENT LOSS IN AMT = ',Per;
print '!!!!!!MORE LOSSES ARE YET TO BE ACCOUNTED FOR!!!!!!!'

