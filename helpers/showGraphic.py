from helpers.get_profil_day import make_columns_for_df_with_0_23_columns
import matplotlib.pyplot as plt


def show_graphic_for_building_day_profil(df, buildind_id):
    # def plot_daily_electricity_profile(df):
    # Extraire les jours de la semaine
    days = df.index

    # Extraire les valeurs de consommation d'électricité pour chaque heure
    values = df.values

    # Créer un graphique
    plt.figure(figsize=(10, 6))
    for i in range(len(days)):
        plt.plot(range(24), values[i], label=days[i])

    # Ajouter des titres et des légendes
    plt.title("Profil journalier de consommation d'électricité")
    plt.xlabel("Heure")
    plt.ylabel("Consommation d'électricité pour la construction {}".format(buildind_id))
    plt.xticks(range(24))
    plt.show()

    # plt.legend()