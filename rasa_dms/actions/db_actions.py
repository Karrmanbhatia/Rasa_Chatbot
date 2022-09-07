
from typing import Any, Text, Dict, List
import mysql.connector as c
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
class ActionExtractDatabase(Action):

    def name(self) -> Text:
        return "action_get_database"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        con = c.connect(host="do-dmscyprep", user="dmscyprep",passwd= "",database= "DMSCYP")
        cursor=con.cursor()
        query="SELECT name,state from changepackage  where timer>'2022-08-10';"
        cursor.execute(query)
        result=cursor.fetchall()
        for x in result:
            dispatcher.utter_message(text=f"{x}")
        dispatcher.utter_message(text="There you go!")
        return []

import mysql.connector as c
con = c.connect(host="do-dmscyprep", user="dmscyprep",passwd= "",database= "DMSCYP")
if con.is_connected():
    print("connected")