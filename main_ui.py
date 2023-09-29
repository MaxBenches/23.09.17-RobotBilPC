import time
import controller
import UDP_pc

def main():

    # Print Start Menu to console
    start_menu()

    while True:
        # Get controller input
        trig_left, trig_right, x_axis_left, \
            button_x, button_y, button_b, \
            button_a, button_select, button_start \
            = controller.get_controller_input()

        # Exit program
        if button_select == 1:
            print("Exiting Program.")
            wait()
            quit()

        # Football Loop
        if button_a == 1:
            print("'Football Mode' selected.\n"
                  "To return to the menu press the 'Start' button.")
            message = str(button_a)
            UDP_pc.msg_send(message, "10.120.0.96", 5005)
            while True:
                trig_left, trig_right, x_axis_left, \
                    button_x, button_y, button_b, \
                    button_a, button_select, button_start \
                    = controller.get_controller_input()

                message = str(trig_left) + ":" + \
                          str(trig_right) + ":" + \
                          str(x_axis_left) + ":" + \
                          str(button_x) + ":" + \
                          str(button_y) + ":" + \
                          str(button_b) + ":" + \
                          str(button_a) + ":" + \
                          str(button_select) + ":" + \
                          str(button_start)

                UDP_pc.msg_send(message, "10.120.0.96", 5005)

                if button_select == 1:
                    break
                break



        """
        # Football loop
        if controller_input == "A":
            print("'Football Mode' selected.\n"
                  "To return to the menu press the 'Start' button.")
            while True:
                controller_input = controller.get_controller_input()
                if controller_input == "Start":
                    print("Returning to menu")
                    wait()
                    break
                elif controller_input == "B":
                    # Insert speaker honking
                    print("HONK HONK")
                elif controller_input is not None:
                    msg_send(controller_input, "10.120.0.18", 5005)
                    print(controller_input)
            break

        # 'Follow the Wall' loop
        # Send a message to pico, so it knows what loop to go into
        if controller_input == "B":
            print("'Follow the Wall Mode' is under construction. Returning to menu.")
            wait()
            break

        # 'Move the Box' loop
        # Send a message to pico, so it knows what loop to go into
        if controller_input == "X":
            print("'Move the Box Mode' is under construction. Returning to menu.")
            wait()
            break
        """


def start_menu():
    print("\nMenu:\n"
          "Football (Press 'A')\n"
          "Follow the Wall (Press 'B')\n"
          "Move the Box (Press 'X')\n"
          "Exit (Press 'Select')")

def wait():
    time.sleep(.3)

main()