def headerselector(data_array):
    y = data_array[:len(data_array)-13]
    return y


def readfile(foldername):
    import sys
    import pandas as pd
    import numpy as np
    import mysql.connector
    import json
    import glob
    # import math
    from exceldatacallfunc import data_framecall, headerselector

    # give the name of the folder containing main excelfiles.
    # here first parameter received from data_framecall is the list of excelfile and second parameter gives its databases.

    df = data_framecall(foldername)
    count = 0
    for element in df[0]:

        file = foldername+'/'+element
        print(type(file))
        print('Started working in file--------'+file)

        # read file from excel data
        df = pd.read_excel(file, index_col=0)
        headers = df.columns.ravel()  # reading the datas using panda of two columns
        df2 = pd.read_excel(file, usecols=[headers[1], headers[2]])
        df2.dropna()
        df = df2[df2[headers[1]].notnull()]
        # data received from pandas dataframe is converted into list
        alist = df.values.tolist()
        # creating the absolute data after filtering nan and garbage values
        head1 = []
        head2 = []
        label1 = headerselector(headers[1])
        label2 = headerselector(headers[2])
        i = 0
        for i in range(len(alist)):
            if (alist[i][0] != '---'):
                head1.append(alist[i][0])
                head2.append(alist[i][1])
        data = [{
            'label': label1,
            'data': head1,
        }, {
            'label': label2,
            'data': head2,
        }]
        count += 1
        print("---------------Completed part-1------count is----"+str(count))
        mydb = mysql.connector.connect(
            host='localhost',
            user='root',
            passwd='',
            database='badc'

        )
        mc = mydb.cursor()

        wlevel1 = json.dumps(data[0]['data'])
        wlevel2 = json.dumps(data[1]['data'])
        # mc.execute("CREATE table waterlevel(id INT AUTO_INCREMENT PRIMARY KEY,nameofarea VARCHAR(50), levelofwater TEXT)")

        # for deleting an entry
        # mc.execute("delete from waterlevel where id=2")
        # commands for inserting data into sql database

        sql = "INSERT INTO waterlevel (place, levelofwater) VALUES (%s, %s)"
        vals = (data[0]['label'], wlevel1)
        mc.execute(sql, vals)
        vals = (data[1]['label'], wlevel2)
        mc.execute(sql, vals)
        mydb.commit()
        #mc.execute("select * from waterlevel")
        # for d in mc.fetchall():
        # print(d)
