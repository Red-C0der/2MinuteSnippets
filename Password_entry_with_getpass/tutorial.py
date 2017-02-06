import getpass


# =====[ Basic input ]=====
def basic_input():

    input_password = getpass.getpass()          # Display password input prompt
    print input_password                        # Print input password


# =====[ Basic input with custom text ]=====
def basic_input_with_custom_text(text):

    input_password = getpass.getpass(text)      # Display password input prompt with custom text
    print input_password                        # Print input password


# =====[ Get current username ]=====
def get_current_username():

    print getpass.getuser()                     # Get and print current username


# =====[ Exception example ]=====
def basic_input_with_exception_handeling():

    try:
        input_password = getpass.getpass()      # Display password input prompt
    except getpass.GetPassWarning:
        print 'error: canceled input due to input maybe being visible!'
        return False

    print input_password                        # Print input password
    return True


if __name__ == '__main__':

    # ===========[ Info ]===========
    # Uncomment function calls to test them out.
    # ==============================

    basic_input()
    #basic_input_with_custom_text('Please enter your password: ')
    #get_current_username()
    #basic_input_with_exception_handeling()