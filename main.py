import week1.output_tasks as wk1_output
import week1.input_tasks as wk1_input
import week2.if_statements as wk2_if
import week2.multiple_conditions as wk2_multiple
import week2.nested_if as wk2_nested
import week3.while_loops as wk3_while


def run_week_one():
    print("Which program in 'Week 1' do you wish to run?")
    print("(simple_message, multiline_message, escape_characters, display_box, enter_name, ascii_robot, data_types, string_operator)")
    response = input("")
    if response == "simple_message":
        wk1_output.simple_message()
    elif response == "multiline_message":
        wk1_output.multiline_message()
    elif response == "escape_characters":
        wk1_output.escape_characters()
    elif response == "display_box":
        wk1_output.display_box()
    elif reponse == "enter_name":
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

def run():

    while(True):
        print("\nWhat would you like to do?")
        print("[a] Run 'week 1' programs")
        print("[b] Run 'week 2' programs")
        print("[c] Run 'week 3' programs")
        print("[q] Quit")
        response = input()
        if response == "a":
            run_week_one()
        elif response =="b":
            run_week_two()
        elif response =="c":
            run_week_three()
        elif response == "q":
            break
        else:
            print("Invalid option! Please try again.")

if __name__=="__main__":
    run()