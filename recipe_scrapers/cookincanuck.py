from ._abstract import AbstractScraper
from ._utils import get_minutes, normalize_string


class CookinCanuck(AbstractScraper):

    @classmethod
    def host(self):
        return 'cookincanuck.com'

    def title(self):
        return self.soup.find('h2', {'itemprop': 'name'}).get_text()

    def total_time(self):
        preptime = soup.find('span', {'class': 'meta-label'}).nextSibling.nextSibling.get_text()
        cookTime = soup.find('meta', {'itemprop': 'cookTime'}).get("content")

        return get_minutes(self.soup.find('meta', {'itemprop': 'totalTime'}))

    def ingredients(self):
        ingredients_html = self.soup.findAll('li', {'itemprop': 'ingredients'})

        return [
            normalize_string(ingredient.get_text())
            for ingredient in ingredients_html
        ]

    def instructions(self):
        instructions_html = self.soup.find('div', {'class': 'recipe-instructions'}).findAll('li')

        return '\n'.join([
            normalize_string(instruction.get_text())
            for instruction in instructions_html
        ])
