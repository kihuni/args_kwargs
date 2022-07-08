def test_var_args(f_arg, *argv):
    print ("first normal arg:", f_arg)
    for arg in argv:
        print ("another arg through *argv :", arg)

test_var_args('stephen', 'loves','learning','python') 

# first normal arg: stephen
# another arg through *argv : loves
# another arg through *argv : learning
# another arg through *argv : python
