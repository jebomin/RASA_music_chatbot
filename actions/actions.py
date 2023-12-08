from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
import mysql.connector

class ActionRecommendMusicByGenre(Action):
    def name(self) -> Text:
        return "action_recommend_music_by_genre"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # MySQL 데이터베이스 연결
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="dgu1234!",
            database="rasa"
        )

        cursor = conn.cursor()

        # 사용자 입력에서 추출한 장르
        genre = tracker.get_slot("genre")

        # SQL 쿼리를 통해 해당 장르에 대한 음악 추출
        query = f"SELECT title FROM music WHERE genre='{genre}'"
        cursor.execute(query)
        results = cursor.fetchall()

        # 추천된 음악 목록
        recommended_music = [result[0] for result in results]

        # 사용자에게 응답
        if recommended_music:
            dispatcher.utter_message(f"Here are some recommended songs in the {genre} genre: {', '.join(recommended_music)}")
        else:
            dispatcher.utter_message(f"Sorry, I couldn't find any songs in the {genre} genre.")

        # 데이터베이스 연결 해제
        conn.close()


        # 슬롯 값을 업데이트
        return [SlotSet("genre", genre)]

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
import mysql.connector

class ActionRecommendMusicByArtist(Action):
    def name(self) -> Text:
        return "action_recommend_music_by_artist"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # MySQL 데이터베이스 연결
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="dgu1234!",
            database="rasa"
        )

        cursor = conn.cursor()

        # 사용자 입력에서 추출한 가수
        artist = tracker.get_slot("artist")

        # SQL 쿼리를 통해 해당 가수에 대한 음악 추출
        query = f"SELECT title FROM music WHERE singer='{artist}'"
        cursor.execute(query)
        results = cursor.fetchall()

        # 추천된 음악 목록
        recommended_music = [result[0] for result in results]

        # 사용자에게 응답
        if recommended_music:
            dispatcher.utter_message(f"Here are some recommended songs by {artist}: {', '.join(recommended_music)}")
        else:
            dispatcher.utter_message(f"Sorry, I couldn't find any songs by {artist}.")

        # 데이터베이스 연결 해제
        conn.close()

        # 슬롯 값을 업데이트
        return [SlotSet("artist", artist)]

