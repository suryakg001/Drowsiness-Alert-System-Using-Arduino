#include <Wire.h>
#include <LiquidCrystal_I2C.h>

#define BUZZER 8
#define RELAY 9

LiquidCrystal_I2C lcd(0x27, 16, 2);

char lastCommand = 'X';

void setup()
{
  pinMode(BUZZER, OUTPUT);
  pinMode(RELAY, OUTPUT);

  digitalWrite(BUZZER, LOW);
  digitalWrite(RELAY, LOW);

  Serial.begin(9000);

  lcd.init();
  lcd.backlight();

  lcd.setCursor(0,0);
  lcd.print("ANTI SLEEP");
  lcd.setCursor(0,1);
  lcd.print("SYSTEM READY");

  delay(1500);
  lcd.clear();
}

void loop()
{
  if (Serial.available())
  {
    char command = Serial.read();

    if(command != lastCommand)
    {
      lastCommand = command;

      if(command == '1')
      {
        digitalWrite(RELAY, LOW);      // Motor ON
        digitalWrite(BUZZER, LOW);     // Buzzer OFF

        lcd.clear();
        lcd.setCursor(0,0);
        lcd.print("Eyes : OPEN");

        lcd.setCursor(0,1);
        lcd.print("Motor Running");
      }

      if(command == '0')
      {
        digitalWrite(RELAY, HIGH);     // Motor OFF
        digitalWrite(BUZZER, HIGH);    // Buzzer ON

        lcd.clear();
        lcd.setCursor(0,0);
        lcd.print("SLEEP ALERT");

        lcd.setCursor(0,1);
        lcd.print("Wake Up!!");
      }
    }
  }
}
