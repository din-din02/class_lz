#Библиотеки
import matplotlib.pyplot as mp
import math

#Создаем класс
class Octagon:
    #Конструктор
    def __init__(self,storona):
        self.storona=storona
        self.corner=2*3.14/8
        self.k=1+2**(1/2)

    #Для описанной окружности
    def opis(self):
        R=self.storona*(self.k/(self.k-1))**(1/2)
        S=3.14*R**2
        print(f"Радиус описанной окружности:{R} Площадь описанной окружности:{S}")
        
    #Для вписанной окружности
    def vpis(self):
        r=(self.k/2)*self.storona
        s=3.14*r**2
        print(f"Радиус вписанной окружности:{r} Площадь вписанной окружности:{s}")
        
    #Для самого октагона
    def oct(self):
        P=self.storona*8
        Area=2*self.storona**2*self.k
        print((f"Площадь октагона:{Area} Периметр октагона:{P}"))
        
    #Создаем график
    def grafik(self):
        R=self.storona*(self.k/(self.k-1))**(1/2)
        r=(self.k/2)*self.storona
        #создаём график и оси https://sky.pro/wiki/media/vyvod-grafikov-matplotlib-v-ipython-notebook/?ysclid=mm9cqmp1o2691985824
        fig, ax = mp.subplots(figsize=(20, 20))  
        #Установка равного соотношения сторон(https://external.software/archives/23129?ysclid=mm9d3ggkuj475114572)
        ax.set_aspect('equal')
        #создаём списки для восьми вершин
        x = [R* math.cos(i * self.corner) for i in range(10)] 
        y = [R* math.sin(i * self.corner) for i in range(10)] 
        #Замыкание фигуры
        x.append(x[0])  
        y.append(y[0])
        #желтый октагон
        ax.plot(x,y,color='yellow',markersize=10) 
         #создаем черную описанную окружность(без заливки)
        circle_out = mp.Circle((0, 0), R, color='black', fill=False, label=" График описанной окружности" )
        #Добавляем на график
        ax.add_patch(circle_out)
        #создаем красную вписанную окружность(без заливки)
        circle_in = mp.Circle((0, 0), r, color='red', fill=False, label=" График вписанной окружности" ) 
        #Добавляем на график
        ax.add_patch(circle_in) 
        #цвета
        mp.legend() 
        #вывод графика
        mp.show() 
        #Деструктор
    def __del__(self):
        print('Сторона удалена',self.storona)    

