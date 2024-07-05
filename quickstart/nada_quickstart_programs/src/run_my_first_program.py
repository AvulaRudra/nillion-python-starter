from nada_dsl import *

def nada_main():
    party1 = Party(name="Party1")
    party2 = Party(name="Party2")
    party3 = Party(name="Party3")
    party4 = Party(name="Party4")
    
    # Inputs from three different parties
    a = SecretInteger(Input(name="A", party=party1))
    b = SecretInteger(Input(name="B", party=party2))
    c = SecretInteger(Input(name="C", party=party3))

    # Calculate the product of the first two inputs
    product = a * b

    # Subtract the third input from the product
    intermediate_result = product - c

    # Calculate the absolute value of the intermediate result
    absolute_result = abs(intermediate_result)

    return [Output(absolute_result, "final_output", party4)]
