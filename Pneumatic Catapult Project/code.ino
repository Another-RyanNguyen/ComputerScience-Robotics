int sol = 3; //The Solenoid pin (White Wire)
int but = 4; //Button Pit
 
void setup() {
  pinMode(sol, OUTPUT);
  pinMode(but, INPUT);
}
 
void loop() {
  // put your main code here, to run repeatedly:
  if (digitalRead(but) == HIGH){ //When you press the button
    digitalWrite(sol, HIGH); //Extend Pneumatic
    delay(1000); //Wait
  }
  else{ //Set Pneumatic back to low 
    digitalWrite(sol, LOW);
  }
}
