# Getting Started

## Environments setup

For Windows user, we advise to use the [Windows Subsystem for Linux (WSL)](https://learn.microsoft.com/en-us/windows/wsl/install) which allows, among many things, to run Python and compile packages in a Linux environment while accessing your notebooks from Windows. 

To try these examples, clone [this GitHub repository](https://github.com/ThibaultSchowing/IMPTOX_XAI.git) or copy the desired files on your local machine and follow the instructions bellow. 




### Create virtual environments  

Some methods require specific packages and thus, we will use a different virtual environment for each example. Here we create the following: 

1. .venvrf for Random Forest

2. .venvshap to use Gradient SHAP over a simple Neural Network

3. .venvrf can be used again for DIMLP Fidex

4. .venvfuzzycoco for FUGE. The package is not yet publicly available and needs to be compiled locally. 


=== "From scratch"

    ```Python
    # 1 - Start WSL and
    # 2 - Create the virtual environments

    python -m venv .venvrf notebook numpy pandas matplotlib seaborn dimlpfidex kagglehub scikit-learn
    python -m venv .venvshap notebook numpy pandas matplotlib seaborn torch torchaudio torchvision kagglehub scikit-learn
    # - for fuzzy coco installation follow the next step bellow

    ```

=== "From txt files"

    ```Python
    # 1 - Start WSL and
    # 2 - Create the virtual environments from files

    python3 -m venv .venvNAME # Replace .venvNAME with the desired name
    source .venvNAME/bin/activate

    # 3 - Within your virtual environment, install from the given txt file. 
    python3 -m pip install -r requirements.txt

    ```

Once you have your environments created:

```Python
# 3 - Activate the desired environment (replace .venv by the created directory)

source .venv/bin/activate

# 4 - Start the Jupyter server on WSL. Specify a different port for each environment if you run them in parallel

jupyter notebook --no-browser --port 9898

```

---

### Environment for Fuzzy CoCo

Currently FuzzCoCoPython is under developpment and will be soon available for Unix based systems (MacOS and Linux). 

1. Clone [this repository (NOT PUBLIC YET)](). 

```python

python -m venv .venvfuzzycoco notebook numpy pandas matplotlib seaborn 
source .venvfuzzycoco/bin/activate 

# from the fuzzycocopython repository folder
python -m pip install .

```

---


## Google Colab

The notebooks should be available on Colab soon.  

1. Random Forest and Fidex (TODO)
2. DIMPL Fidex (TODO)
3. FuzzyCoCo (TODO)
4. SHAP  (TODO)

---




