class Computador:
    def __init__(self,equipos: int, dias: int, adicionales: int):
            self.equipos = equipos
            self.dias = dias
            self.adicionales = adicionales
            
    def alquilarDentroCiudad(self):
        if self.equipos >= 2:
            mul = self.equipos*35000
            resultado_crudo = self.dias*mul
            if self.adicionales > 0 :
                porcentaje = self.adicionales * 0.02
                resultado_add = self.adicionales * mul
                if porcentaje > 1:
                    porcentaje = 1   
                else:
                    porcentaje = porcentaje 
                resta = resultado_add * porcentaje
                resT = resultado_add - resta
                total = resultado_crudo + resT
                return print(f"Valor alquiler: {resultado_crudo}\n"f"dias adicional: {resta}\n"f"Valor alquiler Total: {total}")
            return print(f"Valor alquiler Total: {resultado_crudo}")
        else:
            print("El aquiler debe ser mayor a dos equipos")
            
                
        
       
    
    def alquilarFueraCiudad(self):
        
        if self.equipos >= 2:
            mul = self.equipos*35000
            resultado_crudo = self.dias*mul
            desc = 0.05
            desc = resultado_crudo * desc
            res = resultado_crudo + desc
            if self.adicionales > 0 :
                porcentaje = self.adicionales * 0.02
                resultado_add = self.adicionales * mul
                if porcentaje > 1:
                    porcentaje = 1   
                else:
                    porcentaje = porcentaje 
                resta = resultado_add * porcentaje
                resT = resultado_add - resta
                total = resultado_crudo + resT
                return print(f"Valor alquiler: {resultado_crudo} \n"f"dias adicional: {resta} \n"f"domicilio: {desc} \n"f"Total:{total}")
            return print(f"Valor alquiler: {resultado_crudo} \n"f"domicilio:{desc} \n"f"Valor alquiler Total: {res}\n")
        else:
            print("El aquiler debe ser mayor a dos equipos")
                
    
    def alquilarDentroLocal(self):
            if self.equipos >= 2:
                mul = self.equipos*35000
                resultado_crudo = self.dias*mul
                desc = 0.05
                desc = resultado_crudo * desc
                res = resultado_crudo - desc
                if self.adicionales > 0 :
                    porcentaje = self.adicionales * 0.02
                    resultado_add = self.adicionales * mul
                    if porcentaje > 1:
                        porcentaje = 1   
                    else:
                        porcentaje = porcentaje 
                    resta = resultado_add * porcentaje
                    resT = resultado_add - resta
                    total = resultado_crudo + resT
                    return print(f"Valor alquiler: {resultado_crudo}\n"f"dias adicional: {resta} \n"f"descuento: {desc}\n"f"Total{total}")
                return print(f"Valor alquiler: {resultado_crudo}\n"f"descuento: {desc}\n""Valor alquiler Total {res}")
            else:
                print("El aquiler debe ser mayor a dos equipos")
            
            
            
            
