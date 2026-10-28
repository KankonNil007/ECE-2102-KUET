
const int sensorPin = A0;
const int sampleCount = 500;
const unsigned long sampleIntervalUs = 10000; // 10 ms

void setup() {
  Serial.begin(115200);
}

void loop() {
  Serial.println("BEGIN");

  unsigned long nextSample = micros();

  for (int i = 0; i < sampleCount; i++) {
    while ((long)(micros() - nextSample) < 0) {
      // Wait for the next sampling instant
    }

    int reading = analogRead(sensorPin);
    Serial.println(reading);

    nextSample += sampleIntervalUs;
  }

  Serial.println("END");
}
