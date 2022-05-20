import smbus  # import SMBus module of I2C
from time import sleep  # import

import tkinter as tk
from tkinter import ttk
PWR_MGMT_1 = 0x6B
SMPLRT_DIV = 0x19
CONFIG = 0x1A
INT_ENABLE = 0x38
GYRO_XOUT_H = 0x43
GYRO_YOUT_H = 0x45
GYRO_ZOUT_H = 0x47
Flag_inter = 0

def boton_parar():
    print("parar")

def boton_reiniciar():
    print("reiniciar")

def boton_grafica():
    print("grafica")


def boton_inicio():

    def MPU_Init():
        # write to sample rate register
        bus.write_byte_data(Device_Address, SMPLRT_DIV, 7)
        # Write to power management register
        bus.write_byte_data(Device_Address, PWR_MGMT_1, 1)
        # Write to Configuration register
        bus.write_byte_data(Device_Address, CONFIG, 0)
        # Write to interrupt enable register
        bus.write_byte_data(Device_Address, INT_ENABLE, 1)

    def read_raw_data(addr):
        # Accelero and Gyro value are 16-bit
        high = bus.read_byte_data(Device_Address, addr)
        low = bus.read_byte_data(Device_Address, addr + 1)
        # concatenate higher and lower value
        value = ((high << 8) | low)
        # to get signed value from mpu6050
        if (value > 32768):
            value = value - 65536
        return value

    bus = smbus.SMBus(1)  # or bus = smbus.SMBus(0) for older version boards
    Device_Address = 0x68  # MPU6050 device address

    MPU_Init()
    print("Se leen datos del Giroscopio")

        # Read Gyroscope raw value
        gyro_x = read_raw_data(GYRO_XOUT_H)
        gyro_y = read_raw_data(GYRO_YOUT_H)
        gyro_z = read_raw_data(GYRO_ZOUT_H)

        # Full scale range +/- 250 degree/C as per sensitivity scale factor
        Gx = gyro_x / 131.0
        Gy = gyro_y / 131.0
        Gz = gyro_z / 131.0

        print("Gx=%.2f" % Gx, u'\u00b0' + "/s", "\tGy=%.2f" % Gy, u'\u00b0' + "/s", "\tGz=%.2f" % Gz, u'\u00b0' + "/s")
        sleep(0)


root = tk.Tk()
root.config(width=280, height=200)
root.title("interface giroscopio")
etiqueta = ttk(text= "interface principal")
etiqueta.place(x=25, y=25)
inicio = ttk.Button(text="inicio", command=boton_inicio)
inicio.place(x=50, y=50)
parar = ttk.Button(text="parar", command=boton_parar)
parar.place(x=150, y=50)
reiniciar = ttk.Button(text="reiniciar", command=boton_reiniciar)
reiniciar.place(x=50, y=100)
grafica = ttk.Button(text="grafica", command=boton_grafica)
grafica.place(x=100, y=150)
cerrar = ttk.Button(text="cerrar", command=root.quit)
cerrar.place(x=150, y=100)

root.mainloop()