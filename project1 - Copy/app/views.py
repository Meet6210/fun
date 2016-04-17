from flask import render_template, flash, redirect
from app import app
from forms import LoginForm


@app.route('/index')
def index():
    
    return render_template('index.html')

@app.route('/')
@app.route('/login', methods=['GET', 'POST'])

def login():
    form = LoginForm()
    if form.validate_on_submit():
        Stock=float(form.Stock.data)
        Pe=float(form.Pe.data)
        t=float(form.t.data)
        

        d=0.75 ##density of gasoline in kg/L
        a=0.4536 ##Conversion factor for pound(lb) to kg
        b=3.785 ##conversion factor for gal to litres
          
        Vol1=0.0095*Stock ## DIP METHOD CANNOT NOTICE ERROR OF ABOUT 100L SO REFINERS GIVES 0.95%less as per intake ordered by owner
        ##THERMODYNAMIC LOSSES- UNCONTROLLABLE
        S=1;
        M=66;
        eff=94;
        P=6.6;
        t=80 ###(PRODUCT TEMPERATURE WHICH IS LOADED IN FARENHEIT)
        T=t+460
        LL=10*(12.46*S*P*M*(1-eff/100.0))/T ## lb/1000gal
        L=LL*a/(1000*b) ## Loss in kg/l
        Ma=L*Stock  ##MASS LOSS ACCORINGLY AS ORDER GIVEN BY PETROL OWNER
        Vol2=Ma/d;
        flash ( 'CONTROLLABLE LOSS-SET BY REFINERIES = "%s"'%(Vol1))
   
        flash( 'LOADING LOSS AT REFINERY = "%s"'%(Vol2))
        Vol=Vol1+Vol2;
        Cost=65 ##Cost per litre of petrol in RS
        Err= Vol*1000/Stock;
        Terr=Err*Pe/1000; ## less volume offered to consumer per liter
        R=Cost*Terr
        Amt=Cost*Pe
        Per=R*100/Amt
        flash('VOlUME lOSS FOR CONSUMER (in ml) per liter = "%s"' %(Err))
        flash ('TOTAL VOLUME LOSS FOR PETROL OWNER= "%s" '%(Vol))
        flash ('TOTAL VOLUME LOSS FOR CONSUMER (in liters) = "%s"' %(Terr))   
        flash ('LOSS TO CONSUMER (in RS)="%s"'%(R))
        flash ('ACTUAL AMT PAID BY CONSUMER (in RS)= "%s"'%(Amt))
        flash('PERCENT LOSS IN AMT =  "%s"' %
              (Per))
    
        return redirect('/index')
    return render_template('login.html',
                            form=form)
    
