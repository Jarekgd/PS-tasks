# Activity 2: Multiple Module

import week1.output_tasks as wk1_output
import week1.input_tasks as wk1_input
import week2.if_statements as wk2_if
import week2.multiple_conditions as wk2_multiple
import week2.nested_if as wk2_nested
import week3.while_loops as wk3_while
import week4.built_in_functions as wk4_built
import week4.custom_functions as wk4_custom
import week4.module_tasks as wk4_modules
import week4.multiple_functions as wk4_functions


def run_week_one():
    print("Which program in 'Week 1' do you wish to run?")
    print("(simple_message, multiline_message, escape_characters, display_box, enter_name, ascii_robot, data_types, string_operator)")
    print()
    response = input("")
    if response == "simple_message":
        wk1_output.simple_message()
    elif response == "multiline_message":
        wk1_output.multiline_message()
    elif response == "escape_characters":
        wk1_output.escape_characters()
    elif response == "display_box":
        wk1_output.display_box()
    elif response == "enter_name":
        wk1_input.enter_name()
    elif response == "ascii_robot":
        wk1_input.ascii_robot()
    elif response == "data_types":
        wk1_input.data_types()
    elif response == "string_operator()":
        wk1_input.string_operator()

def run_week_two():
    print("Which program in 'Week 2' do you wish to run?")
    print("(if_statement, if_else, if_elif_else, modulo_operator, comparsion_operators, counter, or_operator, and_operator, review, nested_decision)")
    print()
    response = input()
    if response == "if_statement":
        wk2_if.if_statement()
    elif response == "if_else()":
        wk2_if.if_else()
    elif response == "if_elif_else":
        wk2_if.if_elif_else()
    elif response == "modulo_operator":
        wk2_if.modulo_operator()
    elif response ==  "comparsion_operators":
        wk2_if.comparsion_operators()
    elif response == "counter":
        wk2_if.counter()
    elif response == "or_operator":
        wk2_multiple.or_operator()
    elif response == "and_operator":
        wk2_multiple.and_operator()
    elif response == "review":
        wk2_multiple.review()
    elif response == "nested_decision":
        wk2_nested.nested_decision()
    elif response == "multiple_decisions":
        wk2_nested.multiple_decisions()

def run_week_three():
    print("Which program in 'Week 3' do you wish to run?")
    print("(simple_loop, count, ascii, repeating_word, sum_100, sum_user_numbers)")
    response = input()
    if response == "simple_loop":
        wk3_while.simple_loop()
    if response == "count":
        wk3_while.count()
    if response == "ascii":
        wk3_while.ascii()
    if response == "repeating_word":
        wk3_while.repeating_word()
    if response == "sum_100":
        wk3_while.sum_100()
    if response == "sum_user_numbers":
        wk3_while.sum_user_numbers()

def run_week_four():
    print("Which program in 'Week 4' do you wish to run?")
    print("(ascii_value, ascii_char, listen, identify, escape_by, cross_bridge, climb_ladder, guess, create_ladder, run, menu)")
    response = input()
    if response == "ascii_value":
        wk4_built.ascii_value()
    elif response == "ascii_char":
        wk4_built.ascii_char()
    elif response == "listen":
        wk4_custom.listen()
    elif response == "identify":
        wk4_custom.identify()
    elif response == "escape_by":
        wk4_custom.escape_by("jumping over")
        wk4_custom.escape_by("running around")
        wk4_custom.escape_by("cross bridge ahead")
    elif response == "cross_bridge":
        wk4_custom.cross_bridge(3)
        wk4_custom.cross_bridge(6)
    elif response == "climb_ladder":
        wk4_custom.climb_ladder(5, 2)
        wk4_custom.climb_ladder(2, 5)
    elif response == "guess":
        wk4_modules.guess()
    elif response == "create_ladder":
        wk4_functions.create_ladder()
    elif response == "run":
        wk4_functions.run()
    elif response == "menu":
        wk4_functions.menu()

def run():
    while (True):
        print("\nWhat would you like to do?")
        print("[a] Run 'week 1' programs")
        print("[b] Run 'week 2' programs")
        print("[c] Run 'week 3' programs")
        print("[d] Run 'week 4' programs")
        print("[q] Quit")
        response = input()
        if response == "a":
            run_week_one()
        elif response =="b":
            run_week_two()
        elif response =="c":
            run_week_three()
        elif response == "d":
            run_week_four()
        elif response == "q":
            break
        else:
            print("Invalid option! Please try again.")

if __name__=="__main__":
    run()