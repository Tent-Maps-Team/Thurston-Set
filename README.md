# Thurston Set

A program to efficiently generate points in the Thurston Set.

## Background

The purpose of the research is to better understand and approximate the Thurston Set. This project was computational in nature and Python was used to collect our data. The data set contains encoded itineraries that can be used to compute values that are elements of the Thurston Set. A visual approximation of the Thurston Set can be found [here](http://www-personal.umich.edu/~kochsc/wptEntropy.pdf), on the first page Thurston’s own paper. The data can also be used to study the distribution of superattracting beta values within the interval (1, 2] and to explore an analogous Mandelbrot-Julia Correspondence. This research was conducted through the Lab of Geometry at Michigan under the advisement of Harrison Bray during the Fall semester of 2019.

## Methods

At a high level, we first iterate over all possible itinerary sequences of length less than 34 and encode them as a list of the positions of 1’s in the original binary sequence to save memory. Then, we check which encoded itineraries correspond to a superattracting beta value using the [Milnor-Thurston admissibility criterion](http://www-personal.umich.edu/~kochsc/MilnorThurston.pdf). Next, we ruled out the vast majority (not all) of redundant encoded itineraries. Finally, we saved the unique encoded itineraries into folders named for their length, as the encoding is meaningful only when paired with the length. We utilized multithreading to speed up this exhausting computation. All work was done in Python.

## Folders
### Root
Contains the main Python scripts for generating points in the Thurston Set.
#### Visualizations
Contains uses of the data generated from the main script.
##### Outputs
Contains various images and animations developed from the generated data.
##### Scripts
Contains the scripts that generated the aforementioned outputs
## Links

[TODO], we can fill in arxiv, deep blue, logm, etc

## Contributors

[TODO] will steal from the paper
## License
[Creative Commons - Attribution Non-Commercial](https://creativecommons.org/licenses/by/3.0/)
