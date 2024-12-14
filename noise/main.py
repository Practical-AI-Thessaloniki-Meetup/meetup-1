from utilities import enhance_properties_with_noise


if __name__ == "__main__":
    # Calculating the noise
    enhance_properties_with_noise(
        "./noise/data/properties.parquet.gzip",
        "./noise/data/thessaloniki_day_noise.parquet.gzip",
        "properties_new",
    )
