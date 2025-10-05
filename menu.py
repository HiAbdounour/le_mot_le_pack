from noormi.gaming import *


# class for Button management

class Button:
    def __init__(self,lvl:int,rect:tuple[int,int,pygame.Color],txt_rect:tuple[str,int,int,pygame.Color]):
        self.level = lvl
        self.rect = rect
        self.txt_rect = txt_rect
    def display(self):
        draw_rectangle(Point(self.rect[0],self.rect[1]),50,50,self.rect[2],1)
        display_text(self.txt_rect[0],('Comic sans MS',32),(self.txt_rect[1],self.txt_rect[2]),clr=self.txt_rect[3],text_bold=True)
    def is_clicked(self,pos:Point)-> int:
        if self.rect[0]-25<=pos.x<=self.rect[0]+25 and self.rect[1]-25<=pos.y<=self.rect[1]+25:
            return self.level
        return -1
    

# menu management 

def print_menu():
    display_text("Le Mot",("Comic sans MS",90),(95,80),text_bold=True)
    buttons_list = []
    for i in range(3,7):
        display_text("Jouer avec des mots de",("Comic sans MS",25),(105,230),text_bold=True)
        display_text("lettres",("Comic sans MS",25),(205,330),text_bold=True)
        b = Button(i,(100*(i-2),300,pygame.Color(60,60,60)),(str(i),100*(i-2)-13,275,PYGAME_WHITE))
        buttons_list.append(b)
        b.display()
    return buttons_list

def choice_level(list_buttons,pos):
    for b in list_buttons:
        if b.is_clicked(pos)!=-1:
            return b.is_clicked(pos)
    return -1
