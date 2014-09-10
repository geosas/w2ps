import os
os.system("shp2pgsql -s 2154 -c -D -I /home/jvh/openfluid/workspace/output/output_bourdic/Bourdic_parcelles_RGF93.shp bourdic_parcelle | psql -d mabase -h localhost -U postgres")
os.system("psql -h localhost -U postgres -d mabase -c \"COPY tmp_import_csv FROM '/home/jvh/openfluid/workspace/output/output_bourdic/sum_s2_SU_area.csv' DELIMITER ' ' CSV HEADER;\"")
os.system("pgsql2shp -f /home/jvh/openfluid/workspace/output/output_bourdic/openfluid.shp -h localhost -u postgres mabase 'SELECT * FROM bourdic_parcelle INNER JOIN tmp_import_csv ON (bourdic_parcelle.ofld_id = tmp_import_csv.unitid) order by gid;'")
os.system("psql -h localhost -U postgres -d mabase -c 'delete from tmp_import_csv ; drop table bourdic_parcelle;'")
os.system("ogr2ogr -f 'GML' /home/jvh/openfluid/workspace/output/output_bourdic/openfluid.gml /home/jvh/openfluid/workspace/output/output_bourdic/openfluid.shp")