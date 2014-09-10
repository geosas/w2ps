import os
import time
i=0
while (i<1):
    if 'launch_openfluid=off' in open('/var/www/pywps/processes/bourdic.txt').read():
        i=0
        time.sleep(1)
    if 'launch_openfluid=on' in open('/var/www/pywps/processes/bourdic.txt').read():
        os.system("sed -i s/launch_openfluid=on/launch_openfluid=off/g /var/www/pywps/processes/bourdic.txt") #print "true"
        os.system("openfluid -i /home/jvh/openfluid/workspace/input/onema_bourdic_stat/IN/ -o /home/jvh/openfluid/workspace/output/output_bourdic/")
        os.system("python2.6 /var/www/pywps/processes/bourdic_join.py")
        os.system("b=$(sed -n '4p' /var/www/pywps/processes/bourdic.txt) ; c=$(echo $b | cut -d'=' -f 2) ; sh /var/www/pywps/processes/bourdic_mail.sh $c")
        os.system("sed -i '4s/.*/mail= /' /var/www/pywps/processes/bourdic.txt")        
        os.system("rm -rf /home/jvh/openfluid/workspace/output/output_bourdic/*")
