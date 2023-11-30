from helpers.get_data_consumation import get_excel_data, get_excel_file_data


def get_data_for_building(id, secteur="buildings"):
    if secteur == "residential":
        buildings = get_excel_data("buildings")
    else:
        buildings = get_excel_file_data("BU_all_buildings_IDF.xlsx")
    print(buildings)

    # index_to_drop = buildings.index[buildings['ID'] == id]
    # print(index_to_drop)
    # Soustraire la ligne avec l'ID spécifié
    row_to_subtract = buildings.index[buildings["ID"] == id]
    print("row_to_subtract", row_to_subtract)

    # Soustraire la ligne de 'row_to_subtract' du DataFrame original 'df'
    df_subtracted = buildings.loc[row_to_subtract]

    # Afficher le DataFrame après la suppression
    print(df_subtracted)
    return df_subtracted
    # print(buildings)


def getUserBuilding(secteur="residentiel"):
    # if secteur == "residentiel":
    #     buildings = get_excel_data("buildings")
    # else:

    buildings = get_excel_file_data("BU_all_buildings_IDF.xlsx")

    building_ids = buildings["ID"].tolist()
    while True:
        building_id = input("What building? (the building id)")

        # Check if the building id is valid
        if building_id in building_ids:
            break
        else:
            print("Invalid building id. Please try again.")

    return building_id


def get_consommation_type_wanted():
    file_names = {
        1: "bureau_electricity",
        2: "heating_bureau",
    }
    while True:
        consommation_type = input(
            "What type of consommation we want to cluster? 1:bureau electricity : 2: heating bureau :"
        )

        if consommation_type in ["1", "2"]:
            break
        else:
            print("Invalid choice. Please enter 1, or 2.")

    return file_names[int(consommation_type)]
