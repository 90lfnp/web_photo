#include <Wire.h>
int address = 73;
void setup()
{
    Serial.begin(9600);
    Wire.begin();
    Wire.beginTransmission(0x48);             // connect to DS1621 (#0)
    Wire.write(0xAC); // Access Config
    Wire.write(0x02);                    // set for continuous conversion
    Wire.beginTransmission(0x48);             // restart
    Wire.write(0xEE); // start conversions
    Wire.endTransmission();
}
void loop()
{
    int8_t firstByte;
    int8_t secondByte;
    float temp = 0;
    delay(1000);                       // give time for measurement
    Wire.beginTransmission(0x48);
    Wire.write(0xAA); // read temperature command
    Wire.endTransmission();
    Wire.requestFrom(0x48, 2);        // request two bytes from DS1621 (0.5 deg. resolution)
    firstByte = Wire.read();        // get first byte
    secondByte = Wire.read();        // get second byte
    temp = firstByte;
    if (secondByte) // if there is a 0.5 deg difference
        temp += 0.5;
    Serial.println(temp);
    int temp2 = read_temp(address);
    Serial.println(temp2);
}
int read_temp(int address){
  Wire.beginTransmission(address);
  Wire.write(0);
  Wire.endTransmission();
  Wire.requestFrom(address,1);
  while(Wire.available() == 0);
  int c = Wire.read();
  return c;
}
