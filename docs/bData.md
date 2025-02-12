# Example data

To present the different methods with simplicity, we will use a well known toy dataset

## Context

Here we present a simple dataset from [Kaggle](https://www.kaggle.com/datasets/uciml/pima-indians-diabetes-database) with only numerical data for simplicity. This dataset is originally from the National Institute of Diabetes and Digestive and Kidney Diseases. The objective of the dataset is to diagnostically predict whether or not a patient has diabetes, based on certain diagnostic measurements included in the dataset. Several constraints were placed on the selection of these instances from a larger database. In particular, all patients here are females at least 21 years old of Pima Indian heritage. 


## Content

The datasets consists of several medical predictor variables and one target variable, Outcome. Predictor variables includes the number of pregnancies the patient has had, their BMI, insulin level, age, and so on.



However, there are various way to explain categorical data as well. For example, SHAP can be used to explain where on an image a Neural Network used for object detection focuses



|    |   Pregnancies |   Glucose |   BloodPressure |   SkinThickness |   Insulin |   BMI |   DiabetesPedigreeFunction |   Age |   OUT |
|---:|--------------:|----------:|----------------:|----------------:|----------:|------:|---------------------------:|------:|------:|
|  0 |             1 |        85 |              66 |              29 |         0 |  26.6 |                      0.351 |    31 |     0 |
|  1 |             8 |       183 |              64 |               0 |         0 |  23.3 |                      0.672 |    32 |     1 |
|  2 |             1 |        89 |              66 |              23 |        94 |  28.1 |                      0.167 |    21 |     0 |
|  3 |             0 |       137 |              40 |              35 |       168 |  43.1 |                      2.288 |    33 |     1 |
|  4 |             5 |       116 |              74 |               0 |         0 |  25.6 |                      0.201 |    30 |     0 |
|  5 |             3 |        78 |              50 |              32 |        88 |  31   |                      0.248 |    26 |     1 |
|  6 |            10 |       115 |               0 |               0 |         0 |  35.3 |                      0.134 |    29 |     0 |
|  7 |             2 |       197 |              70 |              45 |       543 |  30.5 |                      0.158 |    53 |     1 |



=== info "Using categories and other data types"
    If your data contain categories, models like Random Forest can easilly include them. However, this is not the case for Neural Networks and Fuzzy Logic with FUGE. To circumvent this, you can either convert your cartegories to numbers, if it makes sense or use [one-hot encoding](https://en.wikipedia.org/wiki/One-hot). For Neural Networks for object detection in images, SHAP can be applied to show the region of the image leading to the decision. You can find more details on the [HES-XPLAIN](https://hes-xplain.github.io/) plateform. 