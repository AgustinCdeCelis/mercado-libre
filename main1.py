from model import second_model
import pandas as pd

from import_data import extraccion1,extraccion2

print(extraccion1.string)


def extraccion(valores:str,num:int):

    lista =valores.string.split()


    full=[]
    cont=0
    for i in lista:
        print(i)
        cont+=1
        print(f' loop n°: {cont}')
        data=second_model.main(i)
        full.append(data)


    category_ids = [d.get('category_id') for d in full]
    marcas = [d.get('marca') for d in full]


    df = pd.DataFrame({'meli':lista,'category_id':category_ids,'marca':marcas})

    df.to_excel(f'./data/archivo{num}.xlsx',index= False)



primer_archivo= extraccion(extraccion1,1)
segundo_archivo= extraccion(extraccion2,2)