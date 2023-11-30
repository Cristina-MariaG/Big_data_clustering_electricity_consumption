import pandas as pd


def make_day_profil_remove_last_row(df):
    # delete the last row of dataframe that correspond to the first hour (00:00) of 2020:01:01 bc when we make a day profil this will add a day with nan values
# Date à vérifier
    date_to_check = pd.Timestamp('2020-01-01 00:00:00')

    # Vérifier si la dernière ligne correspond à la date spécifiée
    if df.iloc[-1]['Datetime'] == date_to_check:
        # Supprimer la dernière ligne si elle correspond à la date spécifiée
        df = df.drop(df.index[-1])
    # Créer un nouveau DataFrame avec l'index souhaité
    new_df = pd.DataFrame(columns=range(24))

    # Remplir le nouveau DataFrame avec les valeurs appropriées
    for index, row in df.iterrows():
        # date = row["Datetime"].strftime("%Y-%m-%d-%A")
        date = row["Datetime"].strftime("%Y-%m-%d-%A")
        hour = row["Datetime"].hour
        new_df.loc[date, hour] = row["electricity"]

    return new_df


def make_day_profil(df):
 
    # Créer un nouveau DataFrame avec l'index souhaité
    new_df = pd.DataFrame(columns=range(24))

    # Remplir le nouveau DataFrame avec les valeurs appropriées
    for index, row in df.iterrows():
        # date = row["Datetime"].strftime("%Y-%m-%d-%A")
        date = row["Datetime"].strftime("%Y-%m-%d-%A")
        hour = row["Datetime"].hour
        new_df.loc[date, hour] = row["electricity"]

    return new_df
