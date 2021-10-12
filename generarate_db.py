from tqdm import tqdm

from constant import SCHEMAS, MAX_LENGTH

def gen_database(db_name):
    with open(f'data_gen/{db_name}.tbl', 'r') as source:
        with open(f'data/{db_name}.txt', 'w') as database:
            with open(f'data/{db_name}_index.txt', 'w') as db_index:
                # The first line is the name of the attributes
                database.write('|'.join(SCHEMAS[db_name]) + '\n')

                # The other follows the scheme
                page = source.readline()[:-1] + '@'
                
                page_num = 1  # page_num = 0 is for the name of attributes
                offset = 0

                db_index.write(page.split('|')[0] + '|' + str(page_num) + '|' + str(offset) + '\n')

                for record in tqdm(source):

                    record_size = len(record)-1

                    if len(page)+record_size < MAX_LENGTH:
                        page += record[:-2] + '@'
                        offset += 1
                        db_index.write(record.split('|')[0] + '|' + str(page_num) + '|' + str(offset) + '\n')
                    else:
                        database.write(page + '\n')
                        page = record[:-1]

                        page_num += 1
                        offset = 0

                        db_index.write(record.split('|')[0] + '|' + str(page_num) + '|' + str(offset) + '\n')

                database.write(page + '\n')



if __name__ == '__main__':

    for db_name in SCHEMAS.keys():
       print(db_name)
       gen_database(db_name)