from setuptools import setup, find_packages


setup(
    name="Practical AI Meetup #1",
    version="1.0.0",
    url="https://github.com/Practical-AI-Thessaloniki-Meetup/meetup-1",
    author="Georgios Kamtziridis",
    author_email="georgekam96@gmail.com",
    description="",
    packages=find_packages(),
    install_requires=[
        "pandas",
        "numpy",
        "matplotlib",
        "scikit-learn",
        "mlflow",
        "scikit-optimize",
        "geopy",
        "pandarallel",
    ],
)
