# Election_Analysis
UT Bootcamp Module 3 - Python

## Overview of Election Audit
This project is for UT Data Science Bootcamp Challege 3 HOmework. The scenario is counting and displaying results of an election.

The project was written in Python 3.7.6 using VS Code on Windows laptop. The data source was a provided csv file.
 

## Election Audit Results
The total number of votes cast in the three counties was 369,711. 

Breakdown by County:
Arapahoe had 24,801 votes (6.7% of total)
Denver had 306,055 votes (82.8% of total)
Jefferson had 38,855 votes (10.5% of total)

Denver had the largest number of votes.

Breakdown by Candidate:
D. DeGette had 272,892 votes (73.8%)
R. Doane had 11,606 votes (3.1%)
C. Stockham had 85,213 votes (23.0%)

Diana DeGette won the election with 272,892 votes (73.8%).

There was zero evidence of voter fraud despite the loser's attempts to claim otherwise.


## Election Audit Summary
This script can be reused in future election analysis. The names of counties and candidates were read in from the file. Thus, as long as the csv file read in contains this information, the script can be reused. It would be necessary to have the same information in the same column order. That is, the first column (which was not used) was ballot id, the second column was county name, and the third column was candidate name.

Possible modifications to the script include: (1) Showing the breakdown for each candidate within each county in a table and (2) Modifying the winner declaration code to ensure that the winner is only declared as such if earning more than 50% of the vote. As it stands now, the winner is the highest percent. With three or more candidates, it is possible that the highest percent is not over 50%. In that case, the script could be modified to indicate that a runoff election is needed between the two candidates with the most votes.

