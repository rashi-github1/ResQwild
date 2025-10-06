#include <Servo.h>  // Include the Servo library

// Define pin numbers for the ultrasonic sensor
const int trigPin = 9;  // Trigger pin of the ultrasonic sensor
const int echoPin = 10; // Echo pin of the ultrasonic sensor

Servo rotatingServo;    // Servo that rotates continuously
Servo indicatingServo;  // Servo that moves to 90 degrees when something is detected

int rotatingServoPin = 3;   // Pin for the rotating servo motor
int indicatingServoPin = 6; // Pin for the indicating servo motor

const int ledPin = 7;       // LED pin
const int buzzerPin = 8;    // Buzzer pin

long duration;              // Variable to store the duration of the pulse from the ultrasonic sensor
int distance;               // Variable to store the distance calculated from the ultrasonic sensor
int thresholdDistance = 20; // Distance threshold in cm to trigger detection actions

void setup() {
  // Set up the ultrasonic sensor pins
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);

  // Set up the LED and buzzer pins
  pinMode(ledPin, OUTPUT);
  pinMode(buzzerPin, OUTPUT);

  // Attach the servo motors to the corresponding pins
  rotatingServo.attach(rotatingServoPin);
  indicatingServo.attach(indicatingServoPin);

  // Start serial communication for debugging and communication with computer
  Serial.begin(9600);
}

void loop() {
  // Check if there is data available from the Python script
  if (Serial.available() > 0) {
    char signal = Serial.read();  // Read the signal sent from Python

    // If the signal is '1', trigger the servo, LED, and buzzer
    if (signal == '1') {
      Serial.println("Animal detected! Activating servo, LED, and buzzer...");

      // Turn on the LED and buzzer
      digitalWrite(ledPin, HIGH);
      digitalWrite(buzzerPin, HIGH);

      // Move the indicating servo to 90 degrees
      indicatingServo.write(90);
      delay(1000);  // Wait for 1 second

      // Move the second servo back to the normal position (0 degrees)
      indicatingServo.write(0);

      // Turn off the LED and buzzer after 1 second
      delay(1000);  
      digitalWrite(ledPin, LOW);
      digitalWrite(buzzerPin, LOW);
    }
  }
}

// Function to get the distance from the ultrasonic sensor
int getDistance() {
  // Send a 10us pulse to trigger the sensor
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);

  // Read the echo pin and calculate the duration of the pulse
  duration = pulseIn(echoPin, HIGH);

  // Calculate the distance in cm (duration / 2 because the pulse travels to the object and back)
  int distanceCm = duration * 0.034 / 2;

  // Print the distance for debugging
  Serial.print("Distance: ");
  Serial.print(distanceCm);
  Serial.println(" cm");

  return distanceCm;
}
