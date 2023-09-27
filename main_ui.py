import time
import controller   # Remember to assign new buttons in controller module

def main():

    # Print Start Menu to console
    start_menu()

    while True:
        # Get controller input
        controller_input = controller.get_controller_input()
        # print(controller_input)    # Prints infinitely, use only for test
        if controller_input == "Select":
            print("Exiting Program.")
            wait()
            quit()
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





def start_menu():
    print("\nMenu:\n"
          "Football (Press 'A')\n"
          "Follow the Wall (Press 'B')\n"
          "Move the Box (Press 'X')\n"
          "Exit (Press 'Select')")

def wait():
    time.sleep(.3)

main()