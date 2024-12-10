meme_dict ={
    'LOL' : 'Una respuesta a algo gracioso',
    'Red Flag' : 'Alguien con defectos peligrosos',
    'XD' : 'Expresion a algo gracioso',
    'LMAO' : 'Expresion a algo muy gracioso',
    'CRINGE' : 'Sinonimo a verguenza ajena',
    'RageBait' : 'Molestar alguien con el proposito que se enoje',
    'Aura' : 'Sinonimo moderno de Cool, pero es algo que se obtiene ( Tengo Aura, Tienes Aura )',
}
word = input('Ingresa la palabra a consultar').upper()

if word in meme_dict.keys():
    print('Lo que significa es: ', meme_dict[word])
else:
    print('La palabra no existe o esta mal escrita')n
