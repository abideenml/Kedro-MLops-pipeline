# churn-modeling

## Overview

This is your new Kedro project, which was generated using `kedro 0.18.13`.

Take a look at the [Kedro documentation](https://docs.kedro.org) to get started.

## Rules and guidelines

In order to get the best out of the template:

* Don't remove any lines from the `.gitignore` file we provide
* Make sure your results can be reproduced by following a data engineering convention
* Don't commit data to your repository
* Don't commit any credentials or your local configuration to your repository. Keep all your credentials and local configuration in `conf/local/`

## How to install dependencies

Declare any dependencies in `src/requirements.txt` for `pip` installation and `src/environment.yml` for `conda` installation.

To install them, run:

```
pip install -r src/requirements.txt
```

## How to run your Kedro pipeline

You can run your Kedro project with:

```
kedro run
```

## How to test your Kedro project

Have a look at the file `src/tests/test_run.py` for instructions on how to write your tests. You can run your tests as follows:

```
kedro test
```

To configure the coverage threshold, go to the `.coveragerc` file.

## Project dependencies

To generate or update the dependency requirements for your project:

```
kedro build-reqs
```

This will `pip-compile` the contents of `src/requirements.txt` into a new file `src/requirements.lock`. You can see the output of the resolution by opening `src/requirements.lock`.

After this, if you'd like to update your project requirements, please update `src/requirements.txt` and re-run `kedro build-reqs`.

[Further information about project dependencies](https://docs.kedro.org/en/stable/kedro_project_setup/dependencies.html#project-specific-dependencies)

## How to work with Kedro and notebooks

> Note: Using `kedro jupyter` or `kedro ipython` to run your notebook provides these variables in scope: `context`, `catalog`, and `startup_error`.
>
> Jupyter, JupyterLab, and IPython are already included in the project requirements by default, so once you have run `pip install -r src/requirements.txt` you will not need to take any extra steps before you use them.

### Jupyter
To use Jupyter notebooks in your Kedro project, you need to install Jupyter:

```
pip install jupyter
```

After installing Jupyter, you can start a local notebook server:

```
kedro jupyter notebook
```

### JupyterLab
To use JupyterLab, you need to install it:

```
pip install jupyterlab
```

You can also start JupyterLab:

```
kedro jupyter lab
```

### IPython
And if you want to run an IPython session:

```
kedro ipython
```

### How to convert notebook cells to nodes in a Kedro project
You can move notebook code over into a Kedro project structure using a mixture of [cell tagging](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#release-5-0-0) and Kedro CLI commands.

By adding the `node` tag to a cell and running the command below, the cell's source code will be copied over to a Python file within `src/<package_name>/nodes/`:

```
kedro jupyter convert <filepath_to_my_notebook>
```
> *Note:* The name of the Python file matches the name of the original notebook.

Alternatively, you may want to transform all your notebooks in one go. Run the following command to convert all notebook files found in the project root directory and under any of its sub-folders:

```
kedro jupyter convert --all
```

### How to ignore notebook output cells in `git`
To automatically strip out all output cell contents before committing to `git`, you can run `kedro activate-nbstripout`. This will add a hook in `.git/config` which will run `nbstripout` before anything is committed to `git`.

> *Note:* Your output cells will be retained locally.

## Package your Kedro project

[Further information about building project documentation and packaging your project](https://docs.kedro.org/en/stable/tutorial/package_a_project.html)



# Customer Churn Predictor
> [Link to Churn Predictor](https://churnpredictorzain.herokuapp.com/)

Customer churn is the percentage of customers your business lost in a set period of time. For instance, if you had 100 customers at the beginning of the month, and lost 
10 of them throughout the month, you had a 10% churn rate for the month.

In this project, I have addressed the problem of churning of customers. I have aggregated data of a Telecommunication company and applied EDA on the data. After 
understanding the data, I have applied many classification models on it like decision tree classifier, random forest, xgboost, logistic regression, LGBM, SVM, 
adaboost, neurel network, Naive Bayes and random forest after PCA.

The results were:

![results](https://user-images.githubusercontent.com/89645252/187369580-07c153a7-53f4-4006-b629-51cd8c732cd7.png)

After that I made a Flask api which takes all the parameters and returns the result back. I deployed the project on Heroku.

I have also made a Power BI report to better understand and visualize the data.

![image](https://user-images.githubusercontent.com/89645252/187371913-e38959bf-e263-4536-ba41-293d871466ed.png)
![image](https://user-images.githubusercontent.com/89645252/187371984-3dbe3c1c-47fc-4588-8f26-0a573d501302.png)
![image](https://user-images.githubusercontent.com/89645252/187372189-ea2ed519-73ba-439b-8570-81d6cc96fb73.png)
![image](https://user-images.githubusercontent.com/89645252/187372251-e7fb19fe-ea00-4c1e-90cc-968970ba03e3.png)

