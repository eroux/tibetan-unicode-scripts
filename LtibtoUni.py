# -*- coding: utf-8 -*-
# The LtibtoUni script
# copyright 2013 © Elie Roux <elie.roux@telecom-bretagne.eu>
#
# LtibtoUni is under the Creative Commons CC0 license, which is as close to 
# public domain as possible in the country of the authors.
# See the full text [1] or the FAQ [2].
# 
# [1]: http://creativecommons.org/publicdomain/zero/1.0/legalcode
# [2]: http://wiki.creativecommons.org/CC0
#
# This script is for LibreOffice, it translates the selected input encoded in
# LTibetan font encoding into Unicode.

ltibUniTab = {' ':u" ", u'!':u"།", u'#':u"ི", u'$':u"ུ", u'%':u"ུ", u'&':u"ུ", u'\'':u"ཧྲ", u'(':u"ོ", u')':u"༄༅", u'*':u"ེ", u'+':u"ྃ", u',':u"", u'-':u"་", u'.':u"ཕ༹", u'/':u"ཝ", u'0':u"༠", u'1':u"༡", u'2':u"༢", u'3':u"༣", u'4':u"༤", u'5':u"༥", u'6':u"༦", u'7':u"༧", u'8':u"༨", u'9':u"༩", u':':u"ཟ", u';':u"ཟ", u'<':u"རྞ", u'=':u"ཾ", u'>':u"ཤ", u'?':u"ྷྭ", u'@':u"ཉ", u'A':u"པ", u'B':u"ཤ", u'C':u"ྲ", u'D':u"བ", u'E':u"ག", u'F':u"མ", u'G':u"ཙ", u'H':u"ཚ", u'I':u"ྙ", u'J':u"ཛ", u'K':u"ྭ", u'L':u"ྀཾ", u'M':u"ཧ", u'N':u"ས", u'O':u"ཏ", u'P':u"ཧཱུྃ", u'Q':u"ཀ", u'R':u"གྱ", u'S':u"ཕ", u'T':u"ཾ", u'U':u"ཇ", u'V':u"ལ", u'W':u"ཀྱ", u'X':u"ྱ", u'Y':u"རྩྱ", u'Z':u"ཱ", u'[':u"ད", u'\\':u"ཏྲ", u']':u"ན", u'^':u"ུ", u'_':u"༈", u'`':u"ཡ", u'a':u"པ", u'b':u"ཤ", u'c':u"ར", u'd':u"བ", u'e':u"ག", u'f':u"མ", u'g':u"ཙ", u'h':u"ཚ", u'i':u"ཉ", u'j':u"ཛ", u'k':u"ཝ", u'l':u"ཞ", u'm':u"ཧ", u'n':u"ས", u'o':u"ཏ", u'p':u"ཐ", u'q':u"ཀ", u'r':u"ང", u's':u"ཕ", u't':u"ཅ", u'u':u"ཇ", u'v':u"ལ", u'w':u"ཁ", u'x':u"ཡ", u'y':u"ཆ", u'z':u"འ", u'{':u"ད", u'|':u"ན", u'}':u"ྲ", u'~':u"ྶ", u' ':u"རྷ", u'¡':u"ྴ", u'¢':u"རྒ", u'£':u"ྚ", u'¤':u"རྐ", u'¥':u"ྛ", u'§':u"ྜ", u'¨':u"ྗ", u'©':u"ྩ", u'ª':u"༐", u'«':u"ྲ", u'¬':u"ཋྲ", u'®':u"ྔ", u'¯':u"ཋ", u'°':u"ེ", u'±':u"ཾ", u'´':u"ྒ", u'µ':u"ྷ", u'¸':u"ྼ", u'º':u"༔", u'»':u"ཋྱ", u'¿':u"ྷཡ", u'À':u"ྀ", u'Á':u"རྠ", u'Â':u"རྔ", u'Ã':u"ཻ", u'Ä':u"རྦ", u'Å':u"རྤ", u'Æ':u"ྟྱ", u'Ç':u"ྑྱ", u'È':u"རྙ", u'É':u"ྜྲ", u'Ê':u"ངྲ", u'Ë':u"རྗ", u'Ì':u"རྩ", u'Í':u"ྲྣ", u'Î':u"རྦ", u'Ï':u"རྨ", u'Ñ':u"ྙྱ", u'Ò':u"རྗ", u'Ó':u"རྟ", u'Ô':u"རྫ", u'Õ':u"ཽ", u'Ö':u"ྑ", u'Ø':u"རྟ", u'Ù':u"ྻ", u'Ú':u"ཉྲ", u'Û':u"ཱ", u'Ü':u"ིཾ", u'ß':u"ྥ", u'à':u"རྴ", u'á':u"ེཾ", u'â':u"ཊྱ", u'ã':u"ང", u'ä':u"ཎ", u'å':u"ྤ", u'æ':u"ཛྱ", u'ç':u"ྲ", u'è':u"ཌ", u'é':u"ཊ", u'ê':u"ྞ", u'ë':u"ཁ", u'ì':u"ཉ", u'í':u"ངྱ", u'î':u"ཉྱ", u'ï':u"ནྱ", u'ñ':u"དྱ", u'ò':u"རྨ", u'ó':u"ཏྱ", u'ô':u"ྚྱ", u'õ':u"ཊ", u'ö':u"ྷ", u'÷':u"ྷྲ", u'ø':u"ྟ", u'ù':u"ཌ", u'ú':u"ཊ", u'û':u"ཎ", u'ü':u"ཤ", u'ÿ':u"ཊྲ", u'ı':u"ཥྱ", u'Œ':u"རྐ", u'œ':u"ྐ", u'Ÿ':u"རྡ", u'ƒ':u"ྨ", u'ˆ':u"ྟྭ", u'ˇ':u"ཛྱ", u'˘':u"ྟྲ", u'˙':u"ྪ", u'˚':u"ྭ", u'˛':u"ཪ", u'˜':u"ཧྱ", u'˝':u"རྱ", u'Σ':u"ཁྱ", u'Ω':u"ཱ", u'π':u"ྠ", u'–':u"༴", u'—':u"༈", u'‘':u"ྣ", u'’':u"རྣ", u'‚':u"༅", u'“':u"ྡ", u'”':u"རྡ", u'„':u"ཁྲ", u'†':u"ྕ", u'‡':u"ཎྱྲ", u'…':u"རྞ", u'‰':u"རྒ", u'‹':u"ི", u'›':u"རྒ", u'™':u"ྴྭ", u'∂':u"ྦ", u'∆':u"ྫ", u'∏':u"ཐྱ", u'∕':u"ཤྱ", u'∙':u"ོ", u'√':u"ླ", u'∞':u"ྛ", u'∫':u"ྵ", u'≈':u"ྱ", u'≠':u"ཿ", u'≤':u"ཌྲ", u'≥':u"ྴྱ", u'◊':u"ྡྱ", u'':u"ྭ", u'':u"ྚྲ", u'':u"ཌྲྱ"}

# helper function
def getNewString( theString ) :
    if( not theString or len(theString) ==0) :
        return u""
    # should we tokenize on "."?
    newString = u""
    for c in theString:
        if c in ltibUniTab:
            newString += ltibUniTab[c]
    #newString = u"གྱ།"
    #newString.encode("utf16")
    return newString

def ltibetanToUnicode(*args): 
    """Change the case of a selection, or current word from upper case, to first char upper case, to all lower case to upper case..."""
    import string

    # The context variable is of type XScriptContext and is available to
    # all BeanShell scripts executed by the Script Framework
    xModel = XSCRIPTCONTEXT.getDocument()

    #the writer controller impl supports the css.view.XSelectionSupplier interface
    xSelectionSupplier = xModel.getCurrentController()

    #see section 7.5.1 of developers' guide
    xIndexAccess = xSelectionSupplier.getSelection()
    count = xIndexAccess.getCount();
    if(count>=1):  #ie we have a selection
        i=0
	while i < count :
            xTextRange = xIndexAccess.getByIndex(i);
            theString = xTextRange.getString();
            if len(theString)!=0 :
                newString = getNewString( theString );
                if newString:
                    xTextRange.setString(newString);
                    xSelectionSupplier.select(xTextRange);
	    i+= 1


# lists the scripts, that shall be visible inside OOo. Can be omited, if
# all functions shall be visible, however here getNewString shall be surpressed
g_exportedScripts = ltibetanToUnicode,
