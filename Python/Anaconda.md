For Windows

### 1. Install Anaconda
> https://docs.anaconda.com/anaconda/install/windows/

### 2. Start conda prompt
> From start in menu, type command: Ananconda Prompt

### 3. update conda
> conda update conda

### 4. list environment
> conda env list

### 5. create a new environment with specific python version
> conda create --name <env-name> python=3.7

### 6. switch to specific environment
> activate <env-name>

in Linux:
> source activate <env-name>

### 7. update pip
> python -m pip install --upgread pip

### 8. install package
> conda install <package-name>

### 9. exit environment
> deactivate

in Linux:
> source deactivate

### 10. remove a package from specific environment
> conda remove --name <env-name> <package-name>

### 11. remove a specific environment
> conda env remove --name <env-name>
