# AUTHOR: @CodeWithSalman
# GOING TO DECLARE A PARAMETRIZED FUNCTON WITH 2 INPUTS.
def linear_Search(array, target_Value):
    # GOING TO USE FOR LOOP TO THE ARRAY LENGTH.
    for i in range(len(array)):
        # HERE CHECKING IF ANY ARRAY ELEMENT MATCH WITH TARGET VALUE.
        if array[i] == target_Value:
            # HERE RETURN i WILL RETURN THE INDEX WHERE THE ELEMENT WILL BE FOUND.
            return i
    # FOR ELSE CASE IF NOT MATCH FOUND.
    return -1
# MAIN CODE OR DRIVER CODE.
if __name__ == '__main__':
    # USE OF ARRAY USING LIST.
    array = [22, 33, 44, 55, 66]
    target_Value = 55
    missing_Value = 77
    # NOW GOING TO CALL THE ABOVE FUNCTION.
    result = linear_Search(array, target_Value)
    # CHECKING IF RESULT WILL NOT BE EQUAL TO -1 THEN OBVIOUSLY IT MEANS THERE IS A MATCH FOUND.
    if result != -1:
        print("Found")
    else:
        print("Not Found")
