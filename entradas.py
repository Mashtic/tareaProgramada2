visitantes = [[305430092, ("Ian", "Coto", "Soto"), [], [], True], [907650321, ("Pedro", "Moto", "Zote"), [], [], True], 
[606960699, ("Loco", "Es", "Poco"), [], [], True]]

visitantesLleno = [[305430092, ("Ian", "Coto", "Soto"), ["I1642", "A1933"], [("La venganza","13/02/2022","Muy lejos", "Uno bonito", "https://www.google.com")], True], [907650321, ("Pedro", "Moto", "Zote"), ["A1933", "V1928"], [("La venganza","14/02/2022","Muy lejos", "Uno bonito", "https://www.google.com")], True], 
[606960699, ("Esteban", "Mi", "Novio"), ["I1642"], [("La venganza","13/02/2022","Muy lejos", "Uno bonito", "https://www.google.com")], False]]

astronomosReal = {'I1642': ['Isaac Newton', 'Woolsthorpe Manor', ('1642', '1727'), 'Newton descubrió las leyes de la gravitación culminando la revolución científica que comenzó Copérnico. En su obra Principia Mathematica expuso las leyes que rigen la gravitación. De estas leyes dedujo la órbita de los cometas y explicó las mareas, además de establecer las bases de la física nuclear por la interacción de las fuerzas de atracción de las partículas. '], 'A1933': ['Arno Allan Penzias', 'Munich', ('1933', ''), 'El aporte sustancial de Arno Penzias y Robert Wilson a la ciencia fue el descubrimiento de la Radiación de Fondo de Microondas. Esta radiación es una consecuencia de la explosión del Big Bang. En sus experimentos descubrieron una radiación constante que no venía de la Tierra ni de la Vía Láctea, sino de fuera. Este descubrimiento les valió un Premio Nobel en 1978. Cuando la información salió a la luz creó grandes disputas, porque todavía existían muchos astrónomos que no creían en la existencia del Big Bang, y esta investigación probó que estaban errados.'], 'V1928': ['Vera Rubin', 'Filadelfia', ('1928', '2016'), 'Observando que existía un alto índice de agrupación en la distribución de las galaxias, conjeturó que éstas se concentraban en ciertas zonas dejando espacios vacíos entre ellas.  Estos resultados no despertaron casi ningún interés en el momento de su publicación, pero fueron confirmados quince años más tarde y ahora constituyen la base del estudio de la estructura a gran escala del Universo.  pionera en la medición de la rotación de las estrellas dentro de una galaxia. Sus mediciones pusieron de manifiesto que las curvas de rotación galácticas se mantenían planas, contradiciendo el modelo teórico, siendo la evidencia más directa y robusta de la existencia de materia oscura.']} 

def limpiarDescAstros(pDescAstro):
    limpCod = ["\nsa"]
    pDescAstroLimp = ""
    for codigo in limpCod:
        pos = 0
        if codigo not in pDescAstro:
            break
        for caracter in pDescAstro:
            if caracter == codigo[0]:
                pos += len(codigo)
            pDescAstroLimp += pDescAstro[pos]
            pos += 1
        pDescAstro = pDescAstroLimp
    return pDescAstroLimp

print(limpiarDescAstros(r"El zorro de maria ahora es de pedro\nsa"))