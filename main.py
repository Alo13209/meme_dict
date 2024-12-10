meme_dict ={
    'LOL' : 'Una respuesta a algo gracioso',
    'Red Flag' : 'Alguien con defectos peligrosos',
    'XD' : 'Expresion a algo gracioso'
    'LMAO' : 'Expresion a algo muy gracioso'
}
word = input('Ingresa la palabra a consultar').upper()

if word in meme_dict.keys():
    print('Lo que significa es: ', meme_dict[word])
else:
    print('La palabra no existe o esta mal escrita')
