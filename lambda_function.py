from __future__ import print_function
from random import randint

countries=['China',
           'India',
           'United States of America',
           'Indonesia',
           'Brazil',
           'Pakistan',
           'Nigeria',
           'Bangladesh',
           'Russia',
           'Mexico',
           'Japan',
           'Ethiopia',
           'Philippines',
           'Egypt',
           'Vietnam',
           'Germany',
           'Democratic Republic of the Congo',
           'Iran',
           'Turkey',
           'Thailand',
           'United Kingdom',
           'France',
           'Italy',
           'Tanzania',
           'South Africa',
           'Myanmar',
           'South Korea',
           'Kenya',
           'Colombia',
           'Spain',
           'Argentina',
           'Ukraine',
           'Uganda',
           'Algeria',
           'Sudan',
           'Iraq',
           'Poland',
           'Canada',
           'Morocco',
           'Afghanistan',
           'Saudi Arabia',
           'Peru',
           'Venezuela',
           'Uzbekistan',
           'Malaysia',
           'Angola',
           'Mozambique',
           'Nepal',
           'Ghana',
           'Yemen',
           'Madagascar',
           'North Korea',
           'Australia',
           'Cameroon',
           'Taiwan',
           'Niger',
           'Sri Lanka',
           'Romania',
           'Burkina Faso',
           'Malawi',
           'Mali',
           'Syria',
           'Kazakhstan',
           'Chile',
           'Zambia',
           'Netherlands',
           'Guatemala',
           'Ecuador',
           'Zimbabwe',
           'Cambodia',
           'Senegal',
           'Chad',
           'Somalia',
           'Guinea',
           'South Sudan',
           'Rwanda',
           'Tunisia',
           'Cuba',
           'Belgium',
           'Benin',
           'Greece',
           'Bolivia',
           'Haiti',
           'Burundi',
           'Dominican Republic',
           'Czechia',
           'Portugal',
           'Sweden',
           'Azerbaijan',
           'Hungary',
           'Jordan',
           'Belarus',
           'United Arab Emirates',
           'Honduras',
           'Tajikistan',
           'Serbia',
           'Austria',
           'Switzerland',
           'Israel',
           'Papua New Guinea',
           'Togo',
           'Sierra Leone',
           'Hong Kong',
           'Bulgaria',
           'Laos',
           'Paraguay',
           'El Salvador',
           'Libya',
           'Nicaragua',
           'Lebanon',
           'Kyrgyzstan',
           'Turkmenistan',
           'Denmark',
           'Singapore',
           'Finland',
           'Slovakia',
           'Norway',
           'Congo',
           'Eritrea',
           'Palestine',
           'Costa Rica',
           'Ireland',
           'Liberia',
           'New Zealand',
           'Central African Republic',
           'Oman',
           'Mauritania',
           'Croatia',
           'Kuwait',
           'Panama',
           'Moldova',
           'Georgia',
           'Puerto Rico',
           'Bosnia and Herzegovina',
           'Uruguay',
           'Mongolia',
           'Armenia',
           'Albania',
           'Jamaica',
           'Lithuania',
           'Qatar',
           'Namibia',
           'Botswana',
           'Lesotho',
           'The Gambia',
           'Republic of Macedonia',
           'Slovenia',
           'Gabon',
           'Latvia',
           'Guinea-Bissau',
           'Bahrain',
           'Trinidad and Tobago',
           'Swaziland',
           'Estonia',
           'Timor-Leste',
           'Equatorial Guinea',
           'Mauritius',
           'Cyprus',
           'Djibouti',
           'Fiji',
           'Reunion',
           'Comoros',
           'Bhutan',
           'Guyana',
           'Montenegro',
           'Macau',
           'Solomon Islands',
           'Luxembourg',
           'Suriname',
           'Western Sahara',
           'Cabo Verde',
           'Guadeloupe',
           'Maldives',
           'Malta',
           'Brunei',
           'Bahamas',
           'Martinique',
           'Belize',
           'Iceland',
           'Barbados',
           'French Polynesia',
           'French Guiana',
           'New Caledonia',
           'Vanuatu',
           'Mayotte',
           'Sao Tome and Principe',
           'Samoa',
           'Saint Lucia',
           'Guernsey',
           'Guam',
           'Curcao',
           'Tonga',
           'Grenada',
           'United States Virgin Islands',
           'Aruba',
           'Andorra',
           'Dominica',
           'Greenland',
           'Marshall Islands',
           'Vatican City']		
country_done=[]
INVALID_COUNTRY=""
def build_speechlet_response(title,output,reprompt_text,should_end_session):
        return {
        'outputSpeech': {
            'type': 'PlainText',
            'text': output
        },
        'card': {
            'type': 'Simple',
            'title': title,
            'content': output
        },
        'reprompt': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': reprompt_text
            }
        },
        'shouldEndSession': should_end_session
        }

def build_response(session_attributes, speechlet_response):
        return {
                'version':'1.0',
                'sessionAttributes':session_attributes,
                'response':speechlet_response
                }

def get_help(intent,session):
        card_title="Help"
        speech_output="You can play country Atlas with me. Just say start atlas for starting the game."
        should_end_session=False
        return build_response({}, build_speechlet_response(
               card_title, speech_output, speech_output, should_end_session))

def getCountryWithLetter(places,letter):
        for x in countries:
                if x[0].lower()==letter and x not in places:
                        return x
                        
def continue_game(intent,session):
        card_title="Continue game"
        should_end_session=False
        value=str(intent['slots']['country']['value'])
        #If utterrance contain null slot or country not valid
        if value not in countries or value is None:
                speech_output="The country name is invalid, you lose. Thank You, for playing."
                reprompt_text=speech_output
                session_attributes={}
                should_end_session=True
                return build_response(session_attributes, build_speechlet_response(
                       card_title, speech_output, reprompt_text, should_end_session))

        done_countries=session['attributes']['countries']
        last_country=done_countries[len(done_countries)-1]

        #If last letter of of last country is not first letter of input. Then invalid
        if last_country[len(last_country)-1] != value[0].lower():
            speech_output="The country name is invalid as last letter of the last country is not first letter of your country."
            speech_output+=" You lose, Thank you for playing."
            reprompt_text=speech_output
            print(last_country[len(last_country)-1])
            print(value[0])
            session_attributes={}
            should_end_session=True
            return build_response(session_attributes, build_speechlet_response(
                   card_title, speech_output, reprompt_text, should_end_session))

        #If the country name was already spoken
        if value in done_countries:
                speech_output="The country name is already spoken. Thank you for playing"
                reprompt_text=speech_output
                should_end_session=True
                session_attributes={}
                return build_response(session_attributes, build_speechlet_response(
                       card_title, speech_output, reprompt_text, should_end_session))

        done_countries.append(value)
        done_countries = [str(r) for r in done_countries]
        print(done_countries)
        c=getCountryWithLetter(done_countries,value[len(value)-1])
        print(c)
        speech_output="It is my turn. I say "+str(c)+". Now you tell a country with "+str(c[len(c)-1])+"."
        reprompt_text=speech_output
        done_countries.append(c)
        session_attributes={}
        session_attributes.update({'countries':done_countries})
        return build_response(session_attributes, build_speechlet_response(
                card_title, speech_output, reprompt_text,should_end_session))

def handle_session_end_request():
        card_title = "Thank you for playing country atlas."
        speech_output = "Thank you for playing country atlas."
        should_end_session = True
        return build_response({}, build_speechlet_response(  
                card_title, speech_output, None, should_end_session))

        
def on_intent(intent_request, session):
        """ Called when the user specifies an intent for this skill """
        print("on_intent requestId=" + intent_request['requestId'] +
          ", sessionId=" + session['sessionId'])

        intent = intent_request['intent']
        intent_name = intent_request['intent']['name']

        #Dispatch to your skill's intent handlers
        if intent_name=="PlayGame":
                return get_country_name(intent,session)
        if intent_name=="ContinueGame":
                return continue_game(intent,session)
        elif intent_name=="AMAZON.HelpIntent":
                return get_help(intent,session)
        elif intent_name == "AMAZON.CancelIntent" or intent_name == "AMAZON.StopIntent":
                return handle_session_end_request()
        else:
                raise ValueError("Invalid intent")

def get_random_country():
        x=randint(0,199)
        return countries[x]

def get_country_name(intent,session):
        card_title="Country name"
        session_attributes={}
        should_end_session=False
        speech_output=""
        country=get_random_country()
        speech_output="Let us start the game. I gave you "+country+" You tell country with "+ country[len(country)-1]+"."
        country_done.append(country)
        session_attributes.update({'countries':country_done})
        return build_response(session_attributes, build_speechlet_response(
               card_title, speech_output, speech_output, should_end_session))

def on_session_ended(session_ended_request,session):
        """ Called when the user ends the session.
        Is not called when the skill returns should_end_session=true
        """
        print("on_session_ended requestId=" + session_ended_request['requestId'] +
              ", sessionId=" + session['sessionId'])
        # add cleanup logic here

def on_session_started(session_started_request, session):
        #Call on session start
        
        print("on_session_started requestId=" + session_started_request['requestId']
              + ", sessionId=" + session['sessionId'])

def on_launch(launch_request, session):
    """ Called when the user launches the skill without specifying what they
    want
    """
    print("on_launch requestId=" + launch_request['requestId'] +
          ", sessionId=" + session['sessionId'])
    # Dispatch to your skill's launch
    return get_welcome_response()

def get_welcome_response():
        card_title="Welcome to Country Atlas"
        should_end_session=False
        session_attributes={}
        speech_output="Welcome to Country Atlas."\
                       "You can start playing the game by just saying start game."
        reprompt_text=speech_output
        return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))


        
def lambda_handler(event,context):
        print("event.session.application.applicationId="+
              event['session']['application']['applicationId'])

        if event['session']['new']:
                on_session_started({'requestId': event['request']['requestId']},
                                   event['session'])

        if event['request']['type']=="LaunchRequest":
                return on_launch(event['request'], event['session'])
        elif event['request']['type']=="IntentRequest":
                return on_intent(event['request'], event['session'])
        elif event['request']['type']=="SessionEndedRequest":
                return on_session_ended(event['request'], event['session'])


        
