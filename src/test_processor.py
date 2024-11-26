import pytest
from data_processor import process_hockey_data

@pytest.fixture
def sample_stats():
    return [
        {"year": "1990", "team": "Team A", "wins": 50, "losses": 20},
        {"year": "1990", "team": "Team B", "wins": 10, "losses": 60},
        {"year": "1991", "team": "Team C", "wins": 40, "losses": 30},
        {"year": "1991", "team": "Team D", "wins": 15, "losses": 50},
    ]

def test_process_hockey_data(sample_stats):
    result = process_hockey_data(sample_stats)
    assert len(result["stats"]) == 4
    assert result["summary"] == [
        {"year": "1990", "winner": "Team A", "winner_wins": 50, "loser": "Team B", "loser_wins": 10},
        {"year": "1991", "winner": "Team C", "winner_wins": 40, "loser": "Team D", "loser_wins": 15},
    ]
