Tibetan Unicode Scripts
=======================

This repository contains some random Tibetan Encoding translation scripts.

I came across difficulties with old documents with Tibetan fonts encoded in old
8-bit hacky non-standard encodings (Dedris, Esama, LTibetan, etc.), and none
of the tools available for Unicode conversion were doing their job. So I decided
to make the conversion tables and make them available to everyone, which is the
point of this repository.

All this is really hacky and will certainly need to be reworked if you want
to use it. Feel free to write new scripts or correct these ones and send your
fixes! They are mainly correspondance tables, so they should be very
straightforward to adapt if you know the script language for your tool.

There is absolutely **NO WARRANTY** that it will work, and you have to read the
output carefully! It should work quite well for LTibetan, Esama (not b or c due
to strange behaviour of InDesign) and (E)Dedris.

I am not going to use them anymore, so feel free also to fork the repo and
maintain it yourself.

The scripts are distributed under the very free CC0 license (see the scripts
headers).

There are currently two scripts:

##All fonts (except LTibetan) to Unicode for AdobeIndesign

This is an InDesign jsx script that you can save to:
 * Windows XP: `C:\Documents and Settings\<username>\Application Data\Adobe\InDesign\<version>\<username>\Scripts\Scripts Panel\`
 * Windows Vista: `C:\Users\<username>\AppData\Roaming\Adobe\InDesign\<version>\<locale>\Scripts\Scripts Panel\`
 * Mac OS: `/Users/<username>/Library/Preferences/Adobe InDesign/<version>/<locale>/Scripts/Scripts Panel`

where `<username>` is your user name, and `<locale>` and `<version>` should be relatively obvious.

Once the script is in the folder, it appears on the Scripts panel inside InDesign.
To display the panel, choose *Window -> Utilities -> Scripts*. Double-click the script
to convert from any old encoding to Unicode. You can set the font and size by
editing the script (it is in the first lines).

Not that it auomatically sets the Paragraph Builder to World-Ready Composer.

##LTibetan to Unicode for LibreOffice

This is a python script that you can save to (under Linux)
    <home>/.config/libreoffice/<version>/user/Scripts/python/LtibtoUni.py
where `<home>` is your home directory and `<version>` your LibreOffice version
directory (there should be only one). Adapting to Windows or MacOSX directories
should be relatively easy.

Once you have saved it, you can convert files with LTibetan font into Unicode.
