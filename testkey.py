import keyboard  # using module keyboard


    while True:  # making a loop
        try:  # used try so that if user pressed other than the given key error will not be shown
            if keyboard.is_pressed('q'):  # if key 'q' is pressed
                print('You Pressed A Key!')
                break
            elif keyboard.is_pressed('x'):  # if key 'q' is pressed
                print('hi!')
                break  # finishing the loop

        except:
            break  # if user pr