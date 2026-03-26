#include <Servo.h>

Servo doorServo;      // Create servo object to control the door
int pirPin = 2;       // Digital pin connected to PIR sensor's signal
int pirState = LOW;   // Assume no motion initially to track state changes
int val = 0;          // Variable for reading the pin status

void setup() {
  doorServo.attach(9);      // Attach the servo on pin 9 
  pinMode(pirPin, INPUT);   // Declare PIR sensor as input
  Serial.begin(9600);       // Initialize serial communication for logging
  
  doorServo.write(0);       // Set initial door position to closed (0 degrees)
  Serial.println("System Initialized. Awaiting users...");
}

void loop() {
  val = digitalRead(pirPin);  // Read input value from the sensor
  
  if (val == HIGH) {          // Check if motion is detected
    if (pirState == LOW) {
      // The sensor just detected someone
      Serial.println("Event Log: User approached. Door opening.");
      doorServo.write(90);    // Open door to 90 degrees
      pirState = HIGH;        // Update state
      delay(3000);            // Keep the door open for 3 seconds
    }
  } else {
    if (pirState == HIGH) {
      // The sensor just stopped detecting someone
      Serial.println("Event Log: Area clear. Door closing.");
      doorServo.write(0);     // Close door back to 0 degrees
      pirState = LOW;         // Update state
    }
  }
}