from sklearn.tree import DecisionTreeRegressor
from core.experiment import run_experiment
from skopt.space import Categorical, Integer


if __name__ == "__main__":
    # Initializing model.
    model = DecisionTreeRegressor()

    # Setting up parameters.
    # Use these for Bayesian optimization.
    # parameters = {
    #     "criterion": Categorical(["squared_error"]),
    #     "splitter": Categorical(["best"]),
    #     "max_depth": Integer(2, 3),
    #     "min_samples_leaf": Integer(5, 6),
    # }
    # Use these for Grid Search optimization.
    parameters = {
        "criterion": ["squared_error"],
        "splitter": ["best"],
        "max_depth": [2],
        "min_samples_leaf": [5, 8],
    }

    # Run the experiment
    run_experiment(model, parameters)
