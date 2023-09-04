import pytest
from game import Game, Player, Computer

def test_game_logic():
    game = Game()

    game.player.get_choice = lambda: "rock"
    game.computer.get_choice = lambda: "scissors"
    assert game.start() == "You win!"

    game.player.get_choice = lambda: "rock"
    game.computer.get_choice = lambda: "paper"
    assert game.start() == "You lose!"

    game.player.get_choice = lambda: "rock"
    game.computer.get_choice = lambda: "rock"
    assert game.start() == "It's a draw!"

def test_game_outcome():
    game = Game()

    game.player.get_choice = lambda: "rock"
    game.computer.get_choice = lambda: "scissors"
    assert game.start() == "You win!"

    game.player.get_choice = lambda: "rock"
    game.computer.get_choice = lambda: "paper"
    assert game.start() == "You lose!"

    game.player.get_choice = lambda: "rock"
    game.computer.get_choice = lambda: "rock"
    assert game.start() == "It's a draw!"
