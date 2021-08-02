import unittest
from selenium import webdriver


class E2ETests(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r'/Users/auguste/Coding/chromedriver')
        self.driver.get('http://localhost:5000')

    def tearDown(self):
        self.driver.quit()

    def test_browser_title_contains_app_name(self):
        self.assertIn('Named Entity Recognizer', self.driver.title)

    def test_page_head_is_named_entity_recognizer(self):
        heading = self._find("heading")
        self.assertEqual('Named Entity Recognizer', heading.text)

    def test_page_has_input_for_text(self):
        input_element = self._find('input-text')
        self.assertIsNotNone(input_element)

    def test_page_has_submit_button(self):
        submit_button = self._find('submit-button')
        self.assertIsNotNone(submit_button)

    def test_submitting_sentence_create_table(self):
        input_element = self._find('input-text')
        submit_button = self._find('submit-button')
        input_element.send_keys("Lithuania is next to Poland")
        submit_button.click()
        table = self._find('ner-table')
        self.assertIsNotNone(table)

    def _find(self, val):
        return self.driver.find_element_by_css_selector(f'[data-test-id="{val}"]')


if __name__ == '__main__':
    unittest.main()
