## `*args` and `**kwargs`

- `*args` and `**kwargs` are used in function defination to pass a number of arguments

 - read more on `*args` [here](https://github.com/kihuni/args_kwargs/tree/main/Args) and `**kwargs` [here](https://github.com/kihuni/args_kwargs/tree/main/kwargs) with examples

 ### using `args` and `**kwargs` to call a function


  - lets take a simple example:

  ```
  def test_args_kwargs(arg1, arg2, arg3):
        print "arg1:", arg1
        print "arg2:", arg2
        print "arg3:", arg3
  ```
- This is how you will call this function  using `*args`

`args = ("stephen", 3,4)`

`test_args_kwargs(*args)`

arg1: stephen

arg2: 3

arg3: 4

- This is how you can use `**kwargs` to call this function

`kwargs = {"name": "stephen", "arg2": 3, "arg1": 4}`

`test_args_kwargs(**kwargs)`

arg1:5

arg2:3

name: stephen
