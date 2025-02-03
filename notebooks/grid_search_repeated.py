import pandas as pd
import argparse
from sklearn.model_selection import GridSearchCV, RepeatedStratifiedKFold
from fuzzycocopython import FuzzyCocoClassifier
from sklearn.ensemble import RandomForestClassifier

# Define parameter grids
fuzzy_system = {
    "nbRules": [5, 7, 10],
    "nbMaxVarPerRule": [3, 5, 7],
    "nbInSets": [2, 4],
    "nbOutSets": [2, 4],
}

fitness_parameters = {
    "sensitivityW": [0.5, 1.0],
    "specificityW": [0.5, 1.0],
    "accuracyW": [0.25, 0.75],
    "ppvW": [0.25, 0.5, 0.75],
    "rmseW": [0.25, 0.5, 0.75],
    "dontCareW": [0.05, 0.1]
}

co_evolution = {
    "popSizePop1": [250, 500],
    "popSizePop2": [250, 500],
    "cxProbPop1": [0.7, 0.9],
    "elitePop1": [6, 12],
    "elitePop2": [6, 12],
    "cxProbPop2": [0.6, 0.8],
}

final_search = {
    "nbRules": [5, 7, 9],
    "nbMaxVarPerRule": [3, 4, 5],
    "popSizePop1": [300, 350, 400],
    "popSizePop2": [150, 200, 250],
}

RFgrid = {
    "n_estimators": [50, 100, 200],          # 3 options
    "max_depth": [10, 20, None],             # 3 options
    "min_samples_split": [2, 5, 10],         # 3 options
    "min_samples_leaf": [1, 2, 4],           # 3 options
    "bootstrap": [True, False]               # 2 options
}

# Combine all parameter grids
grid = {
    "fuzzy_system": fuzzy_system,
    "fitness_parameters": fitness_parameters,
    "co_evolution": co_evolution,
    "final_search": final_search,
    "RFgrid": RFgrid
}


# Predefined parameter sets (non-reduce and reduce)
params_nonreduce = {'maxGenPop1': 500, 'accuracyW': 0.25, 'dontCareW': 0.05, 'ppvW': 0.5, 'rmseW': 0.25, 'sensitivityW': 1.0, 'specificityW': 1.0}
params_nonreduce.update({'cxProbPop1': 0.7, 'cxProbPop2': 0.8, 'elitePop1': 6, 'elitePop2': 6, 'popSizePop1': 250, 'popSizePop2': 250})
# fuzzybest: {'nbInSets': 2, 'nbMaxVarPerRule': 7, 'nbOutSets': 2, 'nbRules': 5}

params_reduce = {'maxGenPop1': 500, 'accuracyW': 0.75, 'dontCareW': 0.05, 'ppvW': 0.5, 'rmseW': 0.5, 'sensitivityW': 0.5, 'specificityW': 0.5}
params_reduce.update({'cxProbPop1': 0.7, 'cxProbPop2': 0.8, 'elitePop1': 12, 'elitePop2': 12, 'popSizePop1': 250, 'popSizePop2': 250})
# fuzzybest
def load_data(data_path):
    data = pd.read_csv(data_path, sep=';')
    X = data.drop('OUT', axis=1)
    y = data['OUT']
    return X, y

def grid_search(data_path, output_path, grid_name, reduce, n_repeats):
    """
    Conducts a GridSearchCV using RepeatedStratifiedKFold on the specified parameter grid.
    """
    X, y = load_data(data_path)

    # Select the desired parameter grid
    param_grid = grid[grid_name]

    # Choose the parameter preset (reduce vs. non-reduce)
    
    if reduce:
        model = FuzzyCocoClassifier(**params_reduce)
        #model = RandomForestClassifier()
    else:
        model = FuzzyCocoClassifier(**params_nonreduce)
        #model = RandomForestClassifier()

    # Repeated Stratified K-Fold (n_splits=4, controlled by n_repeats)
    rskf = RepeatedStratifiedKFold(
        n_splits=4, 
        n_repeats=n_repeats, 
        random_state=1995  # You can change this seed if desired
    )

    gs = GridSearchCV(
        estimator=model,
        param_grid=param_grid,
        cv=rskf,
        n_jobs=2,
        scoring='accuracy',
        verbose=3,
        return_train_score=True
    )
    
    # Just to confirm that X is a DataFrame
    if isinstance(X, pd.DataFrame):
        print("Yes, X is a DataFrame")

    # Fit the grid search
    gs.fit(X, y)

    # Export results to a DataFrame
    results = pd.DataFrame(gs.cv_results_)
    results.to_csv(output_path, index=False)

    # Print best parameters and score
    print("Best Parameters:", gs.best_params_)
    print("Best Score:", gs.best_score_)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--data_path', type=str, required=True,
                        help="Path to the CSV file containing data.")
    parser.add_argument('--output_path', type=str, required=True,
                        help="Path to save the GridSearch results.")
    parser.add_argument('--grid', type=str, required=True,
                        help="Name of the parameter grid to use ('fuzzy_system', "
                             "'fitness_parameters', 'co_evolution').")
    parser.add_argument('--reduce', type=bool, default=False,
                        help="Whether to use the 'reduce' parameter set.")
    parser.add_argument('--n_repeats', type=int, default=3,
                        help="Number of repetitions for RepeatedStratifiedKFold.")
    args = parser.parse_args()

    grid_search(args.data_path, args.output_path, args.grid, args.reduce, args.n_repeats)
