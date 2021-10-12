def get_attributs(table, lst_attribut_id):
    with open(f'data/{table}.txt', 'r') as file:
        with open(f'resultat.txt', 'w') as output:
            # Always add the id of record
            lst_attribut_id = [0] + lst_attribut_id
            
            # first line is for the name of the attribut
            schema = file.readline().strip()
            names_attribut = [name for i, name in enumerate(schema.split('|')) if i in lst_attribut_id]
            output.write('|'.join(names_attribut) + '\n')
            
            for line in file:
                page = ''
                records = line.split('@')[:-1]  # get rid of the newline
                for record in records:
                    fields = record.split('|')
                    attributs = [field for i, field in enumerate(fields) if i in lst_attribut_id]
                    page += '|'.join(attributs) + '@'
                    
                output.write(page[:-1] + '\n')





def print_table(file, page_id):
    with open(f'{file}', 'r') as table:
        for i, page in enumerate(table):
            if i == 0:
                records = [page.strip()]
            if i == page_id:
                records += page.strip().split('@')
                results = [record.split('|') for record in records]
                results = results
                break
        
    lst_max_size = [max([len(fields[i]) for fields in results])+4 for i in range(len(results[0]))]

    str_table = [[f'{value:^{offset}}' for value, offset in zip(records[0].split('|'), lst_max_size)]]
    str_table += [[f'{value:<{offset}}' for value, offset in zip(record.split('|'), lst_max_size)] for record in records[1:]] 

    with open('resultat_nice.txt', 'w') as nice:
        for i, line in enumerate(str_table):
            nice.write('| '.join(line) + '\n')
            if i == 0: 
                nice.write('-'*(sum(lst_max_size)+(len(line)-1)*2) + '\n')


get_attributs('customer', [3])  # --> le résultat est dans le fichier resultat.txt

file = 'resultat.txt'
page_id = 1

print_table(file, page_id)  # ==> Regarder le  fichier 'resultat_nice.txt'
