#!/bin/bash
curl -s --user 'username' \
    https://api.mailgun.net/v2/sandbox0c2e246579c947258829997757476150.mailgun.org/messages \
    -F from='WPS OpenFLUID <vanhouteghem@jonathan.mailgun.org>' \
    -F to='vanhouteghem <'$1'>'\
    -F subject='Votre simulation openfluid est disponible' \
    -F text='Votre simulation OpenFLUID est disponible2' \
    --form-string html='<html>Votre simulation OpenFLUID est disponible</html>' \
    -F attachment=@/home/jvh/openfluid/workspace/output/output_bourdic/openfluid.gml
