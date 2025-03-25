"""
draw_chart.py - Create a basic Seaborn chart using the Penguins dataset.

Date: January 2025
"""

#####################################
# Imports At the Top
#####################################

# Import from external dependencies (must be installed)
# See requirements.txt 
import seaborn as sns
import matplotlib.pyplot as plt

# Import from local project modules
from utils_logger import logger

#####################################
# Define main Function
#####################################


def main() -> None:
    """Create and display a scatter plot of penguin data."""
    logger.info("Starting main function.")

    try:
        # Load the Penguins dataset
        data = sns.load_dataset("penguins")
        logger.info("Loaded penguins dataset successfully.")

        # Create a scatter plot
        sns.scatterplot(data=data, x="bill_length_mm", y="bill_depth_mm", hue="species")
        plt.title("Penguin Bill Dimensions by Species")
        plt.xlabel("Bill Length (mm)")
        plt.ylabel("Bill Depth (mm)")

        logger.info("NOTE: Close the chart window to continue and exit the script.")
        plt.show()
        logger.info("Exiting main function.")

    except Exception as e:
        logger.error(f"Error creating chart: {e}")


#####################################
# Conditional Execution
#####################################

if __name__ == "__main__":
    logger.info("CHARTS - Ready for work.")
    main()
    logger.info("CHARTS - Execution complete.")
