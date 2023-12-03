#include <Arduino.h>
#include <ESP8266WiFi.h>
#include "ThingSpeak.h"

const char* ssid = "Miku Chan";   // your network SSID (name) 
char* password = "cube12345";   // your network password
int PulseSensorPurplePin = 0;        // Pulse Sensor PURPLE WIRE connected to ANALOG PIN 0
int LED13 = 2;   //  The on-board Arduion LED

WiFiClient  client;

int Signal;                // holds the incoming raw data. Signal value can range from 0-1024
int Threshold = 550;            // Determine which Signal to "count as a beat", and which to ingore.

// Timer variables
unsigned long lastTime = 0;
unsigned long timerDelay = 30000;

// The SetUp Function:
void setup() {
     
  pinMode(LED13,OUTPUT);         // pin that will blink to your heartbeat!
  Serial.begin(9600);         // Set's up Serial Communication at certain speed.
  WiFi.mode(WIFI_STA);
  ThingSpeak.begin(client);

}

// The Main Loop Function
void loop() {
  WiFi.begin(ssid, password); 
  delay(5000);     

  Signal = analogRead(PulseSensorPurplePin);  // Read the PulseSensor's value.
  Serial.println(Signal);                    // Send the Signal value to Serial Plotter.
  ThingSpeak.setField(1, Signal);
  if(Signal > Threshold){                          // If the signal is above "550", then "turn-on" Arduino's on-Board LED.
    digitalWrite(LED13,HIGH);
  } else {
    digitalWrite(LED13,LOW);                //  Else, the sigal must be below "550", so "turn-off" this LED.
  }
// set the fields with the values
    

    // Write to ThingSpeak. There are up to 8 fields in a channel, allowing you to store up to 8 different
    // pieces of information in a channel.  Here, we write to field 1.
    int x = ThingSpeak.writeFields(2136253, "EEJQ45S6N48KA6O4");

    if(x == 200){
      Serial.println("Channel update successful.");
    }
    else{
      Serial.println("Problem updating channel. HTTP error code " + String(x));
    }
delay(10);

lastTime = millis();
}