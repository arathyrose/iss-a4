# Introduction to Software Systems: Assignment 4

## Introduction
This project was made by Arathy Rose Tony and Aryaman Shrey as an assignment for Introduction to Software Systems course.

## Disclaimer
This project was made solely for the purpose of an assignment and the content used in this app are in no way owned or distributed by us.

## What is this?
Here we have rewritten the Cryptography Experiment 3 of Virtual labs regarding One-time pad and Perfect Secrecy(link: http://cse29-iiith.vlabs.ac.in/exp3/index.php) using flask framework. 

## Prerequisites
This experiment was developed primarily using Python-Flask. Check out requirements.txt for the exact version of each prerequisites.

## To run it locally

1. Clone this repository
`git clone https://gitlab.com/arathyrose2000/itss-assignment-4`
2. Change directory to app
`cd app`
3. Run the command to set up the server
 `python3 run.py`

If you get a message that indicates that your server is up and running, you are good to go. 
If it shows some error then install the required libraries using pip3. If that does not work, notify the developers by posting an issue here.

# Functionality of each file:

- run.py: contains everything from routing to models to running the main app
- vernam.py: contains the python functions for encrypting and decrypting the files
- Answers.db: database for storing all the questions along with the correct answers
- test.py: supposed to do unit testing. Currently does not work
The remaining files have their usual meanings