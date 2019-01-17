def test_func(name, age, *args, **kwargs):
    print(name, age, args, kwargs)
    print("\n\n")


test_func("Dino", 40, "bankofshanghai", "IT", YYYY='2018', MM='08', DD='28')

test_func("Dino", 40, YYYY='2018', MM='08', DD='28')

