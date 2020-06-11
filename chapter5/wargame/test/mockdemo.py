import unittest
from unittest.mock import Mock, call

class MyClassA:
    """Class for mock demo."""
    
    def foo(self):
        """Return a number."""
        # Assume it does some lengthy computation here(not shown)
        return 100
    
    def foo2(self, num):
        """Return another number."""
        # Assume it does some lengthy computation here(not shown)
        return num + 200
    
    def compute(self):
        """Demonstrate use of mock objects."""
        x1 = self.foo()
        x2 = self.foo2(x1)
        print("x1 = %d, x2 = %d"%(x1, x2))
        result = x1 + x2
        print("In MyClassA.compute, result = x1 + x2 =", result)
        return result

class TestA(unittest.TestCase):
    """Write test cases for methods form class MyClassA."""
    
    def test_compute(self):
        """Unit test for MyClassA.compute."""
        a = MyClassA()
        
        # Create a mock object and mock methods of MyClassA
        mockObj = Mock()
        a.foo = mockObj.foo
        a.foo2 = mockObj.foo2
        
        # Assuming you know the return values, set those for the mocks
        a.foo.return_value = 100
        a.foo2.return_value = 300
        
        # Run the computation. Calls the foo and foo2 in compute method are
        # now replace with mock object calls that return the desired value
        result = a.compute()
        
        # Verify the results
        self.assertEqual(result, 400)
        
        # Get info on how the mock objects are actually called by compute
        test_call_list = mockObj.mock_calls
        print("test_call_list=", test_call_list)
        
        # Compare it against some reference calling order
        reference_call_list = [call.foo(), call.foo2()]
        self.assertEqual(test_call_list, reference_call_list)
        
if __name__ == "__main__":
    unittest.main()
        
        