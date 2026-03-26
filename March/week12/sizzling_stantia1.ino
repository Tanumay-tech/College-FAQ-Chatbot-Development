int trigPin = 7;
int echoPin = 6;
int buzzerPin = 8;
int motorPin = 9;

void setup() {
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
  pinMode(buzzerPin, OUTPUT);
  pinMode(motorPin, OUTPUT);
  
  Serial.begin(9600);
  Serial.println("Forklift Safety System Initialized.");
}

void loop() {
  long duration, distance;
  
  // Send a 10-microsecond high pulse to trigger the sensor
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);
  
  // Read the echo pin; pulseIn returns the time in microseconds
  duration = pulseIn(echoPin, HIGH);
  
  // Calculate the distance in cm (Speed of sound is approx 0.034 cm/microsecond)
  distance = (duration * 0.034) / 2;
  
  // Print distance to Serial Monitor for debugging
  Serial.print("Distance: ");
  Serial.print(distance);
  Serial.println(" cm");
  
  // Safety Logic: Object within 2 meters (200 cm)
  if (distance > 0 && distance <= 200) {
    digitalWrite(buzzerPin, HIGH);  // Sound the alarm
    digitalWrite(motorPin, LOW);    // Stop the motor
    Serial.println("ALERT: Pedestrian detected! Motor stopped.");
  } else {
    digitalWrite(buzzerPin, LOW);   // Turn off alarm
    digitalWrite(motorPin, HIGH);   // Run the motor
  }
  
  delay(100); // Small delay to stabilize sensor readings
}
