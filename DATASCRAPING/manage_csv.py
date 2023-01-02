import csv
import os
def create_csv(save_path,file_name,header,data):


    completeName = os.path.join(save_path,file_name)

    with open(completeName+'.csv', 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)

        # write the header
        writer.writerow(header)

        # write multiple rows
        if type(data[0])==str:
            
            writer.writerow(data)

        else:
            writer.writerows(data)
    f.close()

def add_csv(save_path,file_name,data):

    completeName = os.path.join(save_path,file_name)

    with open(completeName+'.csv', 'a', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        if type(data[0])==str:
            
            writer.writerow(data)
        else:

        # write multiple rows
            writer.writerows(data)
    f.close()
def read_csv(path,filename):
    completeName = os.path.join(path,filename)
    with open(completeName+'.csv',newline='') as f :
        reader = csv.reader(f)
        data_list =list(reader)
    return reader,data_list
    


