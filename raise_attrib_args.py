try:
    raise Exception (1,3,4,5,56)
except Exception as e:
    print(len(e.args))
