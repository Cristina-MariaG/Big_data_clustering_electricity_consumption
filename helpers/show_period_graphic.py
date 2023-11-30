from matplotlib import pyplot as plt
import pandas as pd


def show_only_days_between(
    profil_day_for_building, start="2019-11-01", end="2019-12-01"
):
    # Définir le jour de la semaine pour lequel vous voulez afficher le graphique
    # profil_day_for_building.index = pd.to_datetime(
    #     profil_day_for_building.index, format="%Y-%m-%d-%A"
    # )
    # Convertir l'index en objets datetime
    profil_day_for_building.index = pd.to_datetime(profil_day_for_building.index)

    # Formater l'index avec le jour de la semaine
    profil_day_for_building.index = profil_day_for_building.index.strftime(
        "%Y-%m-%d-%A"
    )

    profils_selected_date = profil_day_for_building.loc[
        (profil_day_for_building.index >= start)
        & (profil_day_for_building.index <= end)
    ]
    # print(profils_selected_date)

    fig, ax = plt.subplots(figsize=(12, 6))

    profils_selected_date.T.plot(ax=ax)

    # Ajouter des étiquettes et un titre
    plt.xlabel("Heure")
    plt.ylabel("Valeurs")
    plt.title(f"Energy Consumption in {start} to {end}")
    plt.show()

    return profils_selected_date


def show_graphic_for_building_day(
    profil_day_for_building, days_list=["Saturday", "Sunday"]
):
    # profil_day_for_building.index = pd.to_datetime(profil_day_for_building.index)

    # # Formater l'index avec le jour de la semaine
    # profil_day_for_building.index = profil_day_for_building.index.strftime(
    #     "%Y-%m-%d-%A"
    # )
    # for day in days_list:
    # print(day)
    # Sélectionner les données pour le jour de la semaine spécifié
    profil_day_for_building.index = pd.to_datetime(profil_day_for_building.index)
    selected_data = profil_day_for_building[
        profil_day_for_building.index.day_name().isin(days_list)
    ]
    # print(selected_data)

    # Tracer les données pour le jour de la semaine spécifié
    fig, ax = plt.subplots(figsize=(12, 6))
    selected_data.T.plot(ax=ax, legend=None)

    # Ajouter des étiquettes et un titre
    plt.xlabel("Heure")
    plt.ylabel("Valeurs")
    plt.title(f"Données pour {days_list}")
    plt.show()
