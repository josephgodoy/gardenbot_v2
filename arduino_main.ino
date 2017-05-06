// Important global variables.

int transistorPin = A0;
int blinkPin = 13;
int inputvalue;

// Retrieve bytes from Python script, convert to int.

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

   // Start serial connection at a 9600 baud rate.

   Serial.begin(9600);

   // Initializing analog output pins, A0 and 13.

   pinMode(transistorPin, OUTPUT);
   pinMode(blinkPin, OUTPUT);
}

void loop()
{

  // While loop to wait until the serial connection is ready.

  while(!Serial.available())
  {
     delay(2);
  }

  //Important: This array catches newline characters from the serial monitor.
  char new_line_catch[1]  = {0};

  // Fetch values from the Python script's output.
  int value = retrieveCoord();

  Serial.readBytes(new_line_catch, 1);

  delay(10);

  if (value == 1)
  {
     digitalWrite(transistorPin, HIGH); // Apply 5V to the motor transistor.
     digitalWrite(blinkPin, HIGH); // Turn on test LED.
     delay(2000); // Wait for 2 seconds. Adjust to taste.
     digitalWrite(transistorPin, LOW);  // Shut off the 5V connection.
     digitalWrite(blinkPin, LOW); // Turn off test LED.

  }

  delay(2000);

}
