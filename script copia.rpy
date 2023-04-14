define c0 = Character("Chica")
define c = Character("[name]")
define m = Character("Manager")
define ade = Character("ADE GOMEZNASAI")
define g0 = Character("Grupo")
define g = Character("[name]")
define f = Character("Fan")
define idk = Character("???")
define j = Character("Juda")



label start:

    # Aquí vamos a tener la presentación del personaje principal:
    # El personaje está en un camerino y recibe la carta de un fan.
    # Se debate si seguir cantando, el grupo y el/la manager le llaman desde la puerta
    # Y tomas la decisión de qué ruta quieres seguir

    scene bg camerino

    with Dissolve(.5)

    "En un camerino, se encontraba una chica preparándose para dar un concierto."

    "A lo lejos, se escuchaba una multitud gritando su nombre."


    python:
        name = renpy.input(_("Se escuchaba el nombre de..."))

        name = name.strip() or __("Manuela")

    c "[name]"

    "Mientras ponía en orden sus pensamientos, alguien llamó a la puerta..."

    m "¡VENGA, TE TOCA SALIR!"

    g0 "¡VAMOS, NO PODEMOS HACER EL ESPECTÁCULO SIN TI!"


    c "..."

    c "No paro de darle vueltas sobre que quiero ser."

    c "..."

    c "Está bien, ya va siendo hora de tomar una decisión..."

    menu:
        "He nacido para esto":
            jump rama1
        "Esto no es lo mío":
            jump rama2
# los labels a la izquierda, con : al final y su contenido indentado
label rama1:
    # Rama 1

    c "DECIDIDO" #shake

    "Al levantarse de sopetón, la montaña de cartas que había delante suya se desplomó, desperdigándose sobre el suelo."

    "Alguna de esas cartas le llamaba particularmente la atención..."

    show carta1 at left

    with Dissolve(.5)

    "Una de ellas tenía un corazón sellándola, lo cual le pareció un gesto tierno."

    show carta2

    with Dissolve(.5)

    "Otra de ellas, una amarilla fosforito, le causó cierta gracia."

    show carta3 at right

    with Dissolve(.5)

    "Y otra carta, completamente negra, hizo que le recorriera un escalofrío por la espalda."


    menu:

        "Qué carta más cuqui...":

            jump rama1_ruta1

        "Qué carta más simpática...":

            jump rama1_ruta2

        "Qué carta más tétrica...":

            jump rama1_ruta3

            # Ruta Sentimental

            label rama1_ruta1:

                hide carta1

                hide carta2

                hide carta3

                "[name] tiene intención de leer la carta en este momento porque la curiosidad de que la firme un tal Willyx le hace mucha gracia."

                "¿Qué persona es capaz de llamarse como el pato de un anuncio de cerveza?"

                "Sin embargo, llaman a la puerta."

                show test at center:

                    alpha 0.25

                with Dissolve(.5)

                idk "[name], soy yo. ¿Estás ocupada?, ¿puedo pasar?"

                idk "Todavía tenemos un poco de tiempo antes del concierto, así que voy a aprovechar para comentarte un asunto. Siéntate, por favor."

                hide test

                with Dissolve(.5)

                show test at center:

                    alpha 0.75

                with Dissolve(.5)

                ade "Mira, tengo que serte franca."

                ade "Tú sabes que nuestro grupo de idols, Andaluz Melody, ha tenido sus momentos de gloria gracias a que 'Hay que venir al sur' llegó al número uno en las listas hace no mucho, y que desde ahí hemos ido subiendo como la espuma…"

                show test at center:

                    alpha 0.5

                with Dissolve(.5)

                "La manager desvía la mirada y termina por llevarse las manos a la cara."

                show test at center:

                    alpha 1

                with Dissolve(.5)

                ade "No te lo voy a esconder más."

                ade "Tenemos una demanda por derechos de autor."

                ade "Yo no lo sabía, pero resulta que tanto nuestro hit como 'Sarandonga', 'Que la detengan', 'Salta la rana' y, bueno, prácticamente todas las canciones que hemos sacado ya estaban registradas…"

                ade "He tenido incluso que despedir a nuestro coach Anfe por no informarme de estas cosas y estar jugando en horas de trabajo al Valorant con Rafa, el profesor de danza urbana."

                ade "Es que siempre tienen que estar enviándose mensajitos a las 6 de la mañana para quedar, y claro, así no me rinden luego entrenando a las idols, y muchas veces ni están."
                ade "Si es que Dios los cría y ellos se juntan"
                ade "A ver, tampoco los puedo juzgar mucho, que lo que ganan no les da ni para una skin del Mercado Nocturno…"
                ade "Por la cara de desconcierto de [name], la manager entiende que hace mucho que se ha desviado del tema"
                ade "Además, apenas les da tiempo de vida a las idols como para que pueda saber que existen juegos y vicios como el Valorant."

                ade "El tema es que económicamente la agencia de idols está en un aprieto, en números rojos, y eso por no hablar del último escándalo en el que nos metió tu compañera Pauwula."
                ade "Es que otra igual, y yo que no tenía ya bastante con que Ermianime se marchase al grupo rival y me dijese que estaba perdiendo perspectiva profesional, que el grupo nunca iba a triunfar si poníamos a las idols a hacer videorreacciones en YouTube…"


                menu:

                    "Sen1":

                        jump rama1_ruta1_end1

                    "Sen2":

                        jump rama1_ruta1_end2

                label rama1_ruta1_end1:

                    "Final A Ruta 1"

                    jump ending

                label rama1_ruta1_end2:

                    "Final B Ruta 1"

                    jump ending

            # Ruta Cachondeo

            label rama1_ruta2:

                hide carta1

                hide carta2

                hide carta3


                c "Qué carta más simpática..."

                menu:

                    "Cacho1":

                        jump rama1_ruta2_end1

                    "Cacho2":

                        jump rama1_ruta2_end2

                label rama1_ruta2_end1:

                    "Final A Ruta 2"

                    jump ending

                label rama1_ruta2_end2:

                    "Final B Ruta 2"

                    jump ending

            # Ruta Meta

            label rama1_ruta3:

                hide carta1

                hide carta2

                hide carta3


                c "Qué carta más tétrica..."

                menu:

                    "Meta1":

                        jump rama1_ruta3_end1

                    "Meta2":

                        jump rama1_ruta3_end2

                label rama1_ruta3_end1:

                    "Final A Ruta 3"

                    jump ending

                label rama1_ruta3_end2:

                    "Final B Ruta 3"

                    jump ending

label rama2:
    # Rama 2

    c "DECIDIDO" #shake

    "Al levantarse de sopetón, la montaña de cartas que había delante suya se desplomó, desperdigándose sobre el suelo"

    "Alguna de esas cartas le llamaba particularmente la atención..."

    show carta1 at left

    with Dissolve(.5)

    "Una de ellas tenía un corazón sellándola, lo cual le pareció un gesto tierno"

    show carta2

    with Dissolve(.5)

    "Otra de ellas, una amarilla fosforito, le causó cierta gracia"

    show carta3 at right

    with Dissolve(.5)

    "Y otra carta, completamente negra, hizo que le recorriera un escalofrío por la espalda"

    menu:

        "Qué carta más cuqui...":

            jump rama2_ruta1

        "Qué carta más simpática...":

            jump rama2_ruta2

        "Qué carta más tétrica...":

            jump rama2_ruta3

            # Ruta Sentimental

            label rama2_ruta1:

                hide carta1

                hide carta2

                hide carta3

                "Qué carta más cuqui..."

                menu:

                    "Sen1":

                        jump rama2_ruta1_end1

                    "Sen2":

                        jump rama2_ruta1_end2

                label rama2s_ruta1_end1:

                    "Final A Ruta 1"

                    jump ending

                label rama2_ruta1_end2:

                    "Final B Ruta 1"

                    jump ending

            # Ruta Cachondeo

            label rama2_ruta2:

                hide carta1

                hide carta2

                hide carta3

                "Qué carta más simpática..."

                menu:

                    "Cacho1":

                        jump rama2_ruta2_end1

                    "Cacho2":

                        jump rama2_ruta2_end2

                label rama2_ruta2_end1:

                    "Final A Ruta 2"

                    jump ending

                label rama2_ruta2_end2:

                    "Final B Ruta 2"

                    jump ending

            # Ruta Meta

            label rama2_ruta3:

                hide carta1

                hide carta2

                hide carta3

                "Qué carta más tétrica..."

                menu:

                    "Meta1":

                        jump rama2_ruta3_end1

                    "Meta2":

                        jump rama2_ruta3_end2

                label rama2_ruta3_end1:

                    "Final A Ruta 3"

                    jump ending

                label rama2_ruta3_end2:

                    "Final B Ruta 3"

                    jump ending


    label ending:

    scene bl

    "..."

    "{i}Sea cual sea la ruta que hayas escogido...{/i}"

    "{i}¡Gracias por jugar!{/i}"

    return
