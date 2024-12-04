# clase_plan.py

class Plan:
    def __init__(self, id_plan, nombre, velocidad, precio):
        self.id_plan = id_plan
        self.nombre = nombre
        self.velocidad = velocidad
        self.precio = precio

class PlanDAO:
    def __init__(self):
        self.planes = []  # Simulación de base de datos

    def agregar_plan(self, plan):
        self.planes.append(plan)

    def get_planes(self):
        return [(plan.id_plan, plan.nombre, plan.velocidad, plan.precio) for plan in self.planes]

def crear_planes(plan_dao):
    plan1 = Plan(1, "Plan Básico", 10, 20)
    plan2 = Plan(2, "Plan Avanzado", 50, 50)
    plan3 = Plan(3, "Plan Premium", 100, 100)
    
    plan_dao.agregar_plan(plan1)
    plan_dao.agregar_plan(plan2)
    plan_dao.agregar_plan(plan3)