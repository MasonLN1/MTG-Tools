# MTG-Tools
Codes for simulations and statistics revolving around the popular trading card game Magic: The Gathering.

Summaries
---

MTGconfidenceintervals - A function in R to provide the 95% confidence interval for a players win-rate based on their recorded wins and losses. The confidence interval is built upon a beta distribution with an initial prior of a 50% win-rate. Can be adapted for any activity with a binary (win/lose) outcome, though the prior may need to be adjusted (Poker, Baseball, etc.)

portentofcalamity - Portent of Calamity is a card in the TCG that requires you pay a given amount of resources, then you reveal as many cards off the top of your deck as the amount of resources you paid. Cards in Magic have "types", and if at least 4 unique types are revealed from among the revealed cards when Portent of Calamity was played, you get to play one of the revealed cards for free. This python code is a Monte Carlo simulation that approximates and plots the probability of successfully revealing at least 4 unique types for a given amount of paid resources, based on the construction of your deck and the amount of each type of card inside the deck.
