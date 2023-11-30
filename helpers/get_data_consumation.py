import pandas as pd

import os


# The function takes a consumption type as an argument and returns the corresponding data
def get_excel_file_data(file_name):
    script_directory = os.path.dirname(os.path.realpath(__file__))
    data_directory = os.path.join(
        script_directory, "..", "data"
    )  # Path to the directory containing the data files

    # Selection of the file based on the consumption type
    absolute_path = os.path.join(
        data_directory, file_name
    )  # Absolute path to the data file

    data = pd.read_excel(absolute_path)  # Reading data from the Excel file

    return data


# The function takes a consumption type as an argument and returns the corresponding data
def get_excel_data(consommation_type):
    # Mapping of consumption types to numerical values for ease of processing

    consommation_types = {
        "bureau_electricity": 1,
        "heating_bureau": 2
    }

    # Checking if the consumption type is valid
    if consommation_type not in consommation_types:
        raise ValueError("Invalid consommation_type value.")

    consommation_type = consommation_types[
        consommation_type
    ]  # Using the mapping to get the numerical value

    script_directory = os.path.dirname(os.path.realpath(__file__))
    data_directory = os.path.join(
        script_directory, "..", "data"
    )  # Path to the directory containing the data files

    # Selection of the file based on the consumption type
    file_names = {
        1: "bureau_electricity.xlsx",
        2: "BU_heating_demand_IDF.xlsx"
    }
    file_name = file_names[
        consommation_type
    ]  # Selecting the appropriate file name based on the consumption type

    absolute_path = os.path.join(
        data_directory, file_name
    )  # Absolute path to the data file

    data = pd.read_excel(absolute_path)  # Reading data from the Excel file

    return data


def make_df_with_time_and_building_consommation(data, building_column_name):
    data["Datetime"] = pd.to_datetime(data["Datetime"])

    df_building = data[["Datetime", building_column_name]]
    df_building.rename(columns={building_column_name: "electricity"}, inplace=True)

    return df_building


def get_Df_for_building(building_id, consommation_type):
    data = get_excel_data(consommation_type)
    copy_data = data.copy()

    consommation_for_building_wanted = make_df_with_time_and_building_consommation(
        copy_data, building_id
    )

    return consommation_for_building_wanted
