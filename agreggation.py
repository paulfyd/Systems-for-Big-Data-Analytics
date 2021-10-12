from projection import get_attributs
from projection import print_table

# Exemple d'une somme sur les nombres de L_QUANTITY, L_EXTENDERDPRICE, L_DISCOUNT, L_TAX  (plus de 6 millions de lignes !)
get_attributs('lineitem', [4, 5, 6, 7])

with open(f'resultat.txt', 'r') as res:
    index = res.readline()
    
    sum_attribut = [0]*len(index.split('|'))
                           
    for page in res:
        records = page.strip().split('@')
        results = [record.split('|') for record in records]
        sum_attribut_page = [sum([float(fields[i]) for fields in results]) for i in range(1,len(results[0]))]
        sum_attribut = [p+q for p,q in zip(sum_attribut, sum_attribut_page)]     
        
with open(f'resultat.txt', 'w') as res:
    res.write('|'.join(index.split('|')[1:]))
    res.write('|'.join([str(sum_tmp) for sum_tmp in sum_attribut]))
    
print_table('resultat.txt', 1) # ==> Regarder le  fichier 'resutlat_nice.txt' (rafrechir le fichier)