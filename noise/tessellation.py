import pandas as pd


def apply_tessellation(df):
    """
    Applies tessellation to the given dataframe. The tessellation
    process is based on the number of decimals on both coordinates.
    Currently, the function keeps the 4 decimals and uses average
    to aggregate the duplicated coordinates.
    :param df: The dataframe on which to apply tessellation.
    :return: The tessellated dataframe.
    """
    # Converting the latitude and longitude values to strings
    df["latitude"] = df["latitude"].astype("string")
    df["longitude"] = df["longitude"].astype("string")

    # Keeping only the first 4 decimals
    df["latitude"] = df["latitude"].str[:7]
    df["longitude"] = df["longitude"].str[:7]

    # Grouping the new latitude/longitude pairs by averaging the noise
    mean = df.groupby(["latitude", "longitude"])["noise"].mean()

    # Creating the tessellated dataframe
    df_tessellated = pd.DataFrame({"noise": mean}).reset_index()

    # Converting the stringified latitude/longitude to floats
    df_tessellated["latitude"] = df_tessellated["latitude"].astype("float64")
    df_tessellated["longitude"] = df_tessellated["longitude"].astype("float64")

    return df_tessellated
