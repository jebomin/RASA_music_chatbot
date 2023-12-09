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
            dispatcher.utter_message(f"Sorry, I couldn't find any songs in that genre.")

        # 데이터베이스 연결 해제
        conn.close()


        # 슬롯 값을 업데이트
        return [SlotSet("genre", genre)]

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
            dispatcher.utter_message(f"Sorry, I couldn't find any songs by that artist")

        # 데이터베이스 연결 해제
        conn.close()

        # 슬롯 값을 업데이트
        return [SlotSet("artist", artist)]
    
    
class ActionRecommendMusicByLyric(Action):
    def name(self) -> Text:
        return "action_recommend_music_by_lyric"

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

        # 사용자 입력에서 추출한 가사
        lyric = tracker.get_slot("lyric")

        # SQL 쿼리를 통해 해당 가사에 대한 음악 추출
        query = f"SELECT title FROM music WHERE lyric='{lyric}'"
        cursor.execute(query)
        results = cursor.fetchall()

        # 추천된 음악 목록
        recommended_music = [result[0] for result in results]

        # 사용자에게 응답
        if recommended_music:
            dispatcher.utter_message(f"Music with lyrics of {lyric}: {', '.join(recommended_music)}")
        else:
            dispatcher.utter_message(f"Sorry, I don't have the music with that lyrics.")

        # 데이터베이스 연결 해제
        conn.close()

        # 슬롯 값을 업데이트
        return [SlotSet("lyric", lyric)]
    

class ActionRecommendMusicByFeeling(Action):
    def name(self) -> Text:
        return "action_recommend_music_by_feeling"

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

        # 사용자 입력에서 추출한 가사
        feeling = tracker.get_slot("feeling")

        # SQL 쿼리를 통해 해당 감정에 대한 음악 추출
        query = f"SELECT title FROM music WHERE feeling='{feeling}'"
        cursor.execute(query)
        results = cursor.fetchall()

        # 추천된 음악 목록
        recommended_music = [result[0] for result in results]

        # 사용자에게 응답
        if recommended_music:
            dispatcher.utter_message(f"These songs that's perfect for {feeling} mood : {', '.join(recommended_music)}")
        else:
            dispatcher.utter_message(f"Sorry, I couldn't find any songs by that mood.")

        # 데이터베이스 연결 해제
        conn.close()

        # 슬롯 값을 업데이트
        return [SlotSet("feeling", feeling)]


class ActionSaveMusic(Action):
    def name(self) -> Text:
        return "action_save_music"

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

        # 사용자 입력에서 추출한 정보
        genre = tracker.get_slot("genre")
        artist = tracker.get_slot("artist")
        title = tracker.get_slot("title")
        lyric = tracker.get_slot("lyric")
        feeling = tracker.get_slot("feeling")

        # SQL 쿼리를 통해 데이터베이스에 값 추가
        query = f"INSERT INTO music (genre, singer, title, lyric, feeling) VALUES ('{genre}', '{artist}', '{title}', '{lyric}', '{feeling}')"
        cursor.execute(query)

        # 데이터베이스에 커밋
        conn.commit()

        # 데이터베이스 연결 해제
        conn.close()

        # 사용자에게 응답
        dispatcher.utter_message(f"Great! I've saved the music information.")

        # 슬롯 값을 업데이트
        return [SlotSet("genre", genre), SlotSet("artist", artist), SlotSet("title", title), SlotSet("lyric", lyric), SlotSet("feeling", feeling)]
