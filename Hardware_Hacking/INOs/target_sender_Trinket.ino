#include <Wire.h>

void setup()
{
  pinMode(LED_BUILTIN, OUTPUT);
  Wire.begin(0x32);
  Wire.onRequest(requestEvent);
}

void blink()
{
  digitalWrite(LED_BUILTIN, HIGH);
  delay(1000);
  digitalWrite(LED_BUILTIN, LOW);
  delay(1000);
}

void loop()
{
  blink();
  //delay(100);
}

void requestEvent()
{
  Wire.write("Hello from Trinket M0!");
}
