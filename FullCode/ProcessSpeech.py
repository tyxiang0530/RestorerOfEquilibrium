from transformers import BertTokenizer, BertConfig,AdamW, BertForSequenceClassification,get_linear_schedule_with_warmup
import serial
import torch
import random
import speech_recognition as sr
from playsound import playsound

# denote model loading

# LABEL DICTIONARY # {'sadness': 4, 'neutral': 3, 'anger': 0, 'fear': 1, 'joy': 2}
# going from emotions to bytes for arduino serial sending
trans_table = {
    4: b'a',
    2: b'b',
    1: b'c',
    3: b'd',
    0: b'e'
}

# going from emotions to audio files
sad_paths = ["audio\\sadcounter.mp3"]
anger_paths = ["audio\\angercounter.mp3"]
joy_paths = ["audio\\joycounter.mp3"]
fear_paths = ["audio\\fearcounter.mp3"]
neutral_paths = ["audio\\neutralcounter.mp3"]

path_trans = {
    b'a': sad_paths,
    b'b': joy_paths,
    b'c': fear_paths,
    b'd': neutral_paths,
    b'e': anger_paths
}

r = sr.Recognizer()

# load the pre-trained model
model = BertForSequenceClassification.from_pretrained("bert-base-uncased",
                                                      num_labels=5,
                                                      output_attentions=False,
                                                      output_hidden_states=False)
# my laptop does not have a compatible GPU so cpu
device = torch.device('cpu')
# send model to device
model.to(device)
# load finetuned part
model.load_state_dict(torch.load('finetuned_BERT_FairyGarbHVCHECK_epoch_3.model',
                                 map_location=torch.device('cpu')))
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased',
                                          do_lower_case=True)
# set max length
MAX_LENGTH = 200


# encodes text into word embeddings
def encode(text_arr_in):
    '''
    encode encodes the text you give it for bert processing
    :param text_arr_in: the text to predict emotion on
    :return: tensors of words you gave it
    '''
    encoded_data = tokenizer.batch_encode_plus(
        text_arr_in,
        add_special_tokens=True,
        return_attention_mask=True,
        pad_to_max_length=True,
        max_length=MAX_LENGTH,
        truncation=True,
        return_tensors='pt'
    )

    return encoded_data


# generates attention masks and input_ids for BERT
def getIDs(encoded_data_in):
    '''
    takes in encoded data and transforms into attention mask
    and input id for BERT
    :param encoded_data_in: encoded data to transform
    :return: attention mask and input ids
    '''
    input_ids_train = encoded_data_in['input_ids']
    attention_masks_train = encoded_data_in['attention_mask']

    return input_ids_train, attention_masks_train


# evaluates emotion of text
def evaluate(text_in):
    '''
    evaluates the text
    :param text_in: the text
    :return: the evaluation
    '''
    input_ids, attention_masks = getIDs(encode(text_in))
    input_in = input_ids.to(device)
    att = attention_masks.to(device)
    output = model(input_in, att, return_dict=False)
    _, prediction = torch.max(output[0], dim=1)
    return prediction.tolist()


# play_prompt plays the audio prompt (How are you doing today)
def play_prompt(path):
    '''
    plays the specified audio track
    :param path: the path of the track
    :return:
    '''
    opening_prompt = path
    playsound(opening_prompt)


# open_mic plays the prompt and stores and returns the response
def open_mic(prompt_path):
    '''
    plays a prompt and stores the users audio response
    :param prompt_path: the path of the prompt
    :return: string of what user said
    '''
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=1)
        play_prompt(prompt_path)
        print("Talk")
        audio_text = r.record(source, duration = 5)
        # audio_text = r.listen(source, timeout = 1, phrase_time_limit=5
        print("Time over, thanks")

        try:
            # using google speech recognition
            speech = r.recognize_google(audio_text)
            print("Text: " + speech)
            return speech

        except:
            print("Sorry, I did not get that")


# have our classifier make a prediction
def predict_emotion(emo_prompt):
    '''
    predict the emotion of text its given
    :param emo_prompt: the path of the emotion prompt
    :return: the emotion in translated byte form
    '''
    prediction = evaluate([open_mic(emo_prompt)])[0]
    print(prediction)
    return trans_table[prediction]


# play the audio clip and send the right byte
def reaction(emo_prompt, arduino):
    """
    finds correct emotion response clip to play to user
    :param emo_prompt: path of the prompt
    :param arduino: the arduino you are writing to
    :return:
    """
    emo_byte = predict_emotion(emo_prompt)
    print(emo_byte)
    arduino.write(emo_byte)
    play_prompt(random.choice(path_trans[emo_byte]))


# function will only exit if keyword is found in speech
def listen_for(keyword, game_prompt, reject_prompt):
    """
    listens for a keywords and response with either
    an accept prompt or a reject prompt
    :param keyword: the keyword to listen for
    :param game_prompt: the prompt to play if the keyword is found
    :param reject_prompt: the prompt to play if keyword is not found
    :return:
    """
    play_prompt(game_prompt)
    exit_cond = True
    while exit_cond:
        with sr.Microphone() as source:
            print("listening")
            audio_text = r.record(source, duration=3)

        print("recognizing")

        try:
            text = r.recognize_google(audio_text)
            print(text)
            if any(word in text for word in keyword):
                print('found')
                exit_cond = False

            else:
                play_prompt(reject_prompt)

        except Exception as e:
            print(e)
            play_prompt(reject_prompt)

