import { useEffect } from "react";
import { gapi } from "gapi-script";

const CLIENT_ID = "1009108183512-mkadji2slcmtnl2eut8mdqmv1b0ta0je.apps.googleusercontent.com";
const API_KEY = ""; // optional
const SCOPES = "https://www.googleapis.com/auth/calendar.events";

function CalendarPage() {

  useEffect(() => {
    function start() {
      gapi.client.init({
        clientId: CLIENT_ID,
        scope: SCOPES,
      });
    }

    gapi.load("client:auth2", start);
  }, []);

  const signIn = () => {
    gapi.auth2.getAuthInstance().signIn();
  };

  const addEvent = () => {
    const event = {
      summary: "Sprint Training Session",
      description: "AI-based sprint performance training",
      start: {
        dateTime: new Date().toISOString(),
        timeZone: "Asia/Kolkata",
      },
      end: {
        dateTime: new Date(Date.now() + 60 * 60 * 1000).toISOString(),
        timeZone: "Asia/Kolkata",
      },
    };

    gapi.client.calendar.events
      .insert({
        calendarId: "primary",
        resource: event,
      })
      .execute(() => {
        alert("Event added to Google Calendar!");
      });
  };

  return (
    <div className="page">
      <div className="card">
        <h2>Google Calendar Integration</h2>
        <p>Schedule your training sessions</p>

        <button onClick={signIn}>Sign in with Google</button>
        <button onClick={addEvent} style={{ marginLeft: "10px" }}>
          Add Training Event
        </button>
      </div>
    </div>
  );
}

export default CalendarPage;
