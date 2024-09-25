const int speaker = 9;

//Notas
int doo = 528;
int re = 592;
int mi = 665;
int fa = 704;
int sol = 790;


void setup() {
  // Inicializa a comunicação serial com uma taxa de transmissão de 9600 bps
  Serial.begin(9600);
  pinMode(speaker, OUTPUT);
}

void loop() {
  // Se houver dados disponíveis para leitura

  
  if (Serial.available() > 0) {
    // Lê o dado recebido

    
    char receivedChar = Serial.read();

    
    
    // Converte o dado para inteiro
    int contador = receivedChar - '0';

  
    
      if (contador == 1){
        tone(speaker, doo);
        
      }

      else if (contador == 2){
        tone(speaker, re);
        
      }
      else if (contador == 3){
        tone(speaker, mi);
       
      }
      else if (contador == 4){
        tone(speaker, fa);
        
      }
      else if (contador == 5){
        tone(speaker, sol);
        
      }
      else {
        noTone(speaker);
        
      }


  

  }
}