#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Cristobal'
__email__ = 'lopeztobal@gmail.com'
__version__ = '1.0.0'

from tkinter import (Tk, Frame, Canvas)
import random


class Pelota(Frame):
    def __init__(self, canvas, raqueta,  color):
        """
        Init Constructor Class ball to plot the ball
        :param canvas: our canvas object
        :param raqueta: our paddle
        :param color: the color of our ball
        """
        Frame.__init__(self, master=None)
        self.canvas = canvas
        self.raqueta = raqueta
        self.color = color
        self.puntos = 0
        self.textPuntos = 0
        self.vidas = 3
        self.textVidas = 0
        self.textTitle = 0
        self.textInstructions = 0
        self.golpea_fondo = False
        self.ball = self.canvas.create_oval(10, 10, 25, 25, fill=self.color, outline='white', width=1)
        self.textTitle = self.canvas.create_text(50, 10, text='My Pong', fill='green', font=('Courier', 16), anchor='w')
        self.canvas.delete(self.textPuntos)
        self.textPuntos = self.canvas.create_text(50, 30, text='Score: ' + str(self.puntos), fill='green',
                                                  font=('Courier', 16), anchor='w')
        self.canvas.delete(self.textVidas)
        self.textVidas = self.canvas.create_text(50, 50, text='Health: ' + str(self.vidas), fill='green',
                                                 font=('Courier', 16), anchor='w')
        self.canvas.move(self.ball, 245, 100)
        empezar = list(range(-3, 3))
        empezar.remove(0)
        random.shuffle(empezar)
        self.x = empezar[0]
        self.y = -3
        self.canvas_height = self.canvas.winfo_reqheight()
        self.canvas_width = self.canvas.winfo_reqwidth()
        self.canvas.bind_all('<Key>', self.key)
        self.canvas.bind_all('<Button-1>', self.inicia_juego)

    def inicia_juego(self, evt):
        """
        We start the game pressing left mouse button, then we start the ball to move
        :param evt: Out event to Start the game
        """
        if evt.num == 1:
            self.canvas.itemconfig(self.textTitle, state='hidden')
            self.canvas.itemconfig(self.textInstructions, state='hidden')
            self.dibujar()

    def pantalla_inicio(self):
        """
        Create  the text to start the game

        """
        self.textTitle = self.canvas.create_text(self.canvas_width / 2 - 200, self.canvas_height / 2, text='MY PONG',
                                                 fill='red', font=('Barbieri-Book', 50), anchor='w')
        self.textInstructions = self.canvas.create_text(self.canvas_width / 2 - 200, self.canvas_height / 2 + 50,
                                                        text='Press Left Mouse Button to Start the Game',
                                                        fill='red', font=('Barbieri-Book', 12), anchor='w')

    def key(self, evt):
        """
        Finishing the game when we are pressing Q or q key on our keyboard
        :param evt: Our event to finish the game
        """
        if evt.char == 'q' or evt.char == 'Q':
            self.master.destroy()

    def golpea_raqueta(self, pos):
        """
        We're testing when the ball touch the paddle
        :param pos: the canvas position of the paddle
        :return: A boolean value
        """
        raqueta_pos = self.canvas.coords(self.raqueta.raqueta)
        if pos[2] >= raqueta_pos[0] and pos[0] <= raqueta_pos[2] and raqueta_pos[1] <= pos[3] <= raqueta_pos[3]:
            return True
        return False

    def puntuar(self):
        """
        We calculate gamer's points and we put score in the canvas

        """
        self.puntos += 1
        pos = self.canvas.coords(self.ball)
        if self.golpea_raqueta(pos):
            self.canvas.delete(self.textPuntos)
            self.textPuntos = self.canvas.create_text(50, 30, text='Scores: ' + str(self.puntos), fill='green',
                                                      font=('Courier', 16), anchor='w')

    def numvidas(self):
        """
        We calculate how many lives are resting to finish the game, and we put the health
        score in the canvas game

        """
        pos = self.canvas.coords(self.ball)
        if pos[3] == self.canvas_height and self.vidas is not 0:
            self.vidas -= 1
            self.canvas.delete(self.textVidas)
            self.textVidas = self.canvas.create_text(50, 50, text='Health: ' + str(self.vidas), fill='green',
                                                     font=('Courier', 16), anchor='w')
        elif self.vidas is 0:
            self.canvas.create_text(self.canvas_width / 2 - 200, self.canvas_height / 2, text='GAME OVER', fill='red',
                                    font=('Courier', 50), anchor='w')
            self.canvas.create_text(self.canvas_width / 2 - 200, self.canvas_height / 2 + 60, text='PRESS Q TO QUIT',
                                    fill='magenta', font=('Courier', 18), anchor='w')
            self.x = self.y = 0

    def dibujar(self):
        """
        With this method we plot the ball while the ball are moving around the canvas

        """
        self.canvas.move(self.ball, self.x, self.y)
        pos = self.canvas.coords(self.ball)
        if pos[1] <= 0:
            self.y = 3
        if pos[3] >= self.canvas_height:
            self.y = -3
        if self.golpea_raqueta(pos):
            self.y = -3
            self.puntuar()
        if pos[0] <= 0:
            self.x = 3
        if pos[2] >= self.canvas_width:
            self.x = -3
        self.numvidas()
        self.after(10, self.dibujar)


class Raqueta(Frame):
    def __init__(self, canvas, color):
        """
        Init Constructor Class paddle to plot the paddle
        :param canvas: Our canvas game
        :param color: the color of the paddle
        """
        Frame.__init__(self, master=None)
        self.canvas = canvas
        self.color = color
        self.x = 0
        self.raqueta = self.canvas.create_rectangle(0, 0, 100, 10, fill=self.color)
        self.canvas.move(self.raqueta, 200, 480)
        self.canvas_width = self.canvas.winfo_reqwidth()
        self.canvas.bind_all('<KeyPress-Left>', self.keypressed)
        self.canvas.bind_all('<KeyRelease-Left>', self.keyrelease)
        self.canvas.bind_all('<KeyPress-Right>', self.keypressed)
        self.canvas.bind_all('<KeyRelease-Right>', self.keyrelease)

    def dibujar(self):
        """
         With this method we plot the paddle

        """
        self.canvas.move(self.raqueta, self.x, 0)
        pos = self.canvas.coords(self.raqueta)
        if pos[0] == 0:
            self.x = 0
        if pos[2] >= self.canvas_width:
            self.x = 0
        self.after(10, self.dibujar)

    def keypressed(self, evt):
        """
        We define how to move the paddle our gamer
        :param evt: event to move the paddle
        """
        pos = self.canvas.coords(self.raqueta)
        if evt.keysym == 'Left':
            if pos[0] < 0:
                self.x = 0
            else:
                self.x = -2
        elif evt.keysym == 'Right':
            if pos[2] >= self.canvas_width:
                self.x = 0
            else:
                self.x = 2

    def keyrelease(self, evt):
        """
        The paddle stops moving when the gamer release the keys
        :param evt: event to stop the paddle
        """
        if evt.keysym == 'Left' or evt.keysym == 'Right':
            self.x = 0


def main():
    """
    Our main method to define our game. Initialize the tk window, the canvas.

    """
    tk = Tk()

    tk.title('TK-Pong Game')
    tk.geometry('500x500+0+0')

    canvas = Canvas(tk, width=500, height=500, bd=0, highlightthickness=0, background='black')
    raqueta = Raqueta(canvas, 'blue')
    pelota = Pelota(canvas, raqueta, 'yellow')
    canvas.pack()
    if not pelota.golpea_fondo:
        pelota.pantalla_inicio()
        raqueta.dibujar()
    tk.mainloop()

main()
