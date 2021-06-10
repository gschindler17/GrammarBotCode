# Copyright (c) Microsoft. All rights reserved.
# Licensed under the MIT license. See LICENSE.md file in the project root for full license information.

# <code>
import azure.cognitiveservices.speech as speechsdk
import time

# Creates an instance of a speech config with specified subscription key and service region.
# Replace with your own subscription key and service region (e.g., "westus").
speech_key, service_region = "7e396ae33fae49668cf4ad2f473ee5b7", "eastus"
speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region)

# Creates a recognizer with the given settings
speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config)

all_results = [] 
def handle_final_result(evt):
    all_results.append(evt.result.text)

speech_recognizer.recognized.connect(handle_final_result)

print("Say something...")

model = speechsdk.KeywordRecognitionModel("keywordGrammar/keywordGrammar.table")
keywordString = "grammar"



speech_recognizer.start_continuous_recognition()
input("Press Enter to continue...")
speech_recognizer.stop_continuous_recognition()


print(all_results)



speech_recognizer.session_started.disconnect_all()
speech_recognizer.recognized.disconnect_all()
speech_recognizer.session_stopped.disconnect_all()


# Starts speech recognition, and returns after a single utterance is recognized. The end of a
# single utterance is determined by listening for silence at the end or until a maximum of 15
# seconds of audio is processed.  The task returns the recognition text as result. 
# Note: Since recognize_once() returns only a single utterance, it is suitable only for single
# shot recognition like command or query. 
# For long-running multi-utterance recognition, use start_continuous_recognition() instead.
# result = speech_recognizer.recognize_once()
