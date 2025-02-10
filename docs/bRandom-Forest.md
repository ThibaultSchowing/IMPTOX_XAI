# Random Forest

Random Forest is a rule based method by nature which can be interpreted by itself bu also with Fidex

See Notebook for example

Here are the main data example and result. 


TODO

=== "Random Forest"

    Simple but powerful, Random Forest creates an ensemble of decision trees which each contain already interpretable but numerous rules. Using [a modified version with the Fidex algorithm](https://hes-xplain.github.io/documentation/dimlpfidex/training-methods/randforeststrn/) allows to extract clear decision rules making the model more transparent and human readable. 



    ```py
        randForestsTrn(
        """
        --train_data_file .../datasets/PimaDiabetes/train.csv 
        --test_data_file .../datasets/PimaDiabetes/test.csv 
        --nb_attributes 8 
        --nb_classes 2"""
        )
    ```



```py title="add_numbers.py" linenums="1"
# Function to add two numbers
def add_two_numbers(num1, num2):
    return num1 + num2

# Example usage
result = add_two_numbers(5, 3)
print('The sum is:', result)
```

```js title="code-examples.md" linenums="1" hl_lines="2-4"
// Function to concatenate two strings
function concatenateStrings(str1, str2) {
  return str1 + str2;
}

// Example usage
const result = concatenateStrings("Hello, ", "World!");
console.log("The concatenated string is:", result);
```