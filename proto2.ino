// Important global variables.

int transistorPin = A0;
int blinkPin = 13;

// Retrieve value from Python script.

int retrieveCoord()
{
   while(!Serial.available())
   {
      delay(2);
   }

   char input[1] = {0};
   Serial.readBytes(input, 1);
   int input_boolean = (int)input[0];

   if (input_boolean == 49)
   {
      inputvalue = 1;
   }
   else if (input_boolean == 48)
   {
      inputvalue = 0;
   }

   return inputvalue;
}

void setup()
{
   Serial.begin(9600);
   pinMode(transistorPin, OUTPUT);
   pinMode(blinkPin, OUTPUT);
}

void loop()
{

  while(!Serial.available())
  {
     delay(2);
  }

  char new_line_catch[1]  = {0};

  int value = retrieveCoord();

  Serial.readBytes(new_line_catch, 1);

  delay(10);

  if (value == 1)
  {
    
     digitalWrite(transistorPin, HIGH); // turn on the motor
     digitalWrite(blinkPin, HIGH); // turn on the LED
     delay(1000);
     digitalWrite(transistorPin, LOW);  // turn off the motor
     digitalWrite(blinkPin, LOW);  // turn off the LED

  }

  delay(1000);

}
