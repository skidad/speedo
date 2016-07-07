

int probePin = 5; // analog 5
int val = 0; // reading from probePin
int boardLedPin = 13;
int highLow = LOW;
int lastVal = 1;
int updateTime = 0;

void setup() {

  Serial.begin(9600);  // initiate serial connection for debugging/etc

  // initialize digital pin 13 as an output.
  pinMode(boardLedPin, OUTPUT);

}

void loop() {
  val = analogRead(probePin);  // take a reading from the probe
  if (val == 0 ) {
    if ( lastVal != 0 ) { 
       highLow = abs( highLow - 1); // toggle highLow every revolution
       digitalWrite(boardLedPin, highLow);
    }
  }
  Serial.print(val);
  Serial.print(";");
  
  lastVal = val;
  
  delay(updateTime);
  
}

