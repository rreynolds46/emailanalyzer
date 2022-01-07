'''

This is using IBM Watson's tone analyzer. Free to make an account

import os
from dotenv import load_dotenv
from ibm_watson import ToneAnalyzerV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import json

load_dotenv()

authenticator = IAMAuthenticator(os.environ.get("IBM_API_KEY"))
tone_analyzer = ToneAnalyzerV3(
    version='2021-08-26',
    authenticator=authenticator
)

tone_analyzer.set_service_url(os.environ.get("IBM_API_URL"))


def get_tone_analysis(text):
    tone_analysis = tone_analyzer.tone(
        {'text': text},
        content_type='application/json'
    ).get_result()
    return tone_analysis
'''