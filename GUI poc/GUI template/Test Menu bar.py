import tkinter as tk
from tkinter import messagebox
from tkinter import ttk


class MenuBar(tk.Menu):
    def __init__(self, parent):
        tk.Menu.__init__(self, parent)