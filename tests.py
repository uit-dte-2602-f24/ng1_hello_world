# DO NOT MODIFY THIS FILE
# DO NOT EVEN LOOK AT THIS FILE
# 👀
# ...but since you already ARE looking, here's a free 🧁
# please close the file now kthxbye

# Imports
import pytest
import the_main_event

def test_hello(): # 1p
    result = the_main_event.say_hello()
    assert "hello" == str.lower(result)

def test_world(): # 1p
    result = the_main_event.say_world()
    assert "world" == str.lower(result)

def test_hello_world(): # 1p
    result = the_main_event.say_hello_world()
    assert "hello world" == str.lower(result)

def test_sum_numbers(): #1p
    number_1 = 17
    number_2 = 25
    answer = 42

    result = the_main_event.sum_numbers(number_1, number_2)

    assert result == answer

def test_count_characters():
    sentence = "this sentence is exactly fifty-three characters long!"
    answer = 53

    result = the_main_event.count_characters(sentence)

    assert result == answer
