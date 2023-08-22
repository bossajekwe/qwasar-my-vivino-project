# Welcome to My Vivino
## Task
The Task here is to scrape the vivino website and build a recommendation system

## Description
To solve the problem I have used a host of modules , the modules are listed below;
we imported

1. the Selenium module for scraping data from the vivino website.
2. The Pandas library for reading the wines data csv.
3. The Numpy  library for mathematical or matrix-like operations
4. The Matplotlib, Seaborn, and Plotly libraries for making visualizations
5. The Json library for reading json file
6. The Scipy library for converting a dense matrix to a sparse matrix
7. The sklearn library which has many tools such as csr_matrix, StandardScaler, NearestNeighbors and Cosine_Similarity.


## Installation
This Project does not need any form of installations, However, Python, Jupyter notebook and other dependencies
must be installed before the proejct can work as it should.

## Usage
This project was desgined as a class called `WineRecommender`.

To initiate the class, you will pass in the dataset to the class in this format

`wr=WineRecommender(df)`

to recommdend wines you will have to choose a method for the recommendation method `KNeighbors` or `Similarity`
to initiate the `KNeighbors` you will pass in the following code 

`recommendation = wr.recommend(pos=None, recommend_by="rating", method="KNeighbors")`

where `pos` is an index from between 0 and 1259, `recommend_by` is the specific column in  the dataset you want to 
base the recommendation upon. The default setting is `rating` and `KNeighbors` is the recommendation algorithm.

To initiate the `Similarity` algorithm, you will pass the following code;

`recommendation=wr.recommdend(winery=None, name=None,method="Similarity")` 

where, `winery` is the brand name of the wine and `name` is the actual name of the wine and `Similarity` is 
the recommendation algorithm.

Other parameters include:
`n_neighbors` which is the number of neighbors you want returned. default is 11.
`sim_elem` which is the number of similar elements you want returned. default is 11.
`algorithm` which is the type of algorithm when using `



### The Core Team
Ajekwe Moses Zanzan(ajekwe_m)
Nana Aisha Muhammad (muhammad_n)

<span><i>Made at <a href='https://qwasar.io'>Qwasar SV -- Software Engineering School</a></i></span>
<span><img alt='Qwasar SV -- Software Engineering School's Logo' src='https://storage.googleapis.com/qwasar-public/qwasar-logo_50x50.png' width='20px'></span>
