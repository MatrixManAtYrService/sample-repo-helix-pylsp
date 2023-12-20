# did not autocomplete
from sample.say_foo import say_it as soft
from sample.say_foo_loudly import say_it_loudly as loud

def test_says_foo():
    assert soft() == "foo"

def test_says_foo_loudly():
    assert loud() == "FOO"
    
