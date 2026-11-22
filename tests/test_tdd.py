import unittest
from game import StrictRule, MedianRule
"""on regroupe les tests en une seule classe"""
class TestsGrouped(unittest.TestCase):
    """Test sur une session de vote sur règle stricte qui nécessite revote"""
    def testCA07a(self):
        self.assertIsNone(StrictRule().is_validated([5,5,8],1))
    """Test sur une session de vote sur règle stricte valide et qui doit garder le résultat du vote"""
    def testCA07b(self):
        self.assertEqual(StrictRule().is_validated([5,5,5],1),5)
    """Test sur une session de vote sur règle médiane invalide qui nécessite revote"""
    def testCA09a(self):
             self.assertIsNone(MedianRule().is_validated([5,5,8],1))   
    """Test sur une session de vote sur règle médiane valide qui nécessite estimation et sauvegarde du résultat"""
    def testCA11b(self):
         self.assertEqual(MedianRule().is_validated([5,5,5],1),5)
    """Test sur une session de vote sur règle médiane au deuxième tour valide qui nécessite estimation et save du résultat"""
    def testCA11a(self):
        self.assertEqual(MedianRule().is_validated([5,8,3],2),5)
    """ test sur une session de vote sur règle stricte au deuxième tour, vote non valide"""
    def testCA07c(self):
        self.assertIsNone(StrictRule().is_validated([5,10,5],2))
    
    """ test sur une session de vote sur règle stricte où la carte café est jouée au deuxième tour et aucune estimation n'est retenue. """
    def testCA12a(self):
        self.assertIsNone(StrictRule().is_validated([-1,5,5],2)) # -1 signifie la carte cafe
    """ test sur une session de vote sur règle stricte où la carte ? est jouée au premier tour et aucune estimation n'est retenue."""
    def testCA06a(self):
        self.assertIsNone(StrictRule().is_validated([-2,5,5],1)) # -2 signifie la carte ?
if __name__ == "__main__":
    unittest.main()