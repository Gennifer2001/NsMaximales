def exterior(Base, conjunto):
    Ext = []

    for i in Base:
        if not any(elem in conjunto for elem in i):
            Ext.extend(i)

    Ext_enteros = [int(elemento) for elemento in Ext]

    print(f"Exterior = {Ext}")

  
def interior(Base,conjunto):
    Int = []

    for i in Base:
        if all(elem in conjunto for elem in i):
            Int.extend(i)

    Int_enteros = [int(elemento) for elemento in Int]

    print(f"Interior = {Int}")
   
def adherencia(Base,A):
        Adh = []

        for i in Base:
          if any(elem in A for elem in i):
           Adh.extend(i)

        Adh_enteros = [int(elemento) for elemento in Adh]

        print(f"Adherencia = {Adh}")

def limite(Base,A):
   Lim = []

   for i in Base:
     for m in i:
       if any(elem in A for elem in i if elem != m):
         Lim.append(m)

   Lim_enteros = [int(elemento) for elemento in Lim]

   print(f"Límite = {Lim}")
  
def frontera(Base,A):
   Fr = []

   for i in Base:
       if any(elem in A for elem in i) and any(elem not in A for elem in i):
           Fr.extend(i)

   Fr_enteros = [int(elemento) for elemento in Fr]

   print(f"Frontera = {Fr}")
