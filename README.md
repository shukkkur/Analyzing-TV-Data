# Analyzing-TV-Data
![Forks](https://img.shields.io/github/forks/shukkkur/Analyzing-TV-Data.svg)
![Stars](https://img.shields.io/github/stars/shukkkur/Analyzing-TV-Data.svg)
![Watchers](https://img.shields.io/github/watchers/shukkkur/Analyzing-TV-Data.svg)
![Last Commit](https://img.shields.io/github/last-commit/shukkkur/Analyzing-TV-Data.svg) 

<p>Using data manipulation and visualization techniques to explore one of two different television broadcast datasets: The Super Bowl and hit sitcom The Office!</p>


### TV, halftime shows, and the Big Game
After exploring and cleaning our data a little, we're going to answer the following questions:
- What are the most extreme game outcomes?
- How does the game affect television viewership?
- How have viewership, TV ratings, and ad cost evolved over time?
- Who are the most prolific musicians in terms of halftime show performances?

```python
# Load the CSV data into DataFrames
super_bowls = pd.read_csv('super_bowls.csv')
tv = pd.read_csv('tv.csv')
halftime_musicians = pd.read_csv('halftime_musicians.csv')
```
|   |    date    | super_bowl |       venue       |     city    |    state   | attendance |      team_winner     | winning_pts |   qb_winner_1  | qb_winner_2 |  coach_winner  |      team_loser      | losing_pts | qb_loser_1 | qb_loser_2 |   coach_loser  | combined_pts | difference_pts |
|:-:|:----------:|:----------:|:-----------------:|:-----------:|:----------:|:----------:|:--------------------:|:-----------:|:--------------:|:-----------:|:--------------:|:--------------------:|:----------:|:----------:|:----------:|:--------------:|:------------:|:--------------:|
| 0 | 2018-02-04 | 52         | U.S. Bank Stadium | Minneapolis | Minnesota  | 67612      | Philadelphia Eagles  | 41          | Nick Foles     | NaN         | Doug Pederson  | New England Patriots | 33         | Tom Brady  | NaN        | Bill Belichick | 74           | 8              |
| 1 | 2017-02-05 | 51         | NRG Stadium       | Houston     | Texas      | 70807      | New England Patriots | 34          | Tom Brady      | NaN         | Bill Belichick | Atlanta Falcons      | 28         | Matt Ryan  | NaN        | Dan Quinn      | 62           | 6              |
| 2 | 2016-02-07 | 50         | Levi's Stadium    | Santa Clara | California | 71088      | Denver Broncos       | 24          | Peyton Manning | NaN         | Gary Kubiak    | Carolina Panthers    | 10         | Cam Newton | NaN        | Ron Rivera     | 34           | 14             |

<br>

|   | super_bowl | network | avg_us_viewers | total_us_viewers | rating_household | share_household | rating_18_49 | share_18_49 | ad_cost |
|:-:|:----------:|:-------:|:--------------:|:----------------:|:----------------:|:---------------:|:------------:|:-----------:|:-------:|
| 0 | 52         | NBC     | 103390000      | NaN              | 43.1             | 68              | 33.4         | 78.0        | 5000000 |
| 1 | 51         | Fox     | 111319000      | 172000000.0      | 45.3             | 73              | 37.1         | 79.0        | 5000000 |
| 2 | 50         | CBS     | 111864000      | 167000000.0      | 46.6             | 72              | 37.7         | 79.0        | 5000000 |

<br>

|   | super_bowl |                musician               | num_songs |
|:-:|:----------:|:-------------------------------------:|:---------:|
| 0 | 52         | Justin Timberlake                     | 11.0      |
| 1 | 52         | University of Minnesota Marching Band | 1.0       |
| 2 | 51         | Lady Gaga                             | 7.0       |

<br>

<p>Let's start by looking at combined points for each Super Bowl by visualizing the distribution. Let's also pinpoint the Super Bowls with the highest and lowest scores.</p>
![image](https://user-images.githubusercontent.com/78250180/115431286-f2bf1c80-a226-11eb-90ac-9b27e809a630.png)
