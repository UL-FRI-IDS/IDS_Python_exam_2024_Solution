# Hands-on exam 1 - IMDB top 250 movies scraping and analysis

This exam will check the basic knowledge of Python and Web scraping during the course Introduction to Data Science. If you use some other language, transform the whole repository accordingly.

Update the marked parts in this document with your answers. Implement Jupyter notebooks or otherwise organize the repository to be fully reproducible. 


Data retrieval and Data exploration parts are standalone, but use the same data. The intended workflow is to produce a JSON file with all scraped data in `01_data_retrieval.ipynb` and use it to complete `02_data_retrieval.ipynb`.

**We provide a small subset (5 entries) of the expected scraped data format that should be the result of `01_data_retrieval.ipynb` in `sample_output.json`.**

## 1. Environment setup

Before you start working on the task, create an empty environment (e.g., using conda or virtualenv) which you will use for the tasks below.

```
TODO: Add here all the commands you needed to enter to set up the environment.
```

## 2. Implement data retrieval

Implement web scraping of IMDB top 250 movies in `01_data_retrieval.ipynb` and save the run version of the notebook, along with a single JSON file with all the data.

## 3. Implement data analysis

Implement data exploration of IMDB top 250 movies in `02_data_exploration.ipynb` and save the run version of the notebook.

## 4. Make your work reproducible

During your work you may have used some libraries that need to be installed prior running your code. Export a list of your dependencies to a file that could be directly used to set up the environment (step 1 above).

## 5. Double-check your submitted work

Go through the instructions again and make sure that you implemented everything as requested, added comments/instuctions, ... and also pushed everything to the remote repository. Especially check the following:

- Your code runs, notebook shows outputs and is saved.
- You updated all the marked parts of this *README.md*.
- You implemented the two Jupyter notebooks (01_data_retrieval.ipynb and 02_data_exploration.ipynb), and the scraped data (single JSON file) along with the environment specification and pushed everything to the remote repository.
