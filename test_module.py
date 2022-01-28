import unittest
from arithmatic_arranger import arithmatic_arranger


# the test case
class Unittest(unittest.TestCase):
    def test_arrangement(self):
        actual = arithmatic_arranger(["3 + 855", "3801 - 2", "45 + 43", "123 + 49"])
        expected = "    3      3801      45      123\n+ 855    -    2    + 43    +  49\n----    ----   ----  -----"
        self.assertEqual(actual, expected, 'Expected different output when calling "arithmatic_arranger()" with ["3 + 855", "3801 - 2", "45 + 43", "123 + 49"]')

        actual = arithmatic_arranger(["11 + 4", "3801 - 2999", "1 + 2", "123 + 49", "1 - 9380"])
        expected = "   11      3801      1      123        1\n+  4    - 2999    + 2     +49     - 9380\n----    ----   ----  -----"
        self.assertEqual(actual, expected, 'Expected different output when calling "arithmatic_arranger()" with ["11 + 4", "3801 - 2999", "1 + 2", "123 + 49", "1- 9380"]')

    def test_too_many_problems(self):
        actual = arithmatic_arranger(["44 + 815", "909 - 2", "45 + 43", "123 + 49", "888 + 40", "653 +87"])
        expected = "Error: Too many problems."
        self.assertEqual(actual, expected, 'Expected calling "arithmatic_arranger()" with more than five probelems tp return "Error: Too many problems."')

    def test_incorrect_operator(self):
        actual = arithmatic_arranger(["3/855","3801-2", "45+43", "123+49"])
        expected = "Error: Operator must be '+' or '-'."
        self.assertEqual(actual, expected,)


    def test_too_many_digits(self):
      actual = arithmatic_arranger(["3/855", "3801-2", "45+43", "123+49"])
      expected = "Error: Numbers cannot be more than four digits."
      self.assertEqual(actual, expected,'Expected calling "arithmetic_arranger()"with a problem that contains a letter character in the number to return "Error:Numbers must only contain digits."' )

    def test_only_digits(self):
        actual = arithmatic_arranger(["98+3g5", "3801-2", "45+43", "123+49"])
        expected = "Error: Numbers must only contain digits."
        self.assertEqual(actual, expected,'Expected calling "arithmetic_arranger()"with a problem that contains a letter character in the number to return "Error:Numbers must only contain digits."' )

    def test_solutions(self):
        actual = arithmatic_arranger(["32-698", "1-3801", "45+43", "123+49"], True)
        expected = "32      1       45      123\n-698       -3801       +43     +49\n-----  ----    ----\n -666     -3800       88      172"
        self.assertEqual(actual, expected,'Expected solutions to be correctly displayed in output when calling arthemetic_arranger()" with arithemetic problems and a second argument of `True`.')
if __name__ == "_main_":
    unittest.main()
