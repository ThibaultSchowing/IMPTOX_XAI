# Random Forest

Simple but powerful, Random Forest creates an ensemble of decision trees which each contain already interpretable but numerous rules. Using [a modified version with the Fidex algorithm](https://hes-xplain.github.io/documentation/dimlpfidex/training-methods/randforeststrn/) allows to extract clear decision rules making the model more transparent and human readable.  

The model obtains a **69% test accuracy** and the rules, local (per sample) and global(over all) leading to this classification result are the following. 

=== "Local rules"

    ```
    Rule for sample 0 :

    Glucose>=158.5 Glucose<160.5 -> class 1
    Train Covering size : 2
    Train Fidelity : 1
    Train Accuracy : 1
    Train Confidence : 0.823333

    -------------------------------------------------

    Rule for sample 1 :

    Glucose<89.5 BloodPressure>=82.5 -> class 0
    Train Covering size : 4
    Train Fidelity : 1
    Train Accuracy : 1
    Train Confidence : 0.904
    ```

 === "Global rules"

    ```
    Number of rules : 152, mean sample covering number per rule : 11.572368, mean number of antecedents per rule : 3.085526
    No decision threshold is used.

    Rule 1: Glucose<104.5 BMI<28.8 -> class 0
    Train Covering size : 81
    Train Fidelity : 1
    Train Accuracy : 1
    Train Confidence : 0.980741

    Rule 2: Glucose<106.5 Age<25.5 BMI<34.900002 -> class 0
    Train Covering size : 79
    Train Fidelity : 1
    Train Accuracy : 1
    Train Confidence : 0.982278
    ```


You can find the notebook in the GitHub repository by clicking the link in the top-right corner. 