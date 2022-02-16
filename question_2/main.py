'''
Developer: Carlos Acácio de Campos Júnior
LinkedIn: https://www.linkedin.com/in/carlos-campos-a0486a11b/
GitHub: https://github.com/Carlos6654
Instagram: https://www.instagram.com/carlos_camposjr/


### Question 2 ###

Requisitos de senha:
    mínimo 6 caracteres
    mínimo 1 dígito
    mínimo 1 letra em maiúsculo
    mínimo 1 letra em minúsculo
    mínimo um caractere especial: !@#$%^&*()-+
'''

if __name__ == '__main__':
    try:    
        password = ''
        all_true = False

        while(all_true is not True):
            # Variables
            min_characters = False
            min_digits = False
            min_uppercase = False
            min_lowercase = False
            min_special_char = False

            password = input("Enter a password: ")

            # Minimum characters:
            if len(password) >= 6:
                min_characters = True
            else:
                print(f'Please enter {6 - len(password)} more characters in the password.')
                continue

            for character in password:
                if character.isdigit() is True:  # Min digits
                    min_digits = True

                if character.isupper() is True:  # Min Uppercase
                    min_uppercase = True

                if character.islower() is True:  # Min Lowercase
                    min_lowercase = True

                if character in '!@#$%^&*()-+':  # Special character
                    min_special_char = True

            if min_digits is not True:
                print(f'* 1 digit is required in password.')
            if min_uppercase is not True:
                print(f'* 1 Uppercase character is required in password.')
            if min_lowercase is not True:
                print(f'* 1 Lowercase character is required in password.')
            if min_special_char is not True:
                print(f'* 1 Special character is required in password.Ex: !@#$%^&*()-+')

            all_true = all([min_characters, min_digits, min_uppercase, min_lowercase, min_special_char])
        print('Password accepted.')

    except Exception as e:
        print(f'Error while running. Message: {e}')
