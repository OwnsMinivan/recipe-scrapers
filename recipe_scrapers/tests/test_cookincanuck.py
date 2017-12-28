import os
import unittest

from recipe_scrapers.cookincanuck import CookinCanuck


class TestCookinCanuckScraper(unittest.TestCase):
    def setUp(self):
        # tests are run from tests.py
        with open(os.path.join(
            os.getcwd(),
            'recipe_scrapers',
            'tests',
            'test_data',
            'cookincanuck.testhtml'
        )) as file_opened:
            self.harvester_class = CookinCanuck(file_opened, test=True)

    def test_host(self):
        self.assertEqual(
            'cookincanuck.com',
            self.harvester_class.host()
        )

    def test_title(self):
        self.assertEqual(
            self.harvester_class.title(),
            'Hearty Chicken Stew With Butternut Squash & Quinoa Recipe'
        )

    def test_total_time(self):
        self.assertEqual(
            75,
            self.harvester_class.total_time()
        )

    def test_ingredients(self):
        self.assertCountEqual(
            [
                '1 1/2 lb. butternut squash, peeled, seeded & chopped into 1/2-inch pieces', 
                '3 1/2 cups chicken broth', 
                '1 1/2 lb. boneless, skinless chicken thighs', 
                '1 tbsp olive oil', 
                '1 medium yellow onion, finely chopped', 
                '1/2 tsp kosher salt', 
                '4 cloves garlic, minced', 
                '1 1/2 tsp dried oregano', 
                '1 can (14 oz) petite diced tomatoes', 
                '2/3 cup uncooked quinoa', 
                '3/4 cup pitted and quartered kalamata olives', 
                'Freshly ground black pepper, to taste', 
                '1/4 cup minced fresh flat-leaf parsley'
            ],
            self.harvester_class.ingredients()
        )

    def test_instructions(self):
        return self.assertEqual(
            'Steam the butternut squash until barely tender, about 10 minutes. Remove half of the squash pieces and set aside. Steam the remaining squash until very tender, an additional 4 to 6 minutes. Mash this squash with the back of a fork. Set aside. In a large saucepan set over medium-high heat, bring the chicken broth to a simmer. Add chicken thighs, cover, and cook until chicken is cooked through, about 15 minutes. Transfer the chicken thighs to a plate and allow to cool. Pour broth into a medium-sized bowl. Return the saucepan to the stovetop and lower heat to medium. Add olive oil. Add onion and cook, stirring occasionally, until onion is starting to turn brown, 8 to 10 minutes. Add the salt, minced garlic and oregano. Cook, stirring, for 1 additional minute. To the saucepan, add tomatoes, butternut squash pieces, mashed butternut squash. Stir to combine. Stir in reserved chicken broth and quinoa. Bring to a simmer, cover and cook until the quinoa turns translucent, about 15 minutes. Shred the chicken with your fingers or a fork. Stir the chicken, olives and pepper into the stew and simmer, uncovered, to heat, about 5 minutes. Stir in parsley and serve.',
            self.harvester_class.instructions()
        )
