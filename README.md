# Decision Tree Classification Tool

When complete this tool will generate a decision tree, prune it to a more reasonable size and then evaluate the tree. Once it is done, this tree will be useful for classifying data points or predicting the values.

To use it you will give it a CSV file where the last column is the one you want to predict (I may add customisation to the target later) and it will work with quantitative and qualitative data by correctly adjusting its algorithm.

## Currently Implemented Features

- Interprets CSVs
- Evaluates most useful decision at a specific node using information theory, specifically using entropy not Gini index. Currently only works on quantitative
- Only uses 80% of the database to train

## Next Features

- Evaluate most beneficial decision for qualitative data
- Allow creation of multiple nodes to form a tree
- Prune the tree based off user specification
- Evaluate the tree with the other 20% of the database
- Interpret the tree (classify or predict data)
- Implement calling from command line

## Weather Classification Data

This is the database I have been using to test the program. It is super basic and contains 13000 separate data points.
