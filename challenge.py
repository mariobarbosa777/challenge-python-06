def make_division_by(n):
    "This closure returns a function that returns the division of an x number by n "
    def division(x):
        return  x // n

    return division

def run():
    division_by_3 = make_division_by(3)
    print(division_by_3(18))  # The expected output is 6

    division_by_5 = make_division_by(5)
    print(division_by_5(100))  # The expected output is 20

    division_by_18 = make_division_by(18)
    print(division_by_18(54))  # The expected output is 3


if __name__ == '__main__':

    import unittest

    class ClosureSuite(unittest.TestCase):
        def setUp(self):
            self.dict_make_division_by = {
            50 : (100, 2),
            33 : (99, 3),
            25 : (100,4),

            }

        def test_closure_make_division_by(self):
            for key, value in self.dict_make_division_by.items():
                division_by_n = make_division_by(value[0])
                self.assertEqual(key, division_by_n(value[0]))
                del(division_by_n)

        def tearDown(self):
            del (self.dict_make_division_by)
            
        run()
        unittest.main()
