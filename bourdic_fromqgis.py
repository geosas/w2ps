from pywps.Process import WPSProcess       
import os
import time                  
class Process(WPSProcess):
####################################################################################
#Ce script recupere un shapefile et un mail fourni par le client (fromqgis), 
#commande une modelisation openfluid sur le serveur (inserver),
#realise sur le serveur la jointure entre le shapefile fourni et le csv genere par la modelisation (join),
#retourne le shapefile+csv par mail a l'utilisateur (inserver)
####################################################################################

    def __init__(self):

        # Process initialization
        WPSProcess.__init__(self,
            identifier = "WPS_bourdic",
            title="WPS pour le Bourdic",
            abstract="""WPS pour le Bourdic""",
            version = "1.0",
            storeSupported = True,
            statusSupported = True)

        # Adding process inputs
        
        self.dataIn = self.addComplexInput(identifier="data",
                    title="Vecteur utilise pour la simulation openfluid",
                    formats = [{'mimeType':'text/xml'}])

        self.textIn = self.addLiteralInput(identifier="text",
                    title = "Email (ex jean.dupont@free.fr)",type = type("String")) # Type par defaut en integer, pour string il faut ajouter typestring

        self.textOut = self.addLiteralOutput(identifier = "text",
                title="Output literal data")

    def execute(self):

        outputPath = "/home/jvh/openfluid/workspace/output/output_bourdic/" 
        self.cmd("cp %s %s" % (self.dataIn.getValue(),outputPath))
        self.cmd("mv %s%s %s%s.gml" % (outputPath,self.dataIn.getValue(),outputPath,'Bourdic_parcelles_RGF93')) 
        os.system("ogr2ogr -f 'ESRI Shapefile' %s%s.shp %s%s.gml" % (outputPath,'Bourdic_parcelles_RGF93',outputPath,'Bourdic_parcelles_RGF93'))

        os.system("sed -i s/launch_openfluid=off/launch_openfluid=on/g /var/www/pywps/processes/bourdic.txt")
        os.system("sed -i s/mail=/mail=%s/g /var/www/pywps/processes/bourdic.txt" % (self.textIn.getValue()))
        self.textOut.setValue("End of simulation") #renvoit un name

        return
