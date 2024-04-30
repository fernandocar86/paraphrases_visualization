import streamlit as st



### This is the hard coded text ###

# First, the title: a simple string
title = 'Primer encuentro'

# Second, the text: a list of tuples. Each tuple corresponds to a sentence.
# If the length of the tuple equals 1, then the sentence has no paraphrase. Otherwise,
# all the elements in the tuple except for tuple[0] are paraphrases.
text = [('No hubo explosión alguna.', 'No hubo ninguna explosión', 'No explotó nada'),
        ('Se encendieron, simplemente, los retrocohetes, y la nave se acercó a la superficie del planeta.'),
        ('Se apagaron los retrocohetes y la nave, entre el polvo y los gases, con suavidad poderosa, se posó.'),
        ('Fue todo.'),
        ('Se sabía que vendrían.'),
        ('Nadie había dicho cuándo; pero la visita de habitantes de otros mundos era inminente.'),
        ('Así, pues, no fue para él una sorpresa total.'),
        ('Es más, había sido entrenado, como todos, para recibirlos.'),
        ('“Debemos estar preparados —le instruyeron en el Comité Cívico—; un día de estos (mañana, hoy mismo…), pueden descender de sus naves.'),
        ('De lo que ocurra en los primeros minutos del encuentro dependerá la dirección de las futuras relaciones interespaciales.'),
        ('Y quizás nuestra supervivencia.'),
        ('Por eso, cada uno de nosotros debe ser un embajador dotado del más fino tacto, de la más cortés de las diplomacias.”'),
        ('Por eso caminó sin titubear el medio kilómetro necesario para llegar hasta la nave.'),
        ('El polvo que los retrocohetes habían levantado le molestó un tanto; pero se acercó sin temor alguno, y sin temor alguno se dispuso a esperar la salida de los lejanos visitantes, preocupado únicamente por hacer de aquel primer encuentro un trance grato para dos planetas, un paso agradable y placentero.'),
        ('Al pie de la nave pasó un rato de espera, la vista fija en el metal dorado que el Sol hacía destellar con reflejos que le herían los ojos; pero ni por eso parpadeó.'),
        ('Luego se abrió la escotilla, por la que se proyectó sin tardanza una estilizada escala de acceso.'),
        ('No se movió de su sitio, pues temía que cualquier movimiento suyo, por inocente que fuera, lo interpretaran los visitantes como un gesto hostil.'),
        ('Hasta se alegró de no llevar sus armas consigo.'),
        ('Lentamente, oteando, comenzó a insinuarse, al fondo de la escotilla, una figura.'),
        ('Cuando la figura se acercó a la escala para bajar, la luz del Sol le pegó de lleno.'),
        ('Se hizo entonces evidente su horrorosa, su espantosa forma.'),
        ('Por eso, él no pudo reprimir un grito de terror.'),
        ('Con todo, hizo un esfuerzo supremo y esperó, fijo en su sitio, el corazón al galope.'),
        ('La figura bajó hasta el pie de la nave, y se detuvo frente a él, a unos pasos de distancia.'),
        ('Pero él corrió entonces.'),
        ('Corrió, corrió y corrió.'),
        ('Corrió hasta avisar a todos, para que prepararan sus armas, no iban a dar la bienvenida a un ser con dos piernas, dos brazos, dos ojos, una cabeza, una boca.')
        ]


def show_text(title, text):
    st.title(title)
    
    clip_1 = """
    <style>
    .tooltip {
        position: relative;
        display: inline-block;
        border-bottom: 1px dotted black; /* If you want dots under the hoverable text */
    }

    .tooltip .tooltiptext {
        visibility: hidden;
        width: 360px;
        background-color: #555;
        color: #fff;
        text-align: center;
        border-radius: 6px;
        padding: 5px 0;
        position: absolute;
        z-index: 1;
        bottom: 125%;
        left: 50%;
        margin-left: -60px;
        opacity: 0;
        transition: opacity 0.3s;
    }

    .tooltip:hover .tooltiptext {
        visibility: visible;
        opacity: 1;
    }
    </style>
    <div class="tooltip">
    """
    
    clip_2 = '<span class="tooltiptext">'
    
    clip_3 = '</span> </div>'
    
    sentence_list = []
    
    for tup in text:
        # If a tuple contains only a string, then its type is string
        if type(tup) == str:
            sentence = tup
            sentence_list.append(sentence)
        
        # The ones that are tuples contain paraphrases
        elif type(tup) == tuple:
            sentence = tup[0]
            
            # this is a tuple containing only the paraphrases
            paraph_only = tup[1:]
            
            # If there is only one paraphrase, it goes to the corresponding variable
            if type(paraph_only) == str:
                paraphrase = paraph_only
                
            # If there are more paraphrases, they are combined into the corresponding variable
            elif type(paraph_only) == tuple:
                paraphrase = ' -- '.join(paraph_only)
            
            
            # This forms the html code for each sentence
            sent_paraph = clip_1 + sentence + clip_2 +paraphrase + clip_3
            
            sentence_list.append(sent_paraph)
            
    for item in sentence_list:
        st.markdown(item, unsafe_allow_html=True)
        st.markdown('')

if __name__ == "__main__":
    #main()
    show_text(title, text)