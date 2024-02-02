#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) == 0:
        return None
    else:
        longeur = ""
        first = ""
        longeur = len(sentence)
        first = sentence[0]
        return (longeur, first)
