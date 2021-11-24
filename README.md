# CS50 Final Project

This is my CS50 Final Project Repository.

## Gringotts

Gringotts is a web app designed to help small businesses with calculating end of day takings.
Its inception was inspired by real-world problems encountered during my career as a community pharmacist.

## Features

Gringotts allows users to register to create an account, login to add a new entry, and review their previous entries via History.

## New Entry
Opens a new entry for the user to log the total takings for the day.
The user is prompted to fill in the forms, which includes: Expected total, cheque, and quantity of notes/coins collected for each value.
The bottom row reflects on the changes made in the forms, calculating total cash collected, cash + cheque, expected total, and variance.
Variance = (Cash + Cheque) - Expected total
The user may save and submit the entry once satisfied. The entry is then saved into SQLite3 executed with SQLAlchemy commands.

## History
Allows the user to view all past entries made by the user.
Data is presented in a table format with columns: Date, Cash, Cheque, Cash + Cheque, Expected Total, Variance.

## Future
Some features that may be implemented in the future include:
- Downloading entries as a csv format
- Edit user's previous entries
- Delete user's previous entries