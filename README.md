# python-challenge


Financial Analysis 

Overview

This repository contains Python scripts to analyze financial records and election poll data. The projects aim to demonstrate the ability to process large datasets using Python, perform calculations, and present the results in a user-friendly format.

Projects

PyBank

In the PyBank challenge, the task is to analyze the financial records of a company using a dataset called `budget_data.csv`. The dataset includes two columns: "Date" and "Profit/Losses". 

#### Objectives

The script performs the following analyses:
- Calculate the total number of months included in the dataset.
- Calculate the net total amount of "Profit/Losses" over the entire period.
- Calculate the changes in "Profit/Losses" over the entire period and the average of those changes.
- Identify the greatest increase in profits (date and amount) over the entire period.
- Identify the greatest decrease in profits (date and amount) over the entire period.

#### Expected Output

The analysis align with the following results:

Financial Analysis
----------------------------
- Total Months: 86
- Total: $22564198
- Average Change: $-8311.11
- Greatest Increase in Profits: Aug-16 ($1862002)
- Greatest Decrease in Profits: Feb-14 ($-1825558)


Election Result Analysis 
PyPoll

In the PyPoll challenge, the task is to modernize the vote-counting process for a small rural town using a dataset called `election_data.csv`. This dataset consists of three columns: "Voter ID", "County", and "Candidate".

 Objectives

The script performs the following analyses:
- Calculate the total number of votes cast.
- Generate a complete list of candidates who received votes.
- Calculate the percentage of votes each candidate won.
- Calculate the total number of votes each candidate won.
- Identify the winner of the election based on popular vote.

Expected Output

The analysis align with the following results:

Election Results
-------------------------
- Total Votes: 369711
-------------------------
- Charles Casper Stockham: 23.049% (85213)
- Diana DeGette: 73.812% (272892)
- Raymon Anthony Doane: 3.139% (11606)
- -------------------------
- Winner: Diana DeGette
- -------------------------
