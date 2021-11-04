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
