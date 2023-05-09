#include <base64.hpp>
#include <Wire.h>

int led = LED_BUILTIN;
int brightness = 0;
int fadeAmount = 5;

void setup()
{
  pinMode(led, OUTPUT);
  Wire.begin(0x30);
  Wire.onRequest(requestEvent);
}

void fade()
{
  analogWrite(led, brightness);

  brightness = brightness + fadeAmount;

  if (brightness <= 0 || brightness >= 255) {
    fadeAmount = -fadeAmount;
  }
  delay(30);
}

void loop()
{
  //delay(100);
  fade();
}

void requestEvent()
{
  Wire.write("Hello from ItsyBitsy!");
}
