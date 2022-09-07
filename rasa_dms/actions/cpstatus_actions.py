import datetime as dt
from typing import Any, Text, Dict, List
import mysql.connector as c
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet

class ActionCp(Action):

    def name(self) -> Text:
        return "action_show_cpstatus"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        con = c.connect(host="do-dmscyprep", user="dmscyprep",passwd= "",database= "DMSCYP")
        cursor=con.cursor()
        current_cp = next(tracker.get_latest_entity_values("cp"), None)
        query=f"SELECT state from changepackage where name ='{current_cp}' "
        cursor.execute(query)
        dispatcher.utter_message(text="CP status is as follows")
        result=cursor.fetchall()
        
        # dispatcher.utter_message(text=f"{result}")
        # dispatcher.utter_message(type(result))

        for item in result:
            status = item[0]
            if status=="closed":
                dispatcher.utter_message(text=f" Your CP {current_cp} is  closed." )
            if status=="deleted":
                dispatcher.utter_message(text=f" Your CP {current_cp} is  deleted." )
            if status=="open":
                dispatcher.utter_message(text=f" Your CP {current_cp} is  open. " )
            if status=="submit review":
                dispatcher.utter_message(text=f" Your CP {current_cp} is in submit review." )
            if status=="rejected":
                dispatcher.utter_message(text=f" Your CP {current_cp} is in rejected." )

                query2=f"select username from internalusers where IDInternalUsers=(select idinternalusers from cpapproval where idchangepackage=(SELECT idchangepackage from changepackage where name='{current_cp}') and state='rejectwait')"
                cursor.execute(query2)
                # dispatcher.utter_message(text="CP is rejected by :-")
                result1=cursor.fetchall()
                for username in result1:
                    dispatcher.utter_message(text=f"USERNAME:{username}")
                    user_name=username[0]
                    if user_name!='zzciadmn' or 'zzcitestadmn':
                        query3=f"select tc_name_first,tc_name_last from people where tc_username=(select username from internalusers where IDInternalUsers=(select idinternalusers from cpapproval where idchangepackage=(SELECT idchangepackage from changepackage where name='{current_cp}') and state='rejectwait'))"
                        cursor.execute(query3)
                        # dispatcher.utter_message(text="The username who has rejected CP is:-")
                        result2=cursor.fetchall()
                        for u_name in result2:
                            complete_user_name=u_name[0]
                            dispatcher.utter_message(text=f"{complete_user_name} has rejected {current_cp}")
                    else:
                        dispatcher.utter_message(text=f" Your CP {current_cp} is rejected by ZZCiAdmin." )

                            
                    
        return []