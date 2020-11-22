#!/usr/bin/env python
import pytest

from fibo_pytest import fib


@pytest.mark.parametrize(
    'n, res', [(0, 0),          # First figure is the number to run in the function, the SECOND is the expected result
               (1, 1),
               (2, 1),
               (3, 2),
               (4, 3),
               (5, 5),
               (6, 8)])
# Running the test function against the number to pass in and the result expected
def test_fib(n, res):
    # assert the function against the input to equal the res listed above ^
    assert fib(n) == res

# def test_fib():                     # Call the function with test before the name
#    assert fib(0) == 0              # use assert keyword to start the test
#    assert fib(1) == 1              # call the function in the assert statement
#    assert fib(10) == 55            # provide an intended output


"""
@pytest.mark.skipif(
    sys.version_info[0] == 3 and sys.version_info[1] == 6,
    reason="Python version has to be higher than 3.5!")

If you wish to skip a function conditionally then you can use skipif. 
In the following example the function test_foo is marked with a skipif. 
The function will not be executed, if the Python version is 3.6.x:

Instead of a conditional skip we can also use an unconditional skip. This way, we can always skip. We can add a reason. 
The following example shows how this can be accomplished by marking the function test_bar with a skip marker. The reason we give is that it is "even fooer than foo":


@pytest.mark.skip(reason="Even fooer than foo, so we skip!")
def test_bar():
    assert bar() == "bar
"""
