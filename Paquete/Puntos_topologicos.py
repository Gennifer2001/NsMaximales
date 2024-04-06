class puntos_topologicos:

  def exterior(Base, conjunto,df):
    Ext = []

    for i in Base:
        if not any(elem in conjunto for elem in i):
            Ext.extend(i)

    Ext_enteros = [int(elemento) for elemento in Ext]
    tabla = df.loc[Ext_enteros]

    print(f"Exterior = {Ext}")
    return tabla
  
  def interior(Base,conjunto,df):
    Int = []

    for i in Base:
        if all(elem in conjunto for elem in i):
            Int.extend(i)

    Int_enteros = [int(elemento) for elemento in Int]
    tabla = df.loc[Int_enteros]

    print(f"Interior = {Int}")
    return tabla
  def adherencia(Base,A,df):
        Adh = []

        for i in Base:
          if any(elem in A for elem in i):
           Adh.extend(i)

        Adh_enteros = [int(elemento) for elemento in Adh]
        tabla = df.loc[Adh_enteros]

        print(f"Adherencia = {Adh}")
        return tabla
  def limite(Base,A,df):
   Lim = []

   for i in Base:
     for m in i:
       if any(elem in A for elem in i if elem != m):
         Lim.append(m)

   Lim_enteros = [int(elemento) for elemento in Lim]
   tabla = df.loc[Lim_enteros]

   print(f"Límite = {Lim}")
   return tabla
  
  def frontera(Base,A,df):
   Fr = []

   for i in Base:
       if any(elem in A for elem in i) and any(elem not in A for elem in i):
           Fr.extend(i)

   Fr_enteros = [int(elemento) for elemento in Fr]
   tabla = df.loc[Fr_enteros]

   print(f"Frontera = {Fr}")
   return tabla
