import pandas as pd

def make_columns_for_df_with_0_23_columns():
    columnsForDf = list(range(24))
    return columnsForDf


def make_profil_df(data_consommation_hour_for_building):
    columns_for_df = make_columns_for_df_with_0_23_columns()

    profil = pd.DataFrame(columns=columns_for_df)

    for i in range(1, 366):
        start = 0 if i == 1 else 24 * (i - 1)
        stop = 24 * i
        profil_day = {}

        df_profil = data_consommation_hour_for_building.iloc[start:stop]

        for index, row in df_profil.iterrows():
            profil_day[row['Datetime'].hour] = row['electricity']

        row_of_df = df_profil.iloc[0]
        index_str = f"{row_of_df['Datetime'].strftime('%Y-%m-%d-%A')}"

        row_dataframe = pd.DataFrame([profil_day], index=[index_str])

        profil = pd.concat([profil, row_dataframe], sort=False)

    return profil











# import pandas as pd

# def make_columns_for_df_with_0_23_columns():
#     columnsForDf=[]
#     for i in range(0,24):
#         columnsForDf.append(i)
#     return columnsForDf


# def make_profil_df(data_consommation_hour_for_building):
#     columns_for_df = make_columns_for_df_with_0_23_columns()

#     profil = pd.DataFrame(columns=columns_for_df)

#     for i in range(1, 366):
#         if i == 1:
#             start = 0
#         else:
#             start = 24 * (i - 1)
        
#         stop = 24 * i
#         profil_day = {}
#         df_profil = data_consommation_hour_for_building.iloc[start:stop]

#         for _, row in df_profil.iterrows():
#             profil_day[row['Datetime'].hour] = row['electricity']

#         row_of_df = df_profil.iloc[0]
#         index_str = f"{row_of_df['Datetime'].strftime('%Y-%m-%d-%A')}"
        

#         row_dataframe = pd.DataFrame([profil_day], index=[index_str])


#         profil = pd.concat([profil, row_dataframe], sort=False)

#     return profil
