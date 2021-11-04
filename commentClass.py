import re
from konlpy.tag import Okt
from tensorflow.keras.preprocessing.sequence import pad_sequences


class movieComment:
    def __init__(self, commentContent, commentWriter, numOfLikes, loaded_model, tokenizer):
        self.COMMENT_CONTENT = commentContent
        self.COMMENT_WRITER = commentWriter
        self.NUM_OF_LIKES = numOfLikes
        self.COMMENT_RATE = -1

        def preprocessing_for_rating(comment, loaded_model, tokenizer):
            okt = Okt()

            hangul = re.compile('[^ ㄱ-ㅣ가-힣]+')
            comment = hangul.sub('', comment)

            stopwords = ['의', '가', '이', '은', '들', '는', '좀', '잘',
                         '걍', '과', '도', '를', '으로', '자', '에', '와', '한', '하다']

            tmp = okt.morphs(comment, stem=True)
            tokens = [word for word in tmp if not word in stopwords]

            if not tokens:
                return -1
            encoding = []
            for i in tokens:
                encoding.append(f"'{i}'")

            encoded = tokenizer.texts_to_sequences([encoding])

            pad_new = pad_sequences(encoded, maxlen=30)

            score = float(loaded_model.predict(pad_new))
            print(comment)
            print(score)
            return score

        self.COMMENT_RATE = preprocessing_for_rating(
            self.COMMENT_CONTENT, loaded_model, tokenizer)

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
