import pandas as pd


def filter_based_on_test_case(df: pd.DataFrame, noise: int):
    """
    Filters the given dataframe based on the test case.
    :param df: The dataframe to be filtered.
    :param noise: The noise usage.
    :return: The filtered dataframe.
    """
    if noise == 0:
        df = df.drop(columns=["noise_day", "noise_night"])
    elif noise == 2:
        df["noise"] = (df["noise_day"] + df["noise_night"]) / 2
        df = df.drop(columns=["noise_day", "noise_night"])
    elif noise == 3:
        df = df.drop(columns=["noise_night"])
    elif noise == 4:
        df = df.drop(columns=["noise_day"])

    return df
