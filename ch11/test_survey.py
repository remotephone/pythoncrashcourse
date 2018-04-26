import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    """Tests for the class AnonymousSurvey"""

# This sets up (get it) the rest of our class. We have values we can import into all our other tests

    def setUp(self):
        """
        Create a survey and a set of responses for use in all test methods.
        """
        question = "What language did you first learn to speak?"
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['English', 'Spanish', 'Mandarin']

# commented out the bits we don't need any more since they're already defined in the previous 
# setUp function from earlier. 

    def test_store_single_response(self):
        """Test that a single response is stored properly."""
        # We can replace allllll of this stuff with the set up we have earlier. But 
        # since we did the set up, we need to reference these items as self.whatever
        # otherwise they aren't defined.
#        question = "What language did you first learn to speak?"
#        my_survey = AnonymousSurvey(question)
#        my_survey.store_response('English')
#        self.assertIn('English', my_survey.responses)
        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0], self.my_survey.responses)

# And again, we've defined this stuff so we can just import it, we have to add the 
# self.stuff to everything since it needs to bring the stuff in from its class
# instead of defining it new each time. 

    def test_store_three_responses(self):
        """Test that three individual responses are stored publicly."""
        # We can replace allllll of this stuff with the set up we have earlier. But 
        # since we did the set up, we need to reference these items as self.whatever
        # otherwise they aren't defined.
#        question = "What language did you first learn to speak?"
#        my_survey = AnonymousSurvey(question)
#        responses = ['English', 'Spanish', 'Mandarin']
#        for response in responses:
#            my_survey.store_response(response)
#        for response in responses:
#            self.assertIn(response, my_survey.responses)
        for response in self.responses:
            self.my_survey.store_response(self.responses)
        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)

unittest.main()