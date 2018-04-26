class AnonymousSurvey():
    """Collect anonymous answers to a survey question."""

# initialize the class. You'll need to give it a question.
    def __init__(self, question):
        """Store a question, and prepare to store repsonses."""
        self.question = question
        # Create an empty list to add responses to.
        self.responses = []

    def show_question(self):
        """Show the survey question."""
        # This is different than what's in the book.
        # question isn't efined, but self.question is up in the __init__ function
        print(self.question)
    
    def store_response(self, new_response):
        """Store a single response to the survey."""
        # Store the answers by appending new_response to responses
        self.responses.append(new_response)

    def show_results(self):
        """Show all the responses that have been given."""
        # print each item in the list
        print("Survey results:")
        # This is also different, we defined self.responses earlier but not here.
        for response in self.responses:
            print('- ' + response)
