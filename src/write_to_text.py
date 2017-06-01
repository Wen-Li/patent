# this file reads in .csv files and write docId, appId, abstractText to a text file
# input: path (where .csv files are), filename (where output file writes)
# output: a text file with docId, appId, abstractText

#####################################
# CHANGE IN_PATH & OUT_PATH IN MAIN
#####################################

import gzip
import pandas as pd
import os

def get_paths(directory):
    file_paths = []  # List which will store all of the full filepaths.
    # Walk the tree.
    for root, directories, files in os.walk(directory):
        for filename in files:
            # Join the two strings in order to form the full filepath.
            if filename.endswith(".csv"):
                filepath = os.path.join(root, filename)
                file_paths.append(filepath)  # Add it to the list.
    print("Files collected:")
    for f in file_paths:
        print(f)
    return file_paths

def write_to_text(in_file_paths, out_path):
    with open(out_path, "w") as f:
        line_count = 0
        for file_path in in_file_paths:
                # grant is a dataframe
            grant = pd.read_csv(file_path, error_bad_lines=False)
            for index, row in grant.iterrows():
            # for row in grant:
                # read a row
                if pd.notnull(row['abstractText']):
                    line_count += 1
                    if line_count % 10000 == 0:
                        print("Processing line {}...".format(line_count))
                    f.write("\t".join([str(row['docId']), str(row['applicationId']), str(row['abstractText'])]))
                    f.write("\n")
    print("No. of abstracts:", line_count)
    return

# def write_to_csv(in_file_paths):
#     line_count = 0
#     for file_path in in_file_paths:
#         out_path = file_path.rstrip(".gz")
#         # f_writer = open(out_path, "w")
#         with gzip.open(file_path, "rb") as f_in:
#             # grant is a dataframe
#             grant =  pd.read_csv(f_in, error_bad_lines=False)
#             grant = grant.dropna(axis=0, how="any")
#             grant.to_csv(out_path, sep="\t",
#                          columns=["docId", "applicationId", "abstractText"],
#                          index=False)
#         # f_writer.close()
#     print("No. of abstracts:", line_count)
#     return

if __name__ == "__main__":
    # read files by year
    for i in range(2010, 2017):
        in_path = "../grant_text3/grantYear={}".format(str(i))
        out_path = "../data/docid_appid_abstract_{}.txt".format(str(i))

        files = get_paths(in_path)
        write_to_text(files, out_path)