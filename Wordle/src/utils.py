from termcolor import colored


def print_success(text, end='\n'):
    print(colored(text, 'green', attrs=['reverse', 'bold']), end=end)


def print_warning(text, end='\n'):
    print(colored(text, 'yellow', attrs=['reverse', 'bold']), end=end)


def print_error(text, end='\n'):
    print(colored(text, 'red', attrs=['reverse', 'bold']), end=end)


def print_grey(text, end='\n'):
    print(colored(text, 'grey', attrs=['reverse', 'bold']), end=end)