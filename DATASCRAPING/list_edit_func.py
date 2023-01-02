## these code is to manage the data to file or file to data
#Note: these code was created before I study the pandas library if you know how to use pandas you can adapt pandas library to these code

import os
import json
def add_list2text(path,name,lis):
    completeName = os.path.join(path,name)
    try:
        with open(completeName+'.txt', 'a') as fp:
            for item in lis:
        # write each item on a new line
                fp.write("%s\n" % str(item));
    except:
        with open(completeName+'.txt', 'a',encoding="utf-8") as fp:
            for item in lis:
        # write each item on a new line
                fp.write("%s\n" % str(item));
    print('Done')
    fp.close()
def read_text2list(path,name):
    names =[]
    completeName = os.path.join(path,name)
    try:
        with open(completeName+'.txt', 'r') as fp:
            for line in fp:
        # remove linebreak from a current name
        # linebreak is the last character of each line
                x = line[:-1]

        # add current item to the list
                names.append(x)
    except:
        with open(completeName+'.txt', 'r',encoding="utf-8") as fp:
            for line in fp:
        # remove linebreak from a current name
        # linebreak is the last character of each line
                x = line[:-1]

        # add current item to the list
                names.append(x)
    fp.close()
    return names
def write_dict2text(path,name,dic):
    completeName = os.path.join(path,name)
    with open(completeName+'.txt', 'w') as convert_file:
        convert_file.write(json.dumps(dic))
    convert_file.close()        
    print('Done')
def read_text2dic(path,name):
    completeName = os.path.join(path,name)
    d2 = json.load(open(completeName+'.txt'))
    print('Done')
    return d2

