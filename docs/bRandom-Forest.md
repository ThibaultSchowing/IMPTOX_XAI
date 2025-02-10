# Random Forest

Random Forest is a rule based method by nature which can be interpreted by itself bu also with Fidex

See Notebook for example

Here are the main data example and result. 


## Training Random Forest



=== "Random Forest"

    Simple but powerful, Random Forest creates an ensemble of decision trees which each contain already interpretable but numerous rules. Using [a modified version with the Fidex algorithm](https://hes-xplain.github.io/documentation/dimlpfidex/training-methods/randforeststrn/) allows to extract clear decision rules making the model more transparent and human readable. 



    ```py title="Training function"
        randForestsTrn(
        """
        --train_data_file .../datasets/PimaDiabetes/train.csv 
        --test_data_file .../datasets/PimaDiabetes/test.csv 
        --nb_attributes 8 
        --nb_classes 2"""
        )
    ```

## Results

Show some image

Link notebook