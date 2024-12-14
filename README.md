# Practical AI Meetup #1
This repository contains the codebase and resources from [Meetup #1](https://www.meetup.com/practical-ai-thessaloniki-meetup-group/events/304722187), 
enabling attendees and the broader community to explore, experiment, and expand upon the concepts presented.

Feel free to dive into the code, modify it, and see AI in action! 
Your contributions and feedback are always welcome. 

Let's make AI practical, together.

## Installation Requirements
All dependencies are declared in the `setup.py` file. For these, I strongly
recommend the use of a virtual environment. To install the dependencies run:
```bash
pip install .
```

Also, make sure tkinter is installed in the appropriate location.

### Basic Dependencies
- [pandas](https://github.com/pandas-dev/pandas/) is used for data manipulation.
- [numpy](https://github.com/numpy/numpy) is used for numerical operations.
- [matplotlib](https://github.com/matplotlib/matplotlib) is used to visualize the results.
- [scikit-learn](https://github.com/scikit-learn/scikit-learn) is used for the ready-to-use ML models.
- [scikit-optimize](https://github.com/scikit-optimize/scikit-optimize) is used for Bayesian optimization algorithms.
- [mlflow](https://github.com/mlflow/mlflow/) is used to handle the MLOps.

### Data Dependencies
To effectively train the models one needs the following two datasets:
- `./data/properties_noise_50.parquet.gzip`
- `./data/properties_noise_100.parquet.gzip`

Both datasets contain properties for **sale** listed on [openhouse.gr](https://openhouse.gr/) in October 2022.
In addition to the basic characteristics, each property includes `noise_day` and `noise_night` columns, 
which indicate the average daytime and nighttime noise levels around the property within a radius of 50 
or 100 meters (depending on the dataset). The datasets are assumed to be cleaned of outliers and edge cases. 
However, additional variations of the datasets may be used as needed (described in [here](#noise-calculation)).

## Project Structure and General Information
The data are stored in the `data` folder, any data related to MLFlow are stored
in the `mlruns` folder, while we manually keep some experiment results in the
`results` folder.

Regarding the core scripts:
- `/core/utilities.py`: contains a utility that reads input parameters through the command line.
- `/core/scale.py`: contains the basic scaling functionalities.
- `/core/experiment.py`: contains the core management of the experiments.
- `/core/train.py`: handles the actual training of the models.
- `/core/evaluate.py`: contains basic model evaluation techniques such as error metrics.

All scripts contain some basic functionality that is frequenty used. The code is
structured in a way to make any enhancements or additions easy to be integrated.
The error metrics as well as some of the interpretability tools are used for
regression problems. However, they can be easily switched to the corresponding
classification metrics if needed.

The hyperparameter tuning can be done in three different ways out-of-the box using
K-fold Cross-Validation:
1) Grid Search
2) Random Search
3) Bayesian Optimization

All scripts related to assigning noise values on properties can be found in the `/noise` folder.
For more details check [here](#noise-calculation)

## Running Experiments
Regardless of the model that is to be trained the core scripts remain the same. To
train a new model one would need to create a script similar to the `decision_trees_experiment.py`
that I have created to showcase how to run experiments. To run a new experiment execute:
```bash
py .\decision_trees_experiment.py --data-file "./data/properties_noise_100.parquet.gzip" --target "Price" --mode "grid_search" --noise 1 --experiment-name "Test"
```
To include an additional run in the same experiment execute:
```bash
py .\decision_trees_experiment.py --data-file "./data/properties_noise_50.parquet.gzip" --target "Price" --mode "bayesian" --noise 2  --experiment-id {experiment_id}
```

The details list of parameters can be found below:
- `--data-file {data_file}` The data file to be used in the training process.
- `--test-size {test_size}` The test size.
- `--target {target}` The column name of the target variable.
- `--mode {hyperparameter_tuning_id}` `'grid_search'` -> Grid Search, `'bayesian'` -> Baysian, else -> Random.
- `--scale {scale}` `'standard'` -> Standard Scaler, `'minmax'` -> Min-Max Scaler.
- `--noise {noise}` Indicates the noise usage (0 -> No noise, 1 -> Day/Night, 2 -> Day/Night average, 3 -> Day, 4 -> Night.
- `--experiment-name {name}` The name of the experiment to be created.
- `--experiment-tags {tags}` A dictionary containing any extra information.
- `--experiment-id {id}` The id of an already existing experiment.

## Results
The results can be visualized in the MLFlow UI. To do so, run:
```bash
mlflow ui
```
Additionally, in the `results` folder one can find extra plots like:
- Feature importance plot
- Permutation importance plot
- Partial dependence plot

Of course, new evaluation metrics or plots can be added via the `evaluation.py`
script.

## Noise Calculation
Each property has a noise value (day/night) assigned to it. 
This noise is calculated by taking the mean of all noise values in a circle of a certain radius around the property. 
However, this is not always the desired method of assigning values. 
To change the method of assigning noise values, update the functions in the `/noise/utilities.py` file accordingly. 
The property data (which do not contain noise values) can be found in the `/noise/data` folder.

To assign new noise values, you will need to use the noise dataset available [here](https://drive.google.com/drive/folders/1cJGPWX40blqbFlk3aHXgmaCeGmGoHJkE). 
Download the required files and move them to the `/noise/data` folder. 
Then, update the `/noise/main.py` file and run the script. 
The new dataset, containing properties with assigned noise values, can also be found in the `/noise/data` folder. 
Properties that could not be assigned a value (for any reason) will have a value of `-1`.
