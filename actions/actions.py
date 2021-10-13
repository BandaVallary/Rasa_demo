# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is an example for creating a form

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet, EventType
from rasa_sdk.executor import CollectingDispatcher

class ValidateRestaurantForm(Action):
    def name(self) -> Text:
        return "user_details_form"
    def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
    ) -> List[EventType]:
        required_slots = ["name", "number"]

        for slot_name in required_slots:
            if tracker.slots.get(slot_name) is None:
                # this slot is not filled, therefore rquest the user to fill it next
                return[SlotSet("requested_slot", slot_name)]
                # if all slots are filled
        return[SlotSet ("requested_slot", None)]

class ActionSubmit(Action):
    def name(self) -> Text:
        return "action_submit"
    def run( self, 
            dispatcher,
            tracker: Tracker,
            domain: "DomainDict",
    ) -> List[Dict[Text, any]]:
        dispatcher.utter_message(template= "utter_details_thanks",
        Name= tracker.get_slot("name"), 
        Phone_number= tracker.get_slot("number") )


