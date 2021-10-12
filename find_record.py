def get_page_offset(table, record_id):
    record_id_str = str(record_id) + '|' # On compare le début de chaque ligne
    record_id_size = len(record_id_str)
    
    with open(f'data/{table}_index.txt', 'r') as index:
        for line in index:
            if line[:record_id_size] == record_id_str:
                line = line.split('|')
                return int(line[1]), int(line[2])


def get_data(table, page_id, offset):
    with open(f'data/{table}.txt', 'r') as file:
        for i, line in enumerate(file):
            if i == page_id:
                try:
                    line.strip()  # get rid of possible newline
                    return line.split('@')[offset]
                except ValueError:
                    print("L'enregistrement est introuvable")

                    
table = 'customer'
record_id = 75000

get_data(table, *get_page_offset(table, record_id))