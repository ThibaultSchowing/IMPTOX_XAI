# IMPTOX - Data Analysis

These pages aim to guide IMPTOX members in creating and interpreting models for tabular numerical data. The shown sample workflows assume fully numeric datasets, including ordinal categories or one-hot encodings, and focuses on predicting a target variable (classification or regression). To illustrate these methods, we will apply XAI techniques to well-known example datasets such as the [Pima Indians Diabetes Database](https://www.kaggle.com/datasets/uciml/pima-indians-diabetes-database) and the [Heart Disease Dataset](https://www.kaggle.com/datasets/johnsmith88/heart-disease-dataset).

!!! info "The project"

    Microplastics and nanoplastics (MNP) are a growing concern for human health and the environment. The IMPTOX project brings together scientists from diverse fields—chemistry, biology, and medicine to investigate this pressing issue. Whether you're measuring MNP in environmental or animal samples, studying their impact on biofilms, tracking them as pathogen carriers, or exploring medical effects such as allergies, ==the project generates a wealth of complex and valuable data==.

    Data is only the beginning. How do we extract meaningful insights or create prediction models from high dimentional and complex data? This is where machine learning (ML) and Explainable Artificial Intelligence (XAI) come into play. XAI helps transform data into knowledge by offering transparent and interpretable models that reveal the why behind predictions.



??? note "How machine learning could help with your research?"

    - **Environmental Insights:** Could patterns in environmental data reveal which microplastic types are present or how they are distributed across ecosystems?  
    - **Pathogen Risks:** Can we uncover hidden relationships between microplastic chemical properties and their role in fostering pathogen growth?  
    - **Health Predictions:** Is it possible to predict health outcomes, such as allergic responses, based on exposure to microplastics combined with patient genotype ?  

    Machine learning allows you to go beyond observations, transforming data into predictions and new hypotheses. With XAI methods, these predictions become understandable and scientifically valuable, allowing to eliminate unused variables and focus on important ones, opening doors to optimized research paths.  






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

=== "SHAP"

    By slightly modifying a model imputs many times and studying the outcome of the model, SHAP is a post-hoc method capable to explain how each variable influences the results for each observation data. 

    Include figures ?

    ![Average influence of variables](./assets/img//GSHAP_MLP.png)
    
=== "DIMLP Fidex"

    ```py
    def main():
        print("Hello world!")

    if __name__ == "__main__":
        main()
    ```
=== "Fuzzy CoCo"

    ```py
    def main():
        print("Hello world!")

    if __name__ == "__main__":
        main()
    ```




## Made With MkDocs

For full documentation visit [mkdocs.org](https://www.mkdocs.org).

### Commands

* `mkdocs new [dir-name]` - Create a new project.
* `mkdocs serve` - Start the live-reloading docs server.
* `mkdocs build` - Build the documentation site.
* `mkdocs -h` - Print help message and exit.

### Project layout

    mkdocs.yml    # The configuration file.
    docs/
        index.md  # The documentation homepage.
        ...       # Other markdown pages, images and other files.



[Documentation](https://squidfunk.github.io/mkdocs-material/getting-started/)!