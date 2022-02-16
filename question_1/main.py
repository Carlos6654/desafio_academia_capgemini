'''
Developer: Carlos Acácio de Campos Júnior
LinkedIn: https://www.linkedin.com/in/carlos-campos-a0486a11b/
GitHub: https://github.com/Carlos6654
Instagram: https://www.instagram.com/carlos_camposjr/


### Question 1 ###
'''
if __name__ == '__main__':
    try:
        inserted_number = '0'
        while (not inserted_number.isnumeric() or inserted_number == '0'):
            inserted_number = input("Enter an integer greater than 0 (Zero): ")
        inserted_number = int(inserted_number)

        for i in range(1, inserted_number+1):
            #for line of ladder
            ladder = ''
            for j in range(0, inserted_number-i):
                ladder += ' '
            for j in range(0, i):
                ladder += '*'
            print(ladder)
    
    except Exception as e:
        print(f'Error while running. Message: {e}')
