import unittest

from NerModelTestDouble import NerModelTestDouble
from ner_client import NamedEntityClient
from parameterized import parameterized


class TestNerClient(unittest.TestCase):
    def test_get_ents_returns_dictionary_given_empty_string_causes_empty_spacy_doc_ents(self):
        model = NerModelTestDouble('eng')
        model.returns_doc_ents([])
        ner = NamedEntityClient(model)
        ents = ner.get_ents("")
        self.assertIsInstance(ents, dict)

    def test_get_ents_returns_list_given_nonempty_string_causes_empty_spacy_doc_ents(self):
        model = NerModelTestDouble('eng')
        doc_ents = [{'text': '', 'label_': ''}]
        model.returns_doc_ents(doc_ents)
        ner = NamedEntityClient(model)
        ents = ner.get_ents("Vilnius is a city in Lithuania")
        self.assertIsInstance(ents, dict)

    @parameterized.expand([
        ['PERSON', 'Barrack Obama', 'Person'],
        ['NORP', 'Lithuanian', 'Group'],
        ['LOC', 'the ocean', 'Location'],
        ['GPE', 'Australia', 'Location']
    ])
    def test_get_ents_given_spacy_LABEL_is_returned_serialized_to_custom_label(self, spacy_ent, text, ent):
        model = NerModelTestDouble('eng')
        doc_ents = [{'text': text, 'label_': spacy_ent}]
        model.returns_doc_ents(doc_ents)
        ner = NamedEntityClient(model)
        ents = ner.get_ents('....')
        expected_result = {'ents': [{'ent': text, 'label': ent}], 'html': ""}
        self.assertListEqual(ents['ents'], expected_result['ents'])

    def test_get_ents_given_spacy_multiple_entities_multiple_entities_are_returned(self):
        model = NerModelTestDouble('eng')
        doc_ents = [{'text': 'Lithuanian', 'label_': 'NORP'}, {'text': 'the ocean', 'label_': 'LOC'}]
        model.returns_doc_ents(doc_ents)
        ner = NamedEntityClient(model)
        ents = ner.get_ents('....')
        expected_result = {'ents':
                               [{'ent': 'Lithuanian', 'label': 'Group'},
                                {'ent': 'the ocean', 'label': 'Location'}], 'html': ""}
        self.assertListEqual(ents['ents'], expected_result['ents'])


if __name__ == '__main__':
    unittest.main()
