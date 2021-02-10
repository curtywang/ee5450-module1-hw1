# EE 5450 Module 1, Homework 1
Building a FastAPI-based Web API for Multi-user, Multi-game Blackjack

# Introduction

In this assignment, you'll be making a Web API using asyncio and FastAPI to make a game server for Blackjack.
Below is a specification of all of the paths (URLs) you should handle, along with their expected responses.
I've made a class called `AsyncBlackjackDB`, which I used to make a global at the top of `web_blackjack.py`.
`AsyncBlackjackDB` simulates a game database (with some sleep calls) of which you can add, get, or delete
Blackjack games.  Your job is to create the handlers below that will use functions (methods) that `AsyncBlackjackDB`
provides to provide a web-based interface to play Blackjack with!

# HTTP Paths and Responses

```
GET /
returns: {'message': 'Welcome to Blackjack!'}
```

