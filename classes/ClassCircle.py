import math;
class circle:
    def __init__(self, _ray: float) -> None:
        self.ray = _ray;
    
    def circle_area(self):
        area = float(0);
        area = (math.pi)*(pow(self.ray, 2));
        print(f'A área do círculo de raio {self.ray} cm é igual a {round(area, 3)} cm².');
        return area; 

    def circle_circumference(self):
        circunference = float(0);
        circunference = 2*(math.pi)*self.ray
        print(f'A circunferência do círculo de raio {self.ray} cm é igual a {round(circunference, 3)} cm.');
        return circunference;

#circle_1 = circle(10);

#print("");
#circle_1.circle_area();
#circle_1.circle_circumference();
#print("");