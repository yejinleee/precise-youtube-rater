from googleapiclient.discovery import build
import pandas as pd
import os
import numpy as np
import re
import urllib.request
from konlpy.tag import Okt
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import load_model


class commentReviewManager:

    def __init__(self, YTVideoReview,youtubeConnection,loaded_model,tokenizer):

        self.YTVideoReview = YTVideoReview 
        self.MOVIE_COMMENT_LIST=[]
        self.AVERAGE_RATE=0
        self.youtubeConnection= youtubeConnection

        search_response = self.youtubeConnection.commentThreads().list(
            part='snippet',
            videoId=YTVideoReview.videoID,
            maxResults=100
            ).execute()

        # for comment csv storage
        
        
        
        
        #take out the first comment..?
        comments=[]
        while search_response:
            for item in search_response['items']:
                comment = item['snippet']['topLevelComment']['snippet']
                
                if comment['likeCount'] <3:
                    continue
                text=self.commentPreprocessing(comment['textDisplay'])
                if text=="":
                    continue
                
                # create movieComment class and insert into the list.

                m_Comment = movieComment(text,comment['authorDisplayName'], comment['likeCount'],loaded_model,tokenizer)
                comments.append([text, comment['authorDisplayName'], comment['likeCount'],m_Comment.COMMENT_RATE])
                self.MOVIE_COMMENT_LIST.append(m_Comment)

            if 'nextPageToken' in search_response:
                search_response = self.youtubeConnection.commentThreads().list(
                    part='snippet',
                    videoId=YTVideoReview.videoID,
                    pageToken=search_response['nextPageToken'],
                    maxResults=100
                    ).execute()
            else:
                break
        try:
            df = pd.DataFrame(comments)
            df.to_csv(f'./comment/results_{YTVideoReview.videoID}.csv', header=['comment', 'author', 'num_likes','rate'], index=False,encoding='utf-8-sig')               
        except:
            pass
        s=[]
        for i in self.MOVIE_COMMENT_LIST:
            if i.COMMENT_RATE!=-1:
                s.append(i.COMMENT_RATE)
        try:
            self.AVERAGE_RATE=sum(s)/len(s)
        except:
            self.AVERAGE_RATE=-1

        
    def commentPreprocessing(self,comment):
            if comment[0]=="@":
                return ""
            if "채널" in comment:
                return ""
            if "스포" in comment:
                return ""
            if "<a href=" in comment:
                return ""
            if "조회수" in comment:
                return ""
            if "결말" in comment:
                return ""
            if "나레이션" in comment:
                return ""
            if "내레이션" in comment:
                return ""
            if "이 분" in comment:
                return ""
            if "목소리" in comment:
                return ""
            if "구독자" in comment:
                return ""
            while "&quot;" in comment:
                st = comment.find('&quot;')
                en=st+6
                start=comment[:st]
                end=comment[en:]
                comment=(start+end).strip(" ")
            while "<" in comment:
                st = comment.find('<')
                en = comment.find(">")
                start=comment[:st]
                end=comment[en+1:]
                comment=(start+" "+end).strip(" ")
            
            return comment

    
        
        

    

class movieComment:
    def __init__(self,commentContent,commentWriter,numOfLikes,loaded_model,tokenizer):   
        
        self.COMMENT_CONTENT=commentContent
        self.COMMENT_WRITER=commentWriter
        self.NUM_OF_LIKES=numOfLikes
        self.COMMENT_RATE=-1
        
        #Calculating the rating
        def preprocessing_for_rating(comment,loaded_model,tokenizer):
            okt=Okt()
        
            hangul = re.compile('[^ ㄱ-ㅣ가-힣]+')
            comment = hangul.sub('', comment)


            stopwords =  ['의','가','이','은','들','는','좀','잘','걍','과','도','를','으로','자','에','와','한','하다']

            tmp = okt.morphs(comment, stem=True)
            tokens = [word for word in tmp if not word in stopwords]


            # If there's nothing left after tokenizing, return -1
            if not tokens:
                return -1
            encoding=[]
            for i in tokens:
                encoding.append(f"'{i}'")

            encoded = tokenizer.texts_to_sequences([encoding])

            pad_new = pad_sequences(encoded, maxlen = 30)

            score = float(loaded_model.predict(pad_new))
            print(comment)
            print(score)
            return score


        self.COMMENT_RATE=preprocessing_for_rating(self.COMMENT_CONTENT,loaded_model,tokenizer)
