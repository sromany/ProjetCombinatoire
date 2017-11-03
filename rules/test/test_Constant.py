from rules.ConstanteRule import ConstanteRule, EpsilonRule, SingletonRule
import unittest, math

class ConstructorRuleTest(unittest.TestCase):
    """
    Test case utilisé pour tester les fonctions du module 'AbstractRule'
    """

    def setUp(self):
        self.rule = ConstanteRule(object())
        self.rule1 = EpsilonRule(object())
        self.rule2 = SingletonRule(object())

    def test_init(self):
        self.assertEqual(self.rule._grammar, {})
        self.assertEqual(type(self.rule._object), type(object()))


    def test_valuation(self):
        """
        Test que l'attribut _valuation a bien la valeur infini
        et que cette valeur est bien entière
        :return:
        """
        b1 = isinstance(self.rule1, EpsilonRule) and issubclass(type(self.rule1), ConstanteRule)
        b2 = isinstance(self.rule2, SingletonRule) and issubclass(type(self.rule2), ConstanteRule)
        self.assertTrue(b1 and self.rule1.valuation() == 0, msg="{}".format(b1))
        self.assertTrue(b2 and self.rule2.valuation() == 1, msg="{}".format(b1))


if __name__ == '__main__':
    unittest.main()