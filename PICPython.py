from math import *
import tkinter as tk
calculo = ' '
calculo_tela = ' '
interface = tk.Tk()
operacoes = {'sqrt': sqrt, 'pi': pi, 'sin': sin, 'cos': cos,
             'tan': tan, 'degrees': degrees, 'radians': radians}


def calcular(simbolo_calc, simbolo_tela=None):
    global calculo
    global calculo_tela
    calculo += str(simbolo_calc)
    calculo_tela += str(simbolo_tela)
    interface_digitavel.delete(1.0, "end")
    interface_digitavel.insert(1.0, calculo_tela)


def resultado_calculo():
    global calculo
    global calculo_tela
    while calculo.count('(') > calculo.count(')'):
        calculo += ')'
    try:
        calculo_tela = calculo = str(eval(calculo, operacoes))
        interface_digitavel.delete(1.0, "end")
        interface_digitavel.insert(1.0, calculo)
    except Exception as error:
        print(error)
        limpar_tela()
        interface_digitavel.insert(1.0, "Error")
        pass


def limpar_tela():
    global calculo
    global calculo_tela
    calculo_tela = calculo = ' '
    interface_digitavel.delete(1.0, "end")
    interface_digitavel.insert(1.0, calculo_tela)


interface.geometry("375x225")
interface_digitavel = tk.Text(interface, height=2, width=30, font=("Arial", 16))
interface_digitavel.grid(columnspan=40)
#   Definir botões
bt_1 = tk.Button(interface, text="1", command=lambda: calcular(1, 1), width=5, font=("Arial", 12))
bt_1.grid(row=2, column=0)
bt_2 = tk.Button(interface, text="2", command=lambda: calcular(2, 2), width=5, font=("Arial", 12))
bt_2.grid(row=2, column=1)
bt_3 = tk.Button(interface, text="3", command=lambda: calcular(3, 3), width=5, font=("Arial", 12))
bt_3.grid(row=2, column=2)
bt_4 = tk.Button(interface, text="4", command=lambda: calcular(4, 4), width=5, font=("Arial", 12))
bt_4.grid(row=3, column=0)
bt_5 = tk.Button(interface, text="5", command=lambda: calcular(5, 5), width=5, font=("Arial", 12))
bt_5.grid(row=3, column=1)
bt_6 = tk.Button(interface, text="6", command=lambda: calcular(6, 6), width=5, font=("Arial", 12))
bt_6.grid(row=3, column=2)
bt_7 = tk.Button(interface, text="7", command=lambda: calcular(7, 7), width=5, font=("Arial", 12))
bt_7.grid(row=4, column=0)
bt_8 = tk.Button(interface, text="8", command=lambda: calcular(8, 8), width=5, font=("Arial", 12))
bt_8.grid(row=4, column=1)
bt_9 = tk.Button(interface, text="9", command=lambda: calcular(9, 9), width=5, font=("Arial", 12))
bt_9.grid(row=4, column=2)
bt_0 = tk.Button(interface, text="0", command=lambda: calcular(0, 0), width=5, font=("Arial", 12))
bt_0.grid(row=5, column=1)
bt_ponto = tk.Button(interface, text=".", command=lambda: calcular('.', '.'), width=5, font=("Arial", 12))
bt_ponto.grid(row=5, column=0)
bt_resultado = tk.Button(interface, text="=", command=lambda: resultado_calculo(), width=5, font=("Arial", 12))
bt_resultado.grid(row=5, column=2)
bt_parenteses_esq = tk.Button(interface, text="(", command=lambda: calcular('(', '('), width=5, font=("Arial", 12))
bt_parenteses_esq.grid(row=4, column=3)
bt_parenteses_dir = tk.Button(interface, text=")", command=lambda: calcular(')', ')'), width=5, font=("Arial", 12))
bt_parenteses_dir.grid(row=5, column=3)
bt_adicao = tk.Button(interface, text="+", command=lambda: calcular('+', '+'), width=5, font=("Arial", 12))
bt_adicao.grid(row=2, column=3)
bt_subtracao = tk.Button(interface, text="-", command=lambda: calcular('-', '-'), width=5, font=("Arial", 12))
bt_subtracao.grid(row=3, column=3)
bt_divisao = tk.Button(interface, text="÷", command=lambda: calcular('/', '÷'), width=5, font=("Arial", 12))
bt_divisao.grid(row=2, column=4)
bt_multiplicacao = tk.Button(interface, text="×", command=lambda: calcular('*', '×'), width=5, font=("Arial", 12))
bt_multiplicacao.grid(row=3, column=4)
bt_potenciacao = tk.Button(interface, text="^", command=lambda: calcular('**', '^'), width=5, font=("Arial", 12))
bt_potenciacao.grid(row=4, column=4)
bt_raiz = tk.Button(interface, text="√", command=lambda: calcular('sqrt(', '√('), width=5, font=("Arial", 12))
bt_raiz.grid(row=5, column=4)
bt_clear = tk.Button(interface, text="CE", command=lambda: limpar_tela(), width=5, font=("Arial", 12))
bt_clear.grid(row=6, column=0)
bt_pi = tk.Button(interface, text="π", command=lambda: calcular('pi', 'π'), width=5, font=("Arial", 12))
bt_pi.grid(row=2, column=5)
bt_sen = tk.Button(interface, text="sen", command=lambda: calcular('sin(radians(', 'sen('), width=5, font=("Arial", 12))
bt_sen.grid(row=3, column=5)
bt_cos = tk.Button(interface, text="cos", command=lambda: calcular('cos(radians(', 'cos('), width=5, font=("Arial", 12))
bt_cos.grid(row=4, column=5)
bt_tan = tk.Button(interface, text="tan", command=lambda: calcular('tan(radians(', 'tan('), width=5, font=("Arial", 12))
bt_tan.grid(row=5, column=5)
#   Abrir janela
interface.mainloop()

