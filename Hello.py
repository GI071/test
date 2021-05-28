def function(*args, **kwargs):
    import ipdb
    ipdb.set_trace()
    print('Hello!')

if __name__ == '__main__':
    function(1, 2, 3, 4, 5, user = "Giorgi", password = 'Hi')

