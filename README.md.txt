Instructions:

In preprocNDparse,

1. Provide input tex file to level_1_parse.py
a. Use python 2 
b. Run "python level_1_parse.py" after placing in "./Tex-files/" repository

2. Pass the output to level_2_parse.py
a. Use python 3
b. Run "python level_2_parse.py 1" after correcting basepath_orig, destpath_new, basepath if needed(flag 1 if we want to remove math equations)

3. Now, pass the output to level_3_parse.py
a. Use python 3
b. Run "python level_3_parse.py" and place list of outputs in "./data-cat-all/" directory

4. Use this output as input to lexrank.py and obtain the labels using "python lexrank.py 3 data.txt"

5. The obtained output is appended to the obtained output file by running "append.py" and adding to appropriate directory.

All these steps have been performed and the output files are stored in main/input_data_final

6. Now, call make_datafiles.py and obtain tokenized files in input_data_tokenized_final and also run write_to_bin to get a concatenated train.bin or individual bins.
Here, we got a concatenated bin

7. Use this bin as input to run summarizer as mentioned in README.md in main/pointer_generator

8. The main/finished_files_final/log2 contains the required model which could be tested with the bins as mentioned in the pointer_generator README/