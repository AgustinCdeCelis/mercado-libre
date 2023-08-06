import requests
import json
import pandas as pd


    


def main(info):

        link = f'https://api.mercadolibre.com/items/{info}?include_attributes=all'
        print(link)
        resp = requests.get(link) #request

        if resp.status_code == 200:
                data = resp.json() #veo json
        #print(data)
                info={}
                for categoria in data: 
                        if categoria== 'category_id':
                       
                                info[categoria]= data[categoria] 
                                #keys                   #values
                        elif categoria=='attributes':
                                for subcategoria in data[categoria]: #lista con diccionarios

                                        if subcategoria['id']=='BRAND':
                                                info['marca']=subcategoria['value_name']

        else:
                print('hay un error')

        print(info)
        return info

if __name__=='__main__':
        main()


        
        
        


