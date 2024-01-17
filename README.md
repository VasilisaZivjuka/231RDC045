# 231RDC045 skolnieces projekta darbs
  Kā visiem dtorspēlētājiem, tā arī man, patīk dažreiz uzspēlēt onlain spēlēs "klikerus", kas pēc savas būtības izskatās kā lieka laika tērēšana, bet dažreiz apakšspēles sižets ir tik aizraujošs, ka gribās tomēr pabeigt. Tāpēc es jau sen aizdomājos par "klikera" izveidošanu.

  Nedaudz par izstrādes procesu:
  Vispirms es gribēju automatizēt vienas konkrētas spēles gaitu, bet izmantojos 'selenium' bibleotēku nekādīgi nevarēje tikt pie atsevišķiem elementiem spēles laukumā (tos nebija HTML kodā), tāpēc aizdomājos par kursora atrašanas vietu un to izmantošanu tālākāja procesā. Es sāku pētīt un vairāk lasīt par bibliotēku 'mouse', kur parādās iespēja ar vienu rindiņu iedarbināt klikšķi. Tālāk radijās problēma ar komandas iedarbināšanu (muļķīgi likt time.sleep(..), jo nav zināms cik ilgu laiku terēs spēlētājs uz to aktivāciju), tāpēc prātā iešaujās ideja par karstām pogām jeb 'hotkey'. Izrādās kā biblieotēka 'keyboard' dod iespēju pašam izveidot tādus. Biju priecīgi pārsteigta, jo nezināju, ka to izdarīt ir tik viegli.
  Galu galā izveidoju divus failus. Vienā ar vārdu "CLICK.py" var apskatīt tikai klikera darbību. 
