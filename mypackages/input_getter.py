

def GetText(prompt='Please enter text\n >'):
    while True:
        try:
            result = input(prompt)
            return result
        except KeyboardInterrupt:
            print("")


def CheckMax(value, max):
    if max != None and value > max:
        print('The value must be at max {}'.format(max))
        return False
    else:
        return True


def CheckMin(value, min):
    if min != None and value < min:
        print('The value must be at least {}'.format(min))
        return False
    else:
        return True

     
def GetIntBase(prompt):
    while True:
        try:
            text_int = GetText(prompt)
            result = int(text_int)
            break
        except ValueError:
            print('Please enter an integer')
    return result


def GetInt(prompt, min=None, max=None):
    while True:
        result = GetIntBase(prompt)
        if not CheckMin(result, min) or not CheckMax(result, max):
            continue
        return result


