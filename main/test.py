import pandas as pd
import re
import parameters as pas

def re_str(old):
    mode = re.compile(r'\d+')
    lt = mode.findall(old)
    new = ''
    for i in lt:
        new += i
    return new

def load_dict_room():
    df_room_orignal = pd.read_table(pas.dict_room, sep="\s+", header=None)
    df_room_dealed = df_room_orignal.dropna()
    dict_room = dict()
    for index, row in df_room_dealed.iterrows():
        student_id = re_str(row[0])
        work_id = re_str(str(int(row[2])))
        dict_room[work_id] = student_id
        # print dict_room[work_id]
    return  dict_room

def load_df_order():
    df_order = pd.read_table(pas.list_all_order, sep="\s+", header=None)
    for index, row in df_order.iterrows():
        df_order.loc[index, [0]] = re_str(str(row[0]))
        #print list(df_order.loc[index])[0]
    return df_order

def load_dict_day2col():
    list_day = pd.read_table(pas.dict_day, sep="\s+", header=None)
    dict_day = dict()
    for index, row in list_day.iterrows():
        dict_day[str(row[0])] = str(int(row[1]))
    return dict_day

def load_dict_col2day():
    list_day = pd.read_table(pas.dict_day, sep="\s+", header=None)
    dict_col = dict()
    for index, row in list_day.iterrows():
        i = int(row[1])
        j = (i-1) * 3 + 1
        dict_col[str(j + 1)] = str(row[0])
        dict_col[str(j + 2)] = str(row[0])
        dict_col[str(j + 3)] = str(row[0])
    return dict_col

def run_data():
    dict_room =load_dict_room()
    dict_day = load_dict_day2col()
    df_order = load_df_order()
    df_order = df_order.set_index(0)

    number_of_col = df_order.size / df_order.__len__()

    for i in range(1, 76):
        df_order[str(number_of_col+i)] = 0
    # print df_order

    df_room_kaoqin = pd.read_table(pas.data_attention, sep="\s+", header=None)
    # print df_room_kaoqin


    for index, row in df_room_kaoqin.iterrows():

        if int(row[0]) == 69 or int(row[0]) == 1:
            continue

        blank_3 = ''
        day_to_Main_col = (int(dict_day[str(row[1])])-1) * 3 + number_of_col
        # print df_order.head()
        # print day_2_Main_col+int(0)

        i_time = int(re_str(str(row[2])))
        #print i_time

        # print df_order.loc[dict_room[str(row[0])], [str(day_to_Main_col + int(1))]]
        if i_time >= 70000 and i_time < 81600:
            print 'early'
            if int(df_order.loc[dict_room[str(row[0])], [str(day_to_Main_col + int(1))]]) == 0:
                df_order.loc[dict_room[str(row[0])], [str(day_to_Main_col + int(1))]] = 1
            else:
                blank_3 += str(row[2])
                try:
                    if int(df_order.loc[dict_room[str(row[0])], [str(day_to_Main_col + int(3))]]) == 0:
                        df_order.loc[dict_room[str(row[0])], [str(day_to_Main_col + int(3))]] = blank_3
                except Exception :
                    blank_3 += ','
                    blank_3 += str(df_order.loc[dict_room[str(row[0])], [str(day_to_Main_col + int(3))]])
                    df_order.loc[dict_room[str(row[0])], [str(day_to_Main_col + int(3))]] = blank_3
                pass
        elif i_time >= 81600 and i_time <= 91600:
            print 'late'
            if int(df_order.loc[dict_room[str(row[0])], [str(day_to_Main_col + int(1))]]) == 0:
                df_order.loc[dict_room[str(row[0])], [str(day_to_Main_col + int(1))]] = -1
            else:
                blank_3 += str(row[2])
                try:
                    if int(df_order.loc[dict_room[str(row[0])], [str(day_to_Main_col + int(3))]]) == 0:
                        df_order.loc[dict_room[str(row[0])], [str(day_to_Main_col + int(3))]] = blank_3
                except Exception :
                    blank_3 += ','
                    blank_3 += str(df_order.loc[dict_room[str(row[0])], [str(day_to_Main_col + int(3))]])
                    df_order.loc[dict_room[str(row[0])], [str(day_to_Main_col + int(3))]] = blank_3
        elif i_time >= 100000 and i_time <113000:
            print 'leave too early'
            if int(df_order.loc[dict_room[str(row[0])], [str(day_to_Main_col + int(2))]]) == 0:
                df_order.loc[dict_room[str(row[0])], [str(day_to_Main_col + int(2))]] = -1
            else:
                blank_3 += str(row[2])
                try:
                    if int(df_order.loc[dict_room[str(row[0])], [str(day_to_Main_col + int(3))]]) == 0:
                        df_order.loc[dict_room[str(row[0])], [str(day_to_Main_col + int(3))]] = blank_3
                except Exception :
                    blank_3 += ','
                    blank_3 += str(df_order.loc[dict_room[str(row[0])], [str(day_to_Main_col + int(3))]])
                    df_order.loc[dict_room[str(row[0])], [str(day_to_Main_col + int(3))]] = blank_3
        elif i_time >= 113000 and i_time <= 130000:
            print 'leave'
            if int(df_order.loc[dict_room[str(row[0])], [str(day_to_Main_col + int(2))]]) == 0:
                df_order.loc[dict_room[str(row[0])], [str(day_to_Main_col + int(2))]] = 1
            else:
                blank_3 += str(row[2])
                try:
                    if int(df_order.loc[dict_room[str(row[0])], [str(day_to_Main_col + int(3))]]) == 0:
                        df_order.loc[dict_room[str(row[0])], [str(day_to_Main_col + int(3))]] = blank_3
                except Exception :
                    blank_3 += ','
                    blank_3 += str(df_order.loc[dict_room[str(row[0])], [str(day_to_Main_col + int(3))]])
                    df_order.loc[dict_room[str(row[0])], [str(day_to_Main_col + int(3))]] = blank_3
        else:
            print 'exception'
            blank_3 += str(row[2])
            try:
                if int(df_order.loc[dict_room[str(row[0])], [str(day_to_Main_col + int(3))]]) == 0:
                    df_order.loc[dict_room[str(row[0])], [str(day_to_Main_col + int(3))]] = blank_3
            except Exception:
                blank_3 += ','
                blank_3 += str(df_order.loc[dict_room[str(row[0])], [str(day_to_Main_col + int(3))]])
                df_order.loc[dict_room[str(row[0])], [str(day_to_Main_col + int(3))]] = blank_3

        # print df_order.loc[dict_room[str(row[0])], [str(day_to_Main_col + int(1))]]
        # print df_order.loc[dict_room[str(row[0])], [str(day_to_Main_col + int(2))]]
        # print df_order.loc[dict_room[str(row[0])], [str(day_to_Main_col + int(3))]]

    del df_order[1]
    header = new_header()
    df_order.rename(columns=header, inplace=True)
    df_order.to_excel(pas.output, sheet_name='new')
    pass

def new_header():
    dict_col = load_dict_col2day()
    cols = dict()
    for i in range(2, 77):
        j = (i-1) % 3
        day = re_str(str(dict_col[str(i)]))[2:]
        if j == 0:
            cols[str(i)] = day + 'Ex'
        if j == 1:
            cols[str(i)] = day + 'Co'
        if j == 2:
            cols[str(i)] = day + 'Le'
    return cols

def main():
    run_data()
    pass