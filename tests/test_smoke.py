"""trivial test to make sure pytest is working"""

from thatcherchess.server import app

def test_the_app_is_built():
    assert app.title == "ThatcherChess"