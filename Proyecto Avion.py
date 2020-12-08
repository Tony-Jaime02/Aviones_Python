import pygame, sys
import pyautogui
import random
#nubes
def nubes (pos1,pos2,pos3):
    screen.blit(nube1, (900,pos1))
    screen.blit(nube2, (900,pos2))
    screen.blit(nube3, (900,pos3))
    return
def nubesres (res1,res2,res3):
    nub1 = Fontnubes.render(str(res1),1,(00,00,00), (255, 255, 255)) 
    screen.blit(nub1, (1000, 90))
    nub2 = Fontnubes.render(str(res2),1,(00,00,00), (255, 255, 255)) 
    screen.blit(nub2, (1000, 280))
    nub3 = Fontnubes.render(str(res3),1,(00,00,00), (255, 255, 255)) 
    screen.blit(nub3, (1000, 470))
    
def decision (x,y,pr):
    if x>=900 and y>0 and y<150:
        if pygame.mouse.get_pressed()[0]:
            a=1
            return a
    elif x>=900 and y>200 and y<350:
        if pygame.mouse.get_pressed()[0]:
            a=2
            return a
    elif x>=900 and y>400 :
        if pygame.mouse.get_pressed()[0]:
            a=3
            return a
def siguiente():
    pyautogui.moveTo(300, 500)
    pygame.time.delay(60)
    correct.play()
    
def contador(score,intentos):
    sco=Fontnubes.render(str(score),1,(255, 255, 255), (69, 245, 87))
    screen.blit(sco, (50, 550))
pr=0
pos1=0
pos2=200
pos3=400
pygame.init()
screen = pygame.display.set_mode((1200,650))
calibriFont = pygame.font.SysFont("Calibri", 40)
calibriFont2 = pygame.font.SysFont("Calibri", 30)
Fontnubes = pygame.font.SysFont("Calibri", 90)
#Sonidos
pygame.mixer.init()
correct = pygame.mixer.Sound("correct.wav")
wrong = pygame.mixer.Sound("wrong.wav")
start = pygame.mixer.Sound("start.wav")

fondo = pygame.image.load("fondo3.jpg")
fondo = pygame.transform.scale(fondo, (1200,650))

fondo2 = pygame.image.load("fondo3.jpg")
fondo2 = pygame.transform.scale(fondo, (1200,650))

avion = pygame.image.load("1_2.png")
avion = pygame.transform.scale(avion, (200,200))

nube1 = pygame.image.load("nube 1_1.png")
nube1 = pygame.transform.scale(nube1, (250,250))

nube2 = pygame.image.load("nube 1_2.png")
nube2 = pygame.transform.scale(nube2, (250,250))

nube3 = pygame.image.load("nube 1_3.png")
nube3 = pygame.transform.scale(nube3, (250,220))

#inicializcion del fondo
delta=0
delta2=1200
score=0
intentos=1
inten=0
B=0

while True:
    x, y = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()    
    #movimiento del fondo
    screen.blit(fondo,(delta,0))
    screen.blit(fondo2,(delta2,0))
    delta=delta - 5
    delta2=delta2 - 5
    if delta <= -1200:
        delta = delta2 + 1200    
    if delta2 <=-1200:
        delta2 = delta + 1200     
    screen.blit(avion, (x-100,y-100))
    if pr==0:
        inicio = calibriFont.render("Bienvenido a este juego de matemáticas,",1,(255, 255, 255), ( 60, 216, 241)) 
        inicio2 = calibriFont.render("donde practicarás tus conocimientos básicos",1,(255, 255, 255), ( 60, 216, 241)) 
        screen.blit(inicio, (270, 200))
        screen.blit(inicio2, (250, 240))
        start.play()
        if pygame.mouse.get_pressed()[0]:
            pr = 1
            pyautogui.moveTo(300, 500)
            pygame.time.delay(60)
            start.stop()
    if pr==1:
        co=contador(score,intentos)
        nu=nubes(pos1,pos2,pos3)
        problema="Pedro tiene 8 manzanas pero le regala 2 a su mamá, ¿Cuántas manzanas le quedan?"
        pf_1=calibriFont2.render(str(problema),1,(255, 255, 255), ( 60, 216, 241))
        screen.blit(pf_1, (10,10))
        pygame.time.delay(6)
        res1=6
        res2=8
        res3=7
        nu2=nubesres(res1,res2,res3)
        screen.blit(avion, (x-100,y-100))
        A=decision(x,y,pr)
        if A==1:
            pr = 2
            si=siguiente()
            if intentos==1:
                score=score+10
            intentos=1
        if A==2:
            wrong.play()
            intentos=0
        if A==3:
            wrong.play()
            intentos=0 
    if pr==2:
        A=0
        co=contador(score,intentos)
        nu=nubes(pos2,pos3,pos1)        
        problema="Tienes 9 pelotas, pero te regalan 1, ¿Cuántas tienes ahora?"
        pf_1=calibriFont2.render(str(problema),1,(255, 255, 255), ( 60, 216, 241))
        screen.blit(pf_1, (10,10))
        pygame.time.delay(6)
        res1=8
        res2=10
        res3=9
        nu2=nubesres(res1,res2,res3)
        screen.blit(avion, (x-100,y-100))
        if B>0:
            A=decision(x,y,pr)
            if A==1:
                wrong.play()
                intentos=0
            if A==2:
                pr = 3        
                pyautogui.moveTo(300, 500)
                pygame.time.delay(60)
                correct.play()
                if intentos==1:
                    score=score+10
                intentos=1
                B=0
            if A==3:
                wrong.play()
                intentos=0
        B=1    
    if pr==3:
        A=0
        co=contador(score,intentos)
        nu=nubes(pos2,pos3,pos1)        
        problema="Si quiero repartir 5 dulces entre 5 personas, ¿De cuántos le toca a cada quien?"
        pf_1=calibriFont2.render(str(problema),1,(255, 255, 255), ( 60, 216, 241))
        screen.blit(pf_1, (10,10))
        pygame.time.delay(6)
        res1=1
        res2=5
        res3=3
        nu2=nubesres(res1,res2,res3)
        screen.blit(avion, (x-100,y-100))
        if B==2:
            A=decision(x,y,pr)
            if A==1:
                
                pr = 4    
                pyautogui.moveTo(300, 500)
                pygame.time.delay(60)
                correct.play()
                if intentos==1:
                    score=score+10
                intentos=1
            if A==2:
                wrong.play()
                intentos=0
            if A==3:
                wrong.play()
                intentos=0
        B=2
        
    if pr==4:
        A=0
        co=contador(score,intentos)
        nu=nubes(pos2,pos3,pos1)        
        problema="En un árbol hay 14 pájaros, si se fueron 5 ¿Cuántos quedan?"
        pf_1=calibriFont2.render(str(problema),1,(255, 255, 255), ( 60, 216, 241))
        screen.blit(pf_1, (10,10))
        pygame.time.delay(6)
        res1=9
        res2=6
        res3=19
        nu2=nubesres(res1,res2,res3)
        screen.blit(avion, (x-100,y-100))
        if B==3:
            A=decision(x,y,pr)
            if A==1:
                pr = 5    
                pyautogui.moveTo(300, 500)
                pygame.time.delay(60)
                correct.play()
                if intentos==1:
                    score=score+10
                intentos=1
            if A==2:
                wrong.play()
                intentos=0
            if A==3:
                wrong.play()
                intentos=0
        B=3
    if pr==5:
        A=0
        co=contador(score,intentos)
        nu=nubes(pos2,pos3,pos1)        
        problema="2,4,6,8...¿Cuál es el siguiente número?"
        pf_1=calibriFont2.render(str(problema),1,(255, 255, 255), ( 60, 216, 241))
        screen.blit(pf_1, (10,10))
        pygame.time.delay(6)
        res1=8
        res2=12
        res3=10
        nu2=nubesres(res1,res2,res3)
        screen.blit(avion, (x-100,y-100))
        if B==4:
            A=decision(x,y,pr)
            if A==1:
                wrong.play()
                intentos=0
            if A==2:
                wrong.play()
                intentos=0
            if A==3:
                pr = 6    
                pyautogui.moveTo(300, 500)
                pygame.time.delay(60)
                correct.play()
                if intentos==1:
                    score=score+10
                intentos=1
        B=4
    if pr==6:
        A=0
        co=contador(score,intentos)
        nu=nubes(pos2,pos3,pos1)        
        problema="Sofía tiene 10 galletas pero compra otras 7, ¿Cuántas tiene ahora?"
        pf_1=calibriFont2.render(str(problema),1,(255, 255, 255), ( 60, 216, 241))
        screen.blit(pf_1, (10,10))
        pygame.time.delay(6)
        res1=15
        res2=17
        res3=18
        nu2=nubesres(res1,res2,res3)
        screen.blit(avion, (x-100,y-100))
        if B==5:
            A=decision(x,y,pr)
            if A==1:
                wrong.play()
                intentos=0
            if A==2:
                pr = 7    
                pyautogui.moveTo(300, 500)
                pygame.time.delay(60)
                correct.play()
                if intentos==1:
                    score=score+10
                intentos=1
            if A==3:
                wrong.play()
                intentos=0
                
        B=5
    if pr==7:
        A=0
        co=contador(score,intentos)
        nu=nubes(pos2,pos3,pos1)        
        problema="A un pastel de 20 rebanadas le quitan 12, ¿Cuántas rebanadas quedan?"
        pf_1=calibriFont2.render(str(problema),1,(255, 255, 255), ( 60, 216, 241))
        screen.blit(pf_1, (10,10))
        pygame.time.delay(6)
        res1=8
        res2=12
        res3=20
        nu2=nubesres(res1,res2,res3)
        screen.blit(avion, (x-100,y-100))
        if B==6:
            A=decision(x,y,pr)
            if A==1:
                pr = 8    
                pyautogui.moveTo(300, 500)
                pygame.time.delay(60)
                correct.play()
                if intentos==1:
                    score=score+10
                intentos=1
            if A==2:
                wrong.play()
                intentos=0
            if A==3:
                wrong.play()
                intentos=0
        B=6
        
    if pr==8:
        A=0
        co=contador(score,intentos)
        nu=nubes(pos2,pos3,pos1)        
        problema="3,5,7,9,...¿Qué número sigue?"
        pf_1=calibriFont2.render(str(problema),1,(255, 255, 255), ( 60, 216, 241))
        screen.blit(pf_1, (10,10))
        pygame.time.delay(6)
        res1=12
        res2=11
        res3=10
        nu2=nubesres(res1,res2,res3)
        screen.blit(avion, (x-100,y-100))
        if B==7:
            A=decision(x,y,pr)
            if A==1:
                wrong.play()
                intentos=0
            if A==2:
                pr = 9    
                pyautogui.moveTo(300, 500)
                pygame.time.delay(60)
                correct.play()
                if intentos==1:
                    score=score+10
                intentos=1
            if A==3:
                wrong.play()
                intentos=0
                
        B=7
    if pr==9:
        A=0
        co=contador(score,intentos)
        nu=nubes(pos2,pos3,pos1)        
        problema="Hay 10 naranjas y 5 niños,¿Cuántas le tocan a cada uno?"
        pf_1=calibriFont2.render(str(problema),1,(255, 255, 255), ( 60, 216, 241))
        screen.blit(pf_1, (10,10))
        pygame.time.delay(6)
        res1=2
        res2=3
        res3=1
        nu2=nubesres(res1,res2,res3)
        screen.blit(avion, (x-100,y-100))
        if B==8:
            A=decision(x,y,pr)
            if A==1:
                pr = 10    
                pyautogui.moveTo(300, 500)
                pygame.time.delay(60)
                correct.play()
                if intentos==1:
                    score=score+10
                intentos=1
            if A==2:
                wrong.play()
                intentos=0
            if A==3:
                wrong.play()
                intentos=0
        B=8
    if pr==10:
        A=0
        co=contador(score,intentos)
        nu=nubes(pos2,pos3,pos1)        
        problema="En un autobus hay 7 niños, se suben 5 y luego otros 3.¿Cuántos son en total?"
        pf_1=calibriFont2.render(str(problema),1,(255, 255, 255), ( 60, 216, 241))
        screen.blit(pf_1, (10,10))
        pygame.time.delay(6)
        res1=16
        res2=12
        res3=15
        nu2=nubesres(res1,res2,res3)
        screen.blit(avion, (x-100,y-100))
        if B==9:
            A=decision(x,y,pr)
            if A==1:
                wrong.play()
                intentos=0
            if A==2:
                wrong.play()
                intentos=0
            if A==3:
                pr = 11   
                pyautogui.moveTo(300, 500)
                pygame.time.delay(60)
                correct.play()
                if intentos==1:
                    score=score+10
                intentos=1
        B=9

    if pr==11:
        pf_1=Fontnubes.render("¡Felicidades!",1,(255, 255, 255), ( 60, 216, 241))
        screen.blit(pf_1, (400,200))
        pf_1=Fontnubes.render("Tu puntaje ha sido: "+str(score),1,(255, 255, 255), ( 60, 216, 241))
        screen.blit(pf_1, (250,300))         
            
    pygame.display.flip()