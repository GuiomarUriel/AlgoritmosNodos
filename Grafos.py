from os import system
import m_grafo
#system ('cls')
system("clear")

def funcion_grafo_erdos_rengy(n,m):
    grafo_er = m_grafo.grafo(n, M= m)
    grafo_er.generar_nodos()
    aristas_generadas = grafo_er.generar_aristas_er()
    grafo_er.generar_grafo_graphviz(aristas_generadas,f"ErdosRengy{n}")
    #print(">>Modelo  Erdős-Rényi: ",aristas_generadas)

def funcion_grafo_gilbert(n,p):
    grafo_gil = m_grafo.grafo(n, p=p)
    grafo_gil.generar_nodos()
    aristas_generadas = grafo_gil.generar_aristas_gilbert()
    grafo_gil.generar_grafo_graphviz(aristas_generadas,f"Gilbert{n}")
    #print(">>Modelo Gilbert: ",aristas_generadas)

def funcion_grafo_geografico(n,r):
    grafo_geo = m_grafo.grafo(n, r=r)
    grafo_geo.generar_nodos()
    aristas_generadas = grafo_geo.generar_arista_geografico()
    grafo_geo.generar_grafo_graphviz(aristas_generadas,f"Geografico{n}")
    #print(">>Modelo Geografico: ",aristas_generadas)

def funcion_grafo_barabasi(n,d):
    grafo_bara = m_grafo.grafo(n, d=d)
    grafo_bara.generar_nodos()
    aristas_generadas = grafo_bara.generar_aristas_Barabasi()
    grafo_bara.generar_grafo_graphviz(aristas_generadas,f"Barabasi{n}")
    #print(">>Modelo Barabasi: ",aristas_generadas)

def funcion_grafo_dorogovtsev(n):
    grafo_dm = m_grafo.grafo(n)
    grafo_dm.generar_nodos()
    aristas_generadas = grafo_dm.generar_aristas_dorogovtset()
    grafo_dm.generar_grafo_graphviz(aristas_generadas,f"Dorogovtsev{n}")
    #print(">>Modelo Dorogovtsev-Mendes: ",aristas_generadas)

def funcion_grafo_malla(n,m):
    grafo_malla = m_grafo.grafo(n,m=m)
    grafo_malla.generar_nodos()
    aristas_generadas = grafo_malla.generar_aristas_malla()
    grafo_malla.generar_grafo_graphviz(aristas_generadas,f"Malla{n}")
    #print(">>Modelo Malla: ",aristas_generadas)

funcion_grafo_erdos_rengy(201,600)

funcion_grafo_gilbert(201,.6)

funcion_grafo_geografico(501,1)

funcion_grafo_barabasi(201,8)

funcion_grafo_dorogovtsev(201)

funcion_grafo_malla(60,12)
