import datetime
import os.path
import pickle
import speech_recognition as sr
import pyttsx3
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from dateutil import parser

# Define the scope for Google Calendar API
SCOPES = ['https://www.googleapis.com/auth/calendar']

def get_calendar_service():
    creds = None
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)
    return build('calendar', 'v3', credentials=creds)

def add_event(service, summary, start_time, end_time):
    event = {
        'summary': summary,
        'start': {'dateTime': start_time.isoformat(), 'timeZone': 'UTC'},
        'end': {'dateTime': end_time.isoformat(), 'timeZone': 'UTC'},
    }
    service.events().insert(calendarId='primary', body=event).execute()
    speak('Event created successfully.')

def list_upcoming_events(service, max_results=10):
    now = datetime.datetime.utcnow().isoformat() + 'Z'
    events_result = service.events().list(calendarId='primary', timeMin=now,
                                          maxResults=max_results, singleEvents=True,
                                          orderBy='startTime').execute()
    events = events_result.get('items', [])
    if not events:
        speak('No upcoming events found.')
    else:
        speak('Here are your upcoming events:')
        for event in events:
            start = event['start'].get('dateTime', event['start'].get('date'))
            speak(f"{start}: {event['summary']}")

def delete_event(service, event_summary):
    events_result = service.events().list(calendarId='primary', singleEvents=True,
                                          orderBy='startTime').execute()
    events = events_result.get('items', [])
    for event in events:
        if event['summary'].lower() == event_summary.lower():
            service.events().delete(calendarId='primary', eventId=event['id']).execute()
            speak(f"Deleted event '{event_summary}'")
            return
    speak(f"No event found with summary '{event_summary}'")

def parse_date_time(date_string):
    return parser.parse(date_string)

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        audio = recognizer.listen(source)
        try:
            return recognizer.recognize_google(audio).lower()
        
        except:
            speak("Sorry, I did not understand that.")
            return None

def main():
    service = get_calendar_service()
    while True:
        speak("Voice Assistant - Calendar Integration")
        speak("Available commands: add event, list events, delete event, exit")
        command = recognize_speech()
        if not command:
            continue

        if 'add event' in command:
            speak("Event summary")
            summary = recognize_speech()
            speak("Start time (YYYY-MM-DD HH:MM)")
            start_time_str = recognize_speech()
            speak("End time (YYYY-MM-DD HH:MM)")
            end_time_str = recognize_speech()
            start_time = parse_date_time(start_time_str)
            end_time = parse_date_time(end_time_str)
            add_event(service, summary, start_time, end_time)

        elif 'list events' in command:
            list_upcoming_events(service)

        elif 'delete event' in command:
            speak("Enter the summary of the event to delete")
            event_summary = recognize_speech()
            delete_event(service, event_summary)

        elif 'exit' in command:
            speak("Exiting the program.")
            break

if __name__ == "__main__":
    main()
