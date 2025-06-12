import pytest
from source.utils import ask
from unittest.mock import patch

def test_ask():
    with patch('builtins.input', return_value='test input'):
        result = ask('Enter something: ')
        assert result == 'test input'

def test_ask_strips_whitespace():
    with patch('builtins.input', return_value='  test input  '):
        result = ask('Enter something: ')
        assert result == 'test input'