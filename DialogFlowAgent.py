# DialogFlowAgent
# Module for integrate Google's Dialogflow with our project.


# Import all required python modules for use.
# Globle modules
import dialogflow  # pip install dialogflow
from google.api_core.exceptions import InvalidArgument


# -------------------------------------Class DialogFlowAgent------------------------------------------#


class DialogFlowAgent:
    def __init__(self, projectId, languageCode, sessionCode):
        """Short summary.

        Args:
            projectId (type): Description of parameter `projectId`.
            languageCode (type): Description of parameter `languageCode`.
            sessionCode (type): Description of parameter `sessionCode`.

        Returns:
            type: Description of returned object.

        """
        self.projectId = projectId
        self.languageCode = languageCode
        self.sessionCode = sessionCode
        self.sessionClient = dialogflow.SessionsClient()
        self.session = self.sessionClient.session_path(self.projectId, self.sessionCode)

    def askQuery(self, queryText):
        """Short summary.

        Args:
            queryText (type): Description of parameter `queryText`.

        Returns:
            type: Description of returned object.

        """
        textInput = dialogflow.types.TextInput(
            text=queryText, language_code=self.languageCode
        )
        queryText = dialogflow.types.QueryInput(text=textInput)
        try:
            response = self.sessionClient.detect_intent(
                session=self.session, query_input=queryText
            )
            return response.query_result.fulfillment_text
        except InvalidArgument as ia:
            return "None"
