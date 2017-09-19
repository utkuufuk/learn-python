import unittest

class AnonymousSurvey():

    def __init__(self, question):
        self.question = question
        self.responses = []
        
    def show_question():
        print(question)
        
    def store_response(self, response):
        self.responses.append(response)

    def show_results(self):
        print("Survey Results:")
        for response in responses:
            print("-", response)

# this would normally be in another module
class TestAnonymousSurvey(unittest.TestCase):
    """Tests the class AnonymousSurvey"""

    def setUp(self):
        """Create a survey and a set of responses for use in all test methods."""
        question = "What foreign language did you first learn to speak?"
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['English', 'Spanish', 'Mandarin']

    def test_store_single_response(self):
        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0], self.my_survey.responses)

    def test_store_three_responses(self):
        for response in self.responses:
            self.my_survey.store_response(response)

        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)

unittest.main()
