class Carro:
    modelo : str
    marca : str
    cor : str
    odometro : 0.0
    motor_on : False
    tanque : float
    consumo : float

    def __init__(self, modelo : str, marca : str, cor : str,
                       odometro : float, motor : bool, tanque:
                       float, consumo : float):
        self.modelo = modelo
        self.marca = marca
        self.cor = cor
        self.odometro = odometro
        self.motor_on = motor
        self.tanque = tanque
        self.consumo = consumo

    def ligar(self):
        if not self.motor_on:
            self.motor_on = True
        else:
            raise Exception("Erro: Motor já ligado!")

    def acelerar(self, velocidade : float, tempo : float):
        if self.motor_on:
            if ((velocidade * tempo) / self.consumo) <= self.tanque:
                self.odometro += velocidade * tempo
                self.tanque -= (velocidade * tempo) / self.consumo
            else:
                raise Exception("Erro: Não tem gasolina suficiente para essa distância.")

        else:
            raise Exception("Erro: Não é possível acelerar! Motor desligado!")

    def desligar(self):
        if self.motor_on:
            self.motor_on = False
        else:
            raise Exception("Erro: Motor já desligado!")

    def __str__(self):
        info = (f'Carro {self.modelo}, marca {self.marca}, '
                f'cor {self.cor}\n{self.odometro} Km, '
                f'motor {self.motor_on}, '
                f'tanque {self.tanque}, consumo {self.consumo}')
        return info





