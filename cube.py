import facelet_cube


def main():
    # Creates the object fc, which is of the class FaceletCube
    fc = facelet_cube.FaceletCube()

    # This defines the initial state of the cube
    state_string = input("Enter initial cube state (leave blank for solved cube): ")
    fc.string_to_facelet(state_string.replace(" ", ""))

    # Skips cube verification if state string is empty
    if state_string != "":
        # Checks that the cube is a valid facelet cube
        is_valid = fc.verify()
        if is_valid != "Valid cube.":
            print(is_valid)
            return 0

        # Checks that the cube is a valid cubelet cube
        cc = fc.facelet_to_cubelet()
        is_valid = cc.is_valid_state()
        if is_valid != "Valid cube.":
            print(is_valid)
            return 0

    # The main program loop
    while True:
        print(fc.facelet_to_string())
        user_input = input("Enter move string: ")
        if user_input in ["quit", "q"]:
            return 0
        if user_input == "display":
            import net_display
            net_display.launch(fc.facelet_to_string())
        if user_input == "solve":
            solve.solve_cube(fc.facelet_to_string())
        move_string = fc.sanitise_move(user_input)
        # If user tells program to repeat, it will perform entered move sequence until returning to starting position
        if "repeat" in user_input:
            print("This move sequence takes %d repetitions to repeat itself" % fc.calculate_degree(move_string))
        # If not, execute the entered move string
        else:
            fc.execute_move(move_string)


if __name__ == "__main__":
    main()
