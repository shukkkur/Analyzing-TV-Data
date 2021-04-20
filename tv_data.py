import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style()
pd.options.display.max_columns = None

# Load the CSV files
super_bowls = pd.read_csv('super_bowls.csv')
tv = pd.read_csv('tv.csv')
halftime_musicians = pd.read_csv('halftime_musicians.csv')


# Inspecting for NaN values
##super_bowls.info()
##tv.info()
##halftime_musicians.info()

# Distribution of Points Combined
##plt.hist(super_bowls.combined_pts, edgecolor='k')
##plt.show()

# Plot a histogram of point differences
##plt.hist(super_bowls.difference_pts)
##plt.xlabel('Point Difference')
##
##plt.ylabel( 'Number of Super Bowls')
##plt.show()
##
### Display the closest game(s) and biggest blowouts
##print(super_bowls[super_bowls.difference_pts == 1])
##print(super_bowls[super_bowls.difference_pts >= 35])

games_tv = pd.merge(tv[tv['super_bowl'] > 1], super_bowls, on='super_bowl')

#sns.regplot(x=super_bowls.difference_pts, y=tv.share_household)



# Create a figure with 3x1 subplot and activate the top subplot
##plt.subplot(3, 1, 1)
##plt.plot(tv.super_bowl,tv.avg_us_viewers, color='#648FFF')
##plt.title('Average Number of US Viewers')
##
### Activate the middle subplot
##plt.subplot(3, 1, 2)
##plt.plot(tv.super_bowl, tv.rating_household, color='#DC267F')
##plt.title('Household Rating')
##
### Activate the bottom subplot
##plt.subplot(3, 1, 3)
##plt.plot(tv.super_bowl,tv.ad_cost, color='#FFB000')
##plt.title('Ad Cost')
##plt.xlabel('SUPER BOWL')
##
### Improve the spacing between subplots
##plt.tight_layout()
##plt.show()


