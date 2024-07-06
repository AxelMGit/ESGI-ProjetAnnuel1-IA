# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []

motos = [

    # TRAILS A2

    {
        "nom": "Honda CB500X",
        "marque": "Honda",
        "type": "trail",
        "permis": "a2",
        "prix": 7000,
        "puissance": 47
    },
    {
        "nom": "Kawasaki Versys-X 300",
        "marque": "Kawasaki",
        "type": "trail",
        "permis": "a2",
        "prix": 5800,
        "puissance": 40
    },
    {
        "nom": "BMW G310GS",
        "marque": "BMW",
        "type": "trail",
        "permis": "a2",
        "prix": 6300,
        "puissance": 34
    },

    #TRAILS A
    {
        "nom": "Yamaha Tenere 700",
        "marque": "Yamaha",
        "type": "trail",
        "permis": "a",
        "prix": 10000,
        "puissance": 72
    },
    {
        "nom": "KTM 890 Adventure",
        "marque": "KTM",
        "type": "trail",
        "permis": "a",
        "prix": 13500,
        "puissance": 105
    },
    {
        "nom": "Honda Africa Twin",
        "marque": "Honda",
        "type": "trail",
        "permis": "a",
        "prix": 14500,
        "puissance": 100
    },

    # SPORTIVES A2

    {
        "nom": "Kawasaki Ninja 400",
        "marque": "Kawasaki",
        "type": "sportive",
        "permis": "a2",
        "prix": 6000,
        "puissance": 45
    },
    {
        "nom": "Yamaha YZF-R3",
        "marque": "Yamaha",
        "type": "sportive",
        "permis": "a2",
        "prix": 6200,
        "puissance": 42
    },
    {
        "nom": "Honda CBR500R",
        "marque": "Honda",
        "type": "sportive",
        "permis": "a2",
        "prix": 7000,
        "puissance": 47
    },

    # SPORTIVES A

    {
        "nom": "Yamaha YZF-R1",
        "marque": "Yamaha",
        "type": "sportive",
        "permis": "a",
        "prix": 18000,
        "puissance": 200
    },
    {
        "nom": "Suzuki GSX-R1000",
        "marque": "Suzuki",
        "type": "sportive",
        "permis": "a",
        "prix": 16000,
        "puissance": 199
    },
    {
        "nom": "BMW S1000RR",
        "marque": "BMW",
        "type": "sportive",
        "permis": "a",
        "prix": 19000,
        "puissance": 205
    },

    # ROADSTERS A2

    {
        "nom": "Yamaha MT-07",
        "marque": "Yamaha",
        "type": "roadster",
        "permis": "a2",
        "prix": 7000,
        "puissance": 47
    },
    {
        "nom": "Kawasaki Z400",
        "marque": "Kawasaki",
        "type": "roadster",
        "permis": "a2",
        "prix": 6200,
        "puissance": 45
    },
    {
        "nom": "Honda CB500F",
        "marque": "Honda",
        "type": "roadster",
        "permis": "a2",
        "prix": 6500,
        "puissance": 47
    },

    # ROADSTERS A

    {
        "nom": "Yamaha MT-09",
        "marque": "Yamaha",
        "type": "roadster",
        "permis": "a",
        "prix": 11000,
        "puissance": 115
    },
    {
        "nom": "Kawasaki Z900",
        "marque": "Kawasaki",
        "type": "roadster",
        "permis": "a",
        "prix": 9500,
        "puissance": 125
    },
    {
        "nom": "Honda CB650R",
        "marque": "Honda",
        "type": "roadster",
        "permis": "a",
        "prix": 8900,
        "puissance": 94
    }
]

def rechercher_moto(permis, type_moto, budget):
    print('Loaded')
    resultats = [moto for moto in motos if moto["permis"] == permis and moto["type"] == type_moto and moto["prix"] <= int(budget)]
    return resultats


from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class action_suggere_moto(Action):

    print('Loaded 2')

    def name(self) -> Text:
        return "action_suggere_moto"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        permis = tracker.get_slot('permis')
        type_moto = tracker.get_slot('type_moto')
        budget = tracker.get_slot('budget')

        print(permis,type_moto,budget)

        resultats = rechercher_moto(permis.lower(), type_moto.lower(), budget)


        if resultats:
            suggestion = resultats[0]  # Prendre la première moto suggérée
            dispatcher.utter_message(text=f"Dans votre budget de {budget}, Je vous suggère une {suggestion['nom']} de chez {suggestion['marque']}.")
            if resultats[1]:
                suggestion2 = resultats[1]
                dispatcher.utter_message(text=f"Rentrant dans vos critères, je peux également vous proposer une {suggestion2['nom']} de chez {suggestion2['marque']}.")
        else:
            dispatcher.utter_message(text="Désolé, je n'ai trouvé aucune moto correspondant à vos critères.")

        return []
