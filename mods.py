print("cargando...")
#!/usr/bin/env Python 3.6
# -*- coding: UTF-8 -*-


import telegram 
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.utils.helpers import escape_markdown
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext ,Filters ,MessageHandler
import os ,sys ,math ,json ,bs4 ,datetime ,requests ,re ,socket ,pickle
from random import *
from io import *
from time   import sleep
from random import randint
# TOKEN AND INIT CONFIGS
def process(name,names,owner,bot_token):
  updater = Updater(token=bot_token,use_context=True)
  dispatcher = updater.dispatcher
  os.system("clear")
  print("""

  --------« CONSOLE OF THE BOT »--------------

  \033[4;33mWELCOME TO THE BOT :\033[0;m {}

  \033[4;33mTOKEN :\033[0;m {}

  \033[4;33mYOUR NAME :\033[0;m {}

  \033[4;33mYOUR GROUP :\033[0;m {}

  \033[4;33mDEVELOPER  :\033[0;m FLYEAD

  \033[4;33mFOR A OPEN SOURCE WORLD\033[0;m

  \033[4;33mDEBES DE APRETAR CTRL+C PARA SALIR\033[0;m

  --------«------------------------»-----------

  ( EN LA CONSOLA SE VERÁN LOS ERRORES DE SE MOSTRARAN EN TIEMPO REAL )

  """.format(names,bot_token,owner,name))

  #end configs

  # ----------------------------------------------------------------
  # CODIGO ABIERTO PARA IMPORTAR Y/O MODIFICAR
  # USO LIBRE Y A SU PROPIA DISCRECION
  #-----------------------------------------------------------------we
  # LOG V0.0.1+ALPHA by L
  def checksum_mod(card_number):
    sum = 0
    num_digits = len(card_number)
    oddeven = num_digits & 1
    for count in range(0, num_digits):
      digit = int(card_number[count])
      if not (( count & 1 ) ^ oddeven ):
        digit = digit * 2
      if digit > 9:
        digit = digit - 9
      sum = sum + digit
    return ( (sum % 10) == 0 )
  class Log():
          def __init__(self, archivo="nombre.txt"):
              self.nombre=archivo
          def write(self, mensaje=""):
              with open(self.nombre,"a+") as f:
                  f.seek(0)
                  data = f.read(100)
                  if len(data) > 0:
                      f.write("\n")
                  f.write(mensaje)
                  f.close()
          def reset(self):
              with open(self.nombre,"w") as f:
                  f.write("")
                  f.close()
          def read(self):
              with open(self.nombre,"r") as f:
                  lineas = f.readlines()
                  f.close()
                  return lineas
  class Tools():
        """
        TOOLS IS BASED IN
        CCTOOLS - Multi Tools of Carding, EDUCATIONAL PURPOSES.
        Copyright (C) 2020  

        DISCLAIMER: This file is for informational and educational purposes only. 
        We are not responsible for any misuse applied to it. All responsibility falls on the user

        ||================================================================================||
        || FRAGMENTS USED FROM https://github.com/Lanniscaf/cctools/blob/master/cctools.py||
        ||================================================================================||

        Adapted BY flyead ALL RIGHTS RESERVED
        """
        def __init__(self):
          self.especialCCG = False
          self.fromFileName = 'binlist.txt'
          super()
        def __cardLuhnChecksumIsValid(self,card_number):
          sum = 0
          num_digits = len(card_number)
          oddeven = num_digits & 1

          for count in range(0, num_digits):
              digit = int(card_number[count])

              if not (( count & 1 ) ^ oddeven ):
                  digit = digit * 2
              if digit > 9:
                  digit = digit - 9

              sum = sum + digit

          return ( (sum % 10) == 0 )
        def __ccgen(self, bin_format):
          permiso = True
          while permiso:
            out_cc = ""
            completo = 0
            #Iteration over the bin
            if(bin_format[:1]=="3"):
                self.especial = True
                for i in range(15):
                    try:
                        if bin_format[i] in ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9"):
                            out_cc = out_cc + bin_format[i]
                            continue
                        elif bin_format[i] in ("x", "X" ):
                            out_cc = out_cc + str(randint(0,9))
                            continue
                    except:
                        largo = 13 - len(bin_format)
                        for x in range(largo):
                            bin_format += 'x'
                        out_cc = out_cc + str(randint(0,9))
                    else:
                        pass
                if(completo>=14):
                    return('Favor extrapole el bin')
                    break
                    
            else:    
                self.especial=False
                for i in range(15):
                    try:
                        if bin_format[i] in ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9"):
                            out_cc = out_cc + bin_format[i]
                            completo+=1
                            continue
                        elif bin_format[i] in ("x", "X" ):
                            out_cc = out_cc + str(randint(0,9))
                            continue
                        
                    except:
                        largo = 15 - len(bin_format)
                        for x in range(largo):
                            bin_format += 'x'
                        out_cc = out_cc + str(randint(0,9))
                    else:
                        return(False)
                        break
                if(completo>=15):
                    return('Favor extrapole')
            #compare common numbers
            numberC=0
            for i in range(len(bin_format)):
              try:
                if bin_format[i] in ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9"):
                    numberC+=1
                    continue
                elif bin_format[i] in ("x", "X" ):
                    continue
              except:
                  return('ERRORFATAL')
            #Generate checksum (last digit) -- IMPLICIT CHECK
            for i in range(10):
                checksum_check = out_cc
                if(bin_format[15:]=="" or bin_format[15:] in ("x","X")):
                    checksum_check = checksum_check + str(i)    
                else:
                    checksum_check = checksum_check + bin_format[15:]
                
                #control numbers common
                respect=0
                if(self.especial):
                  #///
                  #Generate checksum (last digit) -- IMPLICIT CHECK
                  for i in range(10):
                      checksum_check = out_cc
                      checksum_check = checksum_check + str(i)

                      if self.__cardLuhnChecksumIsValid(checksum_check):
                          out_cc = checksum_check
                          break
                      else:
                          checksum_check = out_cc
                  return(checksum_check)
                  #///
                else:

                  for i in range(len(bin_format)):
                    
                    if(bin_format[i]==checksum_check[i]):
                      respect+=1
                    else:
                      continue
                  if (self.__cardLuhnChecksumIsValid(checksum_check) and numberC==respect):
                      out_cc = checksum_check
                      permiso= False
                      break
                  else:
                      checksum_check = out_cc
                    

          return(out_cc)   
        def __ccvgen(self):
          if(self.especial==False):
              ccv = ""
              num = randint(10,999)

              if num < 100:
                  ccv = "0" + str(num)
              else:
                  ccv = str(num)
          else:
              ccv = ""
              num = randint(100,9999)

              if num < 1000:
                  ccv = "0" + str(num)
              else:
                  ccv = str(num)
          
          return(ccv)
        def __dategen(self):
          now = datetime.datetime.now()
          date = ""
          month = str(randint(1, 12))
          if(int(month) < 10):
              month = "0"+month
          current_year = str(now.year)
          year = str(randint(int(current_year[-2:]) + 1, int(current_year[-2:]) + 6))
          date = month + "|" + year

          return date
        def __monthonly(self):
          month= str(randint(1,12))
          if(int(month) < 10):
              month = "0"+month
          return month
        def __yearonly(self):
          now = datetime.datetime.now()
          date = ""
          current_year = str(now.year)
          year = str(randint(int(current_year[-2:]) + 1, int(current_year[-2:]) + 6))
          return year
        def generador(self, bins, month=False, year=False, codigocvv=False):
          try:
            if(bins != ''):
              beans = list()
              beans.append(self.regex(bins[0])[0])
              cc_list = list()
              for _ in range(10):
                bin_format = beans[0]
                banIA = self.__ccgen(bin_format)
                if(banIA == 'Favor extrapole el bin'):
                  # //EL BIN NO ESTA EXTRAPOLADO
                  return False

                if(month == False):
                  mes=self.__monthonly()
                elif(month != False):
                  mes=month
                if(year == False):
                  ano=self.__yearonly()
                elif(year != False):
                  ano=year
                if(codigocvv == False):
                  carverificationv=self.__ccvgen()
                elif(codigocvv != False):
                  carverificationv=codigocvv
                
                if(banIA == False):
                  return False
                cc_list.append('{0}|{1}|{2}|{3}'.format(banIA,mes,ano,carverificationv))
              return cc_list

          except:
            return False
        def regex(self, toParse):
          format = r'([A-WY-wy-z]|\s)'
          return re.subn(format, '', toParse)
        def ccgenFromList(self, bins, month=False, year=False, cvv=False):
          try:
            if(type(bins) == type([])):
              i = 0
              for l in bins:
                i += 1
              if i == 1:
                return self.generador(bins)
              # // el usuario entrgo una lista de bins
              beans = list()
              for bin_f in bins:
                scaped = self.regex(bin_f)
                beans.append(scaped)
              cc_list = list()
              for bin_format in beans:
                banIA = self.__ccgen(bin_format[0])
                if(banIA == 'Favor extrapole el bin'):
                  # //EL BIN NO ESTA EXTRAPOLADO
                  return False

                if(month == False):
                  mes=self.__monthonly()
                elif(month != False):
                  mes=month
                if(year == False):
                  ano=self.__yearonly()
                elif(year != False):
                  ano=year
                if(cvv == False):
                  carverificationv=self.__ccvgen()
                elif(cvv != False):
                  carverificationv=cvv
                
                cc_list.append('{0}|{1}|{2}|{3}'.format(banIA,mes,ano,carverificationv))
              return cc_list  

          except:
            return False
        def fromFileList(self):
          log = Log(archivo= self.fromFileName)
          result = self.ccgenFromList(log.read())
          log.reset()
          message = ''
          # formato
          for i in result:
            message += i + '\n'
          log.write(mensaje=message)
          

        try:
          # // al iniciar el archivo intenta buscar si hay una lista de bins para usar
          Tools().fromFileList()
        except:
          pass

  class IbanNew():
  	def __init__(self):
  		self.msg=''
  	def IbanX(self):
  		url='https://api.generadordni.es/v2/bank/account?results=3&bic,iban_formatted,ccc_formatted'
  		response= requests.get(url)
  		if response.status_code==200:
  			response_json=response.json()
  			assd=response_json[0]
  			ccc=assd['ccc']
  			iban=assd['iban']
  			entity=assd['entity']
  			bicss=assd['bic']
  			saol=str(bicss)
  			ccc_1=str(ccc)
  			iban_2=str(iban)
  			entity_3=str(entity)
  			self.msg="""
ಠ-> CCC : <code>{}</code>

ಠ-> IBAN : <code>{}</code>

ಠ-> Entity : <code>{}</code>

ಠ-> BIC : <code>{}</code>
  """.format(ccc_1,iban_2,entity_3,saol)
  def start(update,context):
    keyboard=[[InlineKeyboardButton("help", callback_data='empezar')],[InlineKeyboardButton("infobot", callback_data='infobot')]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    user = update.message.from_user.username
    msg="""
<-ಠ-> SyruxTools <-ಠ->
ಠ-----------------------ಠ-------------------------ಠ
ಠ-> @{} Bienvenido al Bot del grupo SyruxChat este es un Bot multiusos para lo que es la Bineria y el Carding.
ಠ-----------------------ಠ-------------------------ಠ
ಠ-> Presiona el boton help para ver los comandos
ಠ-----------------------ಠ-------------------------ಠ
ಠ-> Si quieres más información sobre este grupo puedes unirte a el : @SyruxChat""".format(user)
    update.message.reply_text(msg,reply_markup=reply_markup)
  def button(update: Update, context: CallbackContext):
    query = update.callback_query
    oel=query.data
    if oel=="infobot":
      keyboard=[[InlineKeyboardButton("help", callback_data='empezar')],
      [InlineKeyboardButton("menu principal", callback_data='volver')]]
      reply_markup = InlineKeyboardMarkup(keyboard)
      msg="""
<b>NOMBRE DEL BOT : </b><u><i>{}</i></u>

<b>Version : </b><u><i>BETA</i></u>

<b>Sexo :</b> <u>FEMENINO 7W7</u>

<b>OWNER : </b><u><i>{}</i></u>""".format(names,owner)
      query.edit_message_text(text=msg,reply_markup=reply_markup,parse_mode="HTML")
    elif oel=="volver":
      keyboard=[[InlineKeyboardButton("help", callback_data='empezar')],
      [InlineKeyboardButton("infobot", callback_data='infobot')]]
      reply_markup = InlineKeyboardMarkup(keyboard)
      msg="""
      <-ಠ-> SyruxTools <-ಠ->
ಠ-----------------------ಠ-------------------------ಠ
ಠ-> Bienvenido al Bot del grupo SyruxChat este es un Bot multiusos para lo que es la Bineria y el Carding.
ಠ-----------------------ಠ-------------------------ಠ
ಠ-> Presiona el boton help para ver los comandos
ಠ-----------------------ಠ-------------------------ಠ
ಠ-> Si quieres más información sobre este grupo puedes unirte a el : @SyruxChat"""
      query.edit_message_text(text=msg,reply_markup=reply_markup)
    elif oel =="empezar":
      keyboard=[[InlineKeyboardButton("menu principal", callback_data='volver')],
      [InlineKeyboardButton("infobot", callback_data='infobot')]]
      reply_markup = InlineKeyboardMarkup(keyboard)
      msg="""
ಠ--------------ಠ Comandos ಠ--------------ಠ
-> /crearb - <b>Crea un bin.</b>
-> /crearib - <b>Crea una Iban.</b>
-> /extrap - <b>Extrapola.</b>
-> /find - <b>Busca información de una IP.</b>
-> /genera - <b>Genera un Bin.</b>
-> /bincheck - <b>Verifica si el Bin es válido.</b>
-> /info - <b>Información del Bot y del Grupo</b>
ಠ-----------------------ಠ-------------------------ಠ"""
      query.edit_message_text(text=msg,reply_markup=reply_markup,parse_mode="HTML")
    elif oel=="crearnewbin":
        a=randint(4,6)
        b=randint(4,6)
        c=randint(0,9)
        d=randint(0,9)
        e=randint(0,9)
        f=randint(0,13)
        bin=str(int(a))+str(int(b))+str(int(c))+str(int(d))+str(int(d))+str(int(e))+str(int(f))
        if len(bin) >= 6:
          bin= str(bin)
        try:
          bin= bin.replace("x","")
          bin= bin.replace("X","")
          bin= bin.split("|")[0]
        except:
          pass
        bin = str(re.sub('([a-zA-Z]){1,}', '', bin))
        lenLuhn=len(str(bin))
        sinccheck=bin[:16]
        bin = str(bin)
        bin = re.sub('([a-zA-Z]){1,}', '', bin)
        try:
          keyboard=[[InlineKeyboardButton("CREAR", callback_data='crearnewbin')]]
          reply_markup = InlineKeyboardMarkup(keyboard)
          unks = 0
          url='https://lookup.binlist.net/'+str(bin)
          try:
            page = requests.get(url)
            page.raise_for_status()
          except:
            pass
          page= page.content.decode()
          dic = json.loads(page)
          try:
            marca=dic['scheme']
          except:
            marca='DESCONOCIDO'
          try:
            tipo=dic['type']
          except:
            tipo='DESCONOCIDO'
          try:
            brnd=dic['brand']
          except:
            brnd='DESCONOCIDO'
          try:
            el_alpha=dic['country']['alpha2']
          except:
            el_alpha='DESCONOCIDO'
          try:
            pais=dic['country']['name']
          except:
            pais='DESCONOCIDO'
          try:
            emote=dic['country']['emoji']
          except:
            emote='DESCONOCIDO'
          try:
            tipo_moneda=dic['country']['currency']
          except:
            tipo_moneda='DESCONOCIDO'
          try:
            bank_name=dic['bank']['name']
          except:
            bank_name='DESCONOCIDO'
          try:
            bank_url=dic['bank']['url']
          except:
            bank_url='DESCONOCIDO'
          try:
            bank_phone=dic['bank']['phone']
          except:
            bank_phone='DESCONOCIDO'
          ibba_2="""
ಠ-> Bin : <code>{}</code> {}

ಠ-> Marca : <b><u>{}</u></b>

ಠ-> Tipo de tarjeta: <b><u>{}</u></b>

ಠ-> Nivel de tarjeta: <b><u>{}</u></b>

ಠ-> Banco : <b><u>{}</u></b>

ಠ-> País : <b><u>{}</u></b> - <b><u>{}</u></b> - 💲 <b><u>{}</u></b>

ಠ-> URL Banco : <b><u>{}</u></b>
""".format(bin,emote,marca,tipo,brnd,bank_name,pais,el_alpha,tipo_moneda,bank_url)
          query.edit_message_text(text=ibba_2,reply_markup=reply_markup,parse_mode="HTML")
        except:
          keyboard=[[InlineKeyboardButton("CREAR", callback_data='crearnewbin')]]
          reply_markup = InlineKeyboardMarkup(keyboard)
          ibba_2="<b>Mala suerte, reintenta de nuevo :)</b>"
          query.edit_message_text(text=ibba_2,reply_markup=reply_markup,parse_mode="HTML")
    else:
      vale=oel.strip("']").strip("['")
      msg=list()
      msg.append(vale)
      Loxd=vale.split("|")
      if len(msg) > 0:
        if len(Loxd)==1:
          keyboard=[[InlineKeyboardButton("GENERAR", callback_data='{}'.format(msg))]]
          reply_markup = InlineKeyboardMarkup(keyboard)
          binf = msg
          obj = Tools()
          a=obj.ccgenFromList(binf)
          aa=str(a[0])
          bb=str(a[1])
          cc=str(a[2])
          dd=str(a[3])
          ee=str(a[4])
          ff=str(a[5])
          gg=str(a[6])
          hh=str(a[7])
          ii=str(a[8])
          jj=str(a[9])
          msg="""
ಠ-> <code>{}</code>
ಠ-> <code>{}</code>
ಠ-> <code>{}</code>
ಠ-> <code>{}</code>
ಠ-> <code>{}</code>
ಠ-> <code>{}</code>
ಠ-> <code>{}</code>
ಠ-> <code>{}</code>
ಠ-> <code>{}</code>
ಠ-> <code>{}</code>""".format(aa,bb,cc,dd,ee,ff,gg,hh,ii,jj)
          query.edit_message_text(text=msg,reply_markup=reply_markup,parse_mode="HTML")
        if len(Loxd)==2:
          keyboard=[[InlineKeyboardButton("GENERAR", callback_data='{}'.format(msg))]]
          reply_markup = InlineKeyboardMarkup(keyboard)
          binf = list()
          binf.append(Loxd[0])
          obj = Tools()
          a=obj.ccgenFromList(binf)
          aa=str(a[0][0])+str(a[0][1])+str(a[0][2])+str(a[0][3])+str(a[0][4])+str(a[0][5])+str(a[0][6])+str(a[0][7])+str(a[0][8])+str(a[0][9])+str(a[0][10])+str(a[0][11])+str(a[0][12])+str(a[0][13])+str(a[0][14])+str(a[0][15])+"|"+str(Loxd[1])+"|"+str(a[0][20])+str(a[0][21])+"|"+str(a[0][23])+str(a[0][24])+str(a[0][25])
          bb=str(a[1][0])+str(a[1][1])+str(a[1][2])+str(a[1][3])+str(a[1][4])+str(a[1][5])+str(a[1][6])+str(a[1][7])+str(a[1][8])+str(a[1][9])+str(a[1][10])+str(a[1][11])+str(a[1][12])+str(a[1][13])+str(a[1][14])+str(a[1][15])+"|"+str(Loxd[1])+"|"+str(a[1][20])+str(a[1][21])+"|"+str(a[1][23])+str(a[1][24])+str(a[1][25])
          cc=str(a[2][0])+str(a[2][1])+str(a[2][2])+str(a[2][3])+str(a[2][4])+str(a[2][5])+str(a[2][6])+str(a[2][7])+str(a[2][8])+str(a[2][9])+str(a[2][10])+str(a[2][11])+str(a[2][12])+str(a[2][13])+str(a[2][14])+str(a[2][15])+"|"+str(Loxd[1])+"|"+str(a[2][20])+str(a[2][21])+"|"+str(a[2][23])+str(a[2][24])+str(a[2][25])
          dd=str(a[3][0])+str(a[3][1])+str(a[3][2])+str(a[3][3])+str(a[3][4])+str(a[3][5])+str(a[3][6])+str(a[3][7])+str(a[3][8])+str(a[3][9])+str(a[3][10])+str(a[3][11])+str(a[3][12])+str(a[3][13])+str(a[3][14])+str(a[3][15])+"|"+str(Loxd[1])+"|"+str(a[3][20])+str(a[3][21])+"|"+str(a[3][23])+str(a[3][24])+str(a[3][25])
          ee=str(a[4][0])+str(a[4][1])+str(a[4][2])+str(a[4][3])+str(a[4][4])+str(a[4][5])+str(a[4][6])+str(a[4][7])+str(a[4][8])+str(a[4][9])+str(a[4][10])+str(a[4][11])+str(a[4][12])+str(a[4][13])+str(a[4][14])+str(a[4][15])+"|"+str(Loxd[1])+"|"+str(a[4][20])+str(a[4][21])+"|"+str(a[4][23])+str(a[4][24])+str(a[4][25])
          ff=str(a[5][0])+str(a[5][1])+str(a[5][2])+str(a[5][3])+str(a[5][4])+str(a[5][5])+str(a[5][6])+str(a[5][7])+str(a[5][8])+str(a[5][9])+str(a[5][10])+str(a[5][11])+str(a[5][12])+str(a[5][13])+str(a[5][14])+str(a[5][15])+"|"+str(Loxd[1])+"|"+str(a[5][20])+str(a[5][21])+"|"+str(a[5][23])+str(a[5][24])+str(a[5][25])
          gg=str(a[6][0])+str(a[6][1])+str(a[6][2])+str(a[6][3])+str(a[6][4])+str(a[6][5])+str(a[6][6])+str(a[6][7])+str(a[6][8])+str(a[6][9])+str(a[6][10])+str(a[6][11])+str(a[6][12])+str(a[6][13])+str(a[6][14])+str(a[6][15])+"|"+str(Loxd[1])+"|"+str(a[6][20])+str(a[6][21])+"|"+str(a[6][23])+str(a[6][24])+str(a[6][25])
          hh=str(a[7][0])+str(a[7][1])+str(a[7][2])+str(a[7][3])+str(a[7][4])+str(a[7][5])+str(a[7][6])+str(a[7][7])+str(a[7][8])+str(a[7][9])+str(a[7][10])+str(a[7][11])+str(a[7][12])+str(a[7][13])+str(a[7][14])+str(a[7][15])+"|"+str(Loxd[1])+"|"+str(a[7][20])+str(a[7][21])+"|"+str(a[7][23])+str(a[7][24])+str(a[7][25])
          ii=str(a[8][0])+str(a[8][1])+str(a[8][2])+str(a[8][3])+str(a[8][4])+str(a[8][5])+str(a[8][6])+str(a[8][7])+str(a[8][8])+str(a[8][9])+str(a[8][10])+str(a[8][11])+str(a[8][12])+str(a[8][13])+str(a[8][14])+str(a[8][15])+"|"+str(Loxd[1])+"|"+str(a[8][20])+str(a[8][21])+"|"+str(a[8][23])+str(a[8][24])+str(a[8][25])
          jj=str(a[9][0])+str(a[9][1])+str(a[9][2])+str(a[9][3])+str(a[9][4])+str(a[9][5])+str(a[9][6])+str(a[9][7])+str(a[9][8])+str(a[9][9])+str(a[9][10])+str(a[9][11])+str(a[9][12])+str(a[9][13])+str(a[9][14])+str(a[9][15])+"|"+str(Loxd[1])+"|"+str(a[9][20])+str(a[9][21])+"|"+str(a[9][23])+str(a[9][24])+str(a[9][25])
          msg="""
ಠ-> <code>{}</code>
ಠ-> <code>{}</code>
ಠ-> <code>{}</code>
ಠ-> <code>{}</code>
ಠ-> <code>{}</code>
ಠ-> <code>{}</code>
ಠ-> <code>{}</code>
ಠ-> <code>{}</code>
ಠ-> <code>{}</code>
ಠ-> <code>{}</code>""".format(aa,bb,cc,dd,ee,ff,gg,hh,ii,jj)
          query.edit_message_text(text=msg,reply_markup=reply_markup,parse_mode="HTML")
        elif len(Loxd)==3:
          keyboard=[[InlineKeyboardButton("GENERAR", callback_data='{}'.format(msg))]]
          reply_markup = InlineKeyboardMarkup(keyboard)
          binf = list()
          binf.append(Loxd[0])
          obj = Tools()
          a=obj.ccgenFromList(binf)
          aa=str(a[0][0])+str(a[0][1])+str(a[0][2])+str(a[0][3])+str(a[0][4])+str(a[0][5])+str(a[0][6])+str(a[0][7])+str(a[0][8])+str(a[0][9])+str(a[0][10])+str(a[0][11])+str(a[0][12])+str(a[0][13])+str(a[0][14])+str(a[0][15])+"|"+str(Loxd[1])+"|"+str(Loxd[2])+"|"+str(a[0][23])+str(a[0][24])+str(a[0][25])
          bb=str(a[1][0])+str(a[1][1])+str(a[1][2])+str(a[1][3])+str(a[1][4])+str(a[1][5])+str(a[1][6])+str(a[1][7])+str(a[1][8])+str(a[1][9])+str(a[1][10])+str(a[1][11])+str(a[1][12])+str(a[1][13])+str(a[1][14])+str(a[1][15])+"|"+str(Loxd[1])+"|"+str(Loxd[2])+"|"+str(a[1][23])+str(a[1][24])+str(a[1][25])
          cc=str(a[2][0])+str(a[2][1])+str(a[2][2])+str(a[2][3])+str(a[2][4])+str(a[2][5])+str(a[2][6])+str(a[2][7])+str(a[2][8])+str(a[2][9])+str(a[2][10])+str(a[2][11])+str(a[2][12])+str(a[2][13])+str(a[2][14])+str(a[2][15])+"|"+str(Loxd[1])+"|"+str(Loxd[2])+"|"+str(a[2][23])+str(a[2][24])+str(a[2][25])
          dd=str(a[3][0])+str(a[3][1])+str(a[3][2])+str(a[3][3])+str(a[3][4])+str(a[3][5])+str(a[3][6])+str(a[3][7])+str(a[3][8])+str(a[3][9])+str(a[3][10])+str(a[3][11])+str(a[3][12])+str(a[3][13])+str(a[3][14])+str(a[3][15])+"|"+str(Loxd[1])+"|"+str(Loxd[2])+"|"+str(a[3][23])+str(a[3][24])+str(a[3][25])
          ee=str(a[4][0])+str(a[4][1])+str(a[4][2])+str(a[4][3])+str(a[4][4])+str(a[4][5])+str(a[4][6])+str(a[4][7])+str(a[4][8])+str(a[4][9])+str(a[4][10])+str(a[4][11])+str(a[4][12])+str(a[4][13])+str(a[4][14])+str(a[4][15])+"|"+str(Loxd[1])+"|"+str(Loxd[2])+"|"+str(a[4][23])+str(a[4][24])+str(a[4][25])
          ff=str(a[5][0])+str(a[5][1])+str(a[5][2])+str(a[5][3])+str(a[5][4])+str(a[5][5])+str(a[5][6])+str(a[5][7])+str(a[5][8])+str(a[5][9])+str(a[5][10])+str(a[5][11])+str(a[5][12])+str(a[5][13])+str(a[5][14])+str(a[5][15])+"|"+str(Loxd[1])+"|"+str(Loxd[2])+"|"+str(a[5][23])+str(a[5][24])+str(a[5][25])
          gg=str(a[6][0])+str(a[6][1])+str(a[6][2])+str(a[6][3])+str(a[6][4])+str(a[6][5])+str(a[6][6])+str(a[6][7])+str(a[6][8])+str(a[6][9])+str(a[6][10])+str(a[6][11])+str(a[6][12])+str(a[6][13])+str(a[6][14])+str(a[6][15])+"|"+str(Loxd[1])+"|"+str(Loxd[2])+"|"+str(a[6][23])+str(a[6][24])+str(a[6][25])
          hh=str(a[7][0])+str(a[7][1])+str(a[7][2])+str(a[7][3])+str(a[7][4])+str(a[7][5])+str(a[7][6])+str(a[7][7])+str(a[7][8])+str(a[7][9])+str(a[7][10])+str(a[7][11])+str(a[7][12])+str(a[7][13])+str(a[7][14])+str(a[7][15])+"|"+str(Loxd[1])+"|"+str(Loxd[2])+"|"+str(a[7][23])+str(a[7][24])+str(a[7][25])
          ii=str(a[8][0])+str(a[8][1])+str(a[8][2])+str(a[8][3])+str(a[8][4])+str(a[8][5])+str(a[8][6])+str(a[8][7])+str(a[8][8])+str(a[8][9])+str(a[8][10])+str(a[8][11])+str(a[8][12])+str(a[8][13])+str(a[8][14])+str(a[8][15])+"|"+str(Loxd[1])+"|"+str(Loxd[2])+"|"+str(a[8][23])+str(a[8][24])+str(a[8][25])
          jj=str(a[9][0])+str(a[9][1])+str(a[9][2])+str(a[9][3])+str(a[9][4])+str(a[9][5])+str(a[9][6])+str(a[9][7])+str(a[9][8])+str(a[9][9])+str(a[9][10])+str(a[9][11])+str(a[9][12])+str(a[9][13])+str(a[9][14])+str(a[9][15])+"|"+str(Loxd[1])+"|"+str(Loxd[2])+"|"+str(a[9][23])+str(a[9][24])+str(a[9][25])
          msg="""
ಠ-> <code>{}</code>
ಠ-> <code>{}</code>
ಠ-> <code>{}</code>
ಠ-> <code>{}</code>
ಠ-> <code>{}</code>
ಠ-> <code>{}</code>
ಠ-> <code>{}</code>
ಠ-> <code>{}</code>
ಠ-> <code>{}</code>
ಠ-> <code>{}</code>""".format(aa,bb,cc,dd,ee,ff,gg,hh,ii,jj)
          query.edit_message_text(text=msg,reply_markup=reply_markup,parse_mode="HTML")
        elif len(Loxd)==4:
          keyboard=[[InlineKeyboardButton("GENERAR", callback_data='{}'.format(msg))]]
          reply_markup = InlineKeyboardMarkup(keyboard)
          binf = list()
          binf.append(Loxd[0])
          obj = Tools()
          a=obj.ccgenFromList(binf)
          aa=str(a[0][0])+str(a[0][1])+str(a[0][2])+str(a[0][3])+str(a[0][4])+str(a[0][5])+str(a[0][6])+str(a[0][7])+str(a[0][8])+str(a[0][9])+str(a[0][10])+str(a[0][11])+str(a[0][12])+str(a[0][13])+str(a[0][14])+str(a[0][15])+"|"+str(Loxd[1])+"|"+str(Loxd[2])+"|"+str(Loxd[3])
          bb=str(a[1][0])+str(a[1][1])+str(a[1][2])+str(a[1][3])+str(a[1][4])+str(a[1][5])+str(a[1][6])+str(a[1][7])+str(a[1][8])+str(a[1][9])+str(a[1][10])+str(a[1][11])+str(a[1][12])+str(a[1][13])+str(a[1][14])+str(a[1][15])+"|"+str(Loxd[1])+"|"+str(Loxd[2])+"|"+str(Loxd[3])
          cc=str(a[2][0])+str(a[2][1])+str(a[2][2])+str(a[2][3])+str(a[2][4])+str(a[2][5])+str(a[2][6])+str(a[2][7])+str(a[2][8])+str(a[2][9])+str(a[2][10])+str(a[2][11])+str(a[2][12])+str(a[2][13])+str(a[2][14])+str(a[2][15])+"|"+str(Loxd[1])+"|"+str(Loxd[2])+"|"+str(Loxd[3])
          dd=str(a[3][0])+str(a[3][1])+str(a[3][2])+str(a[3][3])+str(a[3][4])+str(a[3][5])+str(a[3][6])+str(a[3][7])+str(a[3][8])+str(a[3][9])+str(a[3][10])+str(a[3][11])+str(a[3][12])+str(a[3][13])+str(a[3][14])+str(a[3][15])+"|"+str(Loxd[1])+"|"+str(Loxd[2])+"|"+str(Loxd[3])
          ee=str(a[4][0])+str(a[4][1])+str(a[4][2])+str(a[4][3])+str(a[4][4])+str(a[4][5])+str(a[4][6])+str(a[4][7])+str(a[4][8])+str(a[4][9])+str(a[4][10])+str(a[4][11])+str(a[4][12])+str(a[4][13])+str(a[4][14])+str(a[4][15])+"|"+str(Loxd[1])+"|"+str(Loxd[2])+"|"+str(Loxd[3])
          ff=str(a[5][0])+str(a[5][1])+str(a[5][2])+str(a[5][3])+str(a[5][4])+str(a[5][5])+str(a[5][6])+str(a[5][7])+str(a[5][8])+str(a[5][9])+str(a[5][10])+str(a[5][11])+str(a[5][12])+str(a[5][13])+str(a[5][14])+str(a[5][15])+"|"+str(Loxd[1])+"|"+str(Loxd[2])+"|"+str(Loxd[3])
          gg=str(a[6][0])+str(a[6][1])+str(a[6][2])+str(a[6][3])+str(a[6][4])+str(a[6][5])+str(a[6][6])+str(a[6][7])+str(a[6][8])+str(a[6][9])+str(a[6][10])+str(a[6][11])+str(a[6][12])+str(a[6][13])+str(a[6][14])+str(a[6][15])+"|"+str(Loxd[1])+"|"+str(Loxd[2])+"|"+str(Loxd[3])
          hh=str(a[7][0])+str(a[7][1])+str(a[7][2])+str(a[7][3])+str(a[7][4])+str(a[7][5])+str(a[7][6])+str(a[7][7])+str(a[7][8])+str(a[7][9])+str(a[7][10])+str(a[7][11])+str(a[7][12])+str(a[7][13])+str(a[7][14])+str(a[7][15])+"|"+str(Loxd[1])+"|"+str(Loxd[2])+"|"+str(Loxd[3])
          ii=str(a[8][0])+str(a[8][1])+str(a[8][2])+str(a[8][3])+str(a[8][4])+str(a[8][5])+str(a[8][6])+str(a[8][7])+str(a[8][8])+str(a[8][9])+str(a[8][10])+str(a[8][11])+str(a[8][12])+str(a[8][13])+str(a[8][14])+str(a[8][15])+"|"+str(Loxd[1])+"|"+str(Loxd[2])+"|"+str(Loxd[3])
          jj=str(a[9][0])+str(a[9][1])+str(a[9][2])+str(a[9][3])+str(a[9][4])+str(a[9][5])+str(a[9][6])+str(a[9][7])+str(a[9][8])+str(a[9][9])+str(a[9][10])+str(a[9][11])+str(a[9][12])+str(a[9][13])+str(a[9][14])+str(a[9][15])+"|"+str(Loxd[1])+"|"+str(Loxd[2])+"|"+str(Loxd[3])
          msg="""
ಠ-> <code>{}</code>
ಠ-> <code>{}</code>
ಠ-> <code>{}</code>
ಠ-> <code>{}</code>
ಠ-> <code>{}</code>
ಠ-> <code>{}</code>
ಠ-> <code>{}</code>
ಠ-> <code>{}</code>
ಠ-> <code>{}</code>
ಠ-> <code>{}</code>""".format(aa,bb,cc,dd,ee,ff,gg,hh,ii,jj)
          query.edit_message_text(text=msg,reply_markup=reply_markup,parse_mode="HTML")
  def genera(update,context):
    user = update.message.from_user.username
    args=context.args
    msg=args
    if len(args) > 0:
      Loxd=str(args[0]).split("|")
      if len(Loxd)==1:
        keyboard=[[InlineKeyboardButton("GENERAR", callback_data='{}'.format(list(args)))]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        binf = msg
        obj = Tools()
        a=obj.ccgenFromList(binf)
        aa=str(a[0])
        bb=str(a[1])
        cc=str(a[2])
        dd=str(a[3])
        ee=str(a[4])
        ff=str(a[5])
        gg=str(a[6])
        hh=str(a[7])
        ii=str(a[8])
        jj=str(a[9])
        msg="""
ಠ-> <code>{}</code>
ಠ-> <code>{}</code>
ಠ-> <code>{}</code>
ಠ-> <code>{}</code>
ಠ-> <code>{}</code>
ಠ-> <code>{}</code>
ಠ-> <code>{}</code>
ಠ-> <code>{}</code>
ಠ-> <code>{}</code>
ಠ-> <code>{}</code>""".format(aa,bb,cc,dd,ee,ff,gg,hh,ii,jj)
        update.message.reply_text(msg,reply_markup=reply_markup,parse_mode='HTML')
      if len(Loxd)==2:
        keyboard=[[InlineKeyboardButton("GENERAR", callback_data='{}'.format(args))]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        binf = list()
        binf.append(Loxd[0])
        obj = Tools()
        a=obj.ccgenFromList(binf)
        aa=str(a[0][0])+str(a[0][1])+str(a[0][2])+str(a[0][3])+str(a[0][4])+str(a[0][5])+str(a[0][6])+str(a[0][7])+str(a[0][8])+str(a[0][9])+str(a[0][10])+str(a[0][11])+str(a[0][12])+str(a[0][13])+str(a[0][14])+str(a[0][15])+"|"+str(Loxd[1])+"|"+str(a[0][20])+str(a[0][21])+"|"+str(a[0][23])+str(a[0][24])+str(a[0][25])
        bb=str(a[1][0])+str(a[1][1])+str(a[1][2])+str(a[1][3])+str(a[1][4])+str(a[1][5])+str(a[1][6])+str(a[1][7])+str(a[1][8])+str(a[1][9])+str(a[1][10])+str(a[1][11])+str(a[1][12])+str(a[1][13])+str(a[1][14])+str(a[1][15])+"|"+str(Loxd[1])+"|"+str(a[1][20])+str(a[1][21])+"|"+str(a[1][23])+str(a[1][24])+str(a[1][25])
        cc=str(a[2][0])+str(a[2][1])+str(a[2][2])+str(a[2][3])+str(a[2][4])+str(a[2][5])+str(a[2][6])+str(a[2][7])+str(a[2][8])+str(a[2][9])+str(a[2][10])+str(a[2][11])+str(a[2][12])+str(a[2][13])+str(a[2][14])+str(a[2][15])+"|"+str(Loxd[1])+"|"+str(a[2][20])+str(a[2][21])+"|"+str(a[2][23])+str(a[2][24])+str(a[2][25])
        dd=str(a[3][0])+str(a[3][1])+str(a[3][2])+str(a[3][3])+str(a[3][4])+str(a[3][5])+str(a[3][6])+str(a[3][7])+str(a[3][8])+str(a[3][9])+str(a[3][10])+str(a[3][11])+str(a[3][12])+str(a[3][13])+str(a[3][14])+str(a[3][15])+"|"+str(Loxd[1])+"|"+str(a[3][20])+str(a[3][21])+"|"+str(a[3][23])+str(a[3][24])+str(a[3][25])
        ee=str(a[4][0])+str(a[4][1])+str(a[4][2])+str(a[4][3])+str(a[4][4])+str(a[4][5])+str(a[4][6])+str(a[4][7])+str(a[4][8])+str(a[4][9])+str(a[4][10])+str(a[4][11])+str(a[4][12])+str(a[4][13])+str(a[4][14])+str(a[4][15])+"|"+str(Loxd[1])+"|"+str(a[4][20])+str(a[4][21])+"|"+str(a[4][23])+str(a[4][24])+str(a[4][25])
        ff=str(a[5][0])+str(a[5][1])+str(a[5][2])+str(a[5][3])+str(a[5][4])+str(a[5][5])+str(a[5][6])+str(a[5][7])+str(a[5][8])+str(a[5][9])+str(a[5][10])+str(a[5][11])+str(a[5][12])+str(a[5][13])+str(a[5][14])+str(a[5][15])+"|"+str(Loxd[1])+"|"+str(a[5][20])+str(a[5][21])+"|"+str(a[5][23])+str(a[5][24])+str(a[5][25])
        gg=str(a[6][0])+str(a[6][1])+str(a[6][2])+str(a[6][3])+str(a[6][4])+str(a[6][5])+str(a[6][6])+str(a[6][7])+str(a[6][8])+str(a[6][9])+str(a[6][10])+str(a[6][11])+str(a[6][12])+str(a[6][13])+str(a[6][14])+str(a[6][15])+"|"+str(Loxd[1])+"|"+str(a[6][20])+str(a[6][21])+"|"+str(a[6][23])+str(a[6][24])+str(a[6][25])
        hh=str(a[7][0])+str(a[7][1])+str(a[7][2])+str(a[7][3])+str(a[7][4])+str(a[7][5])+str(a[7][6])+str(a[7][7])+str(a[7][8])+str(a[7][9])+str(a[7][10])+str(a[7][11])+str(a[7][12])+str(a[7][13])+str(a[7][14])+str(a[7][15])+"|"+str(Loxd[1])+"|"+str(a[7][20])+str(a[7][21])+"|"+str(a[7][23])+str(a[7][24])+str(a[7][25])
        ii=str(a[8][0])+str(a[8][1])+str(a[8][2])+str(a[8][3])+str(a[8][4])+str(a[8][5])+str(a[8][6])+str(a[8][7])+str(a[8][8])+str(a[8][9])+str(a[8][10])+str(a[8][11])+str(a[8][12])+str(a[8][13])+str(a[8][14])+str(a[8][15])+"|"+str(Loxd[1])+"|"+str(a[8][20])+str(a[8][21])+"|"+str(a[8][23])+str(a[8][24])+str(a[8][25])
        jj=str(a[9][0])+str(a[9][1])+str(a[9][2])+str(a[9][3])+str(a[9][4])+str(a[9][5])+str(a[9][6])+str(a[9][7])+str(a[9][8])+str(a[9][9])+str(a[9][10])+str(a[9][11])+str(a[9][12])+str(a[9][13])+str(a[9][14])+str(a[9][15])+"|"+str(Loxd[1])+"|"+str(a[9][20])+str(a[9][21])+"|"+str(a[9][23])+str(a[9][24])+str(a[9][25])
        msg="""
ಠ-> <code>{}</code>
ಠ-> <code>{}</code>
ಠ-> <code>{}</code>
ಠ-> <code>{}</code>
ಠ-> <code>{}</code>
ಠ-> <code>{}</code>
ಠ-> <code>{}</code>
ಠ-> <code>{}</code>
ಠ-> <code>{}</code>
ಠ-> <code>{}</code>""".format(aa,bb,cc,dd,ee,ff,gg,hh,ii,jj)
        update.message.reply_text(msg,reply_markup=reply_markup,parse_mode='HTML')
      elif len(Loxd)==3:
        keyboard=[[InlineKeyboardButton("GENERAR", callback_data='{}'.format(args))]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        binf = list()
        binf.append(Loxd[0])
        obj = Tools()
        a=obj.ccgenFromList(binf)
        aa=str(a[0][0])+str(a[0][1])+str(a[0][2])+str(a[0][3])+str(a[0][4])+str(a[0][5])+str(a[0][6])+str(a[0][7])+str(a[0][8])+str(a[0][9])+str(a[0][10])+str(a[0][11])+str(a[0][12])+str(a[0][13])+str(a[0][14])+str(a[0][15])+"|"+str(Loxd[1])+"|"+str(Loxd[2])+"|"+str(a[0][23])+str(a[0][24])+str(a[0][25])
        bb=str(a[1][0])+str(a[1][1])+str(a[1][2])+str(a[1][3])+str(a[1][4])+str(a[1][5])+str(a[1][6])+str(a[1][7])+str(a[1][8])+str(a[1][9])+str(a[1][10])+str(a[1][11])+str(a[1][12])+str(a[1][13])+str(a[1][14])+str(a[1][15])+"|"+str(Loxd[1])+"|"+str(Loxd[2])+"|"+str(a[1][23])+str(a[1][24])+str(a[1][25])
        cc=str(a[2][0])+str(a[2][1])+str(a[2][2])+str(a[2][3])+str(a[2][4])+str(a[2][5])+str(a[2][6])+str(a[2][7])+str(a[2][8])+str(a[2][9])+str(a[2][10])+str(a[2][11])+str(a[2][12])+str(a[2][13])+str(a[2][14])+str(a[2][15])+"|"+str(Loxd[1])+"|"+str(Loxd[2])+"|"+str(a[2][23])+str(a[2][24])+str(a[2][25])
        dd=str(a[3][0])+str(a[3][1])+str(a[3][2])+str(a[3][3])+str(a[3][4])+str(a[3][5])+str(a[3][6])+str(a[3][7])+str(a[3][8])+str(a[3][9])+str(a[3][10])+str(a[3][11])+str(a[3][12])+str(a[3][13])+str(a[3][14])+str(a[3][15])+"|"+str(Loxd[1])+"|"+str(Loxd[2])+"|"+str(a[3][23])+str(a[3][24])+str(a[3][25])
        ee=str(a[4][0])+str(a[4][1])+str(a[4][2])+str(a[4][3])+str(a[4][4])+str(a[4][5])+str(a[4][6])+str(a[4][7])+str(a[4][8])+str(a[4][9])+str(a[4][10])+str(a[4][11])+str(a[4][12])+str(a[4][13])+str(a[4][14])+str(a[4][15])+"|"+str(Loxd[1])+"|"+str(Loxd[2])+"|"+str(a[4][23])+str(a[4][24])+str(a[4][25])
        ff=str(a[5][0])+str(a[5][1])+str(a[5][2])+str(a[5][3])+str(a[5][4])+str(a[5][5])+str(a[5][6])+str(a[5][7])+str(a[5][8])+str(a[5][9])+str(a[5][10])+str(a[5][11])+str(a[5][12])+str(a[5][13])+str(a[5][14])+str(a[5][15])+"|"+str(Loxd[1])+"|"+str(Loxd[2])+"|"+str(a[5][23])+str(a[5][24])+str(a[5][25])
        gg=str(a[6][0])+str(a[6][1])+str(a[6][2])+str(a[6][3])+str(a[6][4])+str(a[6][5])+str(a[6][6])+str(a[6][7])+str(a[6][8])+str(a[6][9])+str(a[6][10])+str(a[6][11])+str(a[6][12])+str(a[6][13])+str(a[6][14])+str(a[6][15])+"|"+str(Loxd[1])+"|"+str(Loxd[2])+"|"+str(a[6][23])+str(a[6][24])+str(a[6][25])
        hh=str(a[7][0])+str(a[7][1])+str(a[7][2])+str(a[7][3])+str(a[7][4])+str(a[7][5])+str(a[7][6])+str(a[7][7])+str(a[7][8])+str(a[7][9])+str(a[7][10])+str(a[7][11])+str(a[7][12])+str(a[7][13])+str(a[7][14])+str(a[7][15])+"|"+str(Loxd[1])+"|"+str(Loxd[2])+"|"+str(a[7][23])+str(a[7][24])+str(a[7][25])
        ii=str(a[8][0])+str(a[8][1])+str(a[8][2])+str(a[8][3])+str(a[8][4])+str(a[8][5])+str(a[8][6])+str(a[8][7])+str(a[8][8])+str(a[8][9])+str(a[8][10])+str(a[8][11])+str(a[8][12])+str(a[8][13])+str(a[8][14])+str(a[8][15])+"|"+str(Loxd[1])+"|"+str(Loxd[2])+"|"+str(a[8][23])+str(a[8][24])+str(a[8][25])
        jj=str(a[9][0])+str(a[9][1])+str(a[9][2])+str(a[9][3])+str(a[9][4])+str(a[9][5])+str(a[9][6])+str(a[9][7])+str(a[9][8])+str(a[9][9])+str(a[9][10])+str(a[9][11])+str(a[9][12])+str(a[9][13])+str(a[9][14])+str(a[9][15])+"|"+str(Loxd[1])+"|"+str(Loxd[2])+"|"+str(a[9][23])+str(a[9][24])+str(a[9][25])
        msg="""
ಠ-> <code>{}</code>
ಠ-> <code>{}</code>
ಠ-> <code>{}</code>
ಠ-> <code>{}</code>
ಠ-> <code>{}</code>
ಠ-> <code>{}</code>
ಠ-> <code>{}</code>
ಠ-> <code>{}</code>
ಠ-> <code>{}</code>
ಠ-> <code>{}</code>""".format(aa,bb,cc,dd,ee,ff,gg,hh,ii,jj)
        update.message.reply_text(msg,reply_markup=reply_markup,parse_mode='HTML')
      elif len(Loxd)==4:
        keyboard=[[InlineKeyboardButton("GENERAR", callback_data='{}'.format(args))]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        binf = list()
        binf.append(Loxd[0])
        obj = Tools()
        a=obj.ccgenFromList(binf)
        aa=str(a[0][0])+str(a[0][1])+str(a[0][2])+str(a[0][3])+str(a[0][4])+str(a[0][5])+str(a[0][6])+str(a[0][7])+str(a[0][8])+str(a[0][9])+str(a[0][10])+str(a[0][11])+str(a[0][12])+str(a[0][13])+str(a[0][14])+str(a[0][15])+"|"+str(Loxd[1])+"|"+str(Loxd[2])+"|"+str(Loxd[3])
        bb=str(a[1][0])+str(a[1][1])+str(a[1][2])+str(a[1][3])+str(a[1][4])+str(a[1][5])+str(a[1][6])+str(a[1][7])+str(a[1][8])+str(a[1][9])+str(a[1][10])+str(a[1][11])+str(a[1][12])+str(a[1][13])+str(a[1][14])+str(a[1][15])+"|"+str(Loxd[1])+"|"+str(Loxd[2])+"|"+str(Loxd[3])
        cc=str(a[2][0])+str(a[2][1])+str(a[2][2])+str(a[2][3])+str(a[2][4])+str(a[2][5])+str(a[2][6])+str(a[2][7])+str(a[2][8])+str(a[2][9])+str(a[2][10])+str(a[2][11])+str(a[2][12])+str(a[2][13])+str(a[2][14])+str(a[2][15])+"|"+str(Loxd[1])+"|"+str(Loxd[2])+"|"+str(Loxd[3])
        dd=str(a[3][0])+str(a[3][1])+str(a[3][2])+str(a[3][3])+str(a[3][4])+str(a[3][5])+str(a[3][6])+str(a[3][7])+str(a[3][8])+str(a[3][9])+str(a[3][10])+str(a[3][11])+str(a[3][12])+str(a[3][13])+str(a[3][14])+str(a[3][15])+"|"+str(Loxd[1])+"|"+str(Loxd[2])+"|"+str(Loxd[3])
        ee=str(a[4][0])+str(a[4][1])+str(a[4][2])+str(a[4][3])+str(a[4][4])+str(a[4][5])+str(a[4][6])+str(a[4][7])+str(a[4][8])+str(a[4][9])+str(a[4][10])+str(a[4][11])+str(a[4][12])+str(a[4][13])+str(a[4][14])+str(a[4][15])+"|"+str(Loxd[1])+"|"+str(Loxd[2])+"|"+str(Loxd[3])
        ff=str(a[5][0])+str(a[5][1])+str(a[5][2])+str(a[5][3])+str(a[5][4])+str(a[5][5])+str(a[5][6])+str(a[5][7])+str(a[5][8])+str(a[5][9])+str(a[5][10])+str(a[5][11])+str(a[5][12])+str(a[5][13])+str(a[5][14])+str(a[5][15])+"|"+str(Loxd[1])+"|"+str(Loxd[2])+"|"+str(Loxd[3])
        gg=str(a[6][0])+str(a[6][1])+str(a[6][2])+str(a[6][3])+str(a[6][4])+str(a[6][5])+str(a[6][6])+str(a[6][7])+str(a[6][8])+str(a[6][9])+str(a[6][10])+str(a[6][11])+str(a[6][12])+str(a[6][13])+str(a[6][14])+str(a[6][15])+"|"+str(Loxd[1])+"|"+str(Loxd[2])+"|"+str(Loxd[3])
        hh=str(a[7][0])+str(a[7][1])+str(a[7][2])+str(a[7][3])+str(a[7][4])+str(a[7][5])+str(a[7][6])+str(a[7][7])+str(a[7][8])+str(a[7][9])+str(a[7][10])+str(a[7][11])+str(a[7][12])+str(a[7][13])+str(a[7][14])+str(a[7][15])+"|"+str(Loxd[1])+"|"+str(Loxd[2])+"|"+str(Loxd[3])
        ii=str(a[8][0])+str(a[8][1])+str(a[8][2])+str(a[8][3])+str(a[8][4])+str(a[8][5])+str(a[8][6])+str(a[8][7])+str(a[8][8])+str(a[8][9])+str(a[8][10])+str(a[8][11])+str(a[8][12])+str(a[8][13])+str(a[8][14])+str(a[8][15])+"|"+str(Loxd[1])+"|"+str(Loxd[2])+"|"+str(Loxd[3])
        jj=str(a[9][0])+str(a[9][1])+str(a[9][2])+str(a[9][3])+str(a[9][4])+str(a[9][5])+str(a[9][6])+str(a[9][7])+str(a[9][8])+str(a[9][9])+str(a[9][10])+str(a[9][11])+str(a[9][12])+str(a[9][13])+str(a[9][14])+str(a[9][15])+"|"+str(Loxd[1])+"|"+str(Loxd[2])+"|"+str(Loxd[3])
        msg="""
ಠ-> <code>{}</code>
ಠ-> <code>{}</code>
ಠ-> <code>{}</code>
ಠ-> <code>{}</code>
ಠ-> <code>{}</code>
ಠ-> <code>{}</code>
ಠ-> <code>{}</code>
ಠ-> <code>{}</code>
ಠ-> <code>{}</code>
ಠ-> <code>{}</code>""".format(aa,bb,cc,dd,ee,ff,gg,hh,ii,jj)
        update.message.reply_text(msg,reply_markup=reply_markup,parse_mode='HTML')
      elif len(Loxd)>4:
        msg="<b>formato invalido</b>"
        update.message.reply_text(msg,parse_mode='HTML')
    else:
      msg="<b>RECUERDE QUE EL COMANDO VA SEGUIDO DE UN BIN {} </b>".format(user)
      update.message.reply_text(msg,parse_mode='HTML')
  def bincheck(update,context):
    keyboard=[[InlineKeyboardButton("NEW BIN", callback_data='bincheck')]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    user = update.message.from_user.username
    args=context.args
    if len(args)==1:
        bin=str(args[0])
        if len(bin) >= 6:
          bin= str(bin)
        try:
          bin= bin.replace("x","")
          bin= bin.replace("X","")
          bin= bin.split("|")[0]
        except:
          pass
        bin = str(re.sub('([a-zA-Z]){1,}', '', bin))
        lenLuhn=len(str(bin))
        sinccheck=bin[:16]
        bin = str(bin)
        bin = re.sub('([a-zA-Z]){1,}', '', bin)
        try:
          unks = 0
          url='https://lookup.binlist.net/'+str(bin)
          try:
            page = requests.get(url)
            page.raise_for_status()
          except:
            pass
          page= page.content.decode()
          dic = json.loads(page)
          try:
            marca=dic['scheme']
          except:
            marca='DESCONOCIDO'
          try:
            tipo=dic['type']
          except:
            tipo='DESCONOCIDO'
          try:
            brnd=dic['brand']
          except:
            brnd='DESCONOCIDO'
          try:
            el_alpha=dic['country']['alpha2']
          except:
            el_alpha='DESCONOCIDO'
          try:
            pais=dic['country']['name']
          except:
            pais='DESCONOCIDO'
          try:
            emote=dic['country']['emoji']
          except:
            emote='DESCONOCIDO'
          try:
            tipo_moneda=dic['country']['currency']
          except:
            tipo_moneda='DESCONOCIDO'
          try:
            bank_name=dic['bank']['name']
          except:
            bank_name='DESCONOCIDO'
          try:
            bank_url=dic['bank']['url']
          except:
            bank_url='DESCONOCIDO'
          try:
            bank_phone=dic['bank']['phone']
          except:
            bank_phone='DESCONOCIDO'
          ibba_2="""
ಠ-> Bin : <code>{}</code> {}

ಠ-> Marca : <b><u>{}</u></b>

ಠ-> Tipo de tarjeta: <b><u>{}</u></b>

ಠ-> Nivel de tarjeta: <b><u>{}</u></b>

ಠ-> Banco : <b><u>{}</u></b>

ಠ-> País : <b><u>{}</u></b> - <b><u>{}</u></b> - 💲 <b><u>{}</u></b>

ಠ-> URL Banco : {}

ಠ-> BY : @{} """.format(bin,emote,marca,tipo,brnd,bank_name,pais,el_alpha,tipo_moneda,bank_url,user)
        except:
          ibba_2="BIN INVALIDO"
        update.message.reply_text(ibba_2,reply_markup=reply_markup,parse_mode='HTML')
    else:
      ibba_2="{} LO QUE ME PIDIO ES INVALIDO".format(user)
    update.message.reply_text(ibba_2,parse_mode='HTML')
  def find(update,context):
    user = update.message.from_user.username
    args=context.args
    if len(args)>0:
          api = "http://ip-api.com/json/"+str(args[0])
          response=requests.get(api)
          response_json=response.json()
          valida=response_json['status']
          if valida=="success":
              IP=response_json['query']
              ASS=response_json['isp']
              ORG=response_json['org']
              CIUDAD=response_json['city']
              sa=response_json['region']
              pepe=response_json['regionName']
              nose=response_json['lat']
              asd=response_json['lon']
              sss=response_json['timezone']
              pene=response_json['zip']
              paisa=response_json['country']
              asssd=response_json['as']
              msg="""
  *Target:*

  `{}`

  *ISP:*

  `{}`

  *AS:*

  `{}`

  *Organizacion:*

  `{}`

  *Pais:*

  `{}`

  *Ciudad:*

  `{}`

  *Region:*

  `{}`

  *Region nombre:*

  `{}`

  *latitud:*

  `{}`

  *Longitud:*

  `{}`

  *Timezone:*

  `{}`

  *Codigo Postal:*

  `{}`

  BY : `{}`   """.format(IP,ASS,asssd,ORG,paisa,CIUDAD,sa,pepe,nose,asd,sss,pene,user)


          else:
            msg="*IP NO VALIDA*"
    else:
          msg="*IP NO VALIDA*"
    update.message.reply_text(msg,parse_mode='MarkdownV2')
  def extrap(update,context):
    user = update.message.from_user.username
    args=context.args
    if len(args)>0:
      if len(args)==1:
        if len(args[0])==16:
          cc1=str(args[0])
          if cc1.isdigit()==True:
            mult1=int(cc1[0])*int(cc1[8])
            mult2=int(cc1[1])*int(cc1[9])
            mult3=int(cc1[2])*int(cc1[10])
            mult4=int(cc1[3])*int(cc1[11])
            mult5=int(cc1[4])*int(cc1[12])
            mult6=int(cc1[5])*int(cc1[13])
            mult7=int(cc1[6])*int(cc1[14])
            mult8=int(cc1[7])*int(cc1[15])
            cc2=str(cc1[0])+str(cc1[1])+str(cc1[2])+str(cc1[3])+str(cc1[4])+str(cc1[5])+str(cc1[6])+str(cc1[7])+str(int(mult1))+str(int(mult2))+str(int(mult3))+str(int(mult4))+str(int(mult5))+str(int(mult6))+str(int(mult7))+str(int(mult8))
            a=0
            asd=list()
            for i in cc1:
              if i == cc2[a]:
                asd.append(i)
              else:
                asd.append("x")
              a+=1
            res_one=str(asd[0])+str(asd[1])+str(asd[2])+str(asd[3])+str(asd[4])+str(asd[5])+str(asd[6])+str(asd[7])+str(asd[8])+str(asd[9])+str(asd[10])+str(asd[11])+str(asd[12])+str(asd[13])+str(asd[14])+str(asd[15])
            mult1=int(cc1[0])*int(cc1[1])
            mult2=int(cc1[1])*int(cc1[2])
            mult3=int(cc1[2])*int(cc1[3])
            mult4=int(cc1[3])*int(cc1[4])
            mult5=int(cc1[4])*int(cc1[5])
            mult6=int(cc1[5])*int(cc1[6])
            mult7=int(cc1[6])*int(cc1[7])
            cc2=str(cc1[0])+str(cc1[1])+str(cc1[2])+str(cc1[3])+str(cc1[4])+str(cc1[5])+str(cc1[6])+str(cc1[7])+str(int(mult1))+str(int(mult2))+str(int(mult3))+str(int(mult4))+str(int(mult5))+str(int(mult6))+str(int(mult7))
            a=0
            osd=list()
            for i in cc1:
              if i == cc2[a]:
                osd.append(i)
              else:
                osd.append("x")
              a+=1
            res_two=str(osd[0])+str(osd[1])+str(osd[2])+str(osd[3])+str(osd[4])+str(osd[5])+str(osd[6])+str(osd[7])+str(osd[8])+str(osd[9])+str(osd[10])+str(osd[11])+str(osd[12])+str(osd[13])+str(osd[14])+str(osd[15])
            msg="""
*CC EXTRAPOLADA CORRECTAMENTE*

*PRIMER RESULTADO :* `{}`

*SEGUNDO RESULTADO :* `{}`

*BY :* `{}`""".format(res_one,res_two,user)
          else:
            extras=[]
            obj = Tools()
            ass=[]
            ass.append(cc1)
            l=obj.ccgenFromList(ass)
            for a in l:
              cc1=str(a[0])+str(a[1])+str(a[2])+str(a[3])+str(a[4])+str(a[5])+str(a[6])+str(a[7])+str(a[8])+str(a[9])+str(a[10])+str(a[11])+str(a[12])+str(a[13])+str(a[14])+str(a[15])
              mult1=int(cc1[0])*int(cc1[8])
              mult2=int(cc1[1])*int(cc1[9])
              mult3=int(cc1[2])*int(cc1[10])
              mult4=int(cc1[3])*int(cc1[11])
              mult5=int(cc1[4])*int(cc1[12])
              mult6=int(cc1[5])*int(cc1[13])
              mult7=int(cc1[6])*int(cc1[14])
              mult8=int(cc1[7])*int(cc1[15])
              cc2=str(cc1[0])+str(cc1[1])+str(cc1[2])+str(cc1[3])+str(cc1[4])+str(cc1[5])+str(cc1[6])+str(cc1[7])+str(int(mult1))+str(int(mult2))+str(int(mult3))+str(int(mult4))+str(int(mult5))+str(int(mult6))+str(int(mult7))+str(int(mult8))
              a=0
              osd=list()
              for i in cc1:
                if i == cc2[a]:
                  osd.append(i)
                else:
                  osd.append("x")
                a+=1
              res_two=str(osd[0])+str(osd[1])+str(osd[2])+str(osd[3])+str(osd[4])+str(osd[5])+str(osd[6])+str(osd[7])+str(osd[8])+str(osd[9])+str(osd[10])+str(osd[11])+str(osd[12])+str(osd[13])+str(osd[14])+str(osd[15])
              extras.append(res_two)
            aa=str(extras[0])
            bb=str(extras[1])
            cc=str(extras[2])
            dd=str(extras[3])
            ee=str(extras[4])
            ff=str(extras[5])
            gg=str(extras[6])
            hh=str(extras[7])
            ii=str(extras[8])
            jj=str(extras[9])
            msg="""
*EXTRAPOLADOS BY LUHN LISTOS :*

`{}`
`{}`
`{}`
`{}`
`{}`
`{}`
`{}`
`{}`
`{}`
`{}`

*BY : *`{}`""".format(aa,bb,cc,dd,ee,ff,gg,hh,ii,jj,user)
        elif len(args[0])==15:
          cc=str(args[0])
          print(cc)
          mult1=int(cc[0])*int(cc[8])
          mult2=int(cc[1])*int(cc[9])
          mult3=int(cc[2])*int(cc[10])
          mult4=int(cc[3])*int(cc[11])
          mult5=int(cc[4])*int(cc[12])
          mult6=int(cc[5])*int(cc[13])
          mult7=int(cc[13])*int(cc[14])
          ccs=str(cc[0])+str(cc[1])+str(cc[2])+str(cc[3])+str(cc[4])+str(cc[5])+str(int(mult1))+str(int(mult2))+str(int(mult3))+str(int(mult4))+str(int(mult5))+str(int(mult6))+str(int(mult7))
          print(ccs)
          osd=list()
          a=0
          for i in range(0,14):
            if cc[a] == ccs[a]:
              osd.append(cc[a])
            else:
              osd.append("x")
            a+=1
          res=str(osd[0])+str(osd[1])+str(osd[2])+str(osd[3])+str(osd[4])+str(osd[5])+str(osd[6])+str(osd[7])+str(osd[8])+str(osd[9])+str(osd[10])+str(osd[11])+str(osd[12])+str(osd[13])
          mult1=int(cc[0])*int(cc[1])
          mult2=int(cc[1])*int(cc[2])
          mult3=int(cc[2])*int(cc[3])
          mult4=int(cc[3])*int(cc[4])
          mult5=int(cc[4])*int(cc[5])
          mult6=int(cc[5])*int(cc[6])
          mult7=int(cc[6])*int(cc[7])
          ccs=str(cc[0])+str(cc[1])+str(cc[2])+str(cc[3])+str(cc[4])+str(cc[5])+str(int(mult1))+str(int(mult2))+str(int(mult3))+str(int(mult4))+str(int(mult5))+str(int(mult6))+str(int(mult7))
          asd=list()
          a=0
          for i in range(0,15):
            if cc[a] ==ccs[a]:
              asd.append(cc[a])
            else:
              asd.append("x")
            a+=1
          res_two=str(asd[0])+str(asd[1])+str(asd[2])+str(asd[3])+str(asd[4])+str(asd[5])+str(asd[6])+str(asd[7])+str(asd[8])+str(asd[9])+str(asd[10])+str(asd[11])+str(asd[12])+str(asd[13])
          msg="""
*CC EXTRAPOLADA CORRECTAMENTE*

*PRIMER RESULTADO : *`{}`

*SEGUNDO RESULTADO : *`{}`

*BY : *`{}`""".format(res,res_two,user)
          update.message.reply_text(msg,parse_mode='MarkdownV2')
        else:
          msg="*{} RECUERDE QUE DEBE DE METER UNA CC VALIDA*".format(user)
      elif len(args)==2:
        cc=str(args[0])
        bins=list()
        binf=str(args[1])
        bins.append(binf)
        if len(args[0])==16 and len(args[1])==16 and args[0].isdigit()==True and args[1].isdigit()==True:
          cc1=str(args[0])
          cc2=str(args[1])
          suma_1=int(cc1[9])+int(cc1[10])
          suma_2=int(cc2[9])+int(cc2[10])
          div_1=round(int(suma_1)/2)*5
          div_2=round(int(suma_2)/2)*5
          rem=int(div_1)+int(div_2)
          bin_1=str(cc1[0])+str(cc1[1])+str(cc1[2])+str(cc1[3])+str(cc1[4])+str(cc1[5])+str(cc1[6])+str(cc1[7])+str(rem)+'xxxxxx'	
          lista=[]
          lista.append(bin_1)
          obj = Tools()
          a = obj.ccgenFromList(lista)
          lol = str(a[0])
          msg_1=str(lol[0])+str(lol[1])+str(lol[2])+str(lol[3])+str(lol[4])+str(lol[5])+str(lol[6])+'x'+str(lol[8])+str(lol[9])+'xx'+str(lol[12])+str(lol[13])+'x'+str(lol[15])
          mult1=int(cc2[0])*int(cc2[8])
          mult2=int(cc2[1])*int(cc2[9])
          mult3=int(cc2[2])*int(cc2[10])
          mult4=int(cc2[3])*int(cc2[11])
          mult5=int(cc2[4])*int(cc2[12])
          mult6=int(cc2[5])*int(cc2[13])
          mult7=int(cc2[6])*int(cc2[14])
          mult8=int(cc2[7])*int(cc2[15])
          ccl=str(cc2[0])+str(cc2[1])+str(cc2[2])+str(cc2[3])+str(cc2[4])+str(cc2[5])+str(cc2[6])+str(cc2[7])+str(int(mult1))+str(int(mult2))+str(int(mult3))+str(int(mult4))+str(int(mult5))+str(int(mult6))+str(int(mult7))+str(int(mult8))
          e=0
          osd=[]
          for i in cc1:
            if i == str(ccl[e]):
              osd.append(ccl[e])
            else:
              osd.append("x")
            e+=1
          msg_2=str(osd[0])+str(osd[1])+str(osd[2])+str(osd[3])+str(osd[4])+str(osd[5])+str(osd[6])+str(osd[7])+str(osd[8])+str(osd[9])+str(osd[10])+str(osd[11])+str(osd[12])+str(osd[13])+str(osd[14])+str(osd[15])
          mult1=int(cc2[0])*int(cc2[1])
          mult2=int(cc2[1])*int(cc2[2])
          mult3=int(cc2[2])*int(cc2[3])
          mult4=int(cc2[3])*int(cc2[4])
          mult5=int(cc2[4])*int(cc2[5])
          mult6=int(cc2[5])*int(cc2[6])
          mult7=int(cc2[6])*int(cc2[7])
          cc=str(cc2[0])+str(cc2[1])+str(cc2[2])+str(cc2[3])+str(cc2[4])+str(cc2[5])+str(cc2[6])+str(cc2[7])+str(int(mult1))+str(int(mult2))+str(int(mult3))+str(int(mult4))+str(int(mult5))+str(int(mult6))+str(int(mult7))
          o=0
          sd=[]
          for i in cc1:
            if i == str(cc[o]):
              sd.append(i)
            else:
              sd.append("x")
            o+=1
          msg_3=str(sd[0])+str(sd[1])+str(sd[2])+str(sd[3])+str(sd[4])+str(sd[5])+str(sd[6])+str(sd[7])+str(sd[8])+str(sd[9])+str(sd[10])+str(sd[11])+str(sd[12])+str(sd[13])+str(sd[14])+str(sd[15])        
          pol=0
          so=list()
          for i in cc1:
            if i == cc2[pol]:
              so.append(i)
            else:
              so.append("x")
            pol+=1
          msg_4=str(so[0])+str(so[1])+str(so[2])+str(so[3])+str(so[4])+str(so[5])+str(so[6])+str(so[7])+str(so[8])+str(so[9])+str(so[10])+str(so[11])+str(so[12])+str(so[13])+str(so[14])+str(so[15])
          msg="""
*EXTRAPOLADO DE LAS CCS COMPLETO*

*PRIMER RESULTADO : *`{}`

*SEGUNDO RESULTADO : *`{}`

*TERCER RESULTADO : *`{}`

*CUARTO RESULTADO : *`{}`

*BY : *`{}`""".format(msg_1,msg_2,msg_3,msg_4,user)
        elif cc.isdigit()==True:
          if len(cc)==16:
            if binf.isdigit()==False:
              binf = bins
              obj = Tools()
              a=obj.ccgenFromList(binf)
              cc_1=str(a[0][0])+str(a[0][1])+str(a[0][2])+str(a[0][3])+str(a[0][4])+str(a[0][5])+str(a[0][6])+"x"+str(a[0][8])+"x"+str(a[0][10])+"x"+str(cc[12])+str(cc[13])+str(cc[14])+str(cc[15])
              cc_2=str(a[1][0])+str(a[1][1])+str(a[1][2])+str(a[1][3])+str(a[1][4])+str(a[1][5])+str(a[1][6])+"x"+str(a[1][8])+"x"+str(a[1][10])+"x"+str(cc[12])+str(cc[13])+str(cc[14])+str(cc[15])
              new=list()
              new_2=list()
              new.append(cc_1)
              new_2.append(cc_2)
              b=obj.ccgenFromList(new)
              c=obj.ccgenFromList(new_2)
              cc1=round(((int(str(b[0][9]))+int(str(b[0][10])))/2)*5)
              cc2=round(((int(str(c[0][9]))+int(str(c[0][10])))/2)*5)
              final=int(str(cc1))+int(str(cc2))
              res_1=str(b[0][0])+str(b[0][1])+str(b[0][2])+str(b[0][3])+str(b[0][4])+str(b[0][5])+str(b[0][6])+str(b[0][7])+str(int(final))+"xxxxxx"
              res_2=str(c[0][0])+str(c[0][1])+str(c[0][2])+str(c[0][3])+str(c[0][4])+str(c[0][5])+str(c[0][6])+str(c[0][7])+str(int(final))+"xxxxxx"
              msg="""
*CC EXTRAPOLADA CORRECTAMENTE :*

`{}`

`{}`

*BY :* `{}`""".format(res_1,res_2,user)
        elif len(args[0])==14 and len(args[1])==14:
          msg="`{}` *DISCULPE ,AÚN ESTÁ EN DE DESARROLLO*".format(user)
        else:
          msg="`{}` *RECUERDA QUE DEBES DE INGRESAR CC'S VALIDAS*".format(user)
      elif len(args)==3:
        if len(args[0])==16 and len(args[1])==16 and len(args[2])==16:
          msg="`{}` *DISCULPE ,AÚN ESTÁ EN DE DESARROLLO*".format(user)
        else:
          msg="`{}` RECUERDA QUE DEBES DE INGRESAR CC'S VALIDAS".format(user)
      elif len(args) > 3:
        msg="`{}` *CANTIDAD NO VALIDA*".format(user)
    else:
      msg="`{}` *Debes usar el comando acompañado de una o dos cc's, lives o bins generados*".format(user)
    update.message.reply_text(msg,parse_mode='MarkdownV2')
  def info(update,context):
  	user = update.message.from_user.username
  	first_name=update.message.from_user.first_name
  	msg="""
<b>NOMBRE DEL BOT : </b><u><i>{}</i></u>

<b>Version : </b><u><i>BETA</i></u>

<b>Sexo :</b> <u>FEMENINO 7W7</u>

<b>OWNER : </b><u><i>{}</i></u>

<b>USER : </b><u><i>{}</i></u>

<b>FIRST NAME : </b><u><i>{}</i></u>

<b>GRACIAS POR USAR EL BOT</b>""".format(names,owner,user,first_name)
  	update.message.reply_text(msg,parse_mode="HTML")
  def crearB(update,context):
    user = update.message.from_user.username
    args=context.args
    if len(args)==0:
        keyboard=[[InlineKeyboardButton("CREAR", callback_data='crearnewbin')]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        a=randint(4,6)
        b=randint(4,6)
        c=randint(0,9)
        d=randint(0,9)
        e=randint(0,9)
        f=randint(0,13)
        bin=str(int(a))+str(int(b))+str(int(c))+str(int(d))+str(int(d))+str(int(e))+str(int(f))
        if len(bin) >= 6:
          bin= str(bin)
        try:
          bin= bin.replace("x","")
          bin= bin.replace("X","")
          bin= bin.split("|")[0]
        except:
          pass
        bin = str(re.sub('([a-zA-Z]){1,}', '', bin))
        lenLuhn=len(str(bin))
        sinccheck=bin[:16]
        bin = str(bin)
        bin = re.sub('([a-zA-Z]){1,}', '', bin)
        try:
          unks = 0
          url='https://lookup.binlist.net/'+str(bin)
          try:
            page = requests.get(url)
            page.raise_for_status()
          except:
            pass
          page= page.content.decode()
          dic = json.loads(page)
          try:
            marca=dic['scheme']
          except:
            marca='DESCONOCIDO'
          try:
            tipo=dic['type']
          except:
            tipo='DESCONOCIDO'
          try:
            brnd=dic['brand']
          except:
            brnd='DESCONOCIDO'
          try:
            el_alpha=dic['country']['alpha2']
          except:
            el_alpha='DESCONOCIDO'
          try:
            pais=dic['country']['name']
          except:
            pais='DESCONOCIDO'
          try:
            emote=dic['country']['emoji']
          except:
            emote='DESCONOCIDO'
          try:
            tipo_moneda=dic['country']['currency']
          except:
            tipo_moneda='DESCONOCIDO'
          try:
            bank_name=dic['bank']['name']
          except:
            bank_name='DESCONOCIDO'
          try:
            bank_url=dic['bank']['url']
          except:
            bank_url='DESCONOCIDO'
          try:
            bank_phone=dic['bank']['phone']
          except:
            bank_phone='DESCONOCIDO'
          ibba_2="""
ಠ-> Bin : <code>{}</code> {}

ಠ-> Marca : <b><u>{}</u></b>

ಠ-> Tipo de tarjeta: <b><u>{}</u></b>

ಠ-> Nivel de tarjeta: <b><u>{}</u></b>

ಠ-> Banco : <b><u>{}</u></b>

ಠ-> País : <b><u>{}</u></b> - <b><u>{}</u></b> - 💲 <b><u>{}</u></b>

ಠ-> URL Banco : <b><u>{}</u></b>""".format(bin,emote,marca,tipo,brnd,bank_name,pais,el_alpha,tipo_moneda,bank_url,user)
        except:
          ibba_2="Mala suerte, reintenta de nuevo :)"
        update.message.reply_text(ibba_2,reply_markup=reply_markup,parse_mode='HTML')
    else:
      ibba_2="{} LO QUE ME PIDIO ES INVALIDO".format(user)
      update.message.reply_text(ibba_2,parse_mode='HTML')
  def crearib(update,context):
    user=update.message.from_user.username
    args=context.args
    if len(args)==0:
      ibba=IbanNew()
      ibba_1=ibba.IbanX()
      ibba_3=ibba.msg
      ibba_2="""
{}

BY : <b>@{}</b>""".format(ibba_3,user)
    else:
      ibba_2="LO QUE ME PIDIO ES INVALIDO"
    update.message.reply_text(ibba_2,parse_mode="HTML")
  def help(update,context):
    user = update.message.from_user.username
    msg="""
ಠ--------------ಠ Comandos ಠ--------------ಠ
-> /crearb - <b>Crea un bin.</b>
-> /crearib - <b>Crea una Iban.</b>
-> /extrap - <b>Extrapola.</b>
-> /find - <b>Busca información de una IP.</b>
-> /genera - <b>Genera un Bin.</b>
-> /bincheck - <b>Verifica si el Bin es válido.</b>
-> /info - <b>Información del Bot y del Grupo</b>
ಠ-----------------------ಠ-------------------------ಠ"""
    update.message.reply_text(msg,parse_mode="HTML")
  def gay(update,context):
    user=update.message.from_user.username
    args=context.args
    valor=randint(0,100)
    if len(args)==0:
      msg="⚠️ @{} es {}%  gay 🏳️‍🌈".format(user,valor)
    else:
      persona=str(args[0])
      msg="⚠️ {} es {}%  gay 🏳️‍🌈".format(persona,valor)
    update.message.reply_text(msg)
  def nepe(update,context):
    user=update.message.from_user.username
    args=context.args
    valor=randint(0,100)
    if len(args)==0:
      msg="⚠️ el pene de @{} es de {}cm 😳".format(user,valor)
    else:
      persona=str(args[0])
      msg="⚠️ el pene de {} es de {}cm 😳".format(persona,valor)
    update.message.reply_text(msg)
  def WelcomeMSG(update,context):
    bot=context.bot
    chatD=update.message.chat_id
    updateMSG=getattr(update,"message",None)
    for user in updateMSG.new_chat_members:
      username=user.username
    msg="""
BIENVENIDO MI PANA @{}""".format(username)
    bot.sendMessage(text=msg,chat_id=chatD)
  def simp(update,context):
    user=update.message.from_user.username
    bot=context.bot
    chat_id=update.message.chat_id
    args=context.args
    if len(args) == 1:
      simp=str(args[0])
      with open("sticker.webp","rb") as sticker_file:
        bot.sendSticker(chat_id=chat_id,sticker=sticker_file)
        bot.sendMessage(
          chat_id=chat_id,
          text="{} <b>alto simp que eres.</b>".format(simp),
          parse_mode="HTML")
    elif len(args) == 0:
      with open("sticker.webp","rb") as sticker_file:
        bot.sendSticker(chat_id=chat_id,sticker=sticker_file)
        bot.sendMessage(
          chat_id=chat_id,
          text="@{} <b>alto simp que eres.</b>".format(user),
          parse_mode="HTML")
    elif len(args) == 2:
      simp=str(args[0])
      pro=str(args[1])
      with open("sticker.webp","rb") as sticker_file:
        bot.sendSticker(chat_id=chat_id,sticker=sticker_file)
        bot.sendMessage(
          chat_id=chat_id,
          text="{} <b>alto simp de</b> {} <b>que eres.</b>".format(simp,pro),
          parse_mode="HTML")
  def insultar_a(update,context):
    bot=context.bot
    user=update.message.from_user.username
    chat_id=update.message.chat_id
    args=context.args
    if len(args)==1:
      usr=str(args[0])
      lista_de_insultos=[
      "{} <b>calla cachera</b>".format(usr),
      "{} <b>eres tan pro que sacas napster</b>".format(usr),
      "{} <b>te sobran los cromosomas eh?</b>".format(usr),
      "{} <b>cuidado se te suba lo gei</b>".format(usr),
      "{} <b>de bolon pinpon eres un huevon</b>".format(usr),
      "{} <b>me parece que tu vieja es fujimorista</b>".format(usr)]
      msg=choice(lista_de_insultos)
      bot.sendMessage(
        chat_id=chat_id,
        text=msg,
        parse_mode="HTML"
      )
    elif len(args)==0:
      usr=user
      lista_de_insultos=[
      "@{} <b>calla cachera</b>".format(usr),
      "@{} <b>eres tan pro que sacas napster</b>".format(usr),
      "@{} <b>te sobran los cromosomas eh?</b>".format(usr),
      "@{} <b>cuidado se te suba lo gei</b>".format(usr),
      "@{} <b>de bolon pinpon eres un huevon</b>".format(usr),
      "@{} <b>me parece que tu vieja es fujimorista</b>".format(usr)]
      msg=choice(lista_de_insultos)
      bot.sendMessage(
        chat_id=chat_id,
        text=msg,
        parse_mode="HTML"
      )
    else:
      msg="@{} <b>el comando va acompañado de un solo usuario o comando solo pero no más</b>"
      update.message.reply_text(msg,parse_mode="HTML")
  def prueba(update,context):
    msg="""
<b>bold</b>, <strong>bold</strong>
<i>italic</i>, <em>italic</em>
<u>underline</u>, <ins>underline</ins>
<s>strikethrough</s>, <strike>strikethrough</strike>, <del>strikethrough</del>
<b>bold <i>italic bold <s>italic bold strikethrough</s> <u>underline italic bold</u></i> bold</b>
<a href="http://www.example.com/">inline URL</a>
<a href="tg://user?id=123456789">inline mention of a user</a>
<code>inline fixed-width code</code>
<pre>pre-formatted fixed-width code block</pre>
<pre><code class="language-python">pre-formatted fixed-width code block written in the Python programming language</code></pre>"""
    update.message.reply_text(msg,parse_mode="HTML")
  dispatcher.add_handler(CommandHandler("insultar_a",insultar_a))
  dispatcher.add_handler(CommandHandler("simp",simp))
  dispatcher.add_handler(MessageHandler(Filters.status_update.new_chat_members,WelcomeMSG))
  dispatcher.add_handler(CommandHandler("nepe",nepe))
  dispatcher.add_handler(CommandHandler("gay",gay))
  dispatcher.add_handler(CommandHandler("help",help))
  dispatcher.add_handler(CommandHandler("start",start))
  dispatcher.add_handler(CommandHandler("crearB",crearB))
  dispatcher.add_handler(CommandHandler("crearib",crearib))
  dispatcher.add_handler(CommandHandler("info",info))
  dispatcher.add_handler(CommandHandler("extrap",extrap))
  dispatcher.add_handler(CommandHandler("find",find))
  dispatcher.add_handler(CommandHandler("bincheck",bincheck))
  dispatcher.add_handler(CommandHandler('genera',genera))
  dispatcher.add_handler(CallbackQueryHandler(button))
  updater.start_polling()
def guardar(ag,vv):
  file=open("documents/{}.txt".format(vv),"w")
  file.write(ag)
  file.close()
def main():
  group_name=open("documents/name.txt","r")
  group=group_name.readlines()
  group_name.close()
  owner_name=open("documents/owner.txt","r")
  owner=owner_name.readlines()
  owner_name.close()
  bot_name=open("documents/bot.txt","r")
  bot=bot_name.readlines()
  bot_name.close()
  token_val=open("documents/token.txt","r")
  token=token_val.readlines()
  token_val.close()
  if len(group)==0:
    Group=input("\033[4;33mingrese el nombre de su grupo :\033[0;m ")
    guardar(Group,"name")
  else:
    Group=group[0]
  if len(owner)==0:
    Owner=input("\033[4;33mingrese su nombre :\033[0;m ")
    guardar(Owner,"owner")
  else:
    Owner=owner[0]
  if len(bot)==0:
    Bot=input("\033[4;33mingrese el nombre del bot :\033[0;m ")
    guardar(Bot,"bot")
  else:
    Bot=bot[0]
  if len(token)==0:
    Token=input("\033[4;33mingrese el token :\033[0;m ")
    guardar(Token,"token")
  else:
    Token=token[0]
  process(Group,Bot,Owner,Token)
main()
