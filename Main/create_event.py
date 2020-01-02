from __future__ import print_function
from apiclient import discovery
from httplib2 import Http
from oauth2client import file, client, tools

SCOPES = 'https://www.googleapis.com/auth/calendar'
class Create_event():
    def __init__(self,start_date,end_date,description,attendees = None):
        self.start_date = start_date
        self.end_date = end_date
        self.description = description
        self.attendees = attendees
    def create(self):
        store = file.Storage('storage.json')
        creds = store.get()
        if not creds or creds.invalid:
            flow = client.flow_from_clientsecrets('credentials.json', SCOPES)
            creds = tools.run_flow(flow, store)
        GCAL = discovery.build('calendar', 'v3', http=creds.authorize(Http()))

        GMT_OFF = '+02:00'  # PDT/MST/GMT-7
        EVENT = {
            'summary': self.description,
            'start': {'dateTime': self.start_date % GMT_OFF},
            'end': {'dateTime': self.end_date % GMT_OFF},
            # 'attendees': [
            #     {'email': 'friend1@example.com'},
            #
            # ],
        }

        event = GCAL.events().insert(calendarId='primary',
                                     sendNotifications=True, body=EVENT).execute()

        print('''*** %r event added:
                    Start: %s
                    End:   %s''' % (event['summary'].encode('utf-8'),
                                    event['start']['dateTime'], event['end']['dateTime']))

