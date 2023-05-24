# Overview of Project and Code

<table>
<tr>
<td>

The task involves the following steps:

1. **Trace Data**: The malware attacks are captured in the form of trace data, which are sequences of actions. The goal is to group these traces into malware families based on similarity.

2. **Group into Families**: For simplicity, we are considering three traces, T1, T2, and T3.

3. **Compare Traces**: Each trace is compared with the others. The comparison involves taking the union of trace actions and constructing a directed complete graph.

4. **Construct Directed Graph**: A directed complete graph is constructed for each trace, GT1 and GT2, with nodes representing the union of trace actions and each edge labeled with 1.

5. **Compute Occurrences**: The occurrences of each pair of trace action are computed and added to the edges of the graph.

6. **Weight Node Values**: The values of each node in each of the graphs, GT1 and GT2, are weighted. For a node, if the edge weights to other nodes are computed, the new weights will be the old weight divided by the sum of all weights.

7. **Compute Similarity Metric**: A similarity metric is computed between GT1 and GT2 using Kullback-Leibler divergence, Jansen-Shannon, or Wasserstein metric. This metric measures how dissimilar the two graphical structures are.

8. **Output**: The output is a directed completed graph with nodes as trace, T1, T2, and T3 with edge values as the similarity metric.

This process is repeated for hundreds of traces to compute similarities and create a similarity directed graph. The graph can be stored in matrix form or dictionary, depending on what is most comfortable for you.

</td>
<td>

<img src="./images/mermaid-diagram-2023-05-17-195646.svg" width = "100%" height = "100%">

</td>
</tr>
</table>

# The Code

## overview of DriverAlt.py

This Python script is designed to analyze and compare malware trace data. Here's a breakdown of what the script does:

1. **Importing Libraries**: The script begins by importing the math and sys libraries.

2. **Function Definitions**: The script defines several functions that are used to analyze the trace data:

   - `compareTo()`: This function compares two input files. If the files are different, it passes them to the data comparison function.

   - `states_to_arr()`: This function reads two input files and creates two arrays, each containing the states (actions) of a trace from a file.

   - `stArr_union()`: This function creates a union of the states from the two files.

   - `create_all_trans()`: This function creates all possible transitions from the union of the file states.

   - `create_file_trans()`: This function creates an array that stores the transitions that occur in each file.

   - `get_counts()`: This function returns the counts for all of the possible transitions.

   - `get_first_total()`: This function creates an array that contains the total number of transitions away from the first state in each transition.

   - `get_probabilities()`: This function creates an array that stores probabilities associated with transitions.

   - `get_KL()`: This function calculates the Kullback-Leibler (KL) divergence, a measure of how one probability distribution diverges from a second, expected probability distribution.

   - `get_JSD()`: This function calculates the Jensen-Shannon divergence (JSD), a method of measuring the similarity between two probability distributions.

3. **Main Method**: The main part of the script uses the above functions to analyze and compare the trace data. It reads in trace files, calculates the KL divergence and JSD for each pair of files, and stores these values in matrices. The matrices are then written to CSV files for further analysis.

In summary, this script is a tool for analyzing malware trace data. It reads in trace data from files, analyzes the data to find patterns and similarities, and outputs the results in a format that can be easily analyzed further.


## Explination of RecursiveLCS.py

The code provided is implementing the following logic:

1. **Importing the 'sys' library**: This allows you to pass command line arguments. The 'SysArg' variable is an integer input subtracted by 1 that will later be used to specify which dataset to use.

2. **Hardcoded Datasets**: There are 3 datasets hardcoded as lists containing groups of malware traces.

3. **Function Definitions**: Several functions are defined:

   - `LCSubStr(X, Y)`: Calculates the length of the longest common substring (continuous) between strings X and Y. It constructs a 2D matrix `LCSuff`, where `LCSuff[i][j]` contains the length of the longest common suffix of substrings for X[0...i-1] and Y[0...j-1].

   - `lcs(X, Y)`: Calculates the length of the longest common subsequence (non-continuous) between strings X and Y. It constructs a 2D matrix `L`, where `L[i][j]` contains the length of the longest common subsequence of X[0...i-1] and Y[0...j-1].
 
   - `RecursiveLCSSeq(inpStrList)`: Recursively computes the longest common subsequence among a list of strings by calling the `lcs()` function repeatedly. It continues calculating until there's a single longest common subsequence left, and then it prints "LCSSeqDONE" and returns the result.
 
   - `RecursiveLCSStr(inpStrList)`: Recursively computes the longest common substring among a list of strings by calling the `LCSubStr()` function repeatedly. It continues calculating until there's a single longest common substring left, and then it prints "LCSStrDONE" and returns the result.

   - `states_to_list(file1)`: Given an input file name (as an integer/string), this function reads from the respective file, processes its content into a list of integers, and returns the list.

4. **Main Driver**: The main driver of the code starts by selecting one of the predefined datasets.

## Explination of NetworkAnalysis.R

This R script is used for network analysis using the `igraph` package. The script performs the following steps:

1. **Data Loading**: The script starts by loading a CSV file named `CompleteJSD.csv` from a specified directory. This file is stored in a variable called `Data`.

2. **Reading Multiple CSV Files**: The script then sets a working directory and reads all CSV files in that directory. Each file is read into a separate data frame and all data frames are stored in a list called `MyData`.

3. **Minimum Spanning Tree and Plotting**: For each data frame in `MyData`, the script computes a minimum spanning tree (MST) and plots it. The MST is computed using the `minimum.spanning.tree` function from the `igraph` package. The MST is a subgraph of the original graph that connects all vertices with the minimum possible total edge weight.

4. **Graph Creation and MST**: The script then creates a graph `G` from the adjacency matrix `Data` and computes its MST `Gmst`.

5. **Graph Visualization**: The script visualizes the MST graph `Gmst` in various ways. It plots a histogram of node degrees, a network plot, and highlights hubs and authorities in the graph. Hubs and authorities are important nodes in a network, identified using the `hub_score` and `authority.score` functions from the `igraph` package.

6. **Community Detection**: The script performs community detection on the MST graph using the edge betweenness method. This method identifies communities in a network by removing edges with high betweenness centrality. The resulting communities are visualized using a dendrogram.

The script ends by viewing the structure of the community network and printing the communities.

# How the Code Helps with the Project

The provided code is instrumental in the project as it performs several key tasks:

1. **Analyzing Malware Traces**: The Python scripts (`DriverAlt.py` and `RecursiveLCS.py`) are used to analyze malware traces. They compare different traces and calculate similarity metrics between them. This helps in grouping similar traces together, which is a crucial step in malware analysis.

2. **Network Analysis**: The R script (`NetworkAnalysis.R`) performs network analysis on the similarity metrics calculated by the Python scripts. It constructs graphs and computes minimum spanning trees, which are then visualized in various ways. This helps in understanding the structure and relationships between different malware traces.

3. **Community Detection**: The R script also performs community detection on the graphs. This helps in identifying clusters of similar malware traces, which can be useful in understanding the behavior and characteristics of different malware families.

# When to Use the Code

The code should be used in the following steps of the project:

1. **Trace Data Analysis**: After collecting the malware trace data, use the Python scripts to analyze and compare the traces. This involves running `DriverAlt.py` to calculate similarity metrics between traces, and then running `RecursiveLCS.py` to find the longest common subsequence and substring among traces.

2. **Network Construction and Analysis**: Once the similarity metrics have been calculated, use the R script to construct graphs based on these metrics. This involves running `NetworkAnalysis.R` to create graphs, compute minimum spanning trees, and visualize the graphs.

3. **Community Detection**: After constructing and analyzing the graphs, use `NetworkAnalysis.R` to perform community detection on the graphs. This will help in identifying clusters of similar malware traces.

In summary, the provided code is a crucial part of the project that aids in analyzing malware traces, constructing and analyzing networks of traces, and detecting communities within these networks.

