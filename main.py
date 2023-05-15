from model import model_meli
import pandas as pd
from import_data import extraccion

print(extraccion.string)


lista =extraccion.string.split()



full=[]
cont=0
for i in lista:
    print(i)
    cont+=1
    print(f' loop n°: {cont}')
    data=model_meli.take_data(i)
    full.append(data)


df = pd.DataFrame({'meli':lista,'category_id':full})
   
df.to_excel('./data/meliprueba1.xlsx',index= False)







    

    

    
    
    


