import pandas as pd


def manage_missing_day_data(df):
    # Convert the datetime column to a specific format ("%Y-%m-%d %H:%M") and then to datetime object
    df["Datetime"] = df["Datetime"].apply(lambda x: x.strftime("%Y-%m-%d %H:%M"))
    df["Datetime"] = pd.to_datetime(df["Datetime"])

    # Compute the time differences between consecutive rows in the Datetime column
    hour_changes = df["Datetime"].diff().fillna(pd.Timedelta(0))

    # Find the indices where the hour changes by 2 hours
    indices_hour_change = hour_changes[hour_changes == pd.Timedelta(hours=2)].index

    # Print the indices where the hour changes
    print("Indices of hour changes:")
    print(indices_hour_change)

    # Iterate through the indices of the hour changes
    for idx in indices_hour_change:
        # Compute the average consumption between the two existing values
        average_consumption = (
            df.loc[idx - 1, "electricity"] + df.loc[idx + 1, "electricity"]
        ) / 2
        # Append a new row with the adjusted datetime and the average consumption
        df = df.append(
            {
                "Datetime": df.loc[idx, "Datetime"] - pd.Timedelta(hours=1),
                "electricity": average_consumption,
            },
            ignore_index=True,
        )

    # Sort the dataframe by datetime and reset the index
    df = df.sort_values("Datetime").reset_index(drop=True)
    print(df.iloc[indices_hour_change[0]-5:indices_hour_change[0]+5])
    return df


# Function to manage duplicated data with the same hour and date
def manage_duplicates(df):
    # Check for duplicated entries with the same hour and date
    same_hour_and_date_check = df.duplicated(subset="Datetime", keep=False)

    # If there are duplicated entries with the same hour and date
    if len(df[same_hour_and_date_check]) > 0:
        # Create a new dataframe containing the duplicated entries
        result_df = df[same_hour_and_date_check]
        print("Les lignes qui sont duppliquées :")
        print(result_df)

        # Identify the index of the first duplicated entry and drop it from the original dataframe
        index_to_drop = result_df.index[0]
        df = df.drop(index_to_drop)

    # Return the updated dataframe
    return df


def manage_hour_changes(df):
    df = manage_missing_day_data(df)
    df = manage_duplicates(df)
    return df
