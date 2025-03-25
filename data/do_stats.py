"""
do_stats.py - example project to calculate statistics

Date: January 2025
"""

#####################################
# Imports At the Top
#####################################

# Import from Python Standard Library for mathematical statistics
import statistics

# Import from local project modules
# Most projects will have a custom logger - you can use ours as is in any project
from utils_logger import logger

#####################################
# Define Reusable Functions
#####################################


def calculate_min(scores: list) -> float:
    """Return the minimum value in the list."""
    return min(scores)


def calculate_max(scores: list) -> float:
    """Return the maximum value in the list."""
    return max(scores)


def calculate_mean(scores: list) -> float:
    """Return the mean (average) of the list."""
    return statistics.mean(scores)


def calculate_standard_deviation(scores: list) -> float:
    """Return the standard deviation of the list."""
    return statistics.stdev(scores)


#####################################
# Define main Function
#####################################


def main(scores: list) -> None:
    """
    Main function to calculate and log statistics for a given list of scores.

    Args:
        scores (list): A list of numbers to calculate statistics for.
    """
    logger.info("Starting MAIN function.")

    # Calculate and log each statistic
    logger.info(f"Scores: {scores}")
    logger.info(f"Minimum: {calculate_min(scores):.2f}")
    logger.info(f"Maximum: {calculate_max(scores):.2f}")
    logger.info(f"Mean: {calculate_mean(scores):.2f}")
    logger.info(f"Standard Deviation: {calculate_standard_deviation(scores):.2f}")

    logger.info("Exiting MAIN function.")


#####################################
# Conditional Execution (run if this file is executed)
#####################################

if __name__ == "__main__":
    logger.info("STATS - Ready for work.")

    # Provide a default list of scores for the program to analyze
    DEFAULT_SCORES = [3.5, 4.0, 4.8, 2.9, 3.7, 4.3, 3.8]

    # Call the main function with the default scores
    main(DEFAULT_SCORES)

    logger.info("STATS - Execution complete.")
