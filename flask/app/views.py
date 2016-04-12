from app import app


@app.route('/')
@app.route('/index')
def index():
    d=0.75 ##density of gasoline in kg/L
    a=0.4536 ##Conversion factor for pound(lb) to kg
    b=3.785 ##conversion factor for gal to litres
    Pe=int(input('HOW MUCH PETROL TO BE FUELLED IN YOUR CAR, SIR (litres) ='))##petrol to be filled in his car
    Stock=int(input('STOCK ORDERED BY BHARAT PETROLEUM (litres) = ')) ##Owner asks for This amount of stock in litres
   
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
    
    return "DEVELOPMENT OF WEBPAGE IS STILL REMAINING!!! Hold on"
