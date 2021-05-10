#PyPoll UT Bootcamp Module 3

# Import statements
import csv
import os

# Load file path for reading file
file_to_load = os.path.join("Resources","election_results.csv")
# Create filename for creating file to write to
file_to_save = os.path.join("Analysis","election_analysis.txt")

# Open data and read the file
with open(file_to_load) as election_data:  # with statement doesn't require a close
    file_reader = csv.reader(election_data)

    headers = next(file_reader) #read and print the header row
    print(headers)


# Perform analysis



# Find total number of votes cast
# Find complete list of candidateswho rec'd votes
# Find total number of votes for each candidate
# Compute % of total votes for each candidate
# Determine winner of election


# Write data using open() function
with open(file_to_save, "w") as txt_file:
    txt_file.write("Arapahoe\n")
    txt_file.write("Denver\n")
    txt_file.write("Jefferson")
#outfile = open(file_to_save, "w")
# Write some data to the file
#outfile.write("Hola Mundo.")
#outfile.close()
