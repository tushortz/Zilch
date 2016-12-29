# Zilch

A python implementation of the Zilch game. 

You can create your own tactics by modifying or extending all the methods in 
the `Tactic` Class. You can also modify the `zilch.py file` for extra in-game settings.

## Usage
Add as many players as possible using the `add_player` method.

Arguments are:
* name -> Player name : *str*
* tactics -> player tactics to use : *Tactic*
* win_count -> counts how many times a player has won chosen rounds : *dict*
* players -> Player to add to game : *Player*
* chatty -> Enable/Disable commentary : *bool*

> **add_player**(name, tactics, win_count, players, chatty)

With minimal setting, you can just modify the arguments of the `main()` method 
in the `zilch.py` file and pass in `number of rounds -> int` and 
`commentary -> bool`



## Acknowledgement
 I'd first like to say a very big thank you to God my creator. Without him, this wouldn't be possible.
 
## License
 
 © 2016 Taiwo Kareem  [taiwo.kareem36@gmail.com]().
 
 Read `LICENSE`