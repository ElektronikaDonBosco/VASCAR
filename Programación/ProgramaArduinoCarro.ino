/*
 Mediante este programa controlaremos el carro mediante un programa pid
 cada vez que el carro carro se detenga en la habitación pulsaremos el 
 boton para que se reinicie el programa 
*/

//Definicimos las variables del las velocidades de los motores e indicamos los pines para los motores
int Rueda_drc = 10; 
int Vel_drc; 
int Vel_drc2;
int Rueda_izq = 11;
int Vel_izq;
int Vel_izq2;
int v0 = 30;

//Variables para arranque, parada e indicaciones de los leds
int boton=13;
int boton_estado;
char leo ;
int const led = 7;
int const led2 = 8;
int const led3 = 9;
int tension;
int lipo = A5;

//Variables de los sensores 
int SD2; // Derecha
int SD1; 
int SI1;
int SI2; // Izquierda 

//Distintas variables para el algoritmo p.d.
float p = 0.0; 
float p2 = 0.0;
float kp = 0.005205;
float kp2 = 0.0055;
float d = 0.0;
float kd = 0.01;
float u = 0.0;
float u2 = 0.0;
void setup()/*Indicamos las salidas y entradas del arduino*/
{
pinMode(SD1, INPUT);
pinMode(SD2, INPUT);
pinMode(SI1,INPUT);
pinMode(SI2,INPUT);
Serial.begin(9600);
pinMode(Rueda_drc,OUTPUT);
pinMode(Rueda_izq,OUTPUT);
pinMode(led,OUTPUT);
pinMode(led2,OUTPUT);
pinMode(led3,OUTPUT);
pinMode(boton,INPUT);
pinMode(lipo,INPUT);
}

void loop() 
//Empezaremos haciendo una lectura de la bateria para tener un control sobre ella, y en caso de que este baja se nos encendera un led y no podremos arrancar
{
tension = analogRead(lipo);  // Lectura de la bateria 
   if (tension < 650)
        {
        digitalWrite(led,HIGH);
        digitalWrite(led2,LOW);
        digitalWrite(led3,LOW);
        digitalWrite(Rueda_drc,LOW);
        digitalWrite(Rueda_izq,LOW);
        }
    else{                       //La bateria esta bien y podemos arrancar 
        digitalWrite(led,LOW);
        digitalWrite(led2,HIGH);
        digitalWrite(led3,HIGH);
  while(boton_estado == 0){   // Lee el estado el boton a ver si esta apretado 
  leo = Serial.read();
  boton_estado = digitalRead(boton);
 SD2 = analogRead(A1);        //Lee los valores que le llegan de los sensores de forma analogica
 SD1 = analogRead(A2);
 SI1 = analogRead (A3);
 SI2 = analogRead (A4);
                              //Con los valores recividos calculamos el p.d
 p = -2*SD2 -SD1 +SI1 +2*SI2;    
 p2 = -4*SD2 -2*SD1 + 2*SI1 + 4*SI2;
 u = p * kp + d * kd;
 u2 = p2 * kp2;
 Vel_drc = v0 + (u);
 Vel_izq = v0 - (u);
 Vel_drc2 = v0 + (u2);
 Vel_izq2 = v0 - (u2);
  
if (SI2<800 and SI1>800 and SD1>800 and SD2<800){  //Va recto y mantienen ambas ruedas la misma velociad 
  analogWrite(Rueda_drc, v0);
  analogWrite(Rueda_izq, v0);
  }
if (SI2>800 and SI1>800 and SD1<800 and SD2<800){  //Se ha salido por la derecha y la rueda izquierda tendra más velocidad 
  analogWrite(Rueda_drc, Vel_drc);
  analogWrite(Rueda_izq, Vel_izq);
 }
if (SI2>800 and SI1>800 and SD1>800 and SD2<800){ //Se ha salido por la derecha y la rueda izquierda aumentara aun más su velocidad 
  analogWrite(Rueda_drc, Vel_drc2);
  analogWrite(Rueda_izq, Vel_izq);
 }
if (SI2<800 and SI1<800 and SD1>800 and SD2>800)  //Se ha salido por la izquieda y la rueda derecha tendra más velocidad 
  analogWrite(Rueda_drc, Vel_drc);
  analogWrite(Rueda_izq, Vel_izq);
  }
if (SI2<800 and SI1>800 and SD1>800 and SD2>800){ //Se ha salido por la izquierda y la rueda derecha aumentara aun más velocidad 
  analogWrite(Rueda_drc, Vel_drc);
  analogWrite(Rueda_izq, Vel_izq2);
  }
if (Serial.available()>0){
   leo = Serial.read();
  while(leo == 'a'){                            //Si lee el QR adecuado se parara y se nos encendera un led que nos indicara 
  analogWrite(Rueda_drc, 0);
  analogWrite(Rueda_izq, 0);
    digitalWrite(led2,LOW);
    digitalWrite(led,LOW);
    digitalWrite(led3,HIGH);
  
  while (boton_estado == 0){                      //Para poder volver a reanudar la marcha daremos la pulsador 
   boton_estado = digitalRead(boton);
  }
  while (boton_estado == 1){
    boton_estado = digitalRead(boton);
  }
  return;
      }
    }
  }
}

