# This is the function which takes the name of the folder wherer excel file is located.
# This returns the name of the excel files after neglecting corrupeted files as first parameter
# and provides the dataframes of each file as the second parameter.


def data_framecall(folder_name):

    import glob
    import pandas as pd
    file_with_dir = glob.glob("./"+folder_name+"/*.xlsx")
    b = []

    # reading file only the names of excelfile
    for data in range(len(file_with_dir)):
        if file_with_dir[data][22:23] != '~':
            b.append(file_with_dir[data][22:])
    print("---------------------------------------------------------------------------------------------------------------")
    print(b)
    print("---------------------------------------------------------------------------------------------------------------")

    # getting all the dataframes from all those files
    df = []
    i = 0

    for data in range(len(b)):
        file = folder_name + "/"+b[data]
        df.append(pd.read_excel(file))
        i = i+1
        print("Loaded data from "+file+" number of loaded file- "+str(i))
    return b, df


def row_selector(data):
    arry = []
    line_number = 0
    for i in range(len(data)):
        if i == 0:
            arry.append(0)
        elif i >= 1:
            line_number = len(data[i].index)
            line_number = arry[i-1]+line_number
            arry.append(line_number)

    return arry


def headerselector(data_array):
    y = data_array[:len(data_array)-13]
    return y
