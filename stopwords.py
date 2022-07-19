import io
preposiciones = ['a', 'ante', 'bajo', 'cabe', 'con', 'contra', 'de', 'desde', 'durante', 'en', 'entre', 'hacia', 'hasta', 'mediante', 'para', 'por', 'según', 'sin', 'so', 'sobre', 'tras', 'versus', 'vía']
preposiciones2 = [i.capitalize() for i in preposiciones]
conjcoordinadas = ['e','empero','mas','ni','o','ora','pero','sino','siquiera','u','y']

conjcoordinadas2 = [i.capitalize() for i in conjcoordinadas]

conjsubordinadas = ['aunque','como','conque','cuando','donde','entonces','ergo','incluso','luego','mientras','porque','pues','que','sea','si','ya']

conjsubordinadas2 = [i.capitalize() for i in conjsubordinadas]

adverbios = ['aquí', 'ahí', 'allí', 'cerca', 'lejos', 'arriba', 'abajo', 'delante', 'detrás', 'alrededor', 'encima', 'debajo', 'dentro', 'fuera','antes', 'ahora', 'luego', 'después', 'ayer', 'hoy', 'mañana', 'entonces', 'pronto', 'tarde', 'ya', 'siempre', 'aún', 'nunca', 'jamás','así', 'bien', 'mal', 'aprisa', 'deprisa', 'despacio', 'alto', 'bajo','muy', 'demasiado', 'suficiente', 'más', 'menos', 'mucho', 'poco', 'bastante', 'casi', 'apenas','sí', 'también','no', 'tampoco', 'nunca', 'jamás','quizá', 'quizás', 'acaso']

adverbios2 = [i.capitalize() for i in adverbios]

articulos = ['el','la','los','las','un','uno','una','unos','unas','al','del']

articulos2 = [i.capitalize() for i in articulos]

adjposesivos = ['mi', 'mis','tu', 'tus','su','sus','nuestro','nuestros', 'nuestra', 'nuestras','vuestro', 'vuestros', 'vuestra', 'vuestras','mío', 'míos', 'mía', 'mías','tuyo', 'tuyos', 'tuya', 'tuyas','suyo', 'suyos', 'suya', 'suyas']

adjposesivos2 = [i.capitalize() for i in adjposesivos]

adjdemostrativos = ['Estos','Esos','Aquellos','Esta','Esa','Aquella','Estas','Esas','Aquellas','Aquel']

adjdemostrativos2 = [i.capitalize() for i in adjdemostrativos]

adjindefinidos = ['algunas','algunos','ningún','ninguna', 'pocos','pocas', 'muchos', 'muchas', 'escasos','escasas', 'demasiadas', 'demasiados','bastantes', 'otros','otras', 'tantos','tantas', 'todos', 'todas', 'varias', 'varios', 'cada', 'ambos','ambas','equis','ciertos','ciertas', 'tales','ningunos','ningunas','poco','poca','alguno','alguna','mucho','escaso','escasa','demasiado','demasiada','bastante','otro','otra','tanto',
'tanta','todo','toda','cierto','cierta','cualquiera'] 

adjindefinidos2 = [i.capitalize() for i in adjindefinidos]

verbosauxpresente = ['abro','abres','abre','abrimos','abrís','abren','acabo','acabas','acaba','acabamos','acabáis','acaban',
    'alcanzo','alcanzas','alcanza','alcanzamos','alcanzáis','alcanzan','ando','andas','anda','andamos','andáis','andan',
    'comienzo', 'comienzas', 'comienza', 'comenzamos', 'comenzáis', 'comienzan',
    'continuo', 'continuas', 'continua', 'continuamos', 'continuáis','continuan',
    'debo','debes','debe','debemos','debéis','deben',
    'digo','dices','dice','decimos','decís','dicen',
    'empiezo','empiezas','empieza', 'empezamos', 'empezáis', 'empiezan',
    'he', 'has', 'ha', 'habemos', 'habéis', 'han',
    'hallo', 'hallas', 'halla', 'hallamos','halláis','hallan','voy','vas','va','vamos',
    'váis', 'van','llevo', 'llevas', 'lleva', 'llevamos', 'lleváis', 'llevan',    'quedo', 'quedas', 'queda', 'quedamos', 'quedáis', 'quedan',
    'resulto', 'resultas', 'resulta', 'resultamos', 'resultáis', 'resultan',
    'sigo', 'sigues', 'sigue', 'seguimos', 'seguís', 'siguen',
    'soy', 'eres', 'es', 'somos', 'sóis', 'son',
    'tengo', 'tienes', 'tiene', 'tenemos', 'tenéis', 'tienen',
    'estoy', 'estás', 'está', 'estamos', 'estáis', 'están',
    'vengo', 'vienes', 'viene', 'vengo', 'venís', 'vienen']
    
verbosauxpresente2 = [i.capitalize() for i in verbosauxpresente]

verbosauxpasado=['abría','abrías','abría','abríamos','abríais','abrían','acababa','acababas','acababa','acabábamos','acababais','acababan',
    'alcanzaba','alcanzabas','alcanzaba','alcanzábamos','alcanzabais','alcanzaban','andaba','andabas','andaba','andábamos','andabais','andaban',
    'comenzaba', 'comenzabas', 'comenzaba', 'comenzábamos', 'comenzabais', 'comenzaban',
    'continuaba', 'continuabas', 'continuaba', 'continuábamos', 'continuabais','continuaban',
    'debía','debías','debía','debíamos','debíais','debían',
    'decía','decías','decía','decíamos','decíais','decían',
    'empezaba','empezabas','empezaba', 'empezábamos', 'empezabais', 'empezaban',
    'había', 'habías', 'había', 'habíamos', 'habíais', 'habían',
    'hallaba', 'hallabas', 'hallaba', 'hallábamos','hallabais','hallaban','iba','ibas','iba','íbamos',
    'íbais', 'iban','llevaba', 'llevabas', 'llevaba', 'llevábamos', 'llevabais', 'llevaban',    'quedaba', 'quedabas', 'quedaba', 'quedábamos', 'quedabais', 'quedaban',
    'resultaba', 'resultabas', 'resultaba', 'resultábamos', 'resultabais', 'resultaban',
    'seguía', 'seguías', 'seguía', 'seguíamos', 'seguíais', 'seguían',
    'era', 'eras', 'era', 'éramos', 'érais', 'eran',
    'tenía', 'tenías', 'tenía', 'teníamos', 'teníais', 'tenían',
    'estaba', 'estabas', 'estaba', 'estábamos', 'estabais', 'estaban',
    'venía', 'venías', 'venía', 'veníamos', 'veníais', 'venian']

verbosauxpasado2 = [i.capitalize() for i in verbosauxpasado]

verbosauxfuturo=['abriré','abrirás','abrirá','abriremos','abriréis','abrirán','acabaré','acabarás','acabará','acabaremos','acabaréis','acabarán',
    'alcanzaré','alcanzarás','alcanzará','alcanzaremos','alcanzaréis','alcanzarán','andaré','andarás','andará','andaremos','andaréis','andarán',
    'comenzaré', 'comenzarás', 'comenzará', 'comenzaremos', 'comenzareis', 'comenzarán',
    'continuaré', 'continuarás', 'continuará', 'continuaremos', 'continuaréis','continuarán',
    'deberá','deberás','deberá','deberemos','deberéis','deberán',
    'dirá','dirás','dirá','diremos','diréis','dirán',
    'empezaré','empezarás','empezará', 'empezaremos', 'empezaréis', 'empezarán'
    'habré', 'habrás', 'habrá', 'habremos', 'habréis', 'habrán',
    'hallaré', 'hallarás', 'hallará', 'hallaremos','hallaréis','hallarán','iré','irás','irá','iremos',
    'iréis', 'irán','llevaré', 'llevarás', 'llevará', 'llevaremos', 'llevaréis', 'llevarán',    'quedaré', 'quedarás', 'quedará', 'quedaremos', 'quedaréis', 'quedarán',
    'resultaré', 'resultarás', 'resultará', 'resultaremos', 'resultaréis', 'resultarán',
    'seguiré', 'seguirás', 'seguirá', 'seguiremos', 'seguiréis', 'seguirán',
    'seré', 'serás', 'será', 'seremos', 'seréis', 'serán',
    'tendré', 'tendrás', 'tendrá', 'tendremos', 'tendréis', 'tendrán',
    'vendré', 'vendrás', 'vendrá', 'vendremos', 'vendréis', 'vendrán']
verbosauxfuturo2 = [i.capitalize() for i in verbosauxfuturo]
afegides = ['se','lo','le','él','fue','era','ser','es','me','ha','he','nos','son']

afegides2 = [i.capitalize() for i in afegides]
#568 paraules prohibides....llista a ampliar
enc='utf-8'
prohibidas = preposiciones + conjcoordinadas + conjsubordinadas + adverbios + articulos + adjposesivos + adjdemostrativos + adjindefinidos + verbosauxpresente + verbosauxpasado + verbosauxfuturo + afegides
prohibidas2 = preposiciones2 + conjcoordinadas2 + conjsubordinadas2 + adverbios2 + articulos2 + adjposesivos2 + adjdemostrativos2 + adjindefinidos2 + verbosauxpresente2 + verbosauxpasado2 + verbosauxfuturo2 + afegides2
prohibides = prohibidas + prohibidas2



